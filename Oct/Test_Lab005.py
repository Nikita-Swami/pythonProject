import pytest
import allure
import requests

@allure.title("Test GET Request - RESTFUL Booker Project#1")
@allure.description("TC#1->Verify that GET request with ID works")
@allure.tag("regression", "p0", "smoke")
@allure.label("owner", "John Doe")
@allure.testcase("TC1#")
@pytest.mark.smoke

def test_get_single_request_by_id_positive():
    url = "https://restful-booker.herokuapp.com/booking/1"
    response_data = requests.get(url)
    print(response_data.text)
    print(response_data.json())
    print(response_data.headers)
    assert response_data.status_code == 200


@allure.title("Test GET Request - RESTFUL Booker Project#2")
@allure.description("TC#2->Verify that GET request with invalid ID works")
@allure.testcase("TC2#")
@pytest.mark.smoke

def test_get_single_request_by_id_negative():
    url = "https://restful-booker.herokuapp.com/booking/-1"
    response_data = requests.get(url)
    assert response_data.status_code == 404


@allure.title("Test GET Request - RestFUL BOOKER Project#3")
@allure.description("TC#3 -> Verify that GET Request with invalid path param")
@allure.testcase("TC#3")
@pytest.mark.smoke

def test_get_request_by_id_negative():
    url = "https://restful-booker.herokuapp.com/booking/111"
    response_data = requests.get(url)
    assert response_data.status_code == 404


@allure.title("Test GET Request - RestFUL BOOKER Project#4")
@allure.description("TC#4 ->  Verify that GET Request with exceeded ID limit")
@allure.testcase("TC#4")
@pytest.mark.smoke

def test_get_request_by_id_negative():
    url = "https://restful-booker.herokuapp.com/booking/1234567890"
    response_data = requests.get(url)
    assert response_data.status_code == 404

