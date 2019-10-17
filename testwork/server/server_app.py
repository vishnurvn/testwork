import importlib
import os
import re

from flask import Flask, render_template

from source.system_config import SystemConfig

app = Flask(__name__)


@app.route('/')
@app.route('/index')
def index():
    data, test_case_folder = {}, SystemConfig.TEST_CASE_FOLDER
    for item in os.listdir(test_case_folder):
        directory = os.path.join(test_case_folder, item)
        if os.path.isdir(directory) and not item.startswith('__'):
            data[item] = []
            for file in os.listdir(directory):
                if re.match(SystemConfig.TEST_CASE_REGEX, file):
                    file = file.split('.')[0]
                    module = importlib.import_module('.{}'.format(file), 'test_cases.web')
                    test_case_class = [cls for cls in dir(module) if
                                       re.match(SystemConfig.TEST_CLASS_REGEX, cls) is not None][0]
                    test_class = getattr(module, test_case_class)()
                    data[item].append({
                        'description': test_class.__description__,
                        'name': test_class.__name__
                    })
    return render_template("index.html", data=data)


@app.route('/test_case/<string:tc_id>')
def test_case(tc_id):
    return render_template('test_case.html')


if __name__ == '__main__':
    app.run(debug=True)
