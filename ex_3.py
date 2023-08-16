import numpy as np
from ex_2 import funcao_2

def funcao_3(lista1, lista2, lista3, m, n):
    array3 = funcao_2(lista1, lista2, m, n)
    
    array_2d = np.array(lista3)
    array_multiplicado = array3 * array_2d
    
    return array_multiplicado   