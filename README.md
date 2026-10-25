# Práctica 5: Puertas Cuánticas Personalizadas (Custom Gates) con PyQuil

Diseño, definición matemática e implementación en software de puertas cuánticas personalizadas mediante **pyQuil** y **WavefunctionSimulator**, abarcando compuertas no paramétricas, paramétricas y permutadas[cite: 23, 24, 26].

## Contenido del Repositorio

El proyecto aborda tres metodologías de extensión de compuertas en PyQuil[cite: 23]:

### 1. Puertas No Paramétricas (`DefGate`)
Definición de compuertas a partir de matrices complejas estáticas utilizando `DefGate` y verificación de funciones de onda[cite: 24]:
- **$\sqrt{X}$ (Raíz de Pauli-X):** Descomposición espectral y cálculo a partir de la matriz de Hadamard[cite: 23, 24].
- **$\sqrt{Y}$ (Raíz de Pauli-Y):** Deducción matricial a partir de la puerta de fase $S$ mediante $S \cdot X \cdot S^\dagger$[cite: 24].
- **$\sqrt{Z}$ (Raíz de Pauli-Z):** Deducción y simulación matricial basada en transformaciones unitarias[cite: 24].

### 2. Puertas Paramétricas (`DefGate` + `Parameter`)
Modelado de compuertas controladas dependientes de un parámetro continuo $\theta$ mediante funciones simbólicas (`quil_sin`, `quil_cos`)[cite: 24, 25]:
- **$CRX(\theta)$:** Compuerta Pauli-X rotacional controlada implementada vía operadores proyectores[cite: 24, 25].
- **$CRY(\theta)$:** Rotación controlada sobre el eje Y[cite: 25, 26].
- **$CRZ(\theta)$:** Rotación de fase controlada sobre el eje Z con exponenciales complejas[cite: 26].

### 3. Puertas Permutadas (`DefPermutationGate`)
Construcción optimizada de operadores cuánticos clásicos reversibles mediante vectores de permutación[cite: 26]:
- **$CCX$ (Toffoli / CCNOT):** Permutación de base computacional sobre 3 cúbits (`PERMUTATION_CCNOT`)[cite: 26].
- **$CCCX$:** Extensión controlada a 4 cúbits ($|0\rangle\langle0| \otimes I^{\otimes 3} + |1\rangle\langle1| \otimes CCX$)[cite: 26].

## Tecnologías Utilizadas

- Python 3
- NumPy (álgebra lineal matricial)[cite: 24, 25]
- pyQuil (`DefGate`, `DefPermutationGate`, `Parameter`)[cite: 24, 25, 26]
- Rigetti Forest SDK (`quilc` & `QVM`)[cite: 24, 26]