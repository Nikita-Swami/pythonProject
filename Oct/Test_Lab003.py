import pytest
import allure

@allure.title("Test Authentication")
@allure.description("This test attempts to log into the website using a login and a password. Fails if any error happens.\n\nNote that this test does not test 2-Factor Authentication.")
@allure.tag("NewUI", "Essentials", "Authentication")
@allure.severity(allure.severity_level.CRITICAL)
@allure.label("owner", "John Doe")
@allure.link("https://dev.example.com/", name="Website")
@allure.issue("AUTH-123")
@allure.testcase("TMS-456")


@pytest.mark.smoke
def test_verify_sub0():
    assert 5 - 0  ==  5

@pytest.mark.reg
def test_verify_sub1():
    assert 5 - 1  ==  4

@pytest.mark.smoke
def test_verify_sub2():
    assert 5 - 2  ==  3

@pytest.mark.reg
def test_verify_sub3():
    assert 5 - 3 ==  2

@pytest.mark.smoke
def test_verify_sub4():
    assert 5 - 4  ==  1

@pytest.mark.skip(reason = "Not Completed, Skip it")
def test_verify_sub5():
    assert 5 - 5  ==  0

