"""Cereți input de la utilizator cu un cuvânt. Afișați dacă acest cuvant este palindrom.
Introduceti un cuvant: ana
Palindrom: True
Introduceti un cuvant: Ananas
Palindrom: False
"""

x=input("Introduceti un cuvant : ")
a=len(x)
#for i in range(0,a):
if x[0:a] == x[::-1]:
    print("Palindrom : True")
else:
    print("Palindrom : False")