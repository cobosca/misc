import requests
import sys

ab_punkti = []
riepu_punkti = []
metala_punkti = []

try:
    data = requests.get("https://data.gov.lv/dati/lv/api/3/action/datastore_search?resource_id=92ac6e57-c5a5-444e-aaca-ae90c120cc3d&limit=2000").json()
except:
    sys.exit("Something wrong with request")

for punkts in data["result"]["records"]:
    if punkts["8 : Baterijas un akumulatori"] == "x":
        ab_punkti.append(punkts["adrese"])
    if punkts["10 : Nolietotās riepas"] == "x":
        riepu_punkti.append(punkts["adrese"])
    if punkts["3 : Metāls"] == "x":
        metala_punkti.append(punkts["adrese"])

print("AB PUNKTI: ")
if len(ab_punkti) > 0:
    for punkts in ab_punkti:
        print(f"\t-{punkts}")
else:
    print("\n\t!NAV PIEEJAMS NEVIENS PUNKTS!\n")

print("RIEPU PUNTKI: ")
if len(riepu_punkti) > 0:
    for punkts in riepu_punkti:
        print(f"\t-{punkts}")
else:
    print("\n\t!NAV PIEEJAMS NEVIENS PUNKTS!\n")
        
print("METĀLA PUNKTI: ")
if len(metala_punkti) > 0:
    for punkts in metala_punkti:
        print(f"\t-{punkts}")
else:
    print("\n\t!NAV PIEEJAMS NEVIENS PUNKTS!\n")