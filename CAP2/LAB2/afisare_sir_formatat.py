"""
Afișați următoarele șiruri: “Hello Python”, “Ana are mere”, “Pizza Party” în următoarele
formate:
- Fiecare cuvant separat cu _
- Punct la final de sir
- Primul cuvânt din șir multiplicat de 4 ori
"""
sir1="Hello Python"
sir2="Ana are mere"
sir3="Pizza Party"
print('_'.join(sir1.split(" "))+"\n"+'_'.join(sir2.split(" "))+"\n"+'_'.join(sir3.split(" "))+"\n")
print(sir1+'.'+"\n"+sir2+'.'+"\n"+sir3+'.'+"\n")

a1=sir1.split()
a2=sir2.split()
a3=sir3.split()
for i in range(0,4):
    print(a1[0],a2[0],a3[0])