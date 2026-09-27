#Ejercicios de Ciclos For
#EJERCICIO 1 
num = int(input("ingrese un numero entero positivo: "))
for i in range (1 , num + 1 ):
    print (i) 

#EJERCICIO 2
num= int(input("Ingrese un numero entero: "))
sum= 0
for i  in range (1 + (num + 1)):
    sum += i
print ("La suma es: ",sum)

#EJERCICIO 3 
n = int(input("Ingrese el numero que desea multiplicar: "))
for i in range (1 , 11):
    multi = n * i
    print (f"{n} x {i} = {multi}")

#EJERCICIO 4 
palabra = input("Ingrese uan palabra: ").lower()
vocables = "aeiou"
contador = 0
for i in palabra:
    if  i in vocables:
        contador += 1
print ("cantidad de vocales: ",contador)

#EJERCICIO 5
Num = int(input("Ingrese un numero entero positivo: "))
for i in range (1 , Num + 1 ):
    print ("*" * i)