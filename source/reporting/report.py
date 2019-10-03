import os

from jinja2 import Environment, FileSystemLoader

from source.system_config import Config, current_file_path


class SuiteReport:
    pass


class Report:
    def __init__(self):
        self.data = {}

    def add_step(self, step_no, step_data):
        self.data[step_no] = step_data

    def add_screen_shot(self):
        pass

    def generate(self, filename):
        templates = os.path.join(current_file_path, 'source\\reporting\\templates')
        css = os.path.join(current_file_path, 'source\\reporting\\static\\scss\\master_style.css')
        file_loader = FileSystemLoader(templates)
        env = Environment(loader=file_loader)
        template = env.get_template('test_case.html')
        with open(css) as file:
            css_contents = file.read()

        output = template.render(details=self.data, css=css_contents)
        with open(os.path.join(Config.REPORT_FOLDER, f"{filename}.html"), 'w') as file:
            file.write(output)
