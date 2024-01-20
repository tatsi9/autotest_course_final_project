from .base_page import BasePage
from selenium.webdriver.common.by import By
from .locators import MainPageLocators             # урок 4.2.7
from .login_page import LoginPage


class MainPage(BasePage):
    def go_to_login_page(self):
        login_link = self.browser.find_element(*MainPageLocators.LOGIN_LINK)
        #login_link = self.browser.find_element(By.CSS_SELECTOR, "#login_link")
        login_link.click()
        #return LoginPage(browser=self.browser, url=self.browser.current_url) #проинициализировать новый объект Page и вернуть его (добавлена в шаге 4.2.9)

    # версия из урока 4.2.6:
    def should_be_login_link(self):
        assert self.is_element_present(*MainPageLocators.LOGIN_LINK), "Login link is not presented"
        #assert self.is_element_present(By.CSS_SELECTOR, "#login_link"), "Login link is not presented"




        #assert self.is_element_present(By.CSS_SELECTOR, "login_link_invalid"), "Login link is not presented"  # неправильный селектор для проверки работы assert

# первая версия:
#    def should_be_login_link(self):
#        self.browser.find_element(By.CSS_SELECTOR, "#login_link_invalid")
