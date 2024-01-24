from selenium import webdriver
from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from pages.main_page import MainPage
from pages.login_page import LoginPage
from pages.basket_page import BasketPage
import pytest


@pytest.mark.login_guest
class TestLoginFromMainPage():

    def test_guest_can_go_to_login_page(self, browser):
        link = "http://selenium1py.pythonanywhere.com/"
        page = MainPage(browser, link)       # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес 
        page.open()                          # открываем страницу
        page.go_to_login_page()              # доб.в шаге 4.2.9(2) 
        login_page = LoginPage(browser, browser.current_url) # доб.в шаге 4.2.9(2)
        #login_page = page.go_to_login_page()          #переходим на страницу логина изм. в шаге 4.2.9
        login_page.should_be_login_page()


    def test_guest_should_see_login_link(self, browser):
        link = "http://selenium1py.pythonanywhere.com/"
        page = MainPage(browser, link)
        page.open()
        page.should_be_login_link()



#def test_guest_can_go_to_login_page(browser): #перенесен выше в класс TestLoginFromMainPage
#def test_guest_should_see_login_link(browser):#перенесен выше в класс TestLoginFromMainPage


# тест из п.4.3.10 - переход на страницу корзины с главной страницы
def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)
    page.open()
    page.go_to_basket_page()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.should_be_empty_basket()
    basket_page.should_be_empty_basket_message()
    




# версия из шага 4.1.8 с отдельной функцией def go_to_login_page

#def go_to_login_page(browser):
#    login_link = browser.find_element_by_css_selector("#login_link")
#    login_link.click()

#def test_guest_can_go_to_login_page(browser):
#    link = "http://selenium1py.pythonanywhere.com/" 
#    browser.get(link)
#    go_to_login_page(browser)


# первоначальная версия из шага 4.1.6
#def test_guest_can_go_to_login_page(browser):
#    link = "http://selenium1py.pythonanywhere.com/"
#    browser.get(link)
#    login_link = browser.find_element(By.CSS_SELECTOR, "#login_link")
#    login_link.click()