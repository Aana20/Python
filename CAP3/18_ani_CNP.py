"""
Luați input de la utilizator primele 7 cifre ale CNP-ului. Găsiți o metoda sa calculați și sa
afisati dacă utilizatorul are peste 18 ani, folosind if/else.
Introduceti primele 7 cifre din CNP: 2981021
Aveti peste 18 ani.
"""

x=str(input("Inserati primele 7 cifre ale CNP-ului pentru verificare: "))
str=x[1:3]
if int(str)+18 <= 24:
    print("Aveti peste  18 ani")
else:
    print("Nu aveti 18 ani")

