from jinja2 import Environment, FileSystemLoader

templates = r'C:\Users\Vishnu\Documents\auto_framework\source\reporting\templates'
file_loader = FileSystemLoader(templates)
env = Environment(loader=file_loader)

template = env.get_template('test_case.html')

output = template.render()

filename = r'C:\Users\Vishnu\Documents\auto_framework\reports\test_case.html'

with open(filename, 'w') as file:
    file.write(output)
