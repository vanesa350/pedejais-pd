import pandas as pd

dati = pd.read_csv("agenti.csv", sep=";")

print("=" * 60)
print("1. UZDEVUMS - Dati ielādēti")
print("=" * 60)
print(f"Kopā ierakstu: {len(dati)}")
print(f"Kolonnas: {list(dati.columns)}")
print("\nPirmie 3 ieraksti:")
print(dati.head(3).to_string(index=False))

atlasite_tipi = ["Izglītības iestāde", "Valsts iestāde"]
filtreti = dati[dati["TIPS"].isin(atlasite_tipi)]

print("\n" + "=" * 60)
print("2. UZDEVUMS - Filtrēti pēc TIPS")
print("=" * 60)
print(f"Ierakstu skaits pēc filtrēšanas: {len(filtreti)}")
print("\nPirmie 3 ieraksti:")
print(filtreti.head(3).to_string(index=False))

riga = filtreti[filtreti["ADRESE"].str.contains("Rīga", na=False)][["NOSAUKUMS", "ADRESE"]]

print("\n" + "=" * 60)
print("3. UZDEVUMS - Iestādes Rīgā")
print("=" * 60)
print(f"Ierakstu skaits: {len(riga)}")
print("\nPirmie 3 ieraksti:")
print(riga.head(3).to_string(index=False))

sakartoti = riga.sort_values("NOSAUKUMS").reset_index(drop=True)

print("\n" + "=" * 60)
print("4. UZDEVUMS - Sakārtots alfabētiski pēc NOSAUKUMS")
print("=" * 60)
print("\nPirmie 5 ieraksti:")
print(sakartoti.head(5).to_string(index=False))

print("\n" + "=" * 60)
print("5. UZDEVUMS - Galīgais rezultāts (visi Rīgas ieraksti)")
print("=" * 60)
print(f"\nKopā: {len(sakartoti)} iestādes\n")
print(sakartoti.to_string(index=False))

'''
import requests

url = "https://restcountries.com/v3.1/all"
response = requests.get(url)

if response.status_code == 200:
    print("Atbilde saņemta veiksmīgi! Statusa kods:", response.status_code)
else:
    print("Kļūda! Statusa kods:", response.status_code)
    exit()

valstis = response.json()

print("\n--- 3. Visu valstu nosaukumi ---")
nosaukumi = [v["name"]["common"] for v in valstis if "name" in v and "common" in v["name"]]
for nosaukums in nosaukumi:
    print(nosaukums)

print("\n--- 4. Kopējais valstu skaits ---")
print(f"Valstu skaits: {len(valstis)}")

print("\n--- 5. Vidējais iedzīvotāju skaits ---")
iedzivotaji = [v["population"] for v in valstis if "population" in v]
videjais = sum(iedzivotaji) / len(iedzivotaji) if iedzivotaji else 0
print(f"Vidējais iedzīvotāju skaits: {videjais:,.0f}")

print("\n--- 6. Valsts ar vislielāko iedzīvotāju skaitu ---")
lielaka = max(valstis, key=lambda v: v.get("population", 0))
print(f"Valsts: {lielaka['name']['common']}, Iedzīvotāji: {lielaka['population']:,}")

print("\n--- 7. Kopējā platība ---")
platiba = [v["area"] for v in valstis if "area" in v]
kopeja_platiba = sum(platiba)
print(f"Kopējā platība: {kopeja_platiba:,.2f} km²")

print("\n--- 8. Latvijas informācija ---")
latvija = next((v for v in valstis if v["name"]["common"] == "Latvia"), None)
if latvija:
    apaksregions = latvija.get("subregion", "Nav pieejams")
    print(f"Apakšreģions: {apaksregions}")

    robezvalstis = latvija.get("borders", [])
    print(f"Robežvalstu kodi: {', '.join(robezvalstis) if robezvalstis else 'Nav'}")
else:
    print("Latvija netika atrasta datos.")
'''