import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl

def triangular_mf(x, a, b, c):
    return np.fmax(np.fmin((x - a) / (b - a), (c - x) / (c - b)), 0)

sistema = ctrl.ControlSystem()

distancia = ctrl.Antecedent(np.arange(0, 11, 1), 'distancia')
angulo = ctrl.Antecedent(np.arange(0, 121, 1), 'angulo')

distancia['cerca'] = fuzz.trimf(distancia.universe, [0, 2, 5])
distancia['media'] = fuzz.trimf(distancia.universe, [2, 5, 8])
distancia['lejos'] = fuzz.trimf(distancia.universe, [5, 8, 10])

angulo['izquierda'] = triangular_mf(angulo.universe, 0, 30, 60)
angulo['frontal'] = triangular_mf(angulo.universe, 30, 60, 90)
angulo['derecha'] = triangular_mf(angulo.universe, 60, 90, 120)

ubicacion_x = ctrl.Consequent(np.arange(-10, 11, 1), 'ubicacion_x')
ubicacion_y = ctrl.Consequent(np.arange(-10, 11, 1), 'ubicacion_y')

ubicacion_x['izquierda'] = fuzz.trimf(ubicacion_x.universe, [-10, -5, 0])
ubicacion_x['centro'] = fuzz.trimf(ubicacion_x.universe, [-5, 0, 5])
ubicacion_x['derecha'] = fuzz.trimf(ubicacion_x.universe, [0, 5, 10])

ubicacion_y['abajo'] = fuzz.trimf(ubicacion_y.universe, [-10, -5, 0])
ubicacion_y['centro'] = fuzz.trimf(ubicacion_y.universe, [-5, 0, 5])
ubicacion_y['arriba'] = fuzz.trimf(ubicacion_y.universe, [0, 5, 10])

regla1 = ctrl.Rule(distancia['cerca'] & angulo['frontal'], (ubicacion_x['centro'], ubicacion_y['arriba']))
regla2 = ctrl.Rule(distancia['media'] & angulo['frontal'], (ubicacion_x['centro'], ubicacion_y['centro']))
regla3 = ctrl.Rule(distancia['lejos'] & angulo['frontal'], (ubicacion_x['centro'], ubicacion_y['abajo']))
regla4 = ctrl.Rule(distancia['media'] & angulo['izquierda'], (ubicacion_x['izquierda'], ubicacion_y['centro']))
regla5 = ctrl.Rule(distancia['media'] & angulo['derecha'], (ubicacion_x['derecha'], ubicacion_y['centro']))

sistema.add_rules([regla1, regla2, regla3, regla4, regla5])

simulacion = ctrl.ControlSystemSimulation(sistema)

simulacion.input['distancia'] = 3.5
simulacion.input['angulo'] = 45

simulacion.compute()

ubicacion_objeto_x = simulacion.output['ubicacion_x']
ubicacion_objeto_y = simulacion.output['ubicacion_y']

print("Distancia al objeto: 3.5 metros")
print("Ángulo: 45 grados")
print("Ubicación del objeto (X):", ubicacion_objeto_x, "metros")
print("Ubicación del objeto (Y):", ubicacion_objeto_y, "metros")
