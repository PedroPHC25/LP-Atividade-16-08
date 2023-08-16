import numpy as np
from ex_1 import array_soma

array_redimensionado = array_soma.reshape(2, 3)
array_float = array_redimensionado.astype(float)
array_transposta = array_float.transpose()

print(array_float)
print(array_transposta)