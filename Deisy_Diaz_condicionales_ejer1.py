#EJERCICIOS DE CONDICIONALES
#EJERCICIO 1 : Control de acceso
CI = input("Posee documento de identidad?,(si/no): ").lower()
Edad = int(input("Ingrese su edad por favor: "))
if Edad >= 18 and CI == "si" :
    print ("¡Bienvenido!,Puede ingresar") 
elif Edad < 18 and CI == "no":
    print ("¡NO puede ingresar!, no posee documentos y es menor aún")
elif Edad < 18:
    print ("Usted es menor aún , no puede ingresar ")
else:
   print ("No puede ingresar , no posee documento de identidad")
 
#EJERCICIO 2 : Descuentos en una tienda
monto = int(input("Ingrese el monto de su compra: "))
print ("Monto Original: ", monto)
if monto > 500000 :
    total_descuento = monto * 0.20
elif monto > 200000 :
    total_descuento = monto * 0.10
else :
    print ("no posee descuentos ")
    total_descuento = 0

total = monto - total_descuento
print ("Descuento: ", total_descuento)
print ("Su total a pagar es de: ", total)

#EJERCICIO 3 : Semáforo inteligente 
color = input("Ingrese el color del semáforo: ").lower()
if color == "verde":
    print ("Avanzar")
elif color == "amarillo":
    print ("Reducir velocidad")
elif color == "rojo":
    print ("Detenerse")
else :
    print ("¡ERROR!....")
    print ("Ingrese un color igual a verde , amarillo o rojo")

#EJERCICIO 4: Nivel de batería
porcen_bate = int(input("Ingrese su nivel de bateria: "))
if porcen_bate < 0 or porcen_bate > 100 :
    print ("¡ERROR..!, el nivel de bateria debe de estar entre 0 a 100")
elif porcen_bate <= 10 :
    print ("Su nivel de bateria es Crítica")
elif porcen_bate <=30 :
    print ("Su nivel de bateria es Baja")
elif porcen_bate <=80:
    print ("Su nivel de bateria es Normal")
else:
    print ("Su nivel de bateria es Alta") 

#EJERCICIO 5: Evaluación climática
temperatura = int(input("Ingrese el nivel de temperatura actual en su zona: "))
if temperatura < 10 :
    print("Mucho frío")
elif temperatura <=24 :
    print ("Templao")
elif temperatura <=34:
    print ("Caluroso")
else:
    print ("¡Muy caluroso!")

