#EJERCICIOS DE FUNCIONES
#Ejercicio 1
def estadisticas(numeros):
    """Recibe una lista de numeros y retorna el valos maximo, el valor minimo y el promedio."""
    maximo = max (numeros)
    minimo = min (numeros)
    promedio = sum (numeros)/len(numeros)
    promedio = round(promedio)
    return maximo, minimo, promedio

numeros = [10,20,30,40,50]

mayor, menor, promedio = estadisticas(numeros)
print("Mayor:",mayor)
print("Menor:",menor)
print("Promedio:",promedio)

#Ejercicio 2 
def buscar(lista, valor):
    if valor in lista:
        return True
    else:
        return False
alumnos= ["ana","luis","carlos"]

resultado = buscar(alumnos, "luis")
print(resultado)

#Ejercicio 3
def eliminar_duplicados(lista):
    sin_duplicados = set(lista)
    return sin_duplicados
numeros = [1,2,2,3,3,3,4]
resultado = eliminar_duplicados(numeros)
print (resultado)

#Ejercicio 4
def contar_frecuencia(lista):
    frecuencias = {}
    for elemento in lista:
        if elemento in frecuencias:
            frecuencias[elemento] += 1
        else:
            frecuencias[elemento]=1
    return frecuencias
letras = ["a","b","a","c","a","b"]
resultado = contar_frecuencia(letras)
print(resultado)

#Ejercicio 5
def calcular_promedio (notas):
    suma = 0
    for nota in notas:
        suma += nota
    promedio = suma / len(notas)
    return round(promedio)
def estado(promedio):
    if promedio >=60:
        return "Aprovado"
    else:
        return "Reprovado"
notas = [70,80,90,60]
prom = calcular_promedio(notas)
est = estado(prom)
print("Promedio:",prom)
print("Estado:",est) 

#Ejercicio 6
agenda = {
    "juan":"0981111111",
    "ana": "0982222222"
}
def agregar_contacto():
    nombre = input("Ingrese el nombre del contacto: ")
    telefono = input("Ingrese el número de teléfono: ")
    agenda[nombre] = telefono
    print(f"Contacto '{nombre}' agregado con éxito.\n")

def buscar_contacto():
    nombre = input("Ingrese el nombre a buscar: ")
    if nombre in agenda:
        print(f"Teléfono de {nombre}: {agenda[nombre]}\n")
    else:
        print(f"El contacto '{nombre}' no existe en la agenda.\n")

def mostrar_contactos():
    if not agenda:
        print("La agenda está vacía.\n")
    else:
        print("\n--- Lista de Contactos ---")
        for nombre, telefono in agenda.items():
            print(f"Nombre: {nombre} | Teléfono: {telefono}")
        print("-------------------------\n")

# --- Menú Telefonico---
opcion = ""
while opcion != "4":
    print("=== MENÚ  ===")
    print("1. Agregar contacto")
    print("2. Buscar contacto")
    print("3. Mostrar contactos")
    print("4. Salir")
    
    opcion = input("Seleccione una opción (1-4): ")
    
    if opcion == "1":
        agregar_contacto()
    elif opcion == "2":
        buscar_contacto()
    elif opcion == "3":
        mostrar_contactos()
    elif opcion == "4":
        print("¡Saliendo de la agenda! Hasta luego.")
    else:
        print("Opción no válida. Intente de nuevo.\n")

#Ejercicio 7
productos = [
    ("Teclado", 150000),
    ("Mouse", 80000),
    ("Monitor", 1200000)
]
def productos_mas_caro(productos):
    more_caro = productos[0]
    for producto in productos:
        if producto[1] > more_caro[1]:
            more_caro = producto
    return more_caro[0], more_caro[1]

nombre, precio = productos_mas_caro(productos)
print ("Producto:", nombre)
print ("precio:",precio)

#Ejercicio 8
# 1. Definimos primero el diccionario con los datos iniciales
inventario = {
    "Teclado": 10,
    "Mouse": 5,
    "Monitor": 2
}
def agregar_stock():
    producto = input("Producto: ")
    cantidad = int(input("Cantidad a sumar: "))
    inventario[producto] = inventario.get(producto, 0) + cantidad
    print(f"Nuevo stock de {producto}: {inventario[producto]}")

def vender_producto():
    producto = input("Producto a vender: ")
    cantidad = int(input("Cantidad a vender: "))
    if producto not in inventario:
        print("El producto no existe.")
    elif inventario[producto] < cantidad:
        print(f"Stock insuficiente (Disponible: {inventario[producto]}).")
    else:
        inventario[producto] -= cantidad
        print(f"Venta realizada. Quedan {inventario[producto]} unidades.")

def consultar_stock():
    producto = input("Producto a consultar: ")
    if producto in inventario:
        print(f"Stock de {producto}: {inventario[producto]}")
    else:
        print("El producto no existe.")

while True:
    opcion = input("\n1. Agregar stock | 2. Vender | 3. Consultar | 4. Salir: ")
    
    if opcion == "1":
        agregar_stock()
    elif opcion == "2":
        vender_producto()
    elif opcion == "3":
        consultar_stock()
    elif opcion == "4":
        break
    else:
        print("Opción no válida.")


#Ejercicio 9
alumnos = [
    ("Juan", 85),
    ("Ana", 95),
    ("Pedro", 70)
]

def obtener_mejor_alumno(lista):
    mejor = lista[0]
    for alumno in lista:
        if alumno[1] > mejor[1]:
            mejor = alumno
    return mejor

def obtener_peor_alumno(lista):
    peor = lista[0]
    for alumno in lista:
        if alumno[1] < peor[1]:
            peor = alumno
    return peor

def calcular_promedio(lista):
    suma_notas = 0
    for alumno in lista:
        suma_notas += alumno[1]
    return round(suma_notas / len(lista),2)

# Mostramos los resultados
mejor = obtener_mejor_alumno(alumnos)
peor = obtener_peor_alumno(alumnos)
promedio = calcular_promedio(alumnos)

print(f"Mejor alumno: {mejor[0]} ({mejor[1]})")
print(f"Peor alumno: {peor[0]} ({peor[1]})")
print(f"Promedio general: {promedio}")