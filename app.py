import argparse
import os
import re

from source.system_config import Config
from source.system_config import current_file_path

test_cases_path = os.path.join(current_file_path, 'test_cases')
test_data_path = os.path.join(current_file_path, 'test_data')

parser = argparse.ArgumentParser(description='Framework controls')
parser.add_argument('command', help='Create test case')
parser.add_argument('-t', '--type', help='Type for test case. Available - web, api', nargs=2)
parser.add_argument('-a', '--admin', help='Login to server as admin')

args = parser.parse_args()


def get_test_case_list(type_):
    if type_ == 'web':
        web_test_cases = os.path.join(test_cases_path, 'web')
        test_case_list = []
        for file in os.listdir(web_test_cases):
            if re.match(Config.TEST_CASE_REGEX, file):
                test_case_list.append(file)
        return test_case_list


def generate_latest_test_case(test_case_list):
    latest_id = re.search(Config.TEST_CASE_REGEX, max(test_case_list)).group('id')
    return f"test_case_{int(latest_id) + 1}.py"


if args.command == 'create_test_case':
    if args.type[0] == 'web':
        tc_list = get_test_case_list('web')
        latest_tc = generate_latest_test_case(tc_list)
        print(f"Creating test case {latest_tc}")
elif args.command == 'launch_server':
    pass
