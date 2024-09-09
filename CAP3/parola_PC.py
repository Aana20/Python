"""
Parola unui PC este 7788. Creați un script care sa simuleze accesul la PC.
Introduceti parola: 7677
Parola gresita. Mai incercati.
Introduceti parola: 3432
Parola gresita. Mai incercati.
Introduceti parola: 7788
Acces permis.
Process finished with exit code 0
"""
parola="7788"
while True:
    incercare = input("Introduceti parola: ")
    if parola == incercare:
        print("Acces permis.")
        break
    else:
        print("Parola gresita. Mai incercati.")


