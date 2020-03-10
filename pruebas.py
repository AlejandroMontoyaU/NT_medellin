# count2 = 0
# while True:
#     if count2 == 10:
#         break
#     count2+=1
#     print(count2)

categoria = 0
ValorAdicional = 0
total = 0
people = int(input("Ingresa el numero de empleados: "))
for count in range(0,people):
    NameEmpleado = input("Ingresa el nombre del empleado: ")
    SalarioBase = int(input("Ingresa tu salario base"))
    HoraExtra = int(input("Ingresa el numero de horas extras trabajadas"))
    if SalarioBase >= 200000 and SalarioBase <= 600000:
        categoria = "A"
        SalarioBase = SalarioBase * 1.10
        ValorAdicional = SalarioBase * HoraExtra
        total=ValorAdicional+SalarioBase
        print()
    elif SalarioBase < 200000:
        categoria = "No tiene categoria"
    elif SalarioBase > 600000:
        categoria = "B"
    







    closeprogram = input("Desea continuar 'SI', 'NO'")
    if closeprogram != 'SI':
        break
#outside while
tip = input("Desea dejar propina, SI - NO")
if count1 >= 2 or count2 >= 2 or count3 >= 2 or count4 >= 2:
    total = total * 0.95
if total > 20000:
    total = total * 0.90
if tip == "SI":
    total = total * 1.10

print("El total de la cuenta es: "+ str(total))