import requests

API_KEY = "9bc6eb156100e4e2271fa5d3"

def get_exchange_rates():
    url = f"https://api.exchangerate-api.com/v4/latest/MXN?key={API_KEY}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()["rates"]
    else:
        print("Error al obtener las tasas de cambio.")
        return None
def convert_currency(amount, to_currency, exchange_rates):
    if to_currency in exchange_rates:
        rate_to = exchange_rates[to_currency]
        converted_amount = amount * rate_to
        return converted_amount
    else:
        print("Moneda no soportada.")
        return None

def main():
    exchange_rates = get_exchange_rates()
    if exchange_rates:
        print("Tasas de cambio obtenidas correctamente.")
        
        amount = float(input("Introduce la cantidad a convertir (en MXN): "))
        to_currency = input("Introduce la moneda de destino (USD o EUR): ").upper()

        converted_amount = convert_currency(amount, to_currency, exchange_rates)
        if converted_amount is not None:
            print(f"{amount} MXN equivale a {converted_amount:.2f} {to_currency}.")
    else:
        print("No se pudo obtener las tasas de cambio.")

if __name__ == "__main__":
    main()

