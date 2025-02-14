# #Conceptos basicos de programación funcional

# #1. Funciones son ciudadanos de primer orden. 
# #
# def suma (a,b):
#     return a+b

# def resta(a,b):
#     return a-b

# def multi(a,b):
#     return a*b

# def div(a,b):
#     if b != 0:
#         return a/b
        
# val1 = int(input("Ingrese valor 1"))
# val2 = int(input("ingrese valor 2"))
# op = int(input("Ingrese la operación: 1. suma 2. resta 3. multip. 4.div."))

# if op == 1:
#     operacion = suma
# elif op == 2:
#     operacion = resta
# elif op == 3:
#     operacion = multi
# elif op == 4:
#     operacion = div
# else:
#     print ("Operación no válida")

# print (f"El resultado es: {operacion(val1,val2)}")

# #x = suma
# #Y = suma

# #print(x(5,3))
# # 5print(y(6,8))

# #Ejemplo una calculadora.




# #2. Funciones puras
# #3 Funciones anónimas (LAMBDA)
# num = int(input ("Ingrese un número cualquiera:"))
# es_par = lambda x: x % 2 == 0
# print (es_par(27))
# print (f"{num} es par?: {es_par(num)}")

#Funciones de orden superior

# 4. a map
# Ejemplo sin map: normalizar un conjunto de datos:
ciudades = ["Cali", "medellin", "BOGOTA", "bArrAnQuillA"]
 # Es una función pura?
def normalizar_datos(lista_nombres):
    datos_norm = []
    for nombre in lista_nombres:
        datos_norm.append(nombre.capitalize())
    return datos_norm

#Usando map, sin función lambda:
def capitalizar(palabra):
    #Retorna la palabra con la inical en mayúscula,
    return palabra.capitalize()

ciudades_norm2 = list(map( capitalizar, ciudades))

# es una funcion pura. si los parametros de entrada los modifica, si no toca variables globales, si no tiene efectos secundarios sin modificar algo global, lops datos de entrada no los toca, los copia. 
ciudades_norm = normalizar_datos(ciudades)
print(f"Datos sin normalizar:{ciudades}")
print(f"Datos normalizados:{ciudades_norm}")
print(f"Datos normalizados con map (sin lambda): {ciudades_norm2}")

#usando map, con lambda:

ciudades_norm3 = list(map ( lambda n: n.capitalize(), ciudades  ))
print(f"Datos normalizados con mao (con lambda): {ciudades_norm3}")
#las funciones de orden superior son funciones que pueden recibir como parametro referencias de otras funciones, sirven para procesar datos
#map, filter, reduce. 
#Ejemplo con na función de orden superior: map
#la funcion map recibe dos parametros y genera una nueva lista, por ej map(capitalizar, ciudades), ubica la funcion capitaliar y se la aplica a cada uno de los elementos, general una nueva lista mapeando, a cada uno de los elementos de la lista y estoy generando una nueva lista, pero no es la versión mas optima. 