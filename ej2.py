from grafo import Graph

class StarWarsGraph:
    def __init__(self):
        self.graph = Graph(dirigido=False)

    def agregar_personaje(self, personaje):
        self.graph.insert_vertice(personaje)

    def agregar_relacion_episodios(self, personaje1, personaje2, episodios):
        self.graph.insert_arista(personaje1, personaje2, episodios)

    def arbol_expansion_minima(self):
        return self.graph.kruskal(self.graph.elements[0]['value'])

    def contiene_a_yoda(self):
        for nodo in self.graph.elements:
            if nodo['value'] == "Yoda":
                return True
        return False

    def max_episodios_compartidos(self):
        max_episodios = 0
        for nodo in self.graph.elements:
            for arista in nodo['aristas']:
                if arista['peso'] > max_episodios:
                    max_episodios = arista['peso']
        return max_episodios

star_wars_graph = StarWarsGraph()

personajes = [
    "Luke Skywalker", "Yoda", "Darth Vader", "Leia Organa", "Han Solo",
    "Boba Fett", "C-3PO", "Rey", "Kylo Ren", "Chewbacca", "R2-D2", "BB-8"
]
for personaje in personajes:
    star_wars_graph.agregar_personaje(personaje)

star_wars_graph.agregar_relacion_episodios("Luke Skywalker", "Yoda", 5)
star_wars_graph.agregar_relacion_episodios("Luke Skywalker", "Darth Vader", 3)
star_wars_graph.agregar_relacion_episodios("Yoda", "Darth Vader", 2)
star_wars_graph.agregar_relacion_episodios("Leia Organa", "Han Solo", 4)
star_wars_graph.agregar_relacion_episodios("Chewbacca", "Han Solo", 6)
star_wars_graph.agregar_relacion_episodios("C-3PO", "R2-D2", 7)
star_wars_graph.agregar_relacion_episodios("Rey", "Kylo Ren", 3)

arbol_expansion_minima = star_wars_graph.arbol_expansion_minima()
print("Arbol de expansion minimo:", arbol_expansion_minima)
print("¿Contiene a Yoda?:", star_wars_graph.contiene_a_yoda())

max_episodios = star_wars_graph.max_episodios_compartidos()
print("Numero maximo de episodios compartidos entre dos personajes:", max_episodios)
