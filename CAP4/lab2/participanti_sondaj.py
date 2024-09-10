"""
Se cere un script care sa calculeze media de varsta a unor participanți la un sondaj de
opinie. Cerinte:
a. Se cere input de la utilizator numărul de participanți. Dacă utilizatorul introduce
un răspuns invalid, se va trata eroarea cu ajutorul excepțiilor și i se va cere în
mod repetat numărul de participanți pana cand acesta este unul valid.
b. Pentru fiecare participant, se va cere varsta. Dacă varsta nu a fost introdusă
corect, i se va cere din nou varsta pentru același participant.
c. Media varstelor se va face printr-o funcția dedicată acestui lucru, prin pasarea
unei liste care contine toate varstele ca parametru.
Exemplu output:
Cati participanti avem la sondaj? 4
Introduceti varsta participantului 1: 22
Introduceti varsta participantului 2: t
Nu ati introdus un format valid la participantul 2.
Introduceti varsta participantului 2: 34
Introduceti varsta participantului 3: 45
Introduceti varsta participantului 4: 22t
Nu ati introdus un format valid la participantul 4.
Introduceti varsta participantului 4: 45
Media de varsta a participantilor la sondajul de opinie este: 36.5
"""


#a
while True:
    try:
        nr_participants = input("Cati participanti avem la sondaj? :")
        nr_participants=int(nr_participants)
        break
    except ValueError:
        print(f"Nu ati introdus un format valid la numarul de participanti")

#b
varsta1=[]
for i in range(1,nr_participants+1):
    while True:
        try:
            varsta = input(f"Introduceti varsta participantului {i}: ")
            varsta = int(varsta)
            varsta1.append(varsta)
            break
        except ValueError:
            print(f"Nu ati introdus un format valid al participantului {i}")


#c
def medie(varsta1):
    return sum(varsta1) / len(varsta1)

media_varsta = medie(varsta1)
print(f"Media de vârstă a participanților este: {media_varsta} ani.")
