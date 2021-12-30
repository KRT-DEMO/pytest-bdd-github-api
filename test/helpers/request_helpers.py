import json
import requests


def post(url, headers=None, auth=None, data=None, cookies=None):

    data = json.dumps(data)
    response = requests.post(url, headers=headers, auth=auth,
                             data=data, cookies=cookies)

    return response


def put(url, headers=None, auth=None, params=None, data=None, cookies=None):

    data = json.dumps(data)
    print(data)
    response = requests.put(url, headers=headers, auth=auth, params=params,
                            data=data, cookies=cookies)

    return response



def patch(url, headers=None, auth=None, data=None, params=None, cookies=None):

    data = json.dumps(data)
    print(data)
    response = requests.put(url, headers=headers, auth=auth, params=params,
                            data=data, cookies=cookies)

    return response



def get(url, headers=None, auth=None, params=None, cookies=None):

    response = requests.get(url, headers=headers, auth=auth, params=params, cookies=cookies)

    return response


def head(url, headers=None, auth=None, cookies=None):

    response = requests.head(url, headers=headers, auth=auth, cookies=cookies)

    return response


def options(url, headers=None, auth=None, cookies=None):

    response = requests.options(url, headers=headers, auth=auth, cookies=cookies)

    return response


def delete(url, headers=None, auth=None, cookies=None):

    response = requests.delete(url, headers=headers, auth=auth, cookies=cookies)

    return response



