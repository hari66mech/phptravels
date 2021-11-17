import pytest

from pytest_bdd import scenarios, given, when, then
from selenium import webdriver
from selenium.webdriver import ActionChains

PHP_TRAVELS_HOME = "https://phptravels.com/demo/"

scenarios(r'C:\Users\harikrishna.manokara\PycharmProjects\phptravel\tests\features\mousehover.feature')


@pytest.fixture
def test_browser():
    browser = webdriver.Chrome(r"D:\New folder\chromedriver.exe")
    browser.implicitly_wait(10)


@given('I am launching chrome browser')
def test_home(test_browser):
    test_browser.get(PHP_TRAVELS_HOME)


@when("Verify the hover of the submenu tab")
def perform_mousehover(test_browser):
    action = ActionChains(test_browser)
    demo = action.move_to_element(test_browser.find_element_by_xpath("//a[text()='Demo']"))
    demo.perform()
    pricing = action.move_to_element(test_browser.find_element_by_xpath("//a[text()='Pricing']"))
    pricing.perform()
    docs = action.move_to_element(test_browser.find_element_by_xpath("//a[text()='Docs']"))
    docs.perform()
    integrations = action.move_to_element(test_browser.find_element_by_xpath("//a[@class='lvl-0 link nav-link'][normalize-space()='Integrations']"))
    integrations.perform()
    blog = action.move_to_element(test_browser.find_element_by_xpath("//a[@class='lvl-0 link']"))
    blog.perform()
    features = action.move_to_element(test_browser.find_element_by_xpath("//span[text()='Features']"))
    features.click().perform()
    product = action.move_to_element(test_browser.find_element_by_xpath("//span[text()='Product']"))
    product.perform()
    company = action.move_to_element(test_browser.find_element_by_xpath("//span[@class='currentLanguage']"))
    company.perform()


@then("I am closing the browser")
def test_results(test_browser):
    test_browser.quit()
