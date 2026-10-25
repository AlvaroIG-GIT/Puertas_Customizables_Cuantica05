import numpy as np
from pyquil import Program
from pyquil.quilbase import DefGate
from pyquil.quilatom import Parameter, quil_cos, quil_sin
from pyquil.api import WavefunctionSimulator

# 1. Definición del parámetro simbólico
theta = Parameter('theta')

# 2. Matriz paramétrica 4x4: I (x) |0><0| + RY(theta) (x) |1><1|
cry_matrix = np.array([
    [1, 0, 0, 0],
    [0, 1, 0, 0],
    [0, 0, quil_cos(theta / 2), -quil_sin(theta / 2)],
    [0, 0, quil_sin(theta / 2),  quil_cos(theta / 2)]
])

# 3. Registro de la puerta en PyQuil
cry_definition = DefGate("CRY", cry_matrix, [theta])
CRY = cry_definition.get_constructor()

# 4. Construcción del circuito
prog = Program(cry_definition, CRY(np.pi / 2)(0, 1))

# 5. Salidas requeridas
print("--- Declaración del programa ---")
print(prog)

wfs = WavefunctionSimulator()
wf = wfs.wavefunction(prog)
print("\n--- Función de onda resultante ---")
print(wf)