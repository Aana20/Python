"""
1. Declarați o listă care conține următoarele elemente: [‘abc’,123,’1’,1].
- afișarea tipului fiecărui element din lista
- Aflarea numărului numerelor întregi, numerelor float, respectiv a șirurilor din lista
2. Luati ca input un sir de la utilizator. Transformați șirul într-o lista și numarati vocalele din
aceasta. Afisati numarul vocalelor pe consola.
Introduceti un cuvant: Ananas
Vocale in cuvantul dvs: 3
"""
#1

lista=["abc",123,"1",1]
nr_str=0
nr_lista=0
nr_int=0
for i in range(0,len(lista)):
    print(f"Tipul elementului {lista[i]} este : {type(lista[i])}")
    if type(lista[i]) == "<class 'str'>":
        str+=1
    elif type(lista[i]) == "<class 'list'>":
        nr_lista+=1
    else:
        nr_int+=1;
print(f"Numarul numerelor  intregi {nr_int} \n Numarul sirurilor {nr_str} \n Numarul lista {nr_lista}")


#2
sir=str(input("Introduceti un sir : "))
lista2=list(sir)
print(lista2)
vocale=0
for i in range(0,len(lista2)):
    if lista2[i] in ['a', 'e', 'i', 'o', 'u']:
        vocale += 1
print(f"Vocale in cuvantul dvs : {vocale}")
