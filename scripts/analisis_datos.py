#importamos las librerias
import csv
import matplotlib.pyplot as plt
import os

#iniciamos las variables
ventas_totales = 0
productos = {}
ventas_mes = {}

#abrimos el archivo csv
with open("datos/dataset.csv", "r") as archivo:
  reader = csv.DictReader(archivo) #lo leemos como un diccionario

  #recorremos el archivo fila por fila
  for fila in reader:
    #buscamos los datos de las columnas y los guardamos
    producto = fila["Product Name"]
    cantidad = int(fila["Units Sold"])
    precio = float(fila["Unit Price"])
    fecha = fila["Date"]

    #calculamos el precio de la venta y la guardamos
    venta = cantidad * precio 
    ventas_totales += venta

    #determinamos el volumen de stock vendido por producto
    if producto in productos:
      productos[producto] += cantidad
    else:
      productos[producto] = cantidad

    mes = fecha[:7] #cortamos la fecha para quedarnos con año y mes

    #sumamos el monto vendido por mes
    if mes in ventas_mes:
      ventas_mes[mes] += venta
    else:
      ventas_mes[mes] = venta

#buscamos la clave que tiene el valor mas grande de unidades vendidas
producto_mas_vendido = max(productos, key=productos.get)

#resultados
print(f"Ventas totales: ${ventas_totales:.2f}")
print(f"Producto mas vendido: {producto_mas_vendido}")
print("Ventas por mes:")

#listamos los totales mes por mes
for mes in ventas_mes:
  print(f"{mes}: ${ventas_mes[mes]:.2f}")

#Generar el grafico con matplotlib

#transformamos los meses y ventas en listas para usar en cada eje (x,y)
meses = list(ventas_mes.keys()) #eje x
ventas = list(ventas_mes.values()) #eje y

#configuracion estetica del grafico
plt.figure(figsize=(10, 5)) #tamaño de imagen
plt.plot(meses, ventas, marker='x', color='purple') #la linea y sus datos

#textos informativos para el grafico
plt.title("Evolucion mensual de ventas")
plt.xlabel("Mes")
plt.ylabel("Ventas ($)")

# Guardar obligatoriamente en la carpeta resultados antes de mostrarlo
plt.savefig("resultados/evolucion_ventas.png") #mandamos el grafico a resultados
plt.close() #cerramos el grafico
print("Grafico exportado exitosamente en: resultados/evolucion_ventas.png")
