from collections import deque

class Puzzle:
    estadoObjetivo = "12345678 "
    sucesoresTotales = []
    
    @staticmethod
    def busquedaPrimeroAnchura(inicio):
        cola = deque()
        Puzzle.busqueda(inicio, cola)

    @staticmethod
    def busquedaPrimeroProfundidad(inicio):
        pila = []
        Puzzle.busqueda(inicio, pila)

    @staticmethod
    def busqueda(inicio, estructura):
        if Puzzle.sucesoresTotales:
            Puzzle.sucesoresTotales.clear()
        
        estructura.append(inicio)
        Puzzle.sucesoresTotales.append(inicio)
        
        while estructura:
            nodo = estructura.pop(0)
            sucesores = Puzzle.obtenerSucesores(nodo)
            for hijo in sucesores:
                if hijo not in Puzzle.sucesoresTotales:
                    estructura.append(hijo)
                    Puzzle.sucesoresTotales.append(hijo)
                    if hijo == Puzzle.estadoObjetivo:
                        print("Nodos visitados:", len(Puzzle.sucesoresTotales))
                        return

    @staticmethod
    def obtenerSucesores(estadoActual):
        sucesores = []
        indice = estadoActual.index(" ")
        movimientos = [
            [1, 3],
            [0, 2, 4],
            [1, 5],
            [0, 4, 6],
            [1, 3, 5, 7],
            [2, 4, 8],
            [3, 7],
            [4, 6, 8],
            [5, 7]
        ]

        for valor in movimientos[indice]:
            sucesor = Puzzle.cambiarEstado(estadoActual, indice, valor)
            sucesores.append(sucesor)
        return sucesores

    @staticmethod
    def cambiarEstado(estadoActual, indice, valor):
        c1 = estadoActual[indice]
        c2 = estadoActual[valor]
        lista_aux = list(estadoActual)
        lista_aux[indice] = c2
        lista_aux[valor] = c1
        return ''.join(lista_aux)

if __name__ == "__main__":
    estado_inicial = "1234 5678"
    print("Búsqueda en amplitud:")
    # print("Búsqueda en profundidad:")
    
    import time
    inicio = time.time()
    Puzzle.busquedaPrimeroAnchura(estado_inicial)
    # Puzzle.busquedaPrimeroProfundidad(estado_inicial)
    fin = time.time()
    
    print("Tiempo total:", fin - inicio)
