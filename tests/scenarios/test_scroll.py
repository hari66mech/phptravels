import pytest

from pytest_bdd import scenarios, given, when, then
from selenium import webdriver

PHP_TRAVELS_HOME = "https://phptravels.com/demo/"

scenarios(r'C:\Users\harikrishna.manokara\PycharmProjects\phptravel\tests\features\scrolling.feature')


@pytest.fixture
def test_browser():
    browser = webdriver.Chrome(r"D:\New folder\chromedriver.exe")
    browser.implicitly_wait(10)
    yield browser


@given('i am launching chrome browser')
def test_home(test_browser):
    test_browser.get(PHP_TRAVELS_HOME)


@when("I have scrolling the home page and verify header menu")
def perform_mousehover(test_browser):
    test_browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    test_browser.find_element_by_xpath("//a[@title='phptravels']//div//*[name()='svg']")
    test_browser.find_element_by_xpath("//div[@class='whatsapp wow flash animated']//*[name()='svg']")
    test_browser.switch_to.frame("chat-widget")
    test_browser.find_element_by_xpath("//button[@class='e1mwfyk10 lc-kd6d3b e1m5b1js0']")

@then("I am closing the browser")
def test_results(test_browser):
    test_browser.quit()
