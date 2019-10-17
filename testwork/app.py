import argparse
import os

import source

parser = argparse.ArgumentParser(description='Framework control')
parser.add_argument('command', help='Basic framework commands')

args = parser.parse_args()
spaces = " " * 4

if args.command == 'start':
    test_case_types = {
        '1': 'web',
        '2': 'api'
    }
    folders = {
        'web': ['test_cases', 'test_data', 'reports', 'drivers', 'object_map', 'test_cases\\web',
                'test_data\\web'],
        'api': ['test_cases', 'test_data', 'reports', 'test_cases\\api',
                'test_data\\api']
    }
    templates = {
        'web': ['object_map\\templates\\object_map_template.txt'],
    }

    os.system('cls')
    print('> Welcome to testwork setup. Select the type of test cases you will be creating')
    for idx, tc in enumerate(test_case_types.values(), start=1):
        print(f'{spaces}[{idx}] {tc}')
    tc_types = input('> Select option (Use comma for multiple types, e.g. 1,2): ')
    final_type_list = [test_case_types.get(tc_type.strip()) for tc_type in tc_types.split(',') if
                       test_case_types.get(tc_type.strip()) is not None]

    for tc_type in final_type_list:
        for f in folders[tc_type]:
            f_path = os.path.join(os.getcwd(), f)
            if not os.path.exists(f_path):
                os.makedirs(f_path)

        try:
            for temp in templates[test_case_types[tc_types]]:
                _, file = temp.split('\\', maxsplit=1)
                file_path = os.path.join(os.path.dirname(source.__file__), file)
                with open(file_path, 'r') as temp_file:
                    content = temp_file.read()
                    target_file = os.path.join(os.getcwd(), temp.replace('.txt', '.py'))
                    with open(target_file, 'w') as py_file:
                        print(target_file)
                        py_file.write(content)
        except KeyError:
            continue
