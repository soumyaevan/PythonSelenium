from selenium.webdriver.common.by import By

# This class has all Home page related elements
class HomePage:
    def __init__(self, driver):
        self.driver = driver

    linkLogin = (By.CSS_SELECTOR,"a[class='login']")
    def linkToLogin(self):
        return self.driver.find_element(*HomePage.linkLogin)