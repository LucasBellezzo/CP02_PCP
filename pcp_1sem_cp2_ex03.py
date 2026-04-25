cp1 = float(input("Nota do Checkpoint 1= "))
cp2 = float(input("Nota do Checkpoint 2= "))
cp3 = float(input("Nota do Checkpoint 3= "))
sp1 = float(input("Nota da Sprint 1= "))
sp2 = float(input("Nota do Sprint 2= "))
gs = float(input("Nota do Global Solution= "))

menor = cp1

if cp2 < menor:
    menor = cp2
if cp3 < menor:
    menor = cp3


media = ((cp1+cp2+cp3-menor+sp1+sp2)/4)*0.4+gs*0.6


print("A nota final no semestre será ", media)