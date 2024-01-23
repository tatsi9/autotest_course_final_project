from selenium import webdriver
from selenium.webdriver.common.by import By 
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException     
from selenium.common.exceptions import NoAlertPresentException
import time
import math

class BasePage():
    def __init__(self, browser, url, timeout=10):  #timeout добавили на шаге 4.2.6
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)      #добавили на шаге 4.2.6

    def open(self):
        self.browser.get(self.url)     #открывает вебстраницу (вместо browser.get(link))


    def is_element_present(self, how, what):       #добавили на шаге 4.2.6
        try:
            self.browser.find_element(how, what)
        except (NoSuchElementException):
            return False
        return True                     # Метод для перехватывания исключения. args: how (css, id, xpath и тд), what (строку-селектор). try/except


    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        time.sleep(5)
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")

