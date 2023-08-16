import numpy as np
import numpy.random as npr

def funcao_4(minimo, maximo, numero_de_elementos):
    array5 = npr.randint(minimo, maximo, numero_de_elementos)
    array6 = npr.randint(minimo, maximo, numero_de_elementos)
    
    intersecao = np.intersect1d(array5, array6)
    indices_intersecao_array5 = []
    indices_intersecao_array6 = []
    
    for valor_comum in intersecao:
        indices_intersecao_array5.append(np.where(array5 == valor_comum))
        indices_intersecao_array6.append(np.where(array6 == valor_comum))
    
    for indice in indices_intersecao_array5:
        array5_removido = np.delete(array5, indice)
    
    return [array5, array6, intersecao, indices_intersecao_array5, indices_intersecao_array6, array5_removido]
    print([array5, array6, intersecao, indices_intersecao_array5, indices_intersecao_array6, array5_removido])