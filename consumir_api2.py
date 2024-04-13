import requests

url = "https://jsonplaceholder.typicode.com/todos/1"
response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    print('Solicitud Exitosa')
    print("Código de estado:", response.status_code)
    print("Usuario:", data.get('userId'))
else:
    print("Error en la solicitud:", response.text)
