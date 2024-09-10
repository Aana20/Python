"""
Într-un birou se afla 3 PC-uri. Creați un script care sa ceara admin si user pentru fiecare
din cele 3 PC-uri si sa mapeze user-ul fiecărui PC cu parola acestuia într-un dictionar.
Afișați credentialele în formatul următor:
Introduceti utilizatorul PC-ului 1:
admin1
Introduceti parola PC-ului 1:
passme1
Introduceti utilizatorul PC-ului 2:
admin2
Introduceti parola PC-ului 2:
passme2
Introduceti utilizatorul PC-ului 3:
admin3
Introduceti parola PC-ului 3:
passme3
admin1 -> passme1
admin2 -> passme2
admin3 -> passme3
Process finished with exit code 0
"""


def colecteaza_credentiale():
    credentiale = {}


    for i in range(1, 4):
        utilizator = input(f"Introduceti utilizatorul PC-ului {i}: ")
        parola = input(f"Introduceti parola PC-ului {i}: ")

        credentiale[utilizator] = parola


    for utilizator, parola in credentiale.items():
        print(f"{utilizator} -> {parola}")



colecteaza_credentiale()