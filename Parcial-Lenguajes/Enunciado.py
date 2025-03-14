from functools import reduce

def cargar_personajes(archivo):
    with open(archivo, 'r', encoding='utf-8') as file:
        encabezado = file.readline().strip().split(',')
        for linea in file:
            valores = linea.strip().split(',')
            personaje = dict(zip(encabezado, valores))
            personaje['nivel'] = int(personaje['nivel'])
            personaje['ataque'] = int(personaje['ataque'])
            personaje['defensa'] = int(personaje['defensa'])
            yield personaje 

filtrar_nivel = lambda personaje: personaje['nivel'] > 10


calcular_poder = lambda personaje: {**personaje, 'totalPower': personaje['ataque'] + personaje['defensa']}


comparar_poder = lambda p1, p2: p1 if p1['totalPower'] > p2['totalPower'] else p2

def analizar_personajes(archivo):
    personajes = cargar_personajes(archivo)
    personajes_filtrados = filter(filtrar_nivel, personajes)
    personajes_con_poder = map(calcular_poder, personajes_filtrados)
    personaje_mas_poderoso = reduce(comparar_poder, personajes_con_poder)
    return personaje_mas_poderoso


if __name__ == "__main__":
    archivo_csv = "personajes.csv"
    personaje_mas_fuerte = analizar_personajes(archivo_csv)
    print("Personaje más poderoso:", personaje_mas_fuerte)


