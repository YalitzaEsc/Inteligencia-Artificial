import heapq

class Nodo:
    def __init__(self, estado, costo_g=0, costo_h=0, padre=None):
        self.estado = estado
        self.costo_g = costo_g
        self.costo_h = costo_h
        self.padre = padre

    def __lt__(self, otro):
        return (self.costo_g + self.costo_h) < (otro.costo_g + otro.costo_h)

def calcular_distancia(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def obtener_vecinos(actual, mapa):
    movimientos = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    vecinos = []
    for dx, dy in movimientos:
        x, y = actual.estado[0] + dx, actual.estado[1] + dy
        if 0 <= x < len(mapa) and 0 <= y < len(mapa[0]) and mapa[x][y] != '#':
            vecinos.append((x, y))
    return vecinos

def buscar_camino(mapa, inicio, objetivo):
    nodos_abiertos = []
    nodo_inicial = Nodo(inicio, 0, calcular_distancia(inicio, objetivo))
    heapq.heappush(nodos_abiertos, nodo_inicial)
    nodos_visitados = set()

    while nodos_abiertos:
        actual = heapq.heappop(nodos_abiertos)

        if actual.estado == objetivo:
            # Reconstruir camino
            camino = []
            while actual:
                camino.append(actual.estado)
                actual = actual.padre
            return camino[::-1]

        nodos_visitados.add(actual.estado)

        for vecino_estado in obtener_vecinos(actual, mapa):
            if vecino_estado not in nodos_visitados:
                costo_g = actual.costo_g + 1
                costo_h = calcular_distancia(vecino_estado, objetivo)
                nuevo_nodo = Nodo(vecino_estado, costo_g, costo_h, actual)
                heapq.heappush(nodos_abiertos, nuevo_nodo)

    return None

mapa = [
    ['.', '.', '.', '.', '.'],
    ['.', '#', '#', '#', '.'],
    ['.', '.', '.', '.', '.'],
    ['.', '#', '#', '#', '.'],
    ['.', '.', '.', '.', '.']
]

inicio = (0, 0)
objetivo = (4, 4)

camino = buscar_camino(mapa, inicio, objetivo)
if camino:
    print("Camino encontrado:", camino)
else:
    print("No se encontró camino.")
