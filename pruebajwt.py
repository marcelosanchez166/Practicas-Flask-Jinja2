import requests
import time
from flask import Flask, json, jsonify


for i in range(700):
    time.sleep(0.1)
    response= requests.get("http://192.168.220.213:30923/index")
    try:
        # Intenta obtener la respuesta en JSON
        data = response.json()
        print("JSON Response:", data)
    except requests.exceptions.JSONDecodeError:
        # Si falla, imprime la respuesta en texto
        print("Text Response:", response.text)
