from functools import reduce

def cargar_personajes(archivo):
    """Función que lee los datos del archivo y los devuelve uno por uno como un diccionario."""
    with open(archivo, 'r', encoding='utf-8') as file:
        encabezado = file.readline().strip().split(',') 
        for linea in file:
            valores = linea.strip().split(',')  
            personaje = dict(zip(encabezado, valores))  
            
            
            personaje['nivel'] = int(personaje['nivel'])
            personaje['ataque'] = int(personaje['ataque'])
            personaje['defensa'] = int(personaje['defensa'])
            
            yield personaje 

def es_nivel_mayor_a_diez(personaje):
    return personaje['nivel'] > 10

def calcular_poder_total(personaje):
   
    nuevo_personaje = personaje.copy() 
    nuevo_personaje['totalPower'] = personaje['ataque'] + personaje['defensa']
    return nuevo_personaje

def comparar_poder(p1, p2):
    
    if p1['totalPower'] > p2['totalPower']:
        return p1
    else:
        return p2

def analizar_personajes(archivo):

    personajes = cargar_personajes(archivo)  # Obtener los personajes desde el archivo
    personajes_filtrados = filter(es_nivel_mayor_a_diez, personajes)  # Filtrar los personajes
    personajes_con_poder = map(calcular_poder_total, personajes_filtrados)  # Calcular totalPower
    personaje_mas_poderoso = reduce(comparar_poder, personajes_con_poder)  # Encontrar el más fuerte
    return personaje_mas_poderoso

# Ejemplo de uso
if __name__ == "__main__":
    archivo_csv = "dataset.csv"
    personaje_mas_fuerte = analizar_personajes(archivo_csv)
    print("Personaje más poderoso:", personaje_mas_fuerte)




