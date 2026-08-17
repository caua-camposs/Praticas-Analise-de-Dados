'''
lista de listas = sublistas
cada sublista de uma lista corresponde a uma linha da matriz, os elementos de cada lista são as colunas
usando .shape pode-se ver quantas linhas e colunas possui a matriz
'''
import numpy as np
np_2d_teste = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
print(np_2d_teste)
print(type(np_2d_teste))
print(np_2d_teste.shape) # .shape para ver a composição da matriz. Ele é um atributo, apesar de ser chamado no código igual a um método -> métodos tem parênteses depois, atributos não
print(np_2d_teste.ndim) # .ndim para ver quantas dimensões a matriz tem. Ele também é um atributo
'''
assim como no numpy, a regra de apenas um tipo nos arrays também se aplica para as matrizes 2D
para selecionar um elemento específico na matriz 2d, chama-se dois índices, ambos entre colchetes, selecionando primeiro o índice da linha, e depois o índice correspondente ao elemento dentro da linha (lista)
'''
print(np_2d_teste[0][2]) # índice 0 corresponde à linha "[1, 2, 3, 4, 5]", índice 2 corresponde ao número 3
# também é possível fazer a seleção com colchetes e vírgula
print(np_2d_teste[1 , 0]) # índice 1 corresponde à linha "[6, 7, 8, 9, 10]", índice 0 corresponde ao número 6. Valor antes da vírgula = linha, valor depois da vírgula = coluna
# para selecionar mais de um elemento:
# um de cada array:
print(np_2d_teste[[0, 1] , [2, 1]])
# índices 0 e 1 de ambos os arrays (linhas):
print(np_2d_teste[: , [0, 1]])
# pegando uma fatia de elementos de ambos os arrays:
print(np_2d_teste[:, 0:3])
# o contrário dos dois últimos testes:
print(np_2d_teste[[0, 1] , :])
print(np_2d_teste[0:2 , :])
'''
matrizes 2d vão possuir sempre 2 linhas, cujos índices são 0 e 1
as matrizes 2D do NumPy permitem fazer cálculos elemento a elemento, da mesma forma que matrizes 1D
'''