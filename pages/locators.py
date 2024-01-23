from selenium.webdriver.common.by import By

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTRATION_FORM = (By.CSS_SELECTOR, "#register_form")

class ProductPageLocators():
    ADD_TO_CART_BUTTON = (By.CSS_SELECTOR, ".btn-add-to-basket")
    ADDED_TO_CART_MESSAGE = (By.CSS_SELECTOR, "div.alertinner")
    ADDED_TO_CART_PRODUCT_NAME = (By.CSS_SELECTOR, "div.alert-success strong")
    PRODUCT_NAME = (By.CSS_SELECTOR, "div.product_main h1")
    CART_TOTAL_MESSAGE = (By.CSS_SELECTOR, ".alert-info")
    CART_TOTAL_MESSAGE_PRICE = (By.CSS_SELECTOR, ".alert-info .alertinner strong")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".product_main .price_color")