"""
Luați input de la utilizator un număr și parcurgeți intervalul de la 0 pana la numărul
introdus de către utilizator, afisand toate numerele pare.

"""

x=int(input("Introduceti un numar : "))
for i in range(0,x):
    if i%2==0:
        print(i)
