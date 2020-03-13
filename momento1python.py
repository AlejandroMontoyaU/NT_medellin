
print("Finalizar semestre")
total = 0
promedio = 0
count1 = 0
count2 = 0
count3 = 0
count4 = 0
suma=0
prom=0

people = int(input("Ingresa el numero de estudiantes: "))
for count in range(0,people):
    progAca = int(input("Si eres del programa de Sistemas pon el numero 1 o si eres de Finanzas pon el numero 2: "))
    if progAca == 1:
        programa = "Sistemas"
        count1 += 1
    elif progAca == 2:
        programa = "Finanzas"
        count2 += 1
    progAca2 = int(input("Si eres Hombre pon el numero 1 o si eres Mujer pon el numero 2: "))
    if progAca2 == 1:
        sexo = "Hombres"
        count3 += 1
    elif progAca2 == 2:
        sexo = "Mujeres"
        count4 += 1
    print ("Ingresa las 5 notas del semestre: ")
    for i in range (1, 6):
        nota = int(input("Ingresa la nota "+str(i)+" : "))
        suma += nota

    promedio = suma / 5
    prom += promedio

#inside while
    closeprogram = input("Desea continuar 'SI', 'NO'")
    if closeprogram != 'SI':
        break
#outside while
if progAca == 1 and progAca2 == 1:
    total = prom / count3
    print("A el programa de: "+programa+ " pertenecen "+str(count3)+" "+sexo+" y el promedio del curso es: "+str(total))
 
if progAca == 1 and progAca2 == 2:
    total = prom / count4
    print("A el programa de: "+programa+ " pertenecen "+str(count4)+" "+sexo+" y el promedio del curso es: "+str(total))

if progAca == 2 and progAca2 == 1:
    total = prom / count3
    print("A el programa de: "+programa+ " pertenecen "+str(count3)+" "+sexo+" y el promedio del curso es: "+str(total))

if progAca == 2 and progAca2 == 2:
    total = prom / count4
    print("A el programa de: "+programa+ " pertenecen "+str(count4)+" "+sexo+" y el promedio del curso es: "+str(total))








