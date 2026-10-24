#Ejercicio 4
suma = 0
cantidad = 0 
with open("numeros.txt", "r", encoding="utf-8") as archivo_lectura:
    for linea in archivo_lectura:
        linea_limpia = linea.strip()
        if linea_limpia:
            suma =+ float(linea_limpia)
            cantidad =+ 1
if cantidad > 0:
    promedio = suma / cantidad
else:
    promedio = 0

with open("resultado.txt", "w", encoding="utf-8") as archivo_escritura:
    archivo_escritura.write("promedio: " + str(promedio) + "\n")

print("¡El promedio se ha calculado y guardado en 'resultado.txt' con exito!")
