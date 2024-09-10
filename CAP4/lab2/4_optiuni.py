"""
Se cere:
a. Input de la utilizator cu numere, care se vor aduna într-o listă cu elemente de tip
float. Numerele trebuie sa fie valide. Cand utilizatorul nu mai are numere de
introdus, va scrie x.
Introduceti numere. Cand sunteti gata, introduceti x.
Numar: 3
Numar: 5
Numar: 18.8
Numar: 2
Numar: 4
Numar: x
b. După introducerea numerelor, se va afișa un meniu cu 4 opțiuni: medie, suma,
puterea numerelor din lista, iesire. În funcție de ce introduce utilizatorul, se va
calcula rezultatul cu ajutorul funcțiilor din scheletul de mai sus și se va afișa.
Meniu:
1. Media numerelor
2. Suma numerelor
3. Puterea numerelor din lista de numere
4. Iesire
Introduceti optiunea dvs: 1
Rezultatul: 6.56

"""

def suma(lista):
    return sum(lista)
def medie(lista):
    if len(lista) == 0:
        return 0
    return sum(lista) / len(lista)

def putere(lista):
    # Ridicăm fiecare element la puterea 2 și returnăm lista rezultată
    return [num ** 2 for num in lista]
meniu = {
"1": medie,
"2": suma,
"3": putere
}
a=""
lista=[]
print("Introduceti numere. Cand sunteti gata, introduceti x.")
while True:
    a = input("Număr: ")
    if a == 'x':  # Oprirea introducerii numerelor
        break
    try:
        numar = float(a)  # Convertim inputul la float
        lista.append(numar)  # Dacă reușește conversia, adaugăm numărul în listă
    except ValueError:
        print("Nu ați introdus un număr valid.")  # Dacă conversia eșuează, afișăm un mesaj de eroare

while True:
    print("Meniu:\n1.Media numerelor\n2.Suma numerelor\n3.Puterea numerelor din lista de numere\n4.Iesire")
    optiune = input("Introduceti optiune: ")

    if optiune == "1":
        rezultat = medie(lista)
        print(f"Rezultatul: {rezultat:.2f}")
    elif optiune == "2":
        rezultat = suma(lista)
        print(f"Rezultatul: {rezultat}")
    elif optiune == "3":
        rezultat = putere(lista)
        print(f"Rezultatul: {rezultat}")
    elif optiune == "4":
        print("Ieșire din program.")
        break
    else:
        print("Opțiune invalidă. Încercați din nou.")
