

class HeuristicaPolisemias:
    def __init__(self):
        self.reglas = {
            "banco": {"contexto": ["financiero", "económico"], "significado": "institución financiera"},
            "banco": {"contexto": ["asiento"], "significado": "asiento"},
            "llave": {"contexto": ["cerradura"], "significado": "herramienta para abrir cerraduras"},
            "llave": {"contexto": ["agua", "tubería"], "significado": "pieza para abrir o cerrar el paso de un líquido"},
            "corte": {"contexto": ["división", "separación"], "significado": "acción de dividir o separar algo"},
            "corte": {"contexto": ["espacio de tiempo"], "significado": "espacio de tiempo, como en 'a media tarde'"},
            "nota": {"contexto": ["escuela", "examen"], "significado": "calificación en un examen"},
            "nota": {"contexto": ["escritura", "observación"], "significado": "marca escrita, observación o apunte"},
            "mesa": {"contexto": ["mueble"], "significado": "mueble con patas para comer o trabajar"},
            "mesa": {"contexto": ["negociación", "discusión"], "significado": "grupo de personas que negocian o discuten un tema"},
            "planta": {"contexto": ["industrial", "fábrica"], "significado": "instalación de producción"},
            "planta": {"contexto": ["vegetal"], "significado": "especie vegetal"},
            "vela": {"contexto": ["ceremonias"], "significado": "fuente de luz utilizada en ceremonias o como decoración"},
            "vela": {"contexto": ["náutica"], "significado": "pieza de tela que se usa para impulsar una embarcación"},
            "caja": {"contexto": ["contenedor"], "significado": "recipiente para guardar objetos"},
            "caja": {"contexto": ["institución financiera"], "significado": "institución financiera"}
        }

    def determinar_significado(self, palabra, contexto):
        significado_mas_probable = None
        for polisemia, regla in self.reglas.items():
            if polisemia == palabra and contexto in regla["contexto"]:
                significado_mas_probable = regla["significado"]
                break
        return significado_mas_probable

heuristica = HeuristicaPolisemias()
palabra = "banco"
contexto = "financiero"
significado = heuristica.determinar_significado(palabra, contexto)
print(f"El significado más probable de '{palabra}' en el contexto de '{contexto}' es: {significado}")
