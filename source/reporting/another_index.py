import base64
import os

from PIL import Image
from jinja2 import Environment, FileSystemLoader

current_dir = os.path.dirname(__file__)
file_loader = FileSystemLoader('templates')
env = Environment(loader=file_loader)

template = env.get_template('test_case.html')

test_case_details = {
    'name': 'Test case one',
    'num_steps': 15,
    'execution_time': '5min',
    'steps': [
        {
            'step_no': 1,
            'step_desc': "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.",
            'expected_results': 'something',
            'actual_results': 'something',
            'step_status': 1
        }, {
            'step_no': 2,
            'step_desc': "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged.",
            'expected_results': 'something',
            'actual_results': 'something',
            'step_status': 1
        }, {
            'step_no': 3,
            'step_desc': "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer",
            'expected_results': 'something',
            'actual_results': 'another',
            'step_status': 0
        }
    ]
}
master_css = os.path.join(current_dir, 'static\\scss\\master_style.css')
with open(master_css) as file:
    css_contents = file.read()

image = Image.open(r'C:\Users\v.raveendran\Documents\rdp_selenium\source\reporting\sample_image\sample.png')
image_b64 = base64.b64encode(image.tobytes()).decode('utf-8')

output = template.render(details=test_case_details, css=css_contents, image=image_b64)

report_folder = os.path.dirname(os.path.dirname(current_dir))
report_file = os.path.join(report_folder, 'reports\\test_case.html')

with open(report_file, 'w') as file:
    file.write(output)
