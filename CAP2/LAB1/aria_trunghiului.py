"""
Pentru primul exercițiu se cere calcularea ariei unui triunghi folosind forma de mai jos,
cerand parametrii de la utilizator.
    A=1/2*bh
    b=baza h=inaltimea
a. Cereți input de la utilizator cu baza triunghiului și înălțimea acestuia. Asigurati-va
ca utilizatorul știe ce trebuie sa introduca, și stocati valorile cerute într-o variabila.
b. Creați o variabila care sa reprezinte rezultatul calculului.
c. Afișați tipul de data a variabilei rezultate
d. Afișați rezultatul funcției pe ecran.

"""

b=float(input("Baza triunghiului este : "))
h=float(input("Inaltimea triunghiului este : "))

aria=1/2*(b*h)
print(type(aria))
print(f"Aria este :{aria}")