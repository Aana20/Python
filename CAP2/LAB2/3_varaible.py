"""
Creati 3 variabile: a = 5., b = 5, c = “ana”
- Afisati locatia in memorie a fiecarei variabile in hexadecimal
Locatia lui a este: 0x14951d37b70
- Afișați tipul variabilei
Tipul variabilei a este: <class 'float'>

"""
a=5.
b=5
c="ana"
print(a,b,c)
print("locatia lui a este :"+hex(id(a))+"\nlocatia lui b este : "+hex(id(b))+"\nlocatia lui c este : "+hex(id(c))+"\n")
print("Tipul variabilei a este : ",type(a),"\nTipul variabilei b este : ",type(b),"\nTipul variabilei c este : ",type(c))