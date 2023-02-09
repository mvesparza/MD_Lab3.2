"""
Programa que encuentra todos los caminos desde un nodo inicio hasta un nodo meta en un grafo.

Autor: Marco Vinicio Esparza

Versión: v1.2
"""
def búsqueda_en_amplitud(grafo, inicio, meta):
    """
    Proceso que implementa un algoritmo de búsqueda en amplitud para encontrar todos los caminos en el grafo dado.
    Parámetros:
    --------------
    Si, recibe tres:
    grafo: un diccionario que representa un grafo.
    inicio: una cadena de caracteres que representa el nodo inicial.
    meta: una cadena de caracteres que representa el nodo meta o destino.

    Retorna:
    --------------
    Si, retorna una lista de listas de nodos, cada una de las cuales representa un camino posible desde el nodo inicio hasta el nodo meta.
    """

    # Se crea una cola con el primer nodo y su camino
    cola = [(inicio, [inicio])]
    # Se crea una lista para guardar los resultados
    resultados = []
    # Mientras haya nodos en la cola
    while cola:
        # Se extrae el primer nodo y su camino
        (nodo, camino) = cola.pop(0)
        # Si el nodo actual es el nodo objetivo
        if nodo == meta:
            # Se agrega el camino a los resultados
            resultados.append(camino)
        # Para cada grafoad del nodo actual
        for grafoad in grafo[nodo]:
            # Se agrega el grafoad y su camino a la cola
            cola.append((grafoad, camino + [grafoad]))
    # Se devuelve los resultados
    return resultados

if __name__ == '__main__':
    # Se define un grafo como un diccionario en el que cada nodo es una clave y sus adyacentes son los valores asociados a la clave
    grafo = {
    "Quito": ["Guayaquil", "Bogotá"],  # Quito es el inicio y es adyacente a Guayaquil y Bogotá
    "Guayaquil": ["Caracas"],  # Guayaquil es adyacente a Caracas
    "Caracas": ["Madrid"],  # Caracas es adyacente a Madrid
    "Madrid": ["Roma", "Milán"],  # Madrid es adyacente a Roma y Milán
    "Roma": ["Cerdeña"],  # Roma es adyacente a Cerdeña
    "Bogotá": ["París"],  # Bogotá es adyacente a París
    "París": ["Madrid"],  # París es adyacente a Madrid
    "Milán": ["Cerdeña"],  # Milán es adyacente a Cerdeña
    "Cerdeña": [],  # Cerdeña es la meta
    }

    # Se define de un diccionario para almacenar los costos de viajar de un nodo a otro, el costo por cada viaje es 1
    costo = {
    ("Quito", "Guayaquil"): 1,
    ("Quito", "Bogotá"): 1,
    ("Guayaquil", "Caracas"): 1,
    ("Caracas", "Madrid"): 1,
    ("Madrid", "Roma"): 1,
    ("Roma", "Cerdeña"): 1,
    ("Bogotá", "París"): 1,
    ("París", "Madrid"): 1,
    ("Madrid", "Milán"): 1, 
    ("Milán", "Cerdeña"): 1, 
    }
    # inicializar el programa
    print("********* CAMINOS DISPONIBLES DE QUITO A CERDEÑA *********")
    # iniciar bucle para repetir el proceso las veces que el usuario quiera
    while(True):
        # Se define del nodo de inicio
        inicio = "Quito"
        # Se define del nodo meta o destino
        meta = "Cerdeña"
        # Llamada a la función búsqueda_en_amplitud para encontrar los caminos desde inicio hasta meta
        caminos = búsqueda_en_amplitud(grafo, inicio, meta)
        if len(caminos) > 0:
            # Se pregunta al usuario por el camino que desea ver
            opcion = int(input("Hay {} caminos encontrados, ¿Cuál camino desea ver? (Introduzca un número entre 1 y {}): ".format(len(caminos), len(caminos))))
            # Se verifica que la opción introducida sea válida
            if opcion > 0 and opcion <= len(caminos):
                camino_seleccionado = caminos[opcion - 1]
                # Imprime el camino seleccionado en formato: Camino i desde inicio hasta meta: [nodo1, nodo2, ..., nodo_n]
                print("Camino {} desde {} hasta {}: {}".format(opcion, inicio, meta, camino_seleccionado)) 
                # Imprime el costo total del camino seleccionado en formato: Costo total en el camino i: costo
                print("Costo total en el camino {}: {}".format(opcion, sum([costo[(camino_seleccionado[i], camino_seleccionado[i+1])] for i in range(len(camino_seleccionado) - 1)])))
            else:
                # Si la opción introducida no es válida, se imprime un mensaje de error
                print("Opción no válida, introduzca un número entre 1 y {}".format(len(caminos)))
        else:
            # Si no se encontraron caminos, se imprime un mensaje informativo
            print("No se encontraron caminos desde {} hasta {}".format(inicio, meta))
        # Se pregunta al usuario si quiere volver a usar el programa  
        repetirProceso = input("¿Repetir proceso? (si/no): ")
        if repetirProceso.lower() != "si":
            print("********** FIN DEL PROCESO **********")
            # detener el bucle por completo
            break