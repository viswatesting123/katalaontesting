import time
from time import sleep

import pytest

from pageObjects.AddNewPurchaseOrder import AddNewPurchaseOrder
from pageObjects.AddNewPartsOrder import AddNewPartsOrder
from pageObjects.CustomerlookupPage import CustomerlookupPage
from pageObjects.LoginPage import LoginPage
from pageObjects.AddNewCustomerPage import AddNewCustomerPage
from utilities import XLUtils
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen


class Test_Add_New_PartsOrder:
    baseURL = ReadConfig.getApplicationURL()
    clientCode = ReadConfig.getClientCode()
    employeeNumber = ReadConfig.getEmployeeNumber()
    password = ReadConfig.getPassword()
    subject = ReadConfig.getAddSubjectInfo()
    custinfo=ReadConfig.getCustomerInfo()
    partsdesc1=ReadConfig.getPartsDescInfo()
    discount=ReadConfig.getDiscount()
    quantship=ReadConfig.getQuantitytoShip()

    logger = LogGen.loggen()
    path = ".\\TestData\\AddNewPurchaseOrderData.xlsx"

    @pytest.mark.partsorder
    # @pytest.mark.regression
    def test_add_new_parts_order(self, setup):
        self.logger.info("*************** Test_Parts_lookup *****************")
        self.logger.info("****Started customer lookup test ****")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp = LoginPage(self.driver)
        self.lp.setClientCode(self.clientCode)
        self.lp.setEmployeeNumber(self.employeeNumber)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        time.sleep(10)
        self.npo = AddNewPartsOrder(self.driver)
        self.nc = AddNewCustomerPage(self.driver)
        self.nc.addNewCustomerTasksMenu()
        time.sleep(5)
        self.nc.addNewCustomerCreateNew()
        self.npo.addNewPartsOrder()
        # customer tab
        self.npo.setSoldToCustomerInfo(self.custinfo,self.driver)
        self.npo.nextButton()
        # General tab
        self.npo.genaralInfoPartOrder(self.driver)
        self.npo.genaralInfoDepartment(self.driver)
        self.npo.nextButton()
        # Payment tab
        self.npo.nextButton()
        # ship to
        self.npo.nextButton()
        # register tab
        self.npo.newRegisterInfo(self.driver,self.partsdesc1,self.discount,self.quantship)
        self.npo.nextButton()
        # print option tab
        self.npo.savePartsOrder(self.driver)
        time.sleep(5)
