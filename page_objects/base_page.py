import time

from selenium.common import NoSuchElementException, TimeoutException
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webdriver import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class BasePage:
    def __init__(self, driver: WebDriver):
        self._driver = driver

    def _find(self, locator: tuple) -> WebElement:
        return self._driver.find_element(*locator)

    def _type(self, locator: tuple, text: str, time: int = 10):
            self._wait_until_element_is_visible(locator, time)
            self._find(locator).send_keys(text)

    def _click(self, locator: tuple, time: int = 15):
        self._wait_until_element_is_visible(locator, time)
        self._find(locator).click()

    def _limpiar_campos(self, locator: tuple, time: int = 15):
        self._wait_until_element_is_visible(locator, time)
        self._find(locator).clear()

    def _wait_until_element_is_visible(self, locator: tuple, time: int = 5):
        wait = WebDriverWait(self._driver, time)
        try:
            wait.until(ec.visibility_of_element_located(locator))
            return True  # Elemento encontrado y visible
        except TimeoutException:
            return False  # Elemento no encontrado o no visible

    #def _wait_until_element_is_visible(self, locator: tuple, time: int = 5):
    #    wait = WebDriverWait(self._driver, time)
    #    wait.until(ec.visibility_of_element_located(locator))

    #def _wait_until_element_is_clickeabl(self, locator: tuple, time: int = 300):
    #    WebDriverWait(driver, time).until(ec.element_to_be_clickable((locator)))

    def _wait_until_element_is_invisible(self, locator: tuple, time: int = 10):
        wait = WebDriverWait(self._driver, time)
        wait.until(ec.invisibility_of_element_located(locator))

    def _wait_until_element_is_clickable(self, locator: tuple, time: int = 10):
        wait = WebDriverWait(self._driver, time)
        wait.until((ec.element_to_be_clickable(locator)))

    def _wait(self, locator: tuple, time: int = 200):
        try:
            wait = WebDriverWait(self._driver, time)
            element = wait.until(ec.visibility_of_element_located(locator))
            return element
        except TimeoutException:
            raise Exception("El elemento no se ha vuelto visible en la página web.")

    def _wait_trajeta_credito(self, locator: tuple, time: int = 200):
        try:
            wait = WebDriverWait(self._driver, time)
            element = wait.until(ec.visibility_of_element_located(locator))
            return element
        except TimeoutException:
            return False
    @property
    def current_url(self) -> str:
        return self._driver.current_url

    def _is_displayed(self, locator: tuple) -> bool:
        try:
            return self._find(locator).is_displayed()
        except NoSuchElementException or TimeoutException:
            return False

    def _open_url(self, url: str):
        self._driver.get(url)

    def _check_url (self,url:str):
        WebDriverWait(self._driver, 10).until(ec.url_to_be(url))

    def _exit(self):
        self._driver.close()

    def _get_text(self, locator: tuple, time: int = 25) -> str:
        try:
            self._wait_until_element_is_visible(locator, time)
            return self._find(locator).text
        except TimeoutException:
            return False

