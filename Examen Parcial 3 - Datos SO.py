import requests

def get_system_info():
    url = "https://api.whatismybrowser.com/api/v2/user_agent_parse"
    user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
    headers = {
        "Content-Type": "application/json",
        "X-API-KEY": "fccb124ad2fcd3da6c84d481a8a529bf"
    }
    data = {
        "user_agent": user_agent
    }
    response = requests.post(url, headers=headers, json=data)
    if response.status_code == 200:
        system_info = response.json()["parse"]
        return format_system_info(system_info)
    else:
        print("Error al obtener los datos del sistema.")
        return None

def format_system_info(system_info):
    formatted_info = {
        "Navegador": system_info["software"],
        "Versión del navegador": system_info["software_version"],
        "Sistema operativo": system_info["operating_system"],
        "Versión del sistema operativo": system_info["operating_system_version"],
        "Plataforma": system_info["simple_operating_platform_string"],
        "User Agent": system_info["user_agent"]
    }
    return formatted_info

def main():
    system_info = get_system_info()
    if system_info:
        print("Datos del sistema:")
        for key, value in system_info.items():
            print(f"{key}: {value}")
    else:
        print("No se pudieron obtener los datos del sistema.")

if __name__ == "__main__":
    main()