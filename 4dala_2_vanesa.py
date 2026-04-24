#2.1 - izveidot pieprasijumu uz api
import requests #importejam requests biblioteku http pieprasijumiem

url = "https://restcountries.com/v3.1/all" #saglabajam api adresi mainiga
response = requests.get(url) #veicam get pieprasijumu uz api

#2.2 - parbauda vai atbilde ir korekta
if response.status_code == 200: #parbauda vai atbilde ir veiksmiga
    print("Atbilde saņemta, statusa kods:", response.status_code) #izvadam veiksmes zinojumu
else:
    print("Kļūda, statusa kods:", response.status_code) #izvadam kludas zinojumu
    exit() #partraucam programmu ja atbilde nav 200

valstis = response.json() #parveido atbildi par python sarakstu

#2.3 - izvadit visu valstu nosaukumus
print("\nVisu valstu nosaukumi") #izvadam virsrakstu
nosaukumi = [v["name"]["common"] for v in valstis if "name" in v and "common" in v["name"]] #no katras valsts iznemam visparpienemto nosaukumu
for nosaukums in nosaukumi: #ejam cauri katram nosaukumam
    print(nosaukums) #izvadam nosaukumu

#2.4 - izvadit kopejo valstu skaitu
print("\nKopējais valstu skaits") #izvadam virsrakstu
print(f"Valstu skaits: {len(valstis)}") #izvadam kopejo valstu skaitu

#2.5 - aprekina un izvadit videjo iedzivotaju skaitu
print("\nVidējais iedzīvotāju skaits") #izvadam virsrakstu
iedzivotaji = [v["population"] for v in valstis if "population" in v] #iznemam iedzivotaju skaitu no katras valsts
videjais = sum(iedzivotaji) / len(iedzivotaji) if iedzivotaji else 0 #aprekina videjo iedzivotaju skaitu
print(f"Vidējais iedzīvotāju skaits: {videjais:,.0f}") #izvadam videjo iedzivotaju skaitu

#2.6 - atrast un izvadit valsti ar lielako iedzivotaju skaitu
print("\nValsts ar vislielāko iedzīvotāju skaitu") #izvadam virsrakstu
lielaka = max(valstis, key=lambda v: v.get("population", 0)) #atrodam valsti ar lielako iedzivotaju skaitu
print(f"Valsts: {lielaka['name']['common']}, Iedzīvotāji: {lielaka['population']:,}") #izvadam valsts nosaukumu un iedzivotaju skaitu

#2.7 - saskaitit un izvadit visu valstu kopejo platību
print("\nKopējā platība") #izvadam virsrakstu
platiba = [v["area"] for v in valstis if "area" in v] #iznemam platību no katras valsts
kopeja_platiba = sum(platiba) #saskaitam visu valstu platibas
print(f"Kopējā platība: {kopeja_platiba:,.2f} km²") #izvadam kopejo platību

#2.8 - izvadit latvijas apaksregionu un robezvalstu kodus
print("\nLatvija info") #izvadam virsrakstu
latvija = next((v for v in valstis if v["name"]["common"] == "Latvia"), None) #meklejam latviju saraksta
if latvija: #parbauda vai latvija tika atrasta
    apaksregions = latvija.get("subregion", "Nav pieejams") #iznemam apaksregionu
    print(f"Apakšreģions: {apaksregions}") #izvadam apaksregionu

    robezvalstis = latvija.get("borders", []) #iznemam robezvalstu kodus
    print(f"Robežvalstu kodi: {', '.join(robezvalstis) if robezvalstis else 'Nav'}") #izvadam robezvalstu kodus
else:
    print("Latvija netika atrasta") #izvadam zinojumu ja latvija nav datos