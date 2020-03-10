print("Menu muerte lenta")
print("Recuerda que solo puedes ingresar una opcion por persona")
print("Opcion 1: Hamburguesa = 10000")
print("Opcion 2: Perro = 8000")
print("Opcion 3: salchipapas = 6000")
print("Opcion 4: Chorizos = 7000")

total = 0
count1 = 0
count2 = 0
count3 = 0
count4 = 0
while True:
    people = int(input("Ingresa el numero de personas: "))
    for count in range(0,people):
        opcionMenu = int(input("Ingresa la opcion que deseas: "))
        if opcionMenu == 1:
            total += 10000
            count1 += 1
        elif opcionMenu == 2:
            total += 8000
            count2 += 1
        elif opcionMenu == 3:
            total += 6000
            count3 += 1
        elif opcionMenu == 4:
            total+=7000
            count4 += 1
#inside while
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





    