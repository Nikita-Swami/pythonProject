import pytest
import allure
import requests

#Create Token - POST
def create_token():
    url = "https://restful-booker.herokuapp.com/auth"
    headers = {"Content-Type":"application/json"}
    json_payload = {
        "username" : "admin",
        "password" : "password123"
    }
    response = requests.post(url=url, headers=headers, json=json_payload)
    token = response.json()["token"]
    print(token)
    return token

def create_booking():
    base_url = "https://restful-booker.herokuapp.com/"
    base_path = "/booking"
    URL = base_url + base_path
    headers = {"Content-Type": "application/json"}
    json_payload = {
        "firstname" : "Jim",
        "lastname" : "Brown",
        "totalprice" : 111,
        "depositpaid" : False,
        "bookingdates" : {
            "checkin" : "2018-01-01",
            "checkout" : "2019-01-01"
        },
        "additionalneeds" : "Breakfast"
    }
    response = requests.post(url=URL, headers=headers, json=json_payload)
    print(type(URL))
    print(type(headers))
    print(type(json_payload))

    assert response.status_code == 200

    data = response.json()
    booking_id = data["bookingid"]
    return booking_id

def test_put_request_positive():
    base_url = "https://restful-booker.herokuapp.com/"
    base_path = "/booking/" +str(create_booking())
    PUT_URL = base_url + base_path
    cookie = "token=" +create_token()
    headers = {
        "Content-Type" : "application/json",
        "Cookie" : cookie
    }
    json_payload = {
        "firstname": "Jim",
        "lastname": "Brown",
        "totalprice": 111,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2018-01-01",
            "checkout": "2019-01-01"
        },
        "additionalneeds": "Breakfast"
    }
    response = requests.put(url=PUT_URL, headers=headers, json=json_payload)
    assert response.status_code == 200
    data = response.json()
    print(data)
    assert data["firstname"] == "Jim"


def test_delete():
    URL = "https://restful-booker.herokuapp.com/"
    booking_id = create_booking()
    DELETE_URL = URL + str(booking_id)
    cookie_value = "token=" +create_token()
    headers = {
        "Content-Type" : "application/json",
        "Cookie" : cookie_value
    }
    print(headers)

    response = requests.delete(url=DELETE_URL, headers=headers)