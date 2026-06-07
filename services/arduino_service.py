import  random
from config import(MODO_SENSOR,DISTANCIA_MAXIMA_SIMULADA )

def simular_distancia_sensor(chuva,  precipitacao, distancia_maxima=30):
    chuva_total = chuva + precipitacao

    if chuva_total <= 0:
        nivel_agua_cm  = 0
    elif chuva_total <= 2:
        nivel_agua_cm = random.uniform(2, 6)
    elif chuva_total <= 10:
        nivel_agua_cm = random.uniform(5, 12)
    elif chuva_total <= 25:
        nivel_agua_cm = random.uniform(10, 22)
    else:
        nivel_agua_cm = random.uniform(20, 30)

    fator_rua = random.uniform(0.75, 1.25)

    nivel_agua_cm = nivel_agua_cm * fator_rua
    nivel_agua_cm = max(0, min(nivel_agua_cm, distancia_maxima))

    DISTANCIA_SENSOR_SIMULADA = distancia_maxima - nivel_agua_cm

    return round(DISTANCIA_SENSOR_SIMULADA,2)

def obter_dados_sensor(chuva=0,precipitacao=0):

    if MODO_SENSOR == 0:
        DISTANCIA_SENSOR_SIMULADA = simular_distancia_sensor(chuva, precipitacao,DISTANCIA_MAXIMA_SIMULADA)

        return {
            "distancia_sensor": DISTANCIA_SENSOR_SIMULADA,
            "distancia_maxima": DISTANCIA_MAXIMA_SIMULADA,
            "modo": "SIMULADO"
        }
    elif MODO_SENSOR == 1:

        distancia_sensor =  ler_arduino()

        return {
            "distancia_sensor":  distancia_sensor,
            "distancia_maxima": 30,
            "modo": "REAL"
        }