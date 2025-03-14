from functools import reduce


def cargar_personajes(archivo):
    with open(archivo, 'r', encoding='utf-8') as file:
        header = file.readline().strip().split(',')  
        personajes = [] 
        for linea in file:
            values = linea.strip().split(',')  
            personajes = dict(zip(header, values))
            
            personajes['nivel'] = int(personajes['nivel'])
            personajes['ataque'] = int(personajes['ataque'])
            personajes['defensa'] = int(personajes['defensa'])

            
            yield personajes


personajes = cargar_personajes("dataset.csv")
print("Lista de personajes cargados:")
print(personajes)


personajes_filtrados = list(filter(lambda p: p['nivel'] > 10, personajes))
print("\nPersonajes con nivel mayor a 10:")
print(personajes_filtrados)


Total_power = list(map(lambda p: {**p, 'totalPower': p['ataque'] + p['defensa']}, personajes_filtrados))
print("\nPersonajes con total power calculado:")
print(Total_power)


personaje_mas_poderoso = reduce(
    lambda p1, p2: p1 if p1['totalPower'] > p2['totalPower'] else p2,
    Total_power
)
print("\nPersonaje más poderoso:")
print(personaje_mas_poderoso)

 