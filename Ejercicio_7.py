from pyquil import Program
from pyquil.quilbase import DefPermutationGate
from pyquil.api import WavefunctionSimulator

# 1. Definición de la puerta permutada CCX (8 estados)
ccnot_gate = DefPermutationGate("PERMUTATION_CCNOT", [0, 1, 2, 3, 4, 5, 7, 6])
CCNOT_G = ccnot_gate.get_constructor()

# 2. Construcción del programa
prog = Program(ccnot_gate, CCNOT_G(0, 1, 2))

# 3. Salidas requeridas
print("--- Declaración del programa ---")
print(prog)

wfs = WavefunctionSimulator()
wf = wfs.wavefunction(prog)
print("\n--- Función de onda resultante ---")
print(wf)