import argparse
import os

import yaml

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
    basic_folders = ['test_cases', 'test_data', 'reports']
    folders = {
        'web': ['drivers', 'object_map', 'test_cases\\web', 'test_data\\web'],
        'api': ['test_cases\\api', 'test_data\\api']
    }
    templates = {
        'web': ['object_map\\object_map_template.txt'],
    }
    settings = {
        'test_case': {
            'case_descriptors': {},
            'step_descriptors': {}
        },
        'web': {
            'browser': 'chrome',
            'web_driver_wait_time': 60,
            'poll_time': 1,
            'implicit_wait_time': 60,
            'page_load_timeout': 30,
            'chrome_path': 'drivers/chromedriver.exe',
            'firefox_path': 'drivers/geckodriver.exe',
            'ie_path': 'drivers/IEDriverServer.exe',
            'edge_path': 'drivers/edge.exe'
        }
    }
    descriptors = {
        'case_descriptors': 'Test case descriptors',
        'step_descriptors': 'Test step descriptors'
    }

    os.system('cls')
    yaml_settings_dict = {}
    print('> Welcome to testwork setup. Select the type of test cases you will be creating')
    for idx, tc in enumerate(test_case_types.values(), start=1):
        print(f'{spaces}[{idx}] {tc}')
    tc_types = input('> Select option (Use comma for multiple types, e.g. 1,2): ')
    final_type_list = [test_case_types.get(tc_type.strip()) for tc_type in tc_types.split(',') if
                       test_case_types.get(tc_type.strip()) is not None]

    for folder in basic_folders:
        f_path = os.path.join(os.getcwd(), folder)
        if not os.path.exists(f_path):
            os.makedirs(f_path)

    for tc_type in final_type_list:
        for f in folders[tc_type]:
            f_path = os.path.join(os.getcwd(), f)
            if not os.path.exists(f_path):
                os.makedirs(f_path)

    for tc_type in final_type_list:
        try:
            for temp in templates[tc_type]:
                _, file = temp.split('\\')
                file_path = os.path.join(os.path.dirname(os.path.dirname(source.__file__)),
                                         f"{tc_type}\\templates\\{file}")
                with open(file_path, 'r') as temp_file:
                    content = temp_file.read()
                    target_file = os.path.join(os.getcwd(), temp.replace('.txt', '.py'))
                    with open(target_file, 'w') as py_file:
                        py_file.write(content)
        except KeyError:
            continue

    print("> Folder structure created: ")
    start_path = os.getcwd()
    ind = ' ' * 4

    for root, dirs, files in os.walk(start_path):
        level = root.replace(start_path, '').count(os.sep)
        indent = ind * level
        print(f"{ind}{indent}{os.path.basename(root)}/")
        sub_intent = ind * (level + 1)
        for f in files:
            print(f"{ind}{sub_intent}{f}")

    final_type_list.extend(['test_case'])
    for tc_type in final_type_list:
        if tc_type is 'test_case':
            print("> **********Test case settings**********")
            yaml_settings_dict[tc_type] = {}
            for desc in settings[tc_type].keys():
                yaml_settings_dict[tc_type][desc] = {}
                print(f"> Enter {descriptors[desc]}. Separate key, value by : and each descriptor pair"
                      f"by ;. Example key_1:value_1;key_2:value_2")
                desc_values = input(f"> {descriptors[desc]}: ")
                for key, value in list(map(lambda x: x.split(':'), desc_values.split(';'))):
                    yaml_settings_dict[tc_type][desc][key.strip()] = value.strip()

        else:
            print(f"> **********{tc_type} settings**********")
            yaml_settings_dict[tc_type] = {}
            print(f"> Setting default value for other settings. You can change them later in the config.yaml file")
            for desc, value in settings[tc_type].items():
                print(f"> {desc}: {value}")
                yaml_settings_dict[tc_type][desc] = value

    yaml_file_path = os.path.join(os.getcwd(), 'config.yaml')
    with open(yaml_file_path, 'w') as config_file:
        yaml.dump(yaml_settings_dict, config_file, default_flow_style=False)
        print(f"> Writing config file to the path {yaml_file_path}")


elif args.command == 'create_test_case':
    try:
        from source.system_config import SystemConfig
        from source.test_case_src import user_config

        print('> You have not created a project. Run command start to create a project and then run this command')
    except FileNotFoundError:
        exec_dir = os.getcwd()
        print('> config.yaml present')
        source_path = os.path.dirname(source.__file__)
        test_case_temp = os.path.join(source_path, 'templates\\test_case_template.txt')
        test_data_temp = os.path.join(source_path, 'templates\\test_data_template.txt')
        if args.type[0] in user_config['types']:
