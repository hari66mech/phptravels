from pytest_bdd import scenarios, given, when, then
from selenium import webdriver

scenarios(
    r'C:\Users\harikrishna.manokara\PycharmProjects\phptravel\tests\features\pricingmenubutton.feature'
)

PHP_TRAVELS_HOME = "https://phptravels.com/demo/"
browser = webdriver.Chrome(r"D:\New folder\chromedriver.exe")


@given('I am launching chrome browser')
def test_home():
    browser.implicitly_wait(10)
    browser.get(PHP_TRAVELS_HOME)
    browser.maximize_window()


@when("I am giving valid credentials and click download button")
def test_perform_click_about_us():
    company_menu_button = browser.find_element_by_xpath("//a[normalize-space()='Pricing']")
    company_menu_button.click()
    name = browser.find_element_by_xpath("//input[@name='name']")
    name.send_keys("raj")
    email = browser.find_element_by_xpath("//input[@name='email']")
    email.send_keys("hari@gmail.com")
    whatsapp = browser.find_element_by_xpath("//input[@name='whatsapp']")
    whatsapp.send_keys("8870189023")
    download = browser.find_element_by_xpath("//button[text()='Download']")
    download.click()


@then("verify the landing page url")
def test_results():
    assert browser.title == "Thank you - PHPTRAVELS"
    assert browser.current_url == "https://phptravels.com/trial-success"
    browser.quit()
