import time
from time import sleep

import pytest

from pageObjects.AddNewWorkOrder import AddNewWorkOrder
from pageObjects.LoginPage import LoginPage
from pageObjects.AddNewCustomerPage import AddNewCustomerPage
from utilities import XLUtils
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen


class Test_Add_New_Work_Order:
    baseURL = ReadConfig.getApplicationURL()
    clientCode = ReadConfig.getClientCode()
    employeeNumber = ReadConfig.getEmployeeNumber()
    password = ReadConfig.getPassword()
    subject = ReadConfig.getAddSubjectInfo()
    name=ReadConfig.getName()
    lname=ReadConfig.getAddNewCustomerLastname()
    phonenum=ReadConfig.getPhonenum()
    partnum=ReadConfig.getPartNum()
    quantity=ReadConfig.getQuantity()


    logger = LogGen.loggen()
    path = ".\\TestData\\AddNewPurchaseOrderData.xlsx"

    @pytest.mark.workorder
    # @pytest.mark.regression
    def test_add_new_work_order(self, setup):
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
        self.nwo=AddNewWorkOrder(self.driver)
        self.nc = AddNewCustomerPage(self.driver)
        self.nc.addNewCustomerTasksMenu()
        time.sleep(5)
        self.nc.addNewCustomerCreateNew()
        self.nwo.addNewWorkOrder()
        # add customer for work order creation
        self.nwo.setSelectCustomer(self.driver,self.name)
        self.nwo.setNewWorOrderInfo(self.lname,self.phonenum)
        # General info tab
        self.nwo.generalInfo(self.driver)
        self.nwo.nextButton()
        # Est detail
        self.nwo.estDetails(self.driver)
        self.nwo.nextButton()
        # notes tab
        self.nwo.setAddNotes(self.subject)
        self.nwo.nextButton()
        # attachments tab
        self.nwo.nextButton()
        # required parts tab
        self.nwo.setRequireParts(self.partnum,self.driver,self.quantity)
        self.nwo.nextButton()
        # schedule tab
        self.nwo.nextButton()
        # print and save tab
        self.nwo.saveWorkOrder()
        time.sleep(8)

