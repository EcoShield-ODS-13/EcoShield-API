def calcular_nivel_agua(distancia_sensor, distancia_maxima):

    nivel_agua = ((distancia_maxima - distancia_sensor) / distancia_maxima) *100

    if nivel_agua < 0:
        nivel_agua = 0

    if nivel_agua > 100:
        nivel_agua = 100

    return nivel_agua

def calcular_risco(chuva, distancia_sensor, distancia_maxima):

    nivel_agua = calcular_nivel_agua(distancia_sensor, distancia_maxima)

    risco = (0.5 * chuva +10)+(0.3 * nivel_agua)

    if risco >100:
        risco =100

    if risco >81:
        nivel = "CRÍTICO"
        status = "ALAGADA"
        cor = "red"
    elif risco >61:
        nivel = "ALTO"
        status = "RISCO ALTO"
        cor = "orange"
    else:
        nivel = "BAIXO"
        status = "SEGURA"
        cor = "green"

    return {
        "risco_percentual": round(risco, 2),
        "nivel": nivel,
        "status": status,
        "cor": cor,
        "nivel_agua_percentual": round(nivel_agua, 2),
        "distancia_sensor": distancia_sensor,
        "distancia_maxima": distancia_maxima
    }