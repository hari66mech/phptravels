import pytest

from pytest_bdd import scenarios, given, when, then
from selenium import webdriver

PHP_TRAVELS_HOME = "https://phptravels.com/demo/"

scenarios(r'C:\Users\harikrishna.manokara\PycharmProjects\phptravel\tests\features\phptravelsheader.feature')


@pytest.fixture
def test_browser():
    browser = webdriver.Chrome(r"D:\New folder\chromedriver.exe")
    browser.implicitly_wait(10)
    yield browser
    browser.quit()


@given('i am launching chrome browser')
def test_home(test_browser):
    test_browser.get(PHP_TRAVELS_HOME)


@when("I am clicking the php travels header")
def perform_mousehover(test_browser):
    php_travels = test_browser.find_element_by_xpath("//a[@title='phptravels']//div//*[name()='svg']")
    php_travels.click()


@then("verify the landing page url")
def test_results(test_browser):
    assert test_browser.title == "PHPTRAVELS booking script and system for hotels airline flights tours cars online application - PHPTRAVELS"