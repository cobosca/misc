import requests
import sys

try:
    data = requests.get("https://www.data.gouv.fr/fr/datasets/r/cd743070-ad30-4e42-b815-5b527265de75")
except:
    sys.exit("API dati netika saņemti")
    
try:
    dataj = data.json()
except:
    sys.exit("Kļūda konvertējot par JSON datu tipu")
    
placi = []

for placis in dataj:
    try:
        free = int(placis["fields"]["dispo"])
        total = int(placis["fields"]["total"])
    except:
        sys.exit("Iespējama JSON struktūtras kļūda")
    if total!=0:
        perc_free = free/total
    if perc_free >= 0.2:
        placi.append(dict(placis=placis["fields"]["name"], brivs=perc_free))
    perc_free = 0

print("STĀVVIETU NOSKAUKUMI, KUROS VISMAZ 20% VIETU IR BRĪVAS:")
for placis in placi:
    print("\t-",placis["placis"], f"|| BRĪVS: ",round(float(placis["brivs"])*100), "%")

