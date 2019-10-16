import argparse
import os
import re

import yaml

from source.system_config import SystemConfig
from source.system_config import current_file_path

test_cases_path = os.path.join(current_file_path, 'test_cases')
test_data_path = os.path.join(current_file_path, 'test_data')

parser = argparse.ArgumentParser(description='Framework controls')
parser.add_argument('command', help='Create test case')
parser.add_argument('-t', '--type', help='Type for test case. Available - web, api', nargs=1)
parser.add_argument('-a', '--admin', help='Login to server as admin')

args = parser.parse_args()


def get_test_case_list(type_):
    web_test_cases = os.path.join(test_cases_path, type_)
    test_case_list = []
    for file_name in os.listdir(web_test_cases):
        if re.match(SystemConfig.TEST_CASE_REGEX, file_name):
            test_case_list.append(file_name)
    return test_case_list


def generate_latest_id(test_case_list):
    latest_id = re.search(SystemConfig.TEST_CASE_REGEX, max(test_case_list)).group('id')
    return int(latest_id) + 1


if args.command == 'create_test_case':
    source_folder = os.path.join(current_file_path, 'source')
    test_case_template = os.path.join(source_folder, 'test_case_template.txt')
    test_data_template = os.path.join(source_folder, 'test_data_template.txt')
    config_file = os.path.join(current_file_path, 'config.yaml')
    _id = None
    spaces = ' ' * 4

    with open(config_file, 'r') as file:
        tc_config = yaml.safe_load(file)['test_case']

    if args.type[0] == 'web':
        tc_list = get_test_case_list('web')
        _id = generate_latest_id(tc_list)

    with open(test_case_template, 'r') as file:
        content = file.read()
        descriptors = '\n'.join(
            [f'{spaces}__{desc}__ = "{desc} descriptor"' for desc in tc_config['case_descriptors']]
        )
        step_descriptors = '\n'.join(
            [f"{spaces * 2}:{desc}: {desc} descriptor" for desc in tc_config['step_descriptors']])
        with open(os.path.join(current_file_path, f"test_cases/{args.type[0]}/test_case_{_id}.py"), 'w') as tc_file:
            tc_file.write(content.format(idx=_id, descriptors=descriptors, step_descriptors=step_descriptors))

    with open(test_data_template, 'r') as file:
        content = file.read()
        with open(os.path.join(current_file_path, f"test_data/{args.type[0]}/test_data_{_id}.py"), 'w') as data_file:
            data_file.write(content)

elif args.command == 'server':
    pass
