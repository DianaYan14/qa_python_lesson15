import requests


def test_create_user():
    name = "Jeff Bezos"
    job = "entrepreneur"

    response = requests.post(
        url='https://reqres.in/api/users',
        json={
            "name": name,
            "job": job}
    )

    assert response.status_code == 201
    assert response.json()['name'] == name
    assert response.json()['job'] == job


def test_delete_user_return_204():
    response = requests.delete(url='https://reqres.in/api/users/21')

    assert response.status_code == 204
    assert response.text == ''


def test_login_successful():
    email = "eve.holt@reqres.in"
    password = "cityslicka"

    response = requests.post(
        url='https://reqres.in/api/login',
        json={
            "email": email,
            "password": password}
    )

    assert response.status_code == 200
    assert response.json()['token'] != ''


def test_login_unsuccessful():
    email = "peter@klaven"

    response = requests.post(
        url='https://reqres.in/api/login',
        json={
            "email": email}
    )

    assert response.status_code == 400
    assert response.json()['error'] == 'Missing password'


def test_single_user_not_found():
    response = requests.get(url='https://reqres.in/api/users/23')

    assert response.status_code == 404
    assert response.text == '{}'


def test_total_users():
    users_count = 12
    page = 2

    response = requests.get('https://reqres.in/api/users', params={'page': page})

    assert response.json()['total'] == users_count
    assert response.status_code == 200


def test_register_successful():
    email = "eve.holt@reqres.in"
    password = "pistole1233"

    response = requests.post(url='https://reqres.in/api/register',
                             json={
                                 "email": email,
                                 "password": password}
                             )

    assert response.status_code == 200
    assert response.json()['id'] != ''


def test_register_unsuccessful():
    email = "sydney@fife"

    response = requests.post(url='https://reqres.in/api/register', json={"email": email})

    assert response.status_code == 400
    assert response.json()["error"] == "Missing password"


def test_update_user_info():
    name = "Jeff Bezos"
    job = "Amazon founder"

    response = requests.put(url='https://reqres.in/api/users/2',
                            json={"name": name,
                                  "job": job})

    assert response.status_code == 200
    assert response.json()["name"] == name
    assert response.json()["job"] == job


def test_users_list_default_length():
    default_users_count = 6

    response = requests.get('https://reqres.in/api/users')

    assert len(response.json()['data']) == default_users_count

