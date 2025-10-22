# grafos.py

class GrafoPokemon:
    def __init__(self):
        self.grafo = {}

    def construir_grafo(self, chain):
        """Construye el grafo de evolución de forma recursiva"""
        especie = chain["species"]["name"]
        evoluciones = [evo["species"]["name"] for evo in chain.get("evolves_to", [])]
        self.grafo[especie] = evoluciones

        for evolucion in chain.get("evolves_to", []):
            self.construir_grafo(evolucion)

    def mostrar_grafo(self):
        """Imprime el grafo en formato legible"""
        print(" Grafo de evolución construido correctamente:\n")
        for especie, evoluciones in self.grafo.items():
            print(f"{especie} → {evoluciones}")

    @staticmethod
    def busqueda_binaria(lista, objetivo, izquierda=0, derecha=None):
        """Realiza una búsqueda binaria recursiva"""
        if derecha is None:
            derecha = len(lista) - 1

        if izquierda > derecha:
            return False

        medio = (izquierda + derecha) // 2
        valor_medio = lista[medio]

        if valor_medio == objetivo:
            return True
        elif valor_medio < objetivo:
            return GrafoPokemon.busqueda_binaria(lista, objetivo, medio + 1, derecha)
        else:
            return GrafoPokemon.busqueda_binaria(lista, objetivo, izquierda, medio - 1)
