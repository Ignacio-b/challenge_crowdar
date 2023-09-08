import time
from selenium.common import NoSuchElementException, TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from page_objects.base_page import BasePage


class Login(BasePage):

    __url = "https://www.saucedemo.com/"
    __usuario = (By.XPATH, "//input[contains(@id,'user-name')]")
    __contrasena = (By.XPATH, "//input[contains(@id,'password')]")
    __btn_login = (By.XPATH,'//*[@id="login-button"]')
    __confirmar_ingreso = (By.XPATH,"//div[@class='app_logo'][contains(.,'Swag Labs')]")
    __error_ingreso = (By.XPATH, "//h3[@data-test='error'][contains(.,'Epic sadface: Username and password do not match any user in this service')]")
    __nueva_url_esperada = "https://www.saucedemo.com/inventory.html"
    def __init__(self, driver: WebDriver):
        # con herencia
        super().__init__(driver)
        # sin herencia
        # self._driver = driver

    def open(self):
        # herencia
        super()._open_url(self.__url)
        # sin herencia
        # self.driver.get(self.__url)

    def login_page(self,usuario: str, contrasena: str ):
        super()._type(self.__usuario,usuario)
        super()._type(self.__contrasena,contrasena)
        super()._click(self.__btn_login)

    def result_login(self):
        time.sleep(2)
        try:
            super()._check_url(self.__nueva_url_esperada)
            resultado = "Login exitoso"
            return resultado
        except TimeoutException:
            resultado = super()._get_text(self.__error_ingreso)
            return resultado
            print('Tiempo de espera agotado. La URL no cambió o no se inició sesión correctamente.')


    def exit(self):
        super()._exit()
