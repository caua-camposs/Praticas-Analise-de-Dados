# Arrays NumPy - Terceira Prática

import numpy as np

# Exercício 1: Importação de Pacote e Criação de Array
lista = [10, 20, 30, 40, 50]
# conversão da lista para array:
meu_array = np.array(lista) # coloca somente entre parênteses nesse caso, sem necessidade de colchete adicional
print(meu_array)
print(type(meu_array))

# Exercício 2: Substituição de Conteúdo com .replace()
texto = "Estudando linguagem C++ no DataCamp"
novo_texto = texto.replace('C++' , 'Python')
print(novo_texto)

# Exercício 3: Identificando e Corrigindo NameError
# Tentativa de criar um array sem o namespace correto
'''
numeros = [5, 10, 15]
resultado = array(numeros)
print(resultado)
'''
# Execução correta:
numeros = [5, 10, 15]
resultado = np.array(numeros)
print(resultado)

# Exercício 4: Explorando a Documentação com help()
# Execute no seu terminal ou notebook:
help(str.replace)
'''
str.replace(old, new[, count])
Método opcional: count
O parâmetro count define a quantidade máxima de substituições que o método deve realizar na string, contando da esquerda para a direita.
Se você não informar o count, o Python substitui todas as ocorrências encontradas por padrão.
Exemplo:

texto = "banana"

# Sem o argumento count (substitui TUDO):
print(texto.replace("a", "o"))     # Saída: "bonono"

# Com count = 1 (substitui apenas a PRIMEIRA ocorrência):
print(texto.replace("a", "o", 1))  # Saída: "bonana"

# Com count = 2 (substitui apenas as DUAS primeiras ocorrências):
print(texto.replace("a", "o", 2))  # Saída: "bonona"
'''

# Exercício 5: Operações em Arrays NumPy vs. Listas
lista_comum = [1, 2, 3]
array_numpy = np.array([1, 2, 3])
# Multiplicação da lista
lista_mult = lista_comum * 2
# Multiplicação do array
array_mult = array_numpy * 2
print(lista_mult)
print(array_mult)
# Lista * 2 retorna a lista duplicada. Array * 2 retorna cada número dentro do array multiplicados por 2