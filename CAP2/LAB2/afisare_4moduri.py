"""
Cereți input de la utilizator cu un șir și afișați lungimea șirului in 4 moduri:
- Cu metoda format()
- Prin metoda f” ”
- Concatenare (+)
- Cu virgula
Introduceti un sir: Ana are mere.
Lungimea sirului este: 13
"""
#format
sir=input("Introduceti un sir: ")
a=len(sir)
print("Lungimea sirului este : {}".format(a))

#f" "
print(f"Lungimea sirului este : {a}")

#concatenare (+)
m=str(a)
print("Lungimea sirului este : " +m )

#cu virgula
print("Lungimea sirului este :" ,a)