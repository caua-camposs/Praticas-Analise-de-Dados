'''
import numpy
numpy.array = [1,2,3,4,5]
'''

# ARRAYS
import numpy as np

# Lista nativa do Python
minha_lista = [1, 2, 3, 4]

# Array NumPy
meu_array = np.array([1, 2, 3, 4])

# Multiplicação por 2:
print(minha_lista * 2) 
# Saída: [1, 2, 3, 4, 1, 2, 3, 4] (Duplica/repete a lista)

print(meu_array * 2)   
# Saída: [2, 4, 6, 8] (Multiplica cada número individualmente)