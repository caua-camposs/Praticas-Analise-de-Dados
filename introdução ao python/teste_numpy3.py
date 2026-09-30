# Teste dos métodos .flatten() e .reshape()
import numpy as np
x = np.array([[1,2,3] , [5,6,7]])
print(x)
print(x.shape) # 2 linhas, 3 colunas
print(x.ndim) # 2 dimensões
y = x.flatten() # reorganizou o array "x" para uma única dimensão
print(y)
print(x , y) # comparação de que o método .flatten() não modifica o array original, mas sim cria uma cópia
z = x.reshape(3 , 2) # reorganiza o array para uma nova composição, no caso do array x que antes era (2 , 3 - 2 linhas e 3 colunas), agora é (3 , 2 - 3 linhas e 2 colunas)
# é necessário passar para o .reshape() os argumentos de acordo com a nova composição dimensional que você quer no array
print(z)
print(x) # mostrando que, nesse caso, o método .reshape() não modificou o array original
'''
Analisar depois:
passagem de argumento pro método .flatten()
o que acontece se eu não declarar os métodos em uma variável, e sim fora de uma variável
'''