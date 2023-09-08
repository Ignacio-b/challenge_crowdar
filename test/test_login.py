import time
import datetime
import pytest
from page_objects.login import Login
import requests
import os

class TestLoginPage():

    @pytest.mark.login
    @pytest.mark.parametrize("user, password", [("standard_user", "secret_sauce"), ("invalid_user", "invalid_password")])
    def test_valid_login(self,driver,user, password,request):
        start_login_valid = time.time()
        login = Login(driver)
        login.open()
        login.login_page(user, password)
        resultado = login.result_login()
        end_login_valid = time.time()
        tiempo_total_login_valid = end_login_valid - start_login_valid
        minutes, seconds = divmod(tiempo_total_login_valid, 60)
        minutes = str(minutes).split(".")
        seconds = str(seconds).split(".")
        current_datetime = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        if resultado == "Login exitoso":
            print(f"Test para login erroneo: resultado = {resultado}")
            with open(request.getfixturevalue("report_html"), "a") as f:
                f.write(
                    f"<p>Test para login correcto: resultado = {resultado}, Fecha de ejecuccion: {current_datetime}</p>\n"
                    f"<p>Duracion del test{minutes[0]} min : {seconds[0]} seg</p>\n"
                )
        else:
            print(f"Test para login erroneo: resultado = {resultado}")
            with open(request.getfixturevalue("report_html"), "a") as f:
                f.write(
                    f"<p>Test para login erroneo: resultado = {resultado}, Fecha de ejecuccion: {current_datetime}</p>\n"
                    f"<p>Duracion del test{minutes[0]} min : {seconds[0]} seg</p>\n"
                )

@pytest.fixture()
def report_html(request):
    dir_path = os.path.join(request.config.rootdir, 'reports')
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)
    report_path = os.path.join(dir_path, 'report_login.html')
    yield report_path