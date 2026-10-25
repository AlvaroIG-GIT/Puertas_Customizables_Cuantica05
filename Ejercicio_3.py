import numpy as np
from pyquil import Program
from pyquil.quilbase import DefGate
from pyquil.api import WavefunctionSimulator

# 1. Definición de matrices base
H = (1 / np.sqrt(2)) * np.array([
    [1, 1],
    [1, -1]
])

sqrt_x = np.array([
    [0.5 + 0.5j, 0.5 - 0.5j],
    [0.5 - 0.5j, 0.5 + 0.5j]
])

# 2. Cálculo matricial: sqrt(Z) = H @ sqrt(X) @ H
sqrt_z = H @ sqrt_x @ H

# 3. Declaración de la puerta en PyQuil
sqrt_z_definition = DefGate("SQRT-Z", sqrt_z)
SQRT_Z = sqrt_z_definition.get_constructor()

# 4. Construcción del circuito
prog = Program(sqrt_z_definition, SQRT_Z(0))

# 5. Salidas por terminal
print("--- Declaración del programa ---")
print(prog)

wfs = WavefunctionSimulator()
wf = wfs.wavefunction(prog)
print("\n--- Función de onda resultante ---")
print(wf)