from selenium import webdriver
from selenium.webdriver.common.by import By
from pages.main_page import MainPage
from pages.login_page import LoginPage


def test_guest_can_go_to_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)       # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес 
    page.open()                          # открываем страницу
    page.go_to_login_page()              # доб.в шаге 4.2.9(2) 
    login_page = LoginPage(browser, browser.current_url) # доб.в шаге 4.2.9(2)
    #login_page = page.go_to_login_page()          #переходим на страницу логина изм. в шаге 4.2.9
    login_page.should_be_login_page()             #изм. в шаге 4.2.9



def test_guest_should_see_login_link(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)
    page.open()
    page.should_be_login_link()






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