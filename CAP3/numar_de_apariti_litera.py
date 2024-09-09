"""
 Luați ca input de la utilizator un cuvant si afisati numarul ocurentei primei litere din
cuvant. Exemplu:
Introduceti un cuvant (fara majuscule): rabdare
r apare de 2 ori.

"""
from itertools import count

cuvant=input("Inreoduceti un cuvant (fara majuscule):  ")
count=0
for i in range(0,len(cuvant)):
    if cuvant[0] == cuvant[i]:
        count+=1;
print(f"{cuvant[0]} apare de {count} ori")
