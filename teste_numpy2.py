# CÁLCULO DE IMC -> COMPARAÇÃO ENTRE LISTA E ARRAY
'''
altura = [1.80, 1.81, 1.82]
peso = [60, 70, 80]
imc = peso / (altura ** 2)
Mensagem de Erro: Traceback (most recent call last):
  File "/workspaces/Praticas-Analise-de-Dados/teste_numpy2.py", line 3, in <module>
    imc = peso / (altura ** 2)
                  ~~~~~~~^^~~
TypeError: unsupported operand type(s) for ** or pow(): 'list' and 'int'
'''
import numpy as np
np_altura = np.array([1.80, 1.81, 1.82])
print(np_altura)
np_peso = np.array([60, 70, 80])
print(np_peso)
imc = np_peso / (np_altura ** 2) # imc será do tipo array
print(imc)
print(type(imc))
# Alguns comportamentos de arrays se assemelham ao de listas, como por exemplo, na indexação. Se eu quiser pegar um elemento específico do array "imc":
imc_segunda_pessoa = imc[1]
print(imc_segunda_pessoa)
# Exemplos de uso de operador relacional com array (somente com array, tentar fazer isso com uma lista comum gerará erro):
# se os elementos são maiores que 23 (retorna booleano):
maior_que_23 = imc > 23
print(maior_que_23)
# apenas os elementos maiores que 23 (retorna o elemento em si):
maior_que_23_2 = imc[imc > 23]
print(maior_que_23_2)
# Usar o resultado de uma comparação para selecionar dados é uma maneira muito comum de obter insights.