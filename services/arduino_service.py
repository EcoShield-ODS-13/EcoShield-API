from config import(
    MODO_SENSOR,
    DISTANCIA_SENSOR_SIMULADA,
    DISTANCIA_MAXIMA_SIMULADA,
)

def obter_dados_sensor():

    if MODO_SENSOR == 0:

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