from locust import HttpUser, task, constant, User, events
import requests
from faker import Faker


# Command line statement to execute locust in the Terminal or Powershell
# locust --headless --users 10 --spawn-rate 1 --host https://test-api.k6.io  --run-time 5 --html locust_result.html --logfile locust_log.log


# Run Test Start Listener and Requests library to retrieve the initial token


@events.test_start.add_listener
def _(environment, **kwargs):
    # Set token global variable to be used by subsequent calls
    global token
    token = authorization(environment.host)

def authorization(host):
    # Create Fake data for user creation
    fake = Faker()
    first_name = fake.name()
    last_name = fake.name()
    user_name = fake.email()
    password = fake.name()

    # Create a user
    json_user = {
        'first_name': first_name,
        'last_name': last_name,
        'username': user_name,
        'password': password
    }

    requests.post(host + '/user/register/', json=json_user)

    json_creds = {
        'username': user_name,
        'password': password
    }

    # Retrieve bearer token from response
    response = requests.post(host + '/auth/token/login/', json=json_creds)

    # Check for HTTP codes other than 200
    if response.status_code != 200:
        print('Status:', response.status_code, 'Problem with the request. Exiting.')
        print('Response JSON', response.json(), 'JSON output.')
        exit()

    data = response.json()
    return data['access']


class LocustK6API(HttpUser):
    wait_time = constant(2)

    @task
    def get_public_crocodiles(self):
        headers = {'Authorization': 'Bearer ' + token}
        self.client.get('/public/crocodiles/', headers=headers)

    @task
    def get_my_crocodiles(self):
        headers = {'Authorization': 'Bearer ' + token}
        self.client.get('/my/crocodiles/', headers=headers)
