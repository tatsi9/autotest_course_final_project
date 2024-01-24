from selenium.webdriver.common.by import By

class BasePageLocators(): # добавлено в п.4.3.8
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_LINK = (By.PARTIAL_LINK_TEXT, "basket")
    ##BASKET_LINK = (By.CSS_SELECTOR, "a.btn.btn_default")#не работает

#class MainPageLocators():
    #LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

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

class BasketPageLocators():
    BASKET_PRODUCTS = (By.CSS_SELECTOR, "#basket_formset")
    BASKET_EMPTY_MESSAGE = (By.CSS_SELECTOR, "#content_inner>p")