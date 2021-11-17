from pytest_bdd import scenarios, given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

scenarios(
    r'C:\Users\harikrishna.manokara\PycharmProjects\phptravel\tests\features\companymenubutton.feature'
)

PHP_TRAVELS_HOME = "https://phptravels.com/demo/"
browser = webdriver.Chrome(r"D:\New folder\chromedriver.exe")


@given('I am launching chrome browser')
def test_home():
    browser.implicitly_wait(10)
    browser.get(PHP_TRAVELS_HOME)
    browser.maximize_window()


@when("I am clicking the about-as under company button")
def test_perform_click_about_us():
    company_menu_button = browser.find_element_by_xpath("//span[@class='currentLanguage']")
    company_menu_button.click()
    about_us_text = browser.find_element_by_xpath("//a[@class='lvl-1 link nav-link'][normalize-space()='About Us']")
    about_us_text.click()


@then("verify the landing page url and 2018 photos")
def test_results():
    try:
        WebDriverWait(browser, 10).until(EC.presence_of_element_located(
                (By.XPATH, "//strong[normalize-space()='2018']//following::div[2]//child::a[1]")))
    finally:
        browser.quit()
