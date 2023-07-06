import time
from time import sleep

import pytest

from pageObjects.AddNewPosOrderPage import AddNewPosOrder
from pageObjects.AddNewPurchaseOrder import AddNewPurchaseOrder
from pageObjects.AddNewPartsOrder import AddNewPartsOrder
from pageObjects.CustomerlookupPage import CustomerlookupPage
from pageObjects.LoginPage import LoginPage
from pageObjects.AddNewCustomerPage import AddNewCustomerPage
from utilities import XLUtils
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen


class Test_Add_New_Pos_Order:
    baseURL = ReadConfig.getApplicationURL()
    clientCode = ReadConfig.getClientCode()
    employeeNumber = ReadConfig.getEmployeeNumber()
    password = ReadConfig.getPassword()
    subject = ReadConfig.getAddSubjectInfo()
    custinfo=ReadConfig.getCustomerInfo()
    partsdesc1=ReadConfig.getPartsDescInfo()
    discount=ReadConfig.getDiscount()
    quantship=ReadConfig.getQuantitytoShip()
    quantity=ReadConfig.getQuantity()
    payment=ReadConfig.getPayment()

    logger = LogGen.loggen()
    path = ".\\TestData\\AddNewPurchaseOrderData.xlsx"

    @pytest.mark.posorder
    # @pytest.mark.regression
    def test_add_new_pos_order(self, setup):
        self.logger.info("*************** Add_New_Pos_order *****************")
        self.logger.info("****Started Pos Order test ****")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp = LoginPage(self.driver)
        self.lp.setClientCode(self.clientCode)
        self.lp.setEmployeeNumber(self.employeeNumber)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        time.sleep(10)
        self.npo = AddNewPosOrder(self.driver)
        self.nc = AddNewCustomerPage(self.driver)
        self.nc.addNewCustomerTasksMenu()
        time.sleep(5)
        self.nc.addNewCustomerCreateNew()
        self.npo.addNewPosOrder()
        self.npo.setSoldToPointofSale(self.custinfo,self.driver)
        self.npo.setAddNewPosPartsInfo(self.driver,self.quantity,self.payment)
        self.npo.savePosOrder(self.driver)
        time.sleep(5)

