# Matrizes NumPy - Quarta Prática

import numpy as np

# 1. Upcasting de tipos
x = np.array([10, 20, True, "30.5", False])
print(x)
# a saída impressa foi o array "x" com todos os valores como string, pelo fato de haver uma string entre os dados do array. É o que acontece quando se tem tipos de dados distintos no array.

# 2. Comparação e arrays booleanos
x = np.array([15, 22, 8, 30, 4])
resultado = x > 10 # "resultado" verifica se cada valor é maior que 10, gerando resultados booleanos
print(resultado)
print(type(resultado))
print(x[resultado]) # utilizando INDEXAÇÃO BOOLEANA, essa linha de código retornará os valores do array "x" que são maiores que 10
# também seria possível fazer isso sem uma variável, fazendo print(x[x > 10])

# 3. Dimensões de arrays
import numpy as np
x = np.array([[1, 2, 3], [4, 5, 6]])
print(x.ndim)
print(x.shape)
print(x.flatten())