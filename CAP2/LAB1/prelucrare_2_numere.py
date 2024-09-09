
"""
Se va cere input de la utilizator cu 2 numere. Se calculeaza:
a. Media numerelor
b. Impartirea numerelor in ordinea introdusa de catre utilizator (rezultatul trebuie sa
fie număr întreg)
c. Primul număr la puterea celui de-al doilea număr.
** Cand afisati rezultatele pe ecran, afișați-le dintr-o singura funcție print și folosiți
escape character pentru a delimita output-ul. Exemplu output:
Media numerelor este: 8.5
Impartirea numerelor este: 2
A la puterea b: 248832
"""

x=int(input("Primul numar este : "))
y=int(input("Al doilea numar este : "))

media=(x+y)/2
impartire=int(x/y)
puterea=x**y
print(f"Media numerelor este:{media} \n Imaprtirea este :{impartire} \n X la puterea Y: {puterea}\n" )

