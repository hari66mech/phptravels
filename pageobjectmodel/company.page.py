company_button = "//span[@class='currentLanguage']"
about_as_text = "//a[@class='lvl-1 link nav-link'][normalize-space()='About Us']"
year = "//strong[normalize-space()='2018']"
photos = "//*[@id='Main']/div/div/div/div/div[6]"


def __init__(self, driver):
    self.driver = driver


def clickCompanyMenu(self):
    self.driver.find_element_by_xpath(self.company_button).click()


def clickCompanyMenu(self):
    self.driver.find_element_by_xpath(self.company_button).click()
