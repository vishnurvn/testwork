# testwork
##### A test automation framework for all your nonsense
### Installation
You will be provided with a wheel file. To install use the command:
```cmd
pip install testwork_version_x.x.whl
```

### Usage
#### Creating a new project
To start a new project. Create a project directory, launch the command line, cd to the project directory and fire up the command.
```cmd
testwork start
```
Prompt for the settings will appear. You can fill them but can change them later. The following file structure will be created (below example is for web. The structure of the project will depend on the options you select):
```
project_name/
    test_case/
        web/
    test_data/
        web/
    objectmap/
    reports/
    config.yaml
```

#### Creating a new test case
To create a test case. use the command: `testwork create_test_case -t {type}` where `{type}` is the type of the test case (web, api, db etc...). Options either -t or --type maybe used. Available types are defined in the config.yaml file under types.
#####Example for web test cases:
```cmd
testwork create -t web
```
OR
```cmd
testwork create --type web
```

#### Executing test cases.
To execute test cases use the command: `testwork execute -t web {name}` where `{name}` is the filename of the test case. You can also execute multiple test cases at once using the command: `testwork execute --type web {name_1} {name_2}`. To execute all test cases at once, the following command may be used: `testwork execute --type web --all`. 
##### Examples:
Assuming the project contains the following test cases: `test_case_1, test_case_2, test_case_3`.

To execute `test_case_1`:
```cmd
testwork execute -t web test_case_1
```
OR
```cmd
testwork execute --type web test_case_1
```

To execute 2 test cases at once:
```cmd
testwork execute -t web test_case_1 test_case_2
```
OR
```cmd
testwork execute --type web test_case_1 test_case_2
```

To execute all available test cases of type web:
```cmd
testwork execute --type web --all
```