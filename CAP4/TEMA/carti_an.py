"""
Completati sciptul exercitiului anterior in felul urmator:
- Cereti input de la utilizator cu un an de publicatie si afisati toate cartile aparute
dupa anul respectiv
Sample output:
Cartile dvs sunt:
{'nume': 'Inteligenta materiei', 'autor': 'Constantin Dulcan',
'an': '1992'}
{'nume': 'Cosmos', 'autor': 'Carl Sagan', 'an': '1980'}
Anul: 1990
Inteligenta materiei a fost publicat dupa 1990.
Process finished with exit code 0
"""

# Cerem utilizatorului să introducă numărul de cărți
nr = input("Cati carti doriti sa adaugati in biblioteca? ")
lista_carti = []

# Adăugăm informațiile despre fiecare carte
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

# Afișăm lista cărților
print("Cartile dvs sunt:")
for carte in lista_carti:
    print(carte)

# Cerem utilizatorului să introducă anul de publicare pentru filtrare
an_de_publicare = int(input("Anul: "))

# Afișăm cărțile publicate după anul introdus
for carte in lista_carti:
    if int(carte['an']) > an_de_publicare:
        print(f"{carte['nume']} a fost publicat dupa {an_de_publicare}.")
