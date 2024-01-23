from selenium import webdriver
from selenium.webdriver.common.by import By
from pages.product_page import BasePage
from pages.product_page import ProductPage
from pages.login_page import LoginPage
import time
import pytest

#@pytest.mark.parametrize('promo_offer', ["?promo=newYear", "?promo=offer0", "?promo=offer1", "?promo=offer2", "?promo=offer3", "?promo=offer4", "?promo=offer5", "?promo=offer6", pytest.param("?promo=offer7", marks=pytest.mark.xfail), "?promo=offer8", "?promo=offer9"])

@pytest.mark.parametrize('promo_offer', ["?promo=newYear"])
def test_guest_can_add_product_to_basket(browser, promo_offer):
    
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/{promo_offer}"

    #link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"

    page = ProductPage(browser, link)
    page.open()
    page.should_be_add_to_cart_button()
    #page.should_not_be_added_to_cart_message()
    page.add_to_cart()
    page.solve_quiz_and_get_code()
    time.sleep(5)
    page.should_be_added_to_cart_message()
    page.added_to_cart_message_is_correct()
    page.cart_total_price_is_correct()
    #page.should_disappear_added_to_cart_message()


#новые тесты из п.4.3.8 (кнопка "войти" должна быть видна с любой страницы):

def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()

def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()


# новые НЕГАТИВНЫЕ тесты из задания 4.3.6:

#def test_guest_cant_see_success_message(browser):
#    link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/"
#    page = ProductPage(browser, link)
#    page.open()
#    page.should_not_be_added_to_cart_message()

#def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
#    link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/"
#    page = ProductPage(browser, link)
#    page.open()
#    page.add_to_cart()
#    page.should_not_be_added_to_cart_message()
        
#def test_message_disappeared_after_adding_product_to_basket(browser):
#    link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/"
#    page = ProductPage(browser, link)
#    page.open()
#    page.add_to_cart()
#    page.should_disappear_added_to_cart_message()
    
        

