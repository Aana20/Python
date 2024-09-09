
"""
Se cere input de la utilizator cu venit net pe luna. Din acesta, calculati regula 50/30/20:
- 50% din venit acordat necesităților (cumparaturi, intretinere, chirie, etc)
- 30% din venit acordat scopurilor recreative
- 20% din venit acordat datoriilor și economiilor
Venit: 2875
Recomandarile noastre:
Cheltuieli uzuale: 1437.5
Recreere: 862.5
Economii si datorii: 575.0

"""

venit=float(input("Venitul pe luna este : "))
cheltuieli=float((50/100)*venit)
recreere=float((30/100)*venit)
economii=float((20/100)*venit)

print(f"Venit : {venit}\n Recomandarile noastre : \n Cheltuieli uzuale : {cheltuieli}\n"
      f"Recreere : {recreere} \n Economii si datorii : {economii}")
