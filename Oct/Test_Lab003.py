import pytest
import allure

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

