from pytest_bdd import scenarios, given, when, then
from selenium import webdriver

scenarios(r'C:\Users\harikrishna.manokara\PycharmProjects\phptravel\tests\features\phptravelsheader.feature')

PHP_TRAVELS_HOME = "https://phptravels.com/demo/"
browser = webdriver.Chrome(r"D:\New folder\chromedriver.exe")


@given('I am launching chrome browser')
def test_home():
    browser.implicitly_wait(10)
    browser.get(PHP_TRAVELS_HOME)


@when("I am clicking the php travels header")
def test_perform_mousehover():
    php_travels = browser.find_element_by_xpath("//a[@title='phptravels']//div//*[name()='svg']")
    php_travels.click()


@then("verify the landing page url")
def test_results():
    assert browser.title == "PHPTRAVELS booking script and system for hotels airline flights tours cars online application - PHPTRAVELS"
    browser.quit()
