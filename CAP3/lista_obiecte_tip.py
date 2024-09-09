"""
Creați o lista obiecte = [“Masa”, 5, “Scaun”, 4.5, [5,6,7],8]. Parcurgeți lista de obiecte și
afișați tipul fiecăruia. Challenge: Afișați tipul obiectelor în felul următor:
Tipul obiectului Masa este str
Tipul obiectului 5 este int
"""

lista=["Masa", 5, "Scaun", 4.5, [5,6,7],8]
for i in range(0,len(lista)):
    print(f"Tipul obiectului: {lista[i]} este: {type(lista[i])}")