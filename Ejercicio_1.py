import numpy as np
from pyquil import Program
from pyquil.quilbase import DefGate
from pyquil.api import WavefunctionSimulator

# 1. Definición de la matriz raíz de Pauli-X
sqrt_x = np.array([
    [0.5 + 0.5j, 0.5 - 0.5j],
    [0.5 - 0.5j, 0.5 + 0.5j]
])

# 2. Declaración del constructor de la puerta customizada
sqrt_x_definition = DefGate("SQRT-X", sqrt_x)
SQRT_X = sqrt_x_definition.get_constructor()

# 3. Construcción del circuito
prog = Program(sqrt_x_definition, SQRT_X(0))

# 4. Impresión de la declaración del programa
print("--- Declaración del programa ---")
print(prog)

# 5. Cálculo y visualización de la función de onda
wfs = WavefunctionSimulator()
wf = wfs.wavefunction(prog)

print("\n--- Función de onda resultante ---")
print(wf)


