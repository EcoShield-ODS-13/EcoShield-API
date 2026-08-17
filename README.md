# 🌧️ EcoShield API

O **EcoShield** é uma API desenvolvida em Python com o objetivo de auxiliar no monitoramento e análise de riscos de alagamentos em diferentes regiões.

A aplicação combina **dados climáticos, geolocalização, informações do OpenStreetMap e dados de sensores** para calcular um nível estimado de risco de alagamento de uma rua ou região.

O projeto foi desenvolvido durante a **Global Solution da FIAP**.

## 🚀 Funcionalidades

* Consulta de endereço e obtenção de latitude e longitude.
* Consulta de dados climáticos atuais.
* Cálculo do nível de risco de alagamento.
* Simulação de dados de sensor de nível da água.
* Suporte para integração com sensor físico.
* Busca de ruas de uma determinada região.
* Análise de risco de múltiplas ruas.
* API REST desenvolvida com FastAPI.

## 🛠️ Tecnologias utilizadas

* **Python**
* **FastAPI**
* **Uvicorn**
* **Requests**
* **PySerial**
* **Open-Meteo API**
* **OpenStreetMap / Nominatim**
* **Overpass API**

## 📂 Estrutura do projeto

```text
EcoShield-API/
│
├── services/
│   ├── arduino_service.py
│   ├── clima_service.py
│   ├── geocoding_service.py
│   ├── mapa_service.py
│   └── risco_service.py
│
├── config.py
├── main.py
├── bibliotecas
├── LICENSE
└── README.md
```

### Services

**`clima_service.py`**
Responsável pela consulta dos dados climáticos utilizando a Open-Meteo API.

**`geocoding_service.py`**
Transforma o endereço informado pelo usuário em coordenadas geográficas utilizando o Nominatim.

**`arduino_service.py`**
Responsável pelos dados relacionados ao sensor de nível da água. Atualmente o projeto permite trabalhar com dados simulados e possui estrutura para utilização de sensor real.

**`risco_service.py`**
Realiza o cálculo do nível da água e determina o risco estimado de alagamento.

**`mapa_service.py`**
Consulta ruas através da Overpass API e gera informações de risco para uma determinada área.

## ⚙️ Instalação

### 1. Clone o repositório

```bash
git clone <URL-DO-REPOSITORIO>
```

Entre na pasta:

```bash
cd EcoShield-API
```

### 2. Instale as dependências

```bash
pip install fastapi uvicorn requests pyserial
```

## ▶️ Executando o projeto

Execute:

```bash
uvicorn main:app --reload
```

A API ficará disponível localmente em:

```text
http://127.0.0.1:8000
```

A documentação interativa do FastAPI pode ser acessada em:

```text
http://127.0.0.1:8000/docs
```

## 🔗 Endpoints

### `GET /`

Verifica se a API está funcionando.

Exemplo de resposta:

```json
{
  "projeto": "EcoShield API"
}
```

### `GET /status-rua`

Realiza a análise de risco de uma rua específica.

Parâmetros:

```text
rua
bairro
cidade
estado
```

Exemplo:

```text
/status-rua?rua=Frei Gaspar&bairro=Centro&cidade=São Vicente&estado=SP
```

A API realiza o seguinte fluxo:

```text
Endereço
   ↓
Geolocalização
   ↓
Dados climáticos
   ↓
Dados do sensor
   ↓
Cálculo de risco
   ↓
Resultado
```

O resultado apresenta informações como:

* Coordenadas da localização
* Temperatura
* Umidade
* Precipitação
* Chuva
* Nível estimado da água
* Percentual de risco
* Classificação do risco

As classificações utilizadas são:

```text
BAIXO
MÉDIO
ALTO
CRÍTICO
```

### `GET /riscos-area`

Analisa as ruas existentes dentro de uma determinada área geográfica.

Parâmetros:

```text
lat_min
lat_max
lon_min
lon_max
```

A aplicação utiliza a **Overpass API** para encontrar as ruas da região e realiza o cálculo de risco para os pontos encontrados.

## 📡 Sensor

O EcoShield possui dois modos planejados de funcionamento:

```python
MODO_SENSOR = 0
```

**Modo 0 — Simulado**

Os dados de nível da água são simulados de acordo com as condições de chuva e precipitação.

```python
MODO_SENSOR = 1
```

**Modo 1 — Sensor real**

Destinado à leitura de dados provenientes de um sensor físico conectado ao sistema.

Atualmente, o modo simulado é utilizado como padrão e o único disponível.

## ⚠️ Observação

O EcoShield é um **projeto acadêmico e experimental**.

Os cálculos apresentados representam estimativas baseadas nos dados disponíveis e nas regras implementadas no projeto, portanto **não devem ser utilizados como sistema oficial de alerta de enchentes ou situações de emergência**.

## 👨‍💻 Desenvolvido por

<div>
  <a href="https://github.com/LuanSMF">
      <img src="https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white">
  </a>
  
  <a href="https://www.linkedin.com/in/luans%C3%A1muniz/">
      <img src="https://img.shields.io/badge/LinkedIn-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white">
  </a>
</div>

## 📄 Licença

Este projeto possui uma licença disponível no arquivo `LICENSE`.
