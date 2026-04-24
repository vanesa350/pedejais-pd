import pandas as pd #importejam pandas biblioteku datu apstradei

dati = pd.read_csv("agenti.csv", sep=";") #nolasam csv failu, kur atdalitajs ir ;

print("=" * 60) #izvadam atdalitaju
print("Dati") #izvadam virsrakstu
print("=" * 60) #izvadam atdalitaju
print(f"Kopā ieraksti: {len(dati)}") #izvadam cik ierakstu kopa ir failā
print(f"Kolonnas: {list(dati.columns)}") #izvadam kolonnu nosaukumus
print("\nPirmie 3:") #izvadam tekstu
print(dati.head(3).to_string(index=False)) #izvadam pirmas 3 rindas bez indeksa

atlasite_tipi = ["Izglītības iestāde", "Valsts iestāde"] #saraksts ar tipiem ko gribam saglabt
filtreti = dati[dati["TIPS"].isin(atlasite_tipi)] #filtr. tikai tas rindas kur tips atbilst sarakstam

print("\n" + "=" * 60) #izvadam atdalitaju ar jaunu rindu
print("Filtrēti pēc tips") #izvadam virsrakstu
print("=" * 60) #izvadam atdalitaju
print(f"Ierakstu skaits pēc filtrēšanas: {len(filtreti)}") #izvadam cik ierakstu palika pec filtr
print("\nPirmie 3:") #izvadam tekstu
print(filtreti.head(3).to_string(index=False)) #izvadam pirmas 3 filtr rindas bez indeksa

riga = filtreti[filtreti["ADRESE"].str.contains("Rīga", na=False)][["NOSAUKUMS", "ADRESE"]] #filtr tikai riga un atlasam tikai nosaukuma un adreses kolonnas

print("\n" + "=" * 60) #izvadam atdalitaju
print("Iestādes Rīgā") #izvadam virsrakstu
print("=" * 60) #izvadam atdalitaju
print(f"Ierakstu skaits: {len(riga)}") #izvadam cik iestazu atrodas riga
print("\nPirmie 3:") #izvadam tekstu
print(riga.head(3).to_string(index=False)) #izvadam pirmas 3 rigas iestades bez indeksa

sakartoti = riga.sort_values("NOSAUKUMS").reset_index(drop=True) #sakartojam alfabetiski pec nosaukuma un resetejam indeksu

print("\n" + "=" * 60) #izvadam atdalitaju
print("Alfabētiski pēc nosaukuma") #izvadam virsrakstu
print("=" * 60) #izvadam atdalitaju
print("\nPirmie 5:") #izvadam tekstu
print(sakartoti.head(5).to_string(index=False)) #izvadam pirmas 5 sakartotās iestades bez indeksa

print("\n" + "=" * 60) #izvadam atdalitaju
print("Visi Rīgas ieraksti") #izvadam virsrakstu
print("=" * 60) #izvadam atdalitaju
print(f"\nKopā: {len(sakartoti)} iestādes\n") #izvadam kopa iestazu skaitu
print(sakartoti.to_string(index=False)) #izvadam visus sakārtotos ierakstus bez indeksa

'''
import requests #importejam requests biblioteku http pieprasijumiem

url = "https://restcountries.com/v3.1/all" #saglabajam api adresi mainiga
response = requests.get(url) #veicam get pieprasijumu uz api

if response.status_code == 200: #parbauda vai atbilde ir veiksmiga
    print("Atbilde saņemta, statusa kods:", response.status_code) #izvadam veiksmes zinojumu
else:
    print("Kļūda, statusa kods:", response.status_code) #izvadam kludas zinojumu
    exit() #partraucam programmu ja atbilde nav 200

valstis = response.json() #parveido atbildi par python sarakstu

print("\nVisu valstu nosaukumi") #izvadam virsrakstu
nosaukumi = [v["name"]["common"] for v in valstis if "name" in v and "common" in v["name"]] #no katras valsts iznemam visparpienemto nosaukumu
for nosaukums in nosaukumi: #ejam cauri katram nosaukumam
    print(nosaukums) #izvadam nosaukumu

print("\nKopējais valstu skaits") #izvadam virsrakstu
print(f"Valstu skaits: {len(valstis)}") #izvadam kopejo valstu skaitu

print("\nVidējais iedzīvotāju skaits") #izvadam virsrakstu
iedzivotaji = [v["population"] for v in valstis if "population" in v] #iznemam iedzivotaju skaitu no katras valsts
videjais = sum(iedzivotaji) / len(iedzivotaji) if iedzivotaji else 0 #aprekina videjo iedzivotaju skaitu
print(f"Vidējais iedzīvotāju skaits: {videjais:,.0f}") #izvadam videjo iedzivotaju skaitu

print("\nValsts ar vislielāko iedzīvotāju skaitu") #izvadam virsrakstu
lielaka = max(valstis, key=lambda v: v.get("population", 0)) #atrodam valsti ar lielako iedzivotaju skaitu
print(f"Valsts: {lielaka['name']['common']}, Iedzīvotāji: {lielaka['population']:,}") #izvadam valsts nosaukumu un iedzivotaju skaitu

print("\nKopējā platība") #izvadam virsrakstu
platiba = [v["area"] for v in valstis if "area" in v] #iznemam platību no katras valsts
kopeja_platiba = sum(platiba) #saskaitam visu valstu platibas
print(f"Kopējā platība: {kopeja_platiba:,.2f} km²") #izvadam kopejo platību

print("\nLatvija info") #izvadam virsrakstu
latvija = next((v for v in valstis if v["name"]["common"] == "Latvia"), None) #meklejam latviju saraksta
if latvija: #parbauda vai latvija tika atrasta
    apaksregions = latvija.get("subregion", "Nav pieejams") #iznemam apaksregionu
    print(f"Apakšreģions: {apaksregions}") #izvadam apaksregionu

    robezvalstis = latvija.get("borders", []) #iznemam robezvalstu kodus
    print(f"Robežvalstu kodi: {', '.join(robezvalstis) if robezvalstis else 'Nav'}") #izvadam robezvalstu kodus
else:
    print("Latvija netika atrasta") #izvadam zinojumu ja latvija nav datos
'''