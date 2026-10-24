#Ejercicio 1
with open("productos.txt", "w", encoding="utf-8") as archivo:
    for i in range(1,6):
        print ("Producto " + str(i) + " de 5")
        nombre = input("Ingrese el nombre del producto: ")
        precio = input("Ingrese el precio del producto: ")
        archivo.write( nombre + " - " + precio + "\n" )

print("\n¡Los productos se han guardado correctamete en ,'productos.txt', !")
       