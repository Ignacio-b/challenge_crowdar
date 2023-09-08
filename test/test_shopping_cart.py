import time
import datetime
import pytest
from page_objects.login import Login
from page_objects.shopping_cart import ShoppingCart
import requests
import os

class TestShoppingCart():


    @pytest.mark.shop
    @pytest.mark.parametrize("user, password",[("standard_user", "secret_sauce")])
    def test_add_to_cart(self,driver,user,password,request):
        start_shop = time.time()
        login = Login(driver)
        login.open()
        login.login_page(user,password)
        shop = ShoppingCart(driver)
        shop.add_cart()
        resultado = shop.verify_add()

        #si se borra de la linea 24 a la 33 el test andara con normalidad
        try:
            # Añade una aserción que siempre fallará
            assert False, "Esta prueba falla a propósito"
        except AssertionError:
            # Captura de pantalla cuando la aserción falla
            screenshot_dir = os.path.join(os.getcwd(), 'screenshots')
            if not os.path.exists(screenshot_dir):
                os.makedirs(screenshot_dir)
            screenshot_path = os.path.join(screenshot_dir, f"{request.node.name}.png")
            driver.save_screenshot(screenshot_path)

        end_shop = time.time()
        tiempo_total_shop = end_shop - start_shop
        minutes, seconds = divmod(tiempo_total_shop, 60)
        minutes = str(minutes).split(".")
        seconds = str(seconds).split(".")
        current_datetime = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f"Test para shopping_cart fue correcto: resultado = {resultado}, Fecha de ejecuccion: {current_datetime}")
        with open(request.getfixturevalue("report_html"), "a") as f:
            f.write(
                f"<p>Test para shopping_cart fue correcto: resultado = {resultado}, Fecha de ejecuccion: {current_datetime}</p>\n"
                f"<p>Duracion del test{minutes[0]} min : {seconds[0]} seg</p>\n"
            )

    @pytest.mark.shop
    @pytest.mark.parametrize("user, password", [("standard_user", "secret_sauce")])
    def test_add_and_remove_to_cart(self,driver,user,password,request):
        start_shop = time.time()
        login = Login(driver)
        login.open()
        login.login_page(user,password)
        shop = ShoppingCart(driver)
        shop.add_cart()
        resultado = shop.verify_add()
        nro_cart = shop.remove_product_from_cart()
        end_shop = time.time()
        tiempo_total_shop = end_shop - start_shop
        minutes, seconds = divmod(tiempo_total_shop, 60)
        minutes = str(minutes).split(".")
        seconds = str(seconds).split(".")
        current_datetime = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f"Test para _add_and_remove_to_cart fue correcto: se sumaron {nro_cart[0]} producto al carrito y se elimino uno y quedaron {nro_cart[1]}")
        with open(request.getfixturevalue("report_html"), "a") as f:
            f.write(
                f"<p>Test para _add_and_remove_to_cart fue correcto: se sumaron {nro_cart[0]} producto al carrito y se elimino uno y quedaron {nro_cart[1]}</p>\n"
                f"<p>Fecha de ejecuccion: {current_datetime}</p>\n"
                f"<p>Duracion del test{minutes[0]} min : {seconds[0]} seg</p>\n"
            )
@pytest.fixture()
def report_html(request):
    dir_path = os.path.join(request.config.rootdir, 'reports')
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)
    report_path = os.path.join(dir_path, 'report_shopping_cart.html')
    yield report_path
