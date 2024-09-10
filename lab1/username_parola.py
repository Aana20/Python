"""
1. Cereți input de la utilizator cu username și parola dorită. Se cere o funcție care sa
verifice dacă are lungimea de minim 7 caractere, conține o cifra și una din următoarele
caractere: !,@,%.
Exemplu:
Introduceti o parola: hcjdfhks
Parola trebuie sa contina una din urmatoarele caractere: %, !, @.
Parola trebuie sa contina o cifra.
Introduceti o parola: Iosido
Parola trebuie sa contina una din urmatoarele caractere: %, !, @.
Parola trebuie sa contina o cifra.
Parola trebuie sa aiba lungimea mai mare de 7 caractere.
Introduceti o parola: Iosdis5
Parola trebuie sa contina una din urmatoarele caractere: %, !, @.
Introduceti o parola: Isidjsdaj%3
Parola este in regula.
Process finished with exit code 0
Challenge: În scriptul anterior se mai adaugă o condiție la parola: Parola trebuie să
înceapă cu litera mare. Verificati daca parola introdusă de către utilizator începe cu o
litera mare.

"""
import re
user=input("Introduceti un username: ")

def verificare_parola(p):
    if len(p) < 7:
        print("Trebuie sa contina minim 7 caractere ,mai incercati")
    if not any(char.isdigit() for char in p):
        print("Parola trebuie sa contina o cifra.")


    if not re.search(r'[!%@]', p):
        print("Parola trebuie sa contina una din urmatoarele caractere: %, !, @.")

    print("Parola este in regula.")
      


def cere_parola():
    parola_valida = False
    while not parola_valida:
        parola = input("Introduceti o parola: ")
        parola_valida = verificare_parola(parola)

cere_parola()