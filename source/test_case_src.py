import inspect
import os
import re
from configparser import ConfigParser
from datetime import datetime

from source.excpetion import TestCaseFailed
from source.reporting.report import Report
from source.system_config import Config

Config.STEP_REGEX = r'step_\d+'


class TestCase:
    """
    Testcase superclass for managing test cases. All the test cases inherit from this superclass.
    Has methods _steps for getting the list of steps in that particular test case and execute
    for executing that test case.
    """

    def _steps(self) -> list:
        """
        Function for getting the list of steps for that test case. Gets the list of methods from self, matches
        it to a regular expression, appends the matches to a list and returns the sorted array. Only methods matching
        Config.STEP_REGEX pattern are selected.

        Returns
        -------
        steps: list
            List of names of steps from the test case.

        """
        steps = []
        for name in dir(self):
            if re.match(Config.STEP_REGEX, name):
                steps.append([name, getattr(self, name)])
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
        parent_dir = os.path.dirname(os.path.dirname(__file__))
        test_data_path = os.path.join(parent_dir, 'test_data\\web\\{}.data'.format(self.__name__))
        test_data = TestData(test_data_path)

        report.data['name'] = self.__name__
        report.data['num_steps'] = len(list(self._steps()))
        report.data['description'] = self.__description__
        report.data['steps'] = []

        exec_start_time = datetime.now()
        name, arguments, step_data = None, None, None
        try:
            for name, step in self._steps():
                details = inspect.getdoc(step)
                arguments = inspect.signature(step).parameters
                kwargs = dict([(arg, test_data.get_data(run, arg)) for arg in arguments])
                step_data = {
                    'step_desc': re.search(Config.DESCRIPTION_REGEX, details,
                                           re.MULTILINE).group('content').format(**kwargs),
                    'expected_results': re.search(Config.EXPECTED_REGEX, details,
                                                  re.MULTILINE).group('content').format(**kwargs)
                }
                print(step_data)
                step_exec_time = datetime.now().time().strftime('%H:%M:%S')
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
            report.data['steps'].append(step_data)
            time_taken = (datetime.now() - exec_start_time).seconds
            report.data['execution_time'] = time_taken
            report.generate(self.__name__)


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
