import importlib
import inspect
import os
import re
from configparser import ConfigParser
from datetime import datetime

from source.excpetion import TestCaseFailed
from source.report.report import Report
from source.system_config import SystemConfig, user_config


class TestCase:
    """
    Testcase superclass for managing test cases. All the test cases inherit from this superclass.
    Has methods _steps for getting the list of steps in that particular test case and execute
    for executing that test case.
    """

    def __init__(self, test_case, type_):
        self.tc_name = test_case
        self.tc_module = importlib.import_module(f".{test_case}", f'test_cases.{type_}')

    def _steps(self) -> list:
        """
        Function for getting the list of steps for that test case. Gets the list of methods from self, matches
        it to a regular expression, appends the matches to a list and returns the sorted array. Only methods matching
        SystemConfig.STEP_REGEX pattern are selected.

        Returns
        -------
        steps: list
            List of names of steps from the test case.

        """
        steps = []
        for name in dir(self.tc_module):
            if re.match(SystemConfig.STEP_REGEX, name):
                steps.append([name, getattr(self.tc_module, name)])
        return sorted(steps)

    def execute(self, run: str) -> None:
        """
        Function for executing a test case. Gets the list of step from the _steps method. Gets the test data sheet.
        Loops through the steps, fetched the list of parameters required in each step and gets it from the test
        data sheet. Execute the steps in the order returned by _steps.

        Parameters
        ----------
        run: string
            The run number to be executed.

        Returns
        -------
        None

        """
        report = Report()
        parent_dir = os.getcwd()
        test_data_path = os.path.join(parent_dir, 'test_data\\web\\{}.data'.format(self.tc_name))
        test_data = TestData(test_data_path)

        for case_desc, _ in user_config['test_case']['case_descriptors'].items():
            report.data[case_desc] = getattr(self.tc_module, f"__{case_desc}__")

        report.data['num_steps'] = len(list(self._steps()))
        report.data['steps'] = []

        exec_start_time = datetime.now()
        name, arguments, step_data = None, None, None
        try:
            for name, step in self._steps():
                details = inspect.getdoc(step)
                arguments = inspect.signature(step).parameters
                kwargs = dict([(arg, test_data.get_data(run, arg)) for arg in arguments])
                step_data = {}
                for desc, regex in SystemConfig.DESCRIPTOR_REGEX.items():
                    step_data[desc] = re.search(regex, details, re.MULTILINE).group('content').format(**kwargs)
                step(**kwargs)
                step_data['step_status'] = 1
                report.data['steps'].append(step_data)
        except KeyError:
            step_data['step_status'] = 0
            raise TestCaseFailed(f"Skipping run: {run}, arguments not found in the test data: "
                                 f"{[arg for arg in arguments]}")
        except AssertionError as e:
            step_data['step_status'] = 0
            raise TestCaseFailed(f"Assertion failed. Test case failed at {name}, exception: {e}")
        except Exception as e:
            step_data['step_status'] = 0
            raise TestCaseFailed(f"Failed at step: {name}, Exception: {type(e)}, {e}")
        finally:
            time_taken = (datetime.now() - exec_start_time).seconds
            report.data['execution_time'] = time_taken
            report.generate(self.tc_name)

    def execute_debug(self):
        # TODO Create debug execution for easy prototyping
        pass

    def fail(self, message):
        raise TestCaseFailed(message)


class TestData:
    """
    Class for processing test data.

    """

    def __init__(self, filename):
        """
        Receives the filename and parses it as an ini file.

        Parameters
        ----------
        filename: file name of the test data sheet

        """
        self.config = ConfigParser()
        self.config.read(filename)

    def runs(self) -> list:
        """
        Function for returning the number of run for the test case as specified in the test data.

        Returns
        -------
        sections: list
            The list of number of runs as specified in the test data

        """
        return self.config.sections()

    def get_data(self, run: str, argument: str) -> str:
        """
        Function for returning the data of a variable at a specific run.

        Parameters
        ----------
        run: string
            The run number as per the test data
        argument: string
            The variable of the value is to be returned

        Returns
        -------
        variable_value: string
            value of the variable as per the test data

        """
        return self.config[run][argument]


def get_test_case_list(type_):
    # TODO write docs and do testing
    files = os.path.join(os.getcwd(), f"test_cases\\{type_}")
    test_case_list = []
    for file_name in os.listdir(files):
        if re.match(SystemConfig.TEST_CASE_REGEX, file_name):
            test_case_list.append(file_name)
    return test_case_list


def get_latest_case_id(type_):
    # TODO write docs and do testing
    files = os.listdir(os.path.join(os.getcwd(), f"test_cases\\{type_}"))
    test_cases = [file for file in files if re.match(SystemConfig.TEST_CLASS_REGEX, file) is not None]
    try:
        latest_id = re.search(SystemConfig.TEST_CASE_REGEX, max(test_cases)).group('id')
    except ValueError:
        latest_id = '1'
    return int(latest_id)


def get_test_class(test_case_py_file, type_):
    # TODO write docs and do testing
    module_name = test_case_py_file.split('.')[0]
    module = importlib.import_module(f".{module_name}", f"test_cases.{type_}")
    test_case_class = [cls for cls in dir(module) if
                       re.match(SystemConfig.TEST_CLASS_REGEX, cls) is not None][0]
    return getattr(module, test_case_class)
