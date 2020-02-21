# number1 = float(input("Ingrese numero 1: "))
# number2 = float(input("Ingrese numero 2: "))
# total = number1 + number2
# print("el total es: " + str(total))

# edad = float(input("Ingrese su edad: "))
# if edad >= 5 and edad <= 15:
#     print(str(edad) + " Es mayor")
# elif edad >=18:
#     print (str(edad) + "Es mayor de edad")
# elif edad >=35:
#     print(str(edad) + "Es muy mayor")
# else: 
#     print(str(edad) + " No es mayor")

print("Valor credito pregrado = 50000")
print("Valor credito posgrado = 300000")
print("Si eres de la modalidad pregrado escribe el numero 1 o si eres de posgrado escribe el numero 2")
promedio = float(input("Ingrese su promedio: "))
modalidad = float(input("Ingresa la modalidad: "))
# creditos = float(input("Ingrese el numero de creditos"))
if promedio >= 4.5 and modalidad == 1: 
    pregrado = 28 * 50000
    descuento = pregrado * 25 / 100
    print(" Este es el valor de tu semestre : "+ str(pregrado - descuento)+" Cursaras 28 creditos y por obtener este promedio te Damos el 25% de descuento.")
elif promedio >= 4.0 and promedio < 4.5 and modalidad == 1:
    pregrado = 25 * 50000
    descuento = pregrado * 10 / 100
    print(" Este es el valor de tu semestre : "+ str(pregrado - descuento)+" Cursaras 25 creditos y por obtener este promedio te Damos el 10% de descuento.")
elif promedio >= 3.5 and promedio < 4.0 and modalidad == 1:
    pregrado = 20 * 50000
    print(" Este es el valor de tu semestre : "+ str(pregrado)+" Cursaras 20 creditos.")
elif promedio >= 2.5 and promedio < 3.5 and modalidad == 1:
    pregrado = 15 * 50000
    print(" Este es el valor de tu semestre : "+ str(pregrado)+" Cursaras 15 creditos.")
elif promedio < 2.5 and modalidad == 1:
    print(" No es posible matricularse. ")
elif promedio >= 4.5 and modalidad == 2:
    posgrado = 20 * 300000
    descuento = posgrado * 20 / 100
    print(" Este es el valor de tu semestre : "+ str(posgrado - descuento)+" Cursaras 20 creditos y por obtener este promedio te brindamos el 20% de descuento.")
elif promedio < 4.5 and modalidad == 2:
    posgrado = 10 * 300000
    print(" Este es el valor de tu semestre : "+ str(posgrado)+" Cursaras 10 creditos.")
if promedio = 





