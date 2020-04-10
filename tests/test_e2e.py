import pytest
from selenium import webdriver

from TestData.DataForDemo import DataForDemo
from page.HomePage import HomePage
from page.LoginPage import LoginPage
from utilities.BaseClass import BaseClass


class TestOne(BaseClass):

    def test_e2e(self, getData):
        log = self.getLogger()
        homePage = HomePage(self.driver)
        loginPage = LoginPage(self.driver)
        log.info("Clicking on Sign In link")
        homePage.linkToLogin().click()
        log.info("Entering username in username field")
        loginPage.txtEmail().send_keys(getData["username"])
        log.info("Entering username in username field")
        loginPage.txtpasswd().send_keys(getData["password"])
        log.info("Clicking on submit link")
        loginPage.btnSubmit().click()
        log.info("Validating login error message")
        assert (loginPage.errMsg().text == 'Authentication failed.')
        self.driver.refresh()


    @pytest.fixture(params=DataForDemo.getDataForARow("TestCase1"))
    def getData(self,request):
        return request.param