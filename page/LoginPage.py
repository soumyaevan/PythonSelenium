from selenium.webdriver.common.by import By


class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    TxtEmail = (By.XPATH,"//input[@id='email']")
    TxtPasswd = (By.XPATH,"//input[@id='passwd']")
    BtnSubmit = (By.ID,"SubmitLogin")
    ErrMsg = (By.XPATH,"//div[@id='center_column']/div[1]/ol/li")

    def txtEmail(self):
        return self.driver.find_element(*LoginPage.TxtEmail)

    def txtpasswd(self):
        return self.driver.find_element(*LoginPage.TxtPasswd)

    def btnSubmit(self):
        return self.driver.find_element(*LoginPage.BtnSubmit)

    def errMsg(self):
        return self.driver.find_element(*LoginPage.ErrMsg)