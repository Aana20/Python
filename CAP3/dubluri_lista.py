"""
Pentru acest exercițiu aveți începutul codului care cere input de la utilizator cu un șir
separat prin virgula și îl împarte într-o listă.
lista = input("Introduceti lista de taskuri: ")
lista_taskuri = lista.split(",")
print(lista_taskuri)
Parcurgeti lista generata din input-ul utilizatorului si eliminati dublurile din aceasta.
"""

lista = input("Introduceti lista de taskuri separate prin virgula: ")
lista_taskuri = lista.split(",")


lista_taskuri = [task.strip() for task in lista_taskuri]

lista_taskuri_fara_dubluri = list(set(lista_taskuri))


print("Lista de taskuri fără dubluri:", lista_taskuri_fara_dubluri)





