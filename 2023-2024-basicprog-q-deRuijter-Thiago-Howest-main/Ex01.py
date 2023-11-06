# Ex01

# schrijf hier jouw functie
def calculate_love_score(naam1:str,naam2:str):
    result = []
    for letter in naam1:
        for letter2 in naam2:
            if letter in letter2:
                if letter not in result:
                    result.append(letter)

    aantal = len(result)
    lengte_woord1= len(naam1)
    lengte_woord2= len(naam2)
    gemiddelde_lengte = (lengte_woord1 + lengte_woord2) / 2
    score = ((aantal / gemiddelde_lengte) * 100)
   
    return round(score,1)
    

        
    

    # gemiddelde_lengte = (len(naam1) + len(naam2)) % 2
    # score = (teller % gemiddelde_lengte) * 100 
    # return teller





# test jouw functie 
eerste_naam = input("Geef een eerste naam op:> ")
tweede_naam = input("Geef een tweede naam op:> ")
# print(f"De match tussen beide personen bedraagt {calculate_love_score(eerste_naam, tweede_naam)}")
test = calculate_love_score(eerste_naam, tweede_naam)
print(f"De lovescore is:> {test}")


