#Ejercicio 5
with open("origen.txt", "r", encoding="utf-8") as archivo_origen:
     with open("destino.txt", "w", encoding="utf-8") as archivo_destino:
       for linea in archivo_origen:
           archivo_destino.write(linea)
           
print("¡Proceso terminado con exito!")
