import requests
import config
from services.clima_service import consultar_clima
from services.arduino_service import obter_dados_sensor
from services.risco_service import  calcular_risco
from config import url_consulta

def buscar_ruas_osm(lat_min,lat_max,lon_min,lon_max):
    url  = url_consulta
    query =f"""
    [out:json][timeout:25];
    (
       way["highway"]["name"]({lat_min},{lon_min},{lat_max},{lon_max});
    );
    out geom;
    """

    headers = {
        "User-Agent": "EcoShieldAPI/1.0"
    }
    resposta = requests.post(
        url_consulta,
        data={"data": query},
        headers=headers,
        timeout=30
    )
    if resposta.status_code != 200:
        print("STATUS:", resposta.status_code)
        print("RESPOSTA:")
        return [{
            "erro": "Erro ao consultar OpenStreetMap",
            "status_code": resposta.status_code,
            "resposta": resposta.text
        }]

    data = resposta.json()
    ruas = []

    for elemento in data['elements']:
        nome_rua = elemento.get("tags",{}).get("name","Rua sem nome")
        geometria = elemento.get("geometry",[])

        if len(geometria) == 0:
            continue
        pontos_meio = geometria[len(geometria)//2]

        ruas.append({
            "nome": nome_rua,
            "latitude": pontos_meio["lat"],
            "longitude": pontos_meio["lon"],
            "geometria": geometria
        })

    return ruas

def gerar_riscos_area(lat_min,lat_max,lon_min,lon_max):
    ruas = buscar_ruas_osm(lat_min, lat_max, lon_min, lon_max)

    resultado = []

    for rua in ruas[:15]:

        if "latitude" not in rua or "longitude" not in rua:
            return {
                "erro": "Não foi possível carregar ruas do OpenStreetMap",
                "detalhes": rua
            }

        clima = consultar_clima(
            rua["latitude"],
            rua["longitude"]
        )

        dados_sensor = obter_dados_sensor(
            clima["chuva"],
            clima["precipitacao"],
        )

        risco = calcular_risco(
            clima["chuva"],
            dados_sensor["distancia_sensor"],
            dados_sensor["distancia_maxima"]
        )

        resultado.append({
            "rua": rua["nome"],
            "latitude": rua["latitude"],
            "longitude": rua["longitude"],
            "clima": clima,
            "risco": risco,
            "modo_sensor": dados_sensor["modo"]
       })

    return resultado