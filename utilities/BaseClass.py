import inspect
import logging

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.mark.usefixtures("setup")
class BaseClass:
    def waitForElementByXpath(self, selector, value):
        element = WebDriverWait(self.driver,15).until(EC.presence_of_element_located((selector, value)))

    def getLogger(self):
        loggerName = inspect.stack()[1][3]
        logger = logging.getLogger(loggerName)
        fileHandler = logging.FileHandler('../report/lofFile.log')
        fileFormat = logging.Formatter("%(asctime)s : %(levelname)s : %(name)s : %(message)s")
        fileHandler.setFormatter(fileFormat)
        logger.addHandler(fileHandler)
        logger.setLevel(logging.DEBUG)
        return logger