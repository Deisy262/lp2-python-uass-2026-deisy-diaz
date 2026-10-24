#Ejercicio 3
nombre = input("Ingrese el nombre de la persona: ")
edad = input("Ingrese la edad de la persona: ")
with open("registro.txt" , "a", encoding="utf-8") as archivo:
    archivo.write(nombre + "-" + edad + "\n")

print("\n¡Los datos se han agregado correctamente al archivo 'registro.txt'!")
