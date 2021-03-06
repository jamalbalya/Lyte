from element.locators import MainPageLocator
import time

class BasePage(object):

    def __init__(self, driver):
        self.driver = driver


class MainPage(BasePage):
    def Login(self):
        TC1_element_username = self.driver.find_element(*MainPageLocator.USERNAME)
        TC1_element_username.send_keys("standard_user")
        TC1_element_username = self.driver.find_element(*MainPageLocator.PASSWORD)
        TC1_element_username.send_keys("secret_sauce")
        TC1_element_button_login = self.driver.find_element(*MainPageLocator.BUTTON_LOGIN)
        TC1_element_button_login.click()
        time.sleep(3)
        # TC1_element_burger_menu = self.driver.find_element(*MainPageLocator.BURGER_MENU)
        # TC1_element_burger_menu.click()
        # time.sleep(2)
        # TC1_element_logout_side_bar = self.driver.find_element(*MainPageLocator.LOGOUT_BUTTON)
        # TC1_element_logout_side_bar.click()

    def choose_one_item(self):
        TC2_element_username = self.driver.find_element(*MainPageLocator.USERNAME)
        TC2_element_username.send_keys("standard_user")
        TC2_element_username = self.driver.find_element(*MainPageLocator.PASSWORD)
        TC2_element_username.send_keys("secret_sauce")
        TC2_element_button_login = self.driver.find_element(*MainPageLocator.BUTTON_LOGIN)
        TC2_element_button_login.click()
        TC2_element_add_item_backpack = self.driver.find_element(*MainPageLocator.ADD_ITEM_LABS_BACKPACK)
        TC2_element_add_item_backpack.click()
        TC2_element_shopping_cart = self.driver.find_element(*MainPageLocator.SHOPPING_CART)
        TC2_element_shopping_cart.click()
        time.sleep(3)

    def remove_item_shop(self):
        TC3_element_username = self.driver.find_element(*MainPageLocator.USERNAME)
        TC3_element_username.send_keys("standard_user")
        TC3_element_username = self.driver.find_element(*MainPageLocator.PASSWORD)
        TC3_element_username.send_keys("secret_sauce")
        TC3_element_button_login = self.driver.find_element(*MainPageLocator.BUTTON_LOGIN)
        TC3_element_button_login.click()
        self.driver.implicitly_wait(30)
        time.sleep(3)
        TC3_element_add_item_backpack = self.driver.find_element(*MainPageLocator.ADD_ITEM_LABS_BACKPACK)
        TC3_element_add_item_backpack.click()
        self.driver.implicitly_wait(30)
        time.sleep(2)
        TC3_element_shopping_cart = self.driver.find_element(*MainPageLocator.SHOPPING_CART)
        TC3_element_shopping_cart.click()
        self.driver.implicitly_wait(30)
        time.sleep(3)
        TC3_element_remove_backpack = self.driver.find_element(*MainPageLocator.REMOVE_BUTTON_BACKPACK)
        TC3_element_remove_backpack.click()
        time.sleep(3)

    def Delete_on_of_the_selected_items(self):
        TC4_element_username = self.driver.find_element(*MainPageLocator.USERNAME)
        TC4_element_username.send_keys("standard_user")
        TC4_element_username = self.driver.find_element(*MainPageLocator.PASSWORD)
        TC4_element_username.send_keys("secret_sauce")
        TC4_element_button_login = self.driver.find_element(*MainPageLocator.BUTTON_LOGIN)
        TC4_element_button_login.click()
        self.driver.implicitly_wait(30)
        time.sleep(3)
        TC4_element_add_item_backpack = self.driver.find_element(*MainPageLocator.ADD_ITEM_LABS_BACKPACK)
        TC4_element_add_item_backpack.click()
        TC4_element_add_item_back_light = self.driver.find_element(*MainPageLocator.ADD_ITEM_LABS_BIKE_LIGHT)
        TC4_element_add_item_back_light.click()
        self.driver.implicitly_wait(30)
        time.sleep(2)
        TC4_element_shopping_cart = self.driver.find_element(*MainPageLocator.SHOPPING_CART)
        TC4_element_shopping_cart.click()
        self.driver.implicitly_wait(30)
        time.sleep(2)
        TC4_element_remove_back_light = self.driver.find_element(*MainPageLocator.REMOVE_BUTTON_BIKE_LIGHT)
        TC4_element_remove_back_light.click()

    def checkout_payment(self):
        TC5_element_username = self.driver.find_element(*MainPageLocator.USERNAME)
        TC5_element_username.send_keys("standard_user")
        TC5_element_username = self.driver.find_element(*MainPageLocator.PASSWORD)
        TC5_element_username.send_keys("secret_sauce")
        TC5_element_button_login = self.driver.find_element(*MainPageLocator.BUTTON_LOGIN)
        TC5_element_button_login.click()
        TC5_element_add_item_backpack = self.driver.find_element(*MainPageLocator.ADD_ITEM_LABS_BACKPACK)
        TC5_element_add_item_backpack.click()
        TC5_element_add_item_back_light = self.driver.find_element(*MainPageLocator.ADD_ITEM_LABS_BIKE_LIGHT)
        TC5_element_add_item_back_light.click()
        TC5_element_shopping_cart = self.driver.find_element(*MainPageLocator.SHOPPING_CART)
        TC5_element_shopping_cart.click()
        TC5_element_checkout_button = self.driver.find_element(*MainPageLocator.CHECKOUT_BUTTON)
        TC5_element_checkout_button.click()
        TC5_element_firstname_checkout = self.driver.find_element(*MainPageLocator.CHECKOUT_FIRSTNAME)
        TC5_element_firstname_checkout.send_keys("Jamal")
        TC5_element_lastname_checkout = self.driver.find_element(*MainPageLocator.CHECKOUT_LASTNAME)
        TC5_element_lastname_checkout.send_keys("Balya")
        TC5_element_postal_code = self.driver.find_element(*MainPageLocator.POSTAL_CODE)
        TC5_element_postal_code.send_keys(13120)
        TC5_element_continue_button_checkout = self.driver.find_element(*MainPageLocator.CONTINUE_BUTTON_CHECKOUT)
        TC5_element_continue_button_checkout.click()
        TC5_element_finish_button_checkout = self.driver.find_element(*MainPageLocator.FINISH_BUTTON_CHECKOUT)
        TC5_element_finish_button_checkout.click()
