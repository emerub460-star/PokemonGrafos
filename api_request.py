# api_requests.py
import requests

class APIRequest:
    def __init__(self, url):
        self.url = url

    def obtener_datos(self):
        """Obtiene los datos JSON desde la API"""
        try:
            response = requests.get(self.url, timeout=10)
            response.raise_for_status()
            data = response.json()
            return data["chain"]
        except requests.exceptions.RequestException as e:
            print(" Error al obtener datos de la API:", e)
            return None
