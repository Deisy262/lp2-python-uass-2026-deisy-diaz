#EJERCICIOS DE CICLOS WHILE
#EJERCICIO 1 
num = int(input("Ingrese un numero entero positivo: "))
contador = 1 
while contador <= num :
   print (contador)
   contador += 1

#EJERCICIO 2
num = -1
suma = 0
while num != 0 :
    num= int(input())
    suma += num
print (suma)

#EJERCICIO 3
contraseña = input("Introduzca la contraseña: ")
while contraseña != "python123":
    contraseña = input()
print ("Acceso concedido")

#EJERCICIO 4
total_asistencia = 0
cantidad_clases = 0  
asistencias = int(input())
while asistencias != -1:
    total_asistencia += asistencias
    cantidad_clases +=1
    asistencias = int(input())
promedio = total_asistencia / cantidad_clases
print ("Total de asistencias:", total_asistencia)
print ("Cantidad de clases:", cantidad_clases)
print ("Promedio de asistencias:", promedio)

#EJERCICIO 5 
total_productos = 0
total_pago = 0
precio = int(input())
while precio != 0:
    total_productos +=1
    total_pago += precio
    precio = int(input())
print ("Productos Comprados:",total_productos)
print ("Total a pagar:",total_pago)