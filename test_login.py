import time
from time import sleep

import pytest
from selenium import webdriver
from pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen

class Test_001_Login():
    baseURL = ReadConfig.getApplicationURL()
    clientCode = ReadConfig.getClientCode()
    employeeNumber = ReadConfig.getEmployeeNumber()
    password = ReadConfig.getPassword()
    logger=LogGen.loggen()

    @pytest.mark.login
    @pytest.mark.regression
    def test_homePageTitle(self, setup):
        self.logger.info("*************** Test_001_Login *****************")
        self.logger.info("****Started Home page title test for automation ****")
        self.driver = setup
        self.logger.info("****Opening URL****")
        self.driver.get(self.baseURL)
        time.sleep(10)
        act_title=self.driver.title

        if act_title=="Vision":
            self.logger.info("**** Home page title test passed ****")
            self.driver.close()
            assert True
        else:
            self.logger.error("**** Home page title test failed****")
            self.driver.close()
            assert False

    @pytest.mark.viswa
    @pytest.mark.login
    # @pytest.mark.regression
    def test_login(self, setup):

        self.logger.info("****Started Login Test****")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp=LoginPage(self.driver)
        self.lp.setClientCode(self.clientCode)
        self.lp.setEmployeeNumber(self.employeeNumber)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        time.sleep(10)
        vision_title=self.driver.title
        if vision_title=="Vision - DBS5000 on DW server - ALPHA":
            self.logger.info("****Login test passed ****")
            self.driver.close()
            assert True
        else:
            self.logger.error("****Login test failed ****")
            self.driver.close()
            assert False





