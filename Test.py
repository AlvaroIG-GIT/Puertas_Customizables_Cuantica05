from pyquil.api import WavefunctionSimulator
from pyquil import Program
from pyquil.gates import H

wfs = WavefunctionSimulator()
wf = wfs.wavefunction(Program(H(0)))
print("Conexión exitosa:")
print(wf)