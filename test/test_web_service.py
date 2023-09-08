import time
import datetime
import pytest
from page_objects.web_service import WebService
import requests
import os
import json


class TestWebService():
    @pytest.mark.webService

    def test_web_serice (self,request):
        start_web_servise = time.time()
        web_service = WebService()
        url_service = "https://www.mercadolibre.com.ar/menu/departments"
        respuesta = web_service.hacer_peticion_get(url_service)
        data = json.loads(respuesta)
        departamentos = data["departments"]
        nombres_de_departamentos = [departamento["name"] for departamento in departamentos]
        print(nombres_de_departamentos)
        end_web_servise = time.time()
        tiempo_total_shop = end_web_servise - start_web_servise
        minutes, seconds = divmod(tiempo_total_shop, 60)
        minutes = str(minutes).split(".")
        seconds = str(seconds).split(".")
        current_datetime = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        if respuesta:
            print(f"Respuesta recibida:{respuesta}")
            print(f'El/Los departamento/s que tiene Merdacdo libre es/son :{nombres_de_departamentos}')
            with open(request.getfixturevalue("report_html"), "a") as f:
                f.write(
                    f"<p>Respuesta recibida:{respuesta}</p>\n"
                    f"<p>f'El/Los departamento/s que tiene Merdacdo libre es/son :{nombres_de_departamentos}\n"
                    f"<p>Fecha de ejecuccion: {current_datetime},Duracion del test{minutes[0]} min : {seconds[0]} seg</p>\n"
                )
        else:
            print("No se pudo obtener una respuesta.")
            with open(request.getfixturevalue("report_html"), "a") as f:
                f.write(
                    f"<p>Respuesta recibida:{respuesta}</p>\n"
                    f"<p>No se pudo obtener una respuesta.\n"
                    f"<p>Fecha de ejecuccion: {current_datetime}, Duracion del test{minutes[0]} min : {seconds[0]} seg</p>\n"
                )

@pytest.fixture()
def report_html(request):
    dir_path = os.path.join(request.config.rootdir, 'reports')
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)
    report_path = os.path.join(dir_path,'report_web_service.html')
    yield report_path