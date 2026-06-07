from fastapi import FastAPI
from services.geocoding_service import buscar_coordenadas
from services.clima_service import consultar_clima
from services.risco_service import calcular_risco
from services.arduino_service import obter_dados_sensor
from services.mapa_service import gerar_riscos_area

app = FastAPI()

@app.get("/")
def home():
    return {
        "projeto": "EcoShield API",
    }

@app.get("/status-rua")
def status_rua(rua:str,bairro:str,cidade:str,estado:str):

    coordenadas = buscar_coordenadas(rua,bairro,cidade,estado)

    if coordenadas is None:
        return {
            "erro": "Endereço não encontrado",
        }

    clima = consultar_clima(
        coordenadas["latitude"],
        coordenadas["longitude"]
    )

    dados_sensor = obter_dados_sensor(
        clima["chuva"],
        clima["precipitacao"]
    )

    distancia_sensor = dados_sensor["distancia_sensor"]
    distancia_maxima = dados_sensor["distancia_maxima"]

    risco = calcular_risco(
        clima["chuva"],
        distancia_sensor,
        distancia_maxima
    )

    return {
        "rua": rua,
        "bairro": bairro,
        "cidade": cidade,
        "estado": estado,
        "endereco_encontrado": coordenadas["endereco_encontrado"],
        "latitude": coordenadas["latitude"],
        "longitude": coordenadas["longitude"],
        "clima": clima,
        "risco": risco,
        "modo_sensor": dados_sensor["modo"],
        "mensagem": "Consulta recebida com sucesso"
    }

@app.get("/riscos-area")
def riscos_area(lat_min:float, lat_max:float, lon_min:float, lon_max:float):
    pontos = gerar_riscos_area(lat_min, lat_max, lon_min, lon_max)

    return {
        "total": len(pontos),
        "pontos": pontos,
        "mensagem": "Riscos da área carregados com sucesso"
    }