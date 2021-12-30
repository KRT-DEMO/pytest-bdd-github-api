from conftest import USER, HEADER, AUTH
from pytest_bdd import scenarios, given, then, parsers
from pytest_check import equal
from test.helpers import request_helpers

# Scenarios

scenarios('../features/github_repos_api.feature')

# Given

@given('the user executes a GET User call', target_fixture="get_user")
def get_user(urls):
    response = request_helpers.get(urls['githubBaseURL'] + USER, headers=HEADER, auth=AUTH)
    print(response.content)
    return response

# Then

@then(parsers.parse('the response status code is "{code:d}"'))
def get_user_200(get_user, code):
    equal(get_user.status_code, code)