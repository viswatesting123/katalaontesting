import time
from time import sleep

import pytest

from pageObjects.AddNewPurchaseOrder import AddNewPurchaseOrder
from pageObjects.CustomerlookupPage import CustomerlookupPage
from pageObjects.LoginPage import LoginPage
from pageObjects.AddNewCustomerPage import AddNewCustomerPage
from utilities import XLUtils
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen


class Test_Add_New_PurchaseOrder:
    baseURL = ReadConfig.getApplicationURL()
    clientCode = ReadConfig.getClientCode()
    employeeNumber = ReadConfig.getEmployeeNumber()
    password = ReadConfig.getPassword()
    subject = ReadConfig.getAddSubjectInfo()
    logger = LogGen.loggen()
    path = ".\\TestData\\AddNewPurchaseOrderData.xlsx"

    @pytest.mark.purchaseorder
    # @pytest.mark.regression
    def test_add_new_purchase_order(self, setup):
        self.logger.info("*************** Test_Customer_lookup *****************")
        self.logger.info("****Started customer lookup test ****")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp = LoginPage(self.driver)
        self.lp.setClientCode(self.clientCode)
        self.lp.setEmployeeNumber(self.employeeNumber)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        time.sleep(10)
        self.np = AddNewPurchaseOrder(self.driver)
        self.nc = AddNewCustomerPage(self.driver)
        self.nc.addNewCustomerTasksMenu()
        time.sleep(5)
        self.nc.addNewCustomerCreateNew()
        self.np.addNewPurchaseOrder()
        self.np.addNewVendorDetails(self.driver)
        # General tab
        self.np.venderInfoRequestedBy(self.driver)
        self.np.addCenterInfo(self.driver)
        self.np.addDepartmentInfo(self.driver)
        self.np.nextButton()
        # ship to tab
        self.np.nextButton()
        # Register tab
        self.np.registerPoInfo()
        self.np.selectPoInfo(self.driver)
        self.np.nextButton()
        # Notes tab
        self.np.addNotes()
        self.np.setSubject(self.subject)
        self.np.savePoNotes()
        self.np.nextButton()
        # Print tab
        self.np.printPoDetails()
        self.np.savePurchaseOrder(self.driver)
        time.sleep(5)
