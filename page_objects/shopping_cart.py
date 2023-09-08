import time
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from page_objects.base_page import BasePage

class ShoppingCart(BasePage):

    __add_1 = (By.XPATH, '//*[@id="add-to-cart-sauce-labs-backpack"]')
    __add_2 = (By.XPATH, '//*[@id="add-to-cart-sauce-labs-bike-light"]')
    __remove_2=(By.XPATH, '//*[@id="remove-sauce-labs-bike-light"]')
    __nro_items_add = (By.XPATH, '//*[@id="shopping_cart_container"]/a/span')

    def __init__(self, driver: WebDriver):
        # con herencia
        super().__init__(driver)

    def add_cart(self):
        super()._click(self.__add_1)
        super()._click(self.__add_2)

    def verify_add(self):
        if super()._find(self.__nro_items_add):
            resultado = "Items agregados correctamente"
        else:
            resultado = "Items NO agregados correctamente"
        return resultado

    def remove_product_from_cart(self):
        cart_after_remove = super()._get_text(self.__nro_items_add)
        super()._click(self.__remove_2)
        cart_befor_remove = super()._get_text(self.__nro_items_add)
        lst_cart = [cart_after_remove,cart_befor_remove]
        return lst_cart