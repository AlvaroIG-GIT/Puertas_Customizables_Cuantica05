import numpy as np
from pyquil import Program
from pyquil.quilbase import DefGate
from pyquil.quilatom import Parameter, quil_cos, quil_sin
from pyquil.api import WavefunctionSimulator

# 1. Definición del parámetro simbólico
theta = Parameter('theta')

# 2. Exponenciales complejas vía fórmula de Euler:
# exp(-i * theta / 2) = cos(theta / 2) - 1j * sin(theta / 2)
# exp( i * theta / 2) = cos(theta / 2) + 1j * sin(theta / 2)
exp_neg = quil_cos(theta / 2) - 1j * quil_sin(theta / 2)
exp_pos = quil_cos(theta / 2) + 1j * quil_sin(theta / 2)

# 3. Matriz paramétrica 4x4
crz_matrix = np.array([
    [1, 0, 0, 0],
    [0, 1, 0, 0],
    [0, 0, exp_neg, 0],
    [0, 0, 0, exp_pos]
])

# 4. Registro de la puerta en PyQuil
crz_definition = DefGate("CRZ", crz_matrix, [theta])
CRZ = crz_definition.get_constructor()

# 5. Construcción del circuito
prog = Program(crz_definition, CRZ(np.pi / 2)(0, 1))

# 6. Salidas requeridas
print("--- Declaración del programa ---")
print(prog)

wfs = WavefunctionSimulator()
wf = wfs.wavefunction(prog)
print("\n--- Función de onda resultante ---")
print(wf)