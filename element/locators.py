from selenium.webdriver.common.by import By

class MainPageLocator(object):
    USERNAME = (By.ID, "user-name")
    PASSWORD = (By.ID, "password")
    BUTTON_LOGIN = (By.ID, "login-button")
    BURGER_MENU = (By.ID, "react-burger-menu-btn")
    LOGOUT_BUTTON = (By.ID, "logout_sidebar_link")
    ADD_ITEM_LABS_BACKPACK = (By.ID, "add-to-cart-sauce-labs-backpack")
    ADD_ITEM_LABS_BIKE_LIGHT = (By.ID, "add-to-cart-sauce-labs-bike-light")
    SHOPPING_CART = (By.XPATH, "/html/body/div/div/div/div[1]/div[1]/div[3]/a/span")
    REMOVE_BUTTON_BACKPACK = (By.ID, "remove-sauce-labs-backpack")
    REMOVE_BUTTON_BIKE_LIGHT = (By.ID, "remove-sauce-labs-bike-light")
    CHECKOUT_BUTTON = (By.ID, "checkout")
    CHECKOUT_FIRSTNAME = (By.ID, "first-name")
    CHECKOUT_LASTNAME = (By.ID, "last-name")
    POSTAL_CODE = (By.ID, "postal-code")
    CONTINUE_BUTTON_CHECKOUT = (By.ID, "continue")
    FINISH_BUTTON_CHECKOUT = (By.ID, "finish")




