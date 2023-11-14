from selenium import webdriver
import pytest
from selenium.webdriver.common.service import Service
from selenium.webdriver.common.by import By

class BasePage:
    def __init__(self, driver):
        self.driver = driver;

    def click(self, locator):
        if str(locator).endswith("XPATH"):
            self.driver.find_element(By.XPATH).click()
        if str(locator).endswith("ID"):
            self.driver.find_element(By.ID).click()

    def enterValue(self, locator, value):
        if str(locator).endswith("XPATH"):
            self.driver.find_element(By.XPATH).send_keys(value)
        if str(locator).endswith("ID"):
            self.driver.find_element(By.ID).send_keys(value)

    def clickIndex(self, locator, index):
        if str(locator).endswith("XPATH"):
            self.driver.find_elements(By.XPATH)[index].click()
        if str(locator).endswith("ID"):
            self.driver.find_elements(By.ID)[index].click()

    def getText(self, locator):
        if str(locator).endswith("XPATH"):
            text = self.driver.find_element(By.XPATH).text
