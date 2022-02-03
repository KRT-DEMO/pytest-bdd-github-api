from locust import HttpUser, task, constant, TaskSet
from faker import Faker


class LocustK6API(HttpUser):
    wait_time = constant(2)

    def on_start(self):
        self.authorization()

    def authorization(self):
        # Set token global variable to be used by subsequent calls
        global token

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

        self.client.post('/user/register/', json=json_user)

        json_creds = {
            'username': user_name,
            'password': password
        }

        # Retrieve bearer token from response
        response = self.client.post('/auth/token/login/', json=json_creds)

        # Check for HTTP codes other than 200
        if response.status_code != 200:
            print('Status:', response.status_code, 'Problem with the request. Exiting.')
            print('Response JSON', response.json(), 'JSON output.')
            exit()

        data = response.json()
        token = data['access']
        return token

    @task
    def get_public_crocodiles(self):
        headers = {'Authorization': 'Bearer ' + token}
        self.client.get('/public/crocodiles/', headers=headers)

    @task
    def get_my_crocodiles(self):
        headers = {'Authorization': 'Bearer ' + token}
        self.client.get('/my/crocodiles/', headers=headers)

