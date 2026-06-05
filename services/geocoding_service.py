import requests
from config import url_mapa

def buscar_coordenadas(rua,bairro, cidade,estado):
    endereco = f"{rua},{bairro},{cidade},{estado}, Brasil"

    url = url_mapa

    params = {
        "q": endereco,
        "format": "json",
        "limit":1
    }

    headers = {
        "User-Agent":"EcoShieldAPI/1.0"
    }

    resposta = requests.get(url, params=params, headers=headers)

    dados = resposta.json()

    if len(dados) == 0:
        return None

    return {
        "endereco_encontrado": dados[0]["display_name"],
        "latitude": float(dados[0]["lat"]),
        "longitude": float(dados[0]["lon"]),
    }