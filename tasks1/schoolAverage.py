avarage = 0
for i in range(0,3):
   student =  float(input("Digite a nota do aluno: "))
   avarage += student
avarage /= 3
if avarage >= 7:
   print("Aprovado: ", avarage)
else:  print("Reprovado: ", avarage)