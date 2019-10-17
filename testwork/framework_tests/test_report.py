from source.report.report import Report

report = Report()

report.data['num_steps'] = 1
report.data['steps'] = []
step_data = {
    'Description': 'some description',
    'Expected': 'some expected results',
    'step_status': 1
}

report.data['steps'].append(step_data)

report.generate('file')
