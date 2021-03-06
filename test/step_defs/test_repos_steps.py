from conftest import USER, HEADER, AUTH, USER_REPOS
from pytest_bdd import scenarios, given, then, parsers, scenario
from pytest_check import equal
from test.helpers import request_helpers
import uuid
from faker import Faker
from faker.providers import internet

# Scenarios

scenarios('../features/github_repos_api.feature')

# Given

@given('the user executes a GET User call', target_fixture="get_user")
def get_user(urls):
    response = request_helpers.get(urls['githubBaseURL'] + USER, headers=HEADER, auth=AUTH)
    print(response.content)
    return response

#in order to pass in data from the datatable you must use a given parser first then a second given to pass the parsed values into.
@given(parsers.parse('the user creates a new repo with a {description}, {homepage}, {is_private}'), target_fixture="create_repo")
@given('the user creates a new repo with a <description>, <homepage>, <is_private>')
def create_repo(urls, description, homepage, is_private):
    fake = Faker()
    fake.add_provider(internet)
    payload = {
        'name': 'Repo_' + uuid.uuid4().hex,
        'description': fake.company_email(),
        'homepage': homepage,
        'is_private': is_private
    }
    print(payload)
    response = request_helpers.post(urls['githubBaseURL'] + USER_REPOS, headers=HEADER, auth=AUTH, data=payload)
    return response


# Then

@then(parsers.parse('the response status code is "{code:d}"'))
def get_user_200(get_user, code):
    equal(get_user.status_code, code)


@then('the repo is created')
def repo_created(create_repo):
    equal(create_repo.status_code, 201)
