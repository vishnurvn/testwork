import importlib
import os
import re
import sys

from flask import render_template

from source.system_config import Config

test_case_folder = Config.TEST_CASE_FOLDER
data = {}
for item in os.listdir(test_case_folder):
    data[item] = []
    directory = os.path.join(test_case_folder, item)
    if os.path.isdir(directory) and not item.startswith('__'):
        for file in os.listdir(directory):
            if re.match(Config.TEST_CASE_REGEX, file):
                file = file.split('.')[0]
                module = importlib.import_module('.{}'.format(file), 'test_cases.web')
                test_case_class = [cls for cls in dir(module) if
                                   re.match(Config.TEST_CLASS_REGEX, cls) is not None][0]
                test_class = getattr(module, test_case_class)()
                data[item].append({
                    file: {
                        'description': test_class.__description__,
                        'name': test_class.__name__
                    }
                })

print(data)
sys.exit(1)

app = Flask(__name__)


@app.route('/')
@app.route('/index')
def index():
    # module = importlib.import_module('.{}'.format(module_name), 'test_cases.web')
    return render_template('index.html')

#
# if __name__ == '__main__':
#     app.run(debug=True)
