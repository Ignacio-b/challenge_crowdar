from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
#from page_objects.base_page import BasePage
import requests

class WebService():


    def hacer_peticion_get(self,url):
        try:
            response = requests.get(url)
            if response.status_code == 200:
                return response.text
            else:
                print(f"Error en la solicitud GET. Código de estado: {response.status_code}")
                return None
        except requests.exceptions.RequestException as e:
            print(f"Error en la solicitud GET: {str(e)}")
            return None