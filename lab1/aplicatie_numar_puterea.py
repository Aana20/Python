"""
Creați o aplicație care sa ceara input de la utilizator cu un număr. Creați o funcție care
sa ia ca parametru numărul introdus de către utilizator si sa calculeze puterea acestuia.
Cereți input de la utilizator în interiorul unei bucle infinite. Dacă utilizatorul dorește sa
iasa, trebuie sa scrie q.
"""

numar=int(input("Introduceti un numar: "))

def puterea(n):
    print(f"Puterea numarului este:  {n**n}\n")
    a=input("daca doriti sa iesiti tastati: 'q' :")
    if a == "q":
        print("gata")
    else:
        print("Nu e o optiune")

puterea(numar)