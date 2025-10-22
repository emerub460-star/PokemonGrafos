# menu.py
from api_request import APIRequest
from grafos import GrafoPokemon

def main():
    # URL de la cadena de evolución de Bulbasaur
    URL = "https://pokeapi.co/api/v2/evolution-chain/1/"
    
    # Crear instancia de la API
    api = APIRequest(URL)
    chain = api.obtener_datos()

    if not chain:
        print("No se pudo obtener la cadena de evolución.")
        return

    # Construir el grafo
    grafo_pokemon = GrafoPokemon()
    grafo_pokemon.construir_grafo(chain)
    grafo_pokemon.mostrar_grafo()

    # Fase de pruebas
    pokemones = sorted(grafo_pokemon.grafo.keys())
    print("\nPokémon en la cadena (ordenados):", pokemones)

    pruebas = ["ivysaur", "charmander", "venusaur"]
    print("\n Resultados de búsqueda:")
    for nombre in pruebas:
        encontrado = grafo_pokemon.busqueda_binaria(pokemones, nombre)
        print(f"¿'{nombre}' está en la cadena? → {encontrado}")

if __name__ == "__main__":
    main()
