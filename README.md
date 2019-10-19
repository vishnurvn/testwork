# testwork
##### A test automation framework for all your nonsense
### Installation
You will be provided with a wheel file. To install use the command:
```cmd
pip install testwork_version_x.x.whl ## TODO
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
To create a test case. use the command: `testwork create_test_case -t {type} -i {id}` where `{type}` is the type of the test case (web, api, db etc...) and `{id}` is the id of the test case. Options either -t or --type maybe used. Available types are defined in the config.yaml file under types.
#####Example for web test cases: 
```cmd
testwork create -t web -i 1 ## TODO
```
OR
```cmd
testwork create --type web --id 1
```

#### Executing test cases.
To execute test cases use the command: `testwork execute -t web -n {name} -r {run_id}` where `{name}` is the filename of the test case and `{run_id}` is the run_id specified in the test data file or using ID by using the command `testwork execute -t web -i 1 {run_id}`. You can also execute multiple test cases at once using the command: `testwork execute --type web {name_1} {name_2}`. To execute all test cases at once, the following command may be used: `testwork execute --type web --all`. 
##### Examples:
Assuming the project contains the following test cases: `test_case_1, test_case_2, test_case_3`.

To execute `test_case_1`:
```cmd
testwork execute -t web -n test_case_1 -r run_1
testwork execute -t web -i test_case_1 -r run_1
```
OR
```cmd
testwork execute --type web --name test_case_1 -r run_1
testwork execute --type web --id 1 -r run_1
```

To execute multiple test cases, use a csv with either name of the test case of the id of the test case specified in the first column with appropriate headers. i.e. `id` for execution by id and `name` for execution by name and second column with the runs separated by `|` ## TODO

Example csv file:

id | run | name | description | extra columns
---|-----|------|-------------|--------------
1 | run_1 | test_case_1 | tc description 1 | extra
2 | run_2 | test_case_2 | tc description 2 | extra

OR

name | run | id | description | extra columns
-----|-----|----|-------------|--------------
test_case_1 | run_1 | 1 | tc description 1 | extra
test_case_2 | run_2 | 2 | tc description 2 | extra