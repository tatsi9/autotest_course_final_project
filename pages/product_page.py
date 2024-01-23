from .base_page import BasePage
from .locators import ProductPageLocators

class ProductPage(BasePage):
    def add_to_cart(self):
       add_to_cart_button = self.browser.find_element(*ProductPageLocators.ADD_TO_CART_BUTTON) 
       add_to_cart_button.click()

    def should_be_add_to_cart_button(self):
        assert self.is_element_present(*ProductPageLocators.ADD_TO_CART_BUTTON), "Add to cart button is not present"
    
    def should_be_added_to_cart_message(self):
        assert self.is_element_present(*ProductPageLocators.ADDED_TO_CART_MESSAGE), "Added-to-cart message is not present"
    
    def added_to_cart_message_is_correct(self):
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        added_to_cart_product_name = self.browser.find_element(*ProductPageLocators.ADDED_TO_CART_PRODUCT_NAME).text
        assert product_name == added_to_cart_product_name, "Incorrect message"

    def should_be_cart_total_message(self):
        assert self.is_element_present(*ProductPageLocators.CART_TOTAL_MESSAGE), "No cart total message"
    
    def cart_total_price_is_correct(self):
        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
        cart_total_price = self.browser.find_element(*ProductPageLocators.CART_TOTAL_MESSAGE_PRICE).text
        assert product_price == cart_total_price, "Incorrect cart total price"
        