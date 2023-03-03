from datetime import datetime
from requests import get

api = "http://api.nbp.pl/api/exchangerates/tables/A/{date}/?format=json"
print("Kalkulator walut")

while True:
    try:
        date = datetime.strptime(input("Wprowadz date (RRRR-MM-DD) > "), "%Y-%m-%d")
        break
    except ValueError:
        print("Data niepoprawna")

kursy = {currency["code"]: currency["mid"] for currency in get(api.format(date=f"{date:%Y-%m-%d}")).json()[0]["rates"]}

while True:
    currency = input("Wprowadz trzyliterowy kod waluty > ").upper()
    if currency in kursy.keys():
        break
    print("Waluta niepoprawna")

print(f"Kurs na dzien {date:%Y-%m-%d}: 1 {currency} = {kursy[currency]} PLN")
