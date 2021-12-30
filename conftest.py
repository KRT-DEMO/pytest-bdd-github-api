import pytest

# Constants
USER = '/user'
USER_REPOS = '/user/repos'
REPOS = '/repos'
OWNER = '/KTJ-DEMO'
TOKEN = ''
HEADER = {"accept": "application/vnd.github.v3+json"}
AUTH = ('Authorization', TOKEN)

# Enable tests to run across multiple environments

def pytest_addoption(parser):
    parser.addoption("--environment", action="store", default="prod", help="environment to run the api tests against")

@pytest.fixture
def urls(pytestconfig):
    env = pytestconfig.getoption("environment").lower()

    if env == 'dev':
        urls = {
            "githubBaseURL": "https://dev.api.github.com"
        }
        return urls
    elif env == 'test':
        urls = {
            "githubBaseURL": "https://test.api.github.com"
        }
        return urls
    elif env == 'stage':
        urls = {
            "githubBaseURL": "https://stage.api.github.com"
        }
        return urls
    elif env == 'prod':
        urls = {
            "githubBaseURL": "https://api.github.com"
        }
        return urls
    else:
        raise ValueError('Unknown environment: ' + env)


# Hooks

def pytest_bdd_before_scenario(request, feature, scenario):
    print('Before Scenario')


def pytest_bdd_after_scenario(request, feature, scenario):
    print('After Scenario')


def pytest_bdd_step_error(request, feature, scenario, step, step_func, step_func_args, exception):
    print('Step failed: {step}')


# def pytest_bdd_before_step(request, feature, scenario, step, step_func):
#     print('Before Step')
#
#
# def pytest_bdd_after_step(request, feature, scenario, step, step_func, step_func_args):
#     print('After Step')
#
#
# def pytest_bdd_before_step_call(request, feature, scenario, step, step_func, step_func_args):
#     print('Before step call')
#
#
# def pytest_bdd_step_func_lookup_error(request, feature, scenario, step, exception):
#     print('')


# Global Fixtures


# Shared Given Steps


# Shared When Steps


# Shared Then Steps
