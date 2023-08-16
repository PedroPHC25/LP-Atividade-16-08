import numpy as np
from ex_1 import funcao_1


def funcao_2(lista1, lista2, m, n):
    array_soma = funcao_1(lista1, lista2)
    array_redimensionado = array_soma.reshape(m, n)
    array_float = array_redimensionado.astype(float)
    array_transposta = array_float.transpose()
    
    return array_transposta