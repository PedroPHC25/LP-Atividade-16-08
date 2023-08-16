import numpy as np
from ex_4 import funcao_4

def funcao_5(minimo, maximo, numero_de_elementos):
   arrays = funcao_4(minimo, maximo, numero_de_elementos)
   array5 = arrays[0]
   array6 = arrays[1]
   
   array_empilhado = np.row_stack((array5, array6))
   
   media = array_empilhado.mean()
   desvio_padrao = np.std(array_empilhado)
   variancia = np.var(array_empilhado)
   
#   for linha in array_empilhado:
 #      for valor in linha:
  #         if valor%2 == 0:
   #            valor = 1
    #       else:
     #          valor = -1
           
           
   
   print(array_empilhado, media, desvio_padrao, variancia)
   
   
   
funcao_5(0, 5, 10)