from selenium import webdriver
from selenium.webdriver.common.by import By
from pages.product_page import BasePage
from pages.product_page import ProductPage

import time


def test_guest_can_add_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_add_to_cart_button()
    page.add_to_cart()
    page.solve_quiz_and_get_code()
    time.sleep(5)
    page.added_to_cart_message_is_correct()
    page.cart_total_price_is_correct()