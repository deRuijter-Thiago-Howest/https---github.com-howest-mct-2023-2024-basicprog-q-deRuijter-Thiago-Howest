# Ex02

# schrijf hier jouw functie
from typing import List
from typing import Dict

def maak_koppels(lijst_koppels:List[str], aantal_koppels:int) -> Dict[str,str]:
    resultaat = {}
    if aantal_koppels <= 4:

        for naam in lijst_koppels:  
            if naam not in resultaat.keys():
                for naam2 in lijst_koppels:
                    if naam2 not in resultaat.values():
                        if naam2 not in resultaat.keys():
                            resultaat[naam] = naam2


    return resultaat




# test jouw functie
print("💘 Koppels binnen Howest 💘")
studenten = ["Karel", "Ben", "Tim", "Ken", "Henk", "Lies", "Barbie", "Sandra", "Debbie"]
aantal_koppels = int(input("Hoeveel koppels moeten er gevormd worden?:> "))
# ...

koppels = print(f"De koppels van Howest zijn: \n{maak_koppels(studenten,aantal_koppels)}")