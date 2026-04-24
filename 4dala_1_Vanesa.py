import pandas as pd #importejam pandas biblioteku datu apstradei

#1.1 - lejupieladet, atvert datni un saglabjam datos
dati = pd.read_csv("agenti.csv", sep=";") #nolasam csv failu, kur atdalitajs ir ";"

print("=" * 60) #izvadam atdalitaju
print("Dati") #izvadam virsrakstu
print("=" * 60) #izvadam atdalitaju
print(f"Kopā ieraksti: {len(dati)}") #izvadam cik ierakstu kopa ir failā
print(f"Kolonnas: {list(dati.columns)}") #izvadam kolonnu nosaukumus
print("\nPirmie 3:") #izvadam tekstu
print(dati.head(3).to_string(index=False)) #izvadam pirmas 3 rindas bez indeksa

#1.2 - filtret tikai izglitibas un valsts iestades
atlasite_tipi = ["Izglītības iestāde", "Valsts iestāde"] #saraksts ar tipiem ko gribam saglabt
filtreti = dati[dati["TIPS"].isin(atlasite_tipi)] #filtr. tikai tas rindas kur tips atbilst sarakstam

print("\n" + "=" * 60) #izvadam atdalitaju ar jaunu rindu
print("Filtrēti pēc tips") #izvadam virsrakstu
print("=" * 60) #izvadam atdalitaju
print(f"Ierakstu skaits pēc filtrēšanas: {len(filtreti)}") #izvadam cik ierakstu palika pec filtr.
print("\nPirmie 3:") #izvadam tekstu
print(filtreti.head(3).to_string(index=False)) #izvadam pirmas 3 filtr. rindas bez indeksa

#1.3 - atlasit tikai rigas iestades
riga = filtreti[filtreti["ADRESE"].str.contains("Rīga", na=False)][["NOSAUKUMS", "ADRESE"]] #filtr. tikai riga un atlasam tikai nosaukuma un adreses kolonnas

print("\n" + "=" * 60) #izvadam atdalitaju
print("Iestādes Rīgā") #izvadam virsrakstu
print("=" * 60) #izvadam atdalitaju
print(f"Ierakstu skaits: {len(riga)}") #izvadam cik iestazu atrodas riga
print("\nPirmie 3:") #izvadam tekstu
print(riga.head(3).to_string(index=False)) #izvadam pirmas 3 rigas iestades bez indeksa

#1.4 - kartot alfabetiski pec nosaukuma
sakartoti = riga.sort_values("NOSAUKUMS").reset_index(drop=True) #sakartojam alfabetiski pec nosaukuma un resetejam indeksu

print("\n" + "=" * 60) #izvadam atdalitaju
print("Alfabētiski pēc nosaukuma") #izvadam virsrakstu
print("=" * 60) #izvadam atdalitaju
print("\nPirmie 5:") #izvadam tekstu
print(sakartoti.head(5).to_string(index=False)) #izvadam pirmas 5 sakartotās iestades bez indeksa

#1.5 - izvadit galigo rezultatu
print("\n" + "=" * 60) #izvadam atdalitaju
print("Visi Rīgas ieraksti") #izvadam virsrakstu
print("=" * 60) #izvadam atdalitaju
print(f"\nKopā: {len(sakartoti)} iestādes\n") #izvadam kopa iestazu skaitu
print(sakartoti.to_string(index=False)) #izvadam visus sakārtotos ierakstus bez indeksa