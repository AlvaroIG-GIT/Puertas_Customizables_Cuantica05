import numpy as np
from pyquil import Program
from pyquil.quilbase import DefGate
from pyquil.api import WavefunctionSimulator

# 1. Definición de las matrices base
S = np.array([
    [1, 0],
    [0, 1j]
])

sqrt_x = np.array([
    [0.5 + 0.5j, 0.5 - 0.5j],
    [0.5 - 0.5j, 0.5 + 0.5j]
])

# 2. Cálculo matricial: sqrt(Y) = S @ sqrt(X) @ S.T
sqrt_y = S @ sqrt_x @ S.T

# 3. Declaración de la puerta en PyQuil
sqrt_y_definition = DefGate("SQRT-Y", sqrt_y)
SQRT_Y = sqrt_y_definition.get_constructor()

# 4. Construcción del circuito
prog = Program(sqrt_y_definition, SQRT_Y(0))

# 5. Salidas por terminal
print("--- Declaración del programa ---")
print(prog)

wfs = WavefunctionSimulator()
wf = wfs.wavefunction(prog)
print("\n--- Función de onda resultante ---")
print(wf)