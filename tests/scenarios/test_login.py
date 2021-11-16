import pytest

from pytest_bdd import scenarios, given, when, then
from selenium import webdriver

PHP_TRAVELS_HOME = "https://phptravels.com/demo/"

scenarios(r'C:\Users\harikrishna.manokara\PycharmProjects\phptravel\tests\features\phptravels.feature')


@pytest.fixture
def test_browser():
    browser = webdriver.Chrome(r"D:\New folder\chromedriver.exe")
    browser.implicitly_wait(10)
    yield browser


@given('i am launching chrome browser')
def test_home(test_browser):
    test_browser.get(PHP_TRAVELS_HOME)


@when("login as the valid credential")
def test_login(test_browser):
    search_input = test_browser.find_element_by_xpath('//a[text()="Login"]')
    search_input.click()

    handles = test_browser.window_handles
    for handle in handles:
        test_browser.switch_to.window(handle)

    name = test_browser.find_element_by_xpath("//input[@name='username']")
    name.send_keys("user@phptravels.com")
    password = test_browser.find_element_by_xpath("//input[@id='inputPassword']")
    password.send_keys("demouser")
    remember_me = test_browser.find_element_by_xpath("//input[@name='rememberme']")
    remember_me.click()
    login = test_browser.find_element_by_xpath("//input[@id='login']")
    login.click()


@then("redirect to the home page")
def test_results(test_browser):
    assert test_browser.title == 'Login - PHPTRAVELS'
    test_browser.quit()
