# Introduction 

This is a python-bdd starter project for service tests using Python-BDD and Requests library.

# Getting Started

Setup pipenv:

Pre-Requisite:

    pip install pipenv

In Powershell:

1. Execute the 'pipenv install' command to install all of the required python libraries from the Pipfile.  (Result of this is a Pipfile.lock file that packages and caches the dependencies) 
2. Execute the 'pipenv shell' command in order to activate the virtual environment


# Build and Test

To run tests by a specific tag use the following command substituting in the appropriate tag for the set of tests to run:

    pytest -k "githubAPITest"

To run tests with pytest-html reporting:

    pytest -k "githubAPITest" --html=report.html --self-contained-html

To run tests with pytest-html reporting and approval tests:

    pytest -k "githubAPITest" --html=report.html --self-contained-html --approvaltests-use-reporter='PythonNative' 

    pytest --html=report.html --self-contained-html --approvaltests-add-reporter="C:\Program Files\WinMerge\WinMergeU.exe"

To execute tests in parallel using pytest-xdist pass the -n NumProc argument in via the CLI (https://pypi.org/project/pytest-xdist/):

    pytest -n 2 -k "githubAPITest" --html=report.html --self-contained-html --approvaltests-use-reporter='PythonNative'