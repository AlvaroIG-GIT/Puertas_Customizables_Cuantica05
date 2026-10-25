from pyquil import Program
from pyquil.quilbase import DefPermutationGate
from pyquil.api import WavefunctionSimulator

# 1. Definición del vector de permutación para 16 estados (4 qúbits)
# Se mantienen iguales del 0 al 13, y se intercambian el 14 y el 15:
permutacion_cccx = list(range(14)) + [15, 14]

# 2. Definición de la puerta permutada CCCX
cccx_gate = DefPermutationGate("PERMUTATION_CCCX", permutacion_cccx)
CCCX_G = cccx_gate.get_constructor()

# 3. Construcción del programa
prog = Program(cccx_gate, CCCX_G(0, 1, 2, 3))

# 4. Salidas requeridas
print("--- Declaración del programa ---")
print(prog)

wfs = WavefunctionSimulator()
wf = wfs.wavefunction(prog)
print("\n--- Función de onda resultante ---")
print(wf)