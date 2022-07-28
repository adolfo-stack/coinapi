import requests


apikey = "2073DF1E-6166-4B5B-8481-B2E5E9F37774"
cabeceras = {
    "X-CoinAPI-Key": apikey
} 
api_url = "https://rest.coinapi.io"
endpoint = "/v1/exchanges"

url = api_url + endpoint

respuesta = requests.get(url, headers=cabeceras)
codigo = respuesta.status_code

if codigo == 200:
    print("El resultado de la consulta es:")
    print(respuesta.text)
else:
    print("La petición a la API ha fallado")
    print(f"Código del error {codigo}")
    print(f"Razón del error {respuesta.reason}")
    print(respuesta.text)
