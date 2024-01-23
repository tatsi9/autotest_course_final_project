from selenium import webdriver
from selenium.webdriver.common.by import By
from pages.product_page import BasePage
from pages.product_page import ProductPage

import time
import pytest

@pytest.mark.parametrize('promo_offer', ["?promo=newYear", "?promo=offer0", "?promo=offer1", "?promo=offer2", "?promo=offer3", "?promo=offer4", "?promo=offer5", "?promo=offer6", pytest.param("?promo=offer7", marks=pytest.mark.xfail), "?promo=offer8", "?promo=offer9"])

def test_guest_can_add_product_to_basket(browser, promo_offer):
    
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/{promo_offer}"

    #link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"

    page = ProductPage(browser, link)
    page.open()
    page.should_be_add_to_cart_button()
    page.add_to_cart()
    page.solve_quiz_and_get_code()
    time.sleep(5)
    page.added_to_cart_message_is_correct()
    page.cart_total_price_is_correct()