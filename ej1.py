from cola import Queue
from arbol import BinaryTree

class Pokemon:
    def __init__(self, nombre, numero, tipos):
        self.nombre = nombre
        self.numero = numero
        self.tipos = tipos



# Crear el árbol binario para almacenar Pokémon
tree_by_name = BinaryTree()
tree_by_number = BinaryTree()
tree_by_type = BinaryTree()

# Lista de Pokémon
pokemons = [
    Pokemon("Bulbasaur", 1, ["planta", "veneno"]),
    Pokemon("Ivysaur", 2, ["planta", "veneno"]),
    Pokemon("Venusaur", 3, ["planta", "veneno"]),
    Pokemon("Charmander", 4, ["fuego"]),
    Pokemon("Charmeleon", 5, ["fuego"]),
    Pokemon("Charizard", 6, ["fuego", "volador"]),
    Pokemon("Squirtle", 7, ["agua"]),
    Pokemon("Wartortle", 8, ["agua"]),
    Pokemon("Blastoise", 9, ["agua"]),
    Pokemon("Pikachu", 25, ["eléctrico"]),
    Pokemon("Raichu", 26, ["eléctrico"]),
    Pokemon("Jolteon", 135, ["eléctrico"]),
    Pokemon("Magnemite", 81, ["eléctrico", "acero"]),
    Pokemon("Magneton", 82, ["eléctrico", "acero"]),
    Pokemon("Steelix", 208, ["acero", "tierra"]),
    Pokemon("Electabuzz", 125, ["eléctrico"]),
    Pokemon("Zapdos", 145, ["eléctrico", "volador"]),
    Pokemon("Flareon", 136, ["fuego"]),
    Pokemon("Vaporeon", 134, ["agua"]),
    Pokemon("Leafeon", 470, ["planta"]),
    Pokemon("Glaceon", 471, ["hielo"]),
    Pokemon("Sylveon", 700, ["hada"]),
    Pokemon("Espeon", 196, ["psíquico"]),
    Pokemon("Umbreon", 197, ["siniestro"]),
    Pokemon("Lycanroc", 745, ["roca"]),
    Pokemon("Tyrantrum", 697, ["roca", "dragón"]),
    Pokemon("Gyarados", 130, ["agua", "volador"]),
    Pokemon("Alakazam", 65, ["psíquico"]),
    Pokemon("Mewtwo", 150, ["psíquico"]),
    Pokemon("Dragonite", 149, ["dragón", "volador"]),
    Pokemon("Lucario", 448, ["lucha", "acero"]),
    Pokemon("Greninja", 658, ["agua", "siniestro"]),
    Pokemon("Decidueye", 724, ["planta", "fantasma"]),
]

# Insertar Pokémon en los árboles
for pokemon in pokemons:
    tree_by_name.insert_node(pokemon.nombre.lower(), pokemon)
    tree_by_number.insert_node(pokemon.numero, pokemon)
    for tipo in pokemon.tipos:
        tree_by_type.insert_node(tipo.lower(), pokemon)

name_search = tree_by_name.search_by_prefix("bul")
print("\nPokémon que contienen 'bul' en el nombre:")
for p in name_search:
    print(f'Nombre: {p.nombre}')

print("\nListado de Pokémon por número (ascendente):")
pokemons_by_number = tree_by_number.in_order()
for pokemon in pokemons_by_number:
    print(f'Número: {pokemon.numero}, Nombre: {pokemon.nombre}')

print("\nListado de Pokémon por nombre (ascendente):")
pokemons_by_name = tree_by_name.in_order()
for pokemon in pokemons_by_name:
    print(f'Nombre: {pokemon.nombre}, Número: {pokemon.numero}')

water_pokemons = tree_by_type.search_by_prefix("agua")

print("Pokémon de tipo agua:")
for pokemon in water_pokemons:
    print(f'Nombre: {pokemon.nombre}')

pokemons_to_search = ["jolteon", "lycanroc", "tyrantrum"]
for name in pokemons_to_search:
    pokemon_found = tree_by_name.search(name)
    if pokemon_found:
        print(f'Pokémon encontrado: {pokemon_found.other_value.nombre}, Número: {pokemon_found.other_value.numero}, Tipos: {", ".join(pokemon_found.other_value.tipos)}')
    else:
        print(f'Pokémon {name} no encontrado.')

electric_count = tree_by_type.count_by_type("eléctrico")
steel_count = tree_by_type.count_by_type("acero")

print("\nCantidad de Pokémon tipo eléctrico: ", electric_count)
print("Cantidad de Pokémon tipo acero: ", steel_count)



