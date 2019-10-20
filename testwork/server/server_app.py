import importlib
import inspect
import os
import re
import sys

from flask import Flask, render_template

from source.system_config import SystemConfig, user_config

app = Flask(__name__)
sys.path.append(os.getcwd())
test_case_folder = SystemConfig.TEST_CASE_FOLDER


@app.route('/')
@app.route('/index')
def index():
    header = {}
    for case_desc, value in user_config['test_case']['case_descriptors'].items():
        header[case_desc] = value
    data = {}
    for item in os.listdir(test_case_folder):
        if os.path.isdir(os.path.join(test_case_folder, item)):
            data[item] = []
            for file in os.listdir(os.path.join(test_case_folder, item)):
                if re.match(SystemConfig.TEST_CASE_REGEX, file):
                    filename = file.split('.')[0]
                    module = importlib.import_module(f".{filename}", 'test_cases.web')
                    for case_desc in header.keys():
                        data[item].append({
                            case_desc: getattr(module, f"__{case_desc}__")
                        })
    return render_template("index.html", data=data, header=header)


@app.route('/test_case/<string:tc_type>/<string:tc_id>')
def test_case(tc_type, tc_id):
    filename = f"test_case_{tc_id}"
    module = importlib.import_module(f".{filename}", f"test_cases.{tc_type}")
    step_data = {}
    for item in dir(module):
        if re.match(SystemConfig.STEP_REGEX, item):
            func = getattr(module, item)
            step_data[func.__name__] = {}
            doc_string = inspect.getdoc(func)
            for key, value in user_config['test_case']['step_descriptors'].items():
                content = re.search(SystemConfig.DESCRIPTOR_REGEX[value], doc_string).group('content')
                step_data[func.__name__][value] = content
    print(step_data)
    return render_template('test_case.html', step_data=step_data)


if __name__ == '__main__':
    app.run(debug=True)
