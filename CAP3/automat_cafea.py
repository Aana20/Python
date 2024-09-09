"""
Un automat de cafea are următoarele opțiuni: Cappuccino, Espresso. Cappuccino
costa 4 lei, iar Espresso costa 3,5 lei. Aparatul de cafea accepta doar bancnote de 5 si
10 lei.
Utilizatorului îi este afișat meniul, după care i se cere o opțiune. Dacă utilizatorul a
introdus o opțiune validă, i se cere o bancnota. Dacă utilizatorul a introdus o bancnotă
validă, acesta va primi restul și i se va livra produsul.
Creați un script care sa simuleze acest automat de cafea în mod similar cu exemplul
următor:
1. Cappuccino ... 4 lei
2. Espresso ...3.5 lei
Ce optiune alegeti? [1,2]: 1
Introduceti o bacnota [5,10]: 5
Veti primi restul de 1 lei.
Produsul se livreaza...

"""
cap=4
esp=3.5

print("1.Cappuccino    ....4 lei \n 2.Espresso    ....3.5 lei\n")
optiune=int(input("Ce optiune alegeti? [1,2] :  "))
if optiune == 1 or optiune == 2:
    bacnota = int(input("Introduceti o bacnota [5,10] : "))
    if bacnota ==5 or bacnota ==10:
        if optiune==1:
            rest=bacnota-cap
        else:
            rest=bacnota-esp
        print(f"Veti primi restul de: {rest} lei. \n Produsul se livreaza...\n")
    else:
        print("Nu e ok bacnota")
else:
    print("Nu e o optiune")
