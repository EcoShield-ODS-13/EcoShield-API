from fastapi import FastAPI
from services.geocoding_service import buscar_coordenadas
from services.clima_service import consultar_clima
from services.risco_service import calcular_risco
from services.arduino_service import obter_dados_sensor

app = FastAPI()

@app.get("/")
def home():
    return {
        "projeto": "EcoShield API",
    }

@app.get("/status-rua")
def status_rua(rua:str,bairro:str,cidade:str,estado:str):

    dados_sensor = obter_dados_sensor()
    distancia_sensor = dados_sensor["distancia_sensor"]
    distancia_maxima = dados_sensor["distancia_maxima"]

    coordenadas = buscar_coordenadas(rua,bairro,cidade,estado)

    if coordenadas is None:
        return {
            "erro": "Endereço não encontrado",
        }

    clima = consultar_clima(
        coordenadas["latitude"],
        coordenadas["longitude"]
    )

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