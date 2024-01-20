from selenium.common.exceptions import NoSuchElementException     


class BasePage():
    def __init__(self, browser, url, timeout=10):  #timeout добавили на шаге 4.2.6
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)      #добавили на шаге 4.2.6

    def open(self):
        self.browser.get(self.url)     #открывает вебстраницу (вместо browser.get(link))

    
    # Метод для перехватывания исключения. Аргументы: как искать (css, id, xpath и тд) и что искать (строку-селектор). Конструкция try/except

    def is_element_present(self, how, what):       #добавили на шаге 4.2.6
        try:
            self.browser.find_element(how, what)
        except (NoSuchElementException):
            return False
        return True