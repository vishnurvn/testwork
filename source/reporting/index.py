import calendar
import hashlib
from datetime import datetime

from jinja2 import Environment, FileSystemLoader

templates = r'C:\Users\Vishnu\Documents\auto_framework\source\reporting\templates'
file_loader = FileSystemLoader(templates)
env = Environment(loader=file_loader)

template = env.get_template('index.html')

test_case_data = [
    {
        'id': hashlib.sha1('Test case one'.encode('utf-8')).hexdigest(),
        'name': 'Test case one',
        'description': "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum",
        'run_time': '1 minute 35 seconds',
        'status': 1
    }, {
        'id': hashlib.sha1('Test case two'.encode('utf-8')).hexdigest(),
        'name': 'Test case two',
        'description': "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged",
        'run_time': '1 minute 58 seconds',
        'status': 0
    }, {
        'id': hashlib.sha1('Test case three'.encode('utf-8')).hexdigest(),
        'name': 'Test case three',
        'description': "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of",
        'run_time': '2 minute 2 seconds',
        'status': 1
    }
]

status = {
    'passed': 0,
    'failed': 0,
    'skipped': 0
}

for test_case in test_case_data:
    stat = test_case['status']
    if stat == 1:
        status['passed'] += 1
    elif stat == 0:
        status['failed'] += 1
    else:
        status['skipped'] += 1

date = datetime.now()
date_ = f"{calendar.month_name[date.date().month]}  {date.date().day}, {date.date().year}"
time = date.time()
time_ = f"{time.hour}:{time.minute}:{time.second}"

with open(r'C:\Users\Vishnu\Documents\auto_framework\reports\css\master_style.css') as file:
    css_contents = file.read()

output = template.render(content='Hello there', status=status, date=date_, time=time_, test_case_data=test_case_data,
                         css=css_contents)

filename = r'C:\Users\Vishnu\Documents\auto_framework\reports\index.html'

with open(filename, 'w') as file:
    file.write(output)
