"""
Creati un script care cere input de la utilizator cu numarul de carti pe care doreste sa il
adauge in biblioteca. Pentru fiecare carte pe care utilizatorul doreste sa o adauge, cere
input cu numele cartii, autorul acesteia si anul publicarii. Creati cate un dictionar pentru
fiecare carte si creati o lista care sa contina aceste dictionare. Afisati dictionarele.
Sample code:
nr = input("Cati carti doriti sa adaugati in biblioteca?")
lista_carti = []
for i in range(int(nr)):
# todo
print(lista_carti)

Sample output:
======== Cartea 1 =========
Cati carti doriti sa adaugati la lista? 2
Numele cartii: Inteligenta materiei
Numele autorului: Constantin Dulcan
Anul publicarii: 1992
======== Cartea 2 =========
Numele cartii: Cosmos
Numele autorului: Carl Sagan
Anul publicarii:1980
Cartile dvs sunt:
{'nume': 'Inteligenta materiei', 'autor': 'Constantin Dulcan',
'an': '1992'}
{'nume': 'Cosmos', 'autor': 'Carl Sagan', 'an': '1980'}
Process finished with exit code 0
"""
nr = input("Cati carti doriti sa adaugati in biblioteca? ")
lista_carti = []

for i in range(int(nr)):
    print(f"======== Cartea {i + 1} =========")
    nume = input("Numele cartii: ")
    autor = input("Numele autorului: ")
    an = input("Anul publicarii: ")

    carte = {
        'nume': nume,
        'autor': autor,
        'an': an
    }

    lista_carti.append(carte)

print("Cartile dvs sunt:")
for carte in lista_carti:
    print(carte)
