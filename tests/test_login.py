import pytest

from pytest_bdd import scenarios, given, when, then
from selenium import webdriver

PHP_TRAVELS_HOME = "https://phptravels.com/demo/"

scenarios(r'C:\Users\harikrishna.manokara\PycharmProjects\phptravel\tests\phptravels.feature')


# Fixtures

@pytest.fixture
def test_browser():
    b = webdriver.Chrome(r"D:\New folder\chromedriver.exe")
    b.implicitly_wait(10)
    yield b

# Given Steps

@given('launch chrome browser')
def test_home(test_browser):
    test_browser.get(PHP_TRAVELS_HOME)


# When Steps

@when("login as a given credential")
def search_phrase(test_browser):
    search_input = test_browser.find_element_by_xpath('//a[text()="Login"]')
    search_input.click()

    print(test_browser.current_window_handle)
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

# Then Steps

@then("redirect to the home page")
def test_results(test_browser):
    print(test_browser.title)
    # assert test_browser.title == 'Login - PHPTRAVELS'
    test_browser.quit()
