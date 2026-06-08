import requests

def consultar_clima(latitude, longitude):
    try:
        url = (
            f"https://api.open-meteo.com/v1/forecast?"
            f"latitude={latitude}&longitude={longitude}"
            f"&current=temperature_2m,relative_humidity_2m,precipitation,rain"
        )

        resposta = requests.get(url, timeout =10)
        dados = resposta.json()

        atual = dados["current"]

        return {
            "temperatura": atual["temperature_2m"],
            "umidade": atual["relative_humidity_2m"],
            "precipitacao": atual["precipitation"],
            "chuva": atual["rain"]
        }
    except Exception as e:
        print("Erro Open-Meteo:", e)

        return {
            "temperatura": 0,
            "umidade": 0,
            "precipitacao": 0,
            "chuva": 0
        }