=============================================
2.1. Darbinieki, kas pašlaik ir atvaļinājumā
=============================================

#No tabulas "darbinieki" atlasām vārdu un uzvārdu tikai tiem darbiniekiem, kuriem lauks "atvalinajuma" ir TRUE
SELECT vards, uzvards
FROM darbinieki
WHERE atvalinajuma = TRUE;


=============================================
2.2. Pasūtījumu kopējais skaits
=============================================

#Saskaita visus ierakstus tabulā "pasutijumi"
SELECT COUNT(*) AS pasutijumu_skaits
FROM pasutijumi;


=============================================
2.3. Katra darbinieka pasūtījumu kopējais skaits
=============================================


#Apvieno darbiniekus ar pasūtījumiem un saskaita, cik pasūtījumu ir katram darbiniekam
#LEFT JOIN nodrošina, ka parādās arī darbinieki bez pasūtījumiem
SELECT d.vards, d.uzvards, COUNT(p.id) AS pasutijumu_skaits
FROM darbinieki d
LEFT JOIN pasutijumi p ON p.darbinieka_id = d.id
GROUP BY d.id, d.vards, d.uzvards;


=============================================
2.4. Katra darbinieka pasūtījumu vislielākā summa
=============================================

#Atrod lielāko pasūtījuma summu katram darbiniekam
#MAX() funkcija izvēlas lielāko vērtību
SELECT d.vards, d.uzvards, MAX(p.summa) AS max_summa
FROM darbinieki d
LEFT JOIN pasutijumi p ON p.darbinieka_id = d.id
GROUP BY d.id, d.vards, d.uzvards;


=============================================
2.5. Katras kafejnīcas pasūtījumu vidējā summa
=============================================

#Apvieno kafejnīcas, darbiniekus, pasūtījumus un aprēķina vidējo pasūtījuma summu katrai kafejnīcai
#AVG() funkcija aprēķina vidējo vērtību
SELECT k.nosaukums, AVG(p.summa) AS videja_summa
FROM kafejnicas k
LEFT JOIN darbinieki d ON d.kafejnicas_id = k.id
LEFT JOIN pasutijumi p ON p.darbinieka_id = d.id
GROUP BY k.id, k.nosaukums;