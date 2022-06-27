import time
import unittest
from ClearCache.ClearCache import webdriver
import pageUI.page



class AutomationTest(unittest.TestCase):


    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(30)
        self.driver.get("https://www.saucedemo.com/")

    def test_login(self):
        self.driver.implicitly_wait(30)
        mainPage = pageUI.page.MainPage(self.driver)
        mainPage.Login()
        time.sleep(3)
        print("Test Login Completed.....")

    def test_choose_one_item(self):
        mainPage = pageUI.page.MainPage(self.driver)
        mainPage.choose_one_item()
        time.sleep(3)
        print("Test Choose One Item Completed.....")


    def test_checkout_payment(self):
        mainPage = pageUI.page.MainPage(self.driver)
        mainPage.checkout_payment()
        time.sleep(3)
        print("Test Checkout Payment Completed.....")

    def tearDown(self):
        time.sleep(3)
        self.driver.close()

if __name__ == "__main__":
    unittest.main()