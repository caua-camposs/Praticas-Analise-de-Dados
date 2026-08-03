# Noções básicas de Python - Primeira prática

# Exercício 1: Atribuição e Verificação de Tipos
nome = 'Python' # classe str pois é uma string (está entre aspas)
idade = 33 # classe int pois é um número inteiro
status = 'True' # classe str pois é uma string (está entre aspas e há a pegadinha de ser uma string referente a um valor booleano)
print(type(nome))
print(type(idade))
print(type(status))

# Exercício 2: Repetição e Concatenação de Strings
palavra = 'Code'
quantidade = 3
print(palavra * quantidade)

# Exercício 3: Identificando e Corrigindo TypeError
texto = "Preço: "
valor = int("10") # no type cast, a conversão do tipo vem antes do valor, o valor é dado entre parênteses
resultado = texto * valor
print(resultado)

# Exercício 4: Conversão de Tipos (Casting)
num_str = int("42")
bool_str = bool("False")
print(num_str)
print(bool_str)
'''
Comportamento de Python para strings em bool:
Strings não vazias (tem caractere entre as aspas): True
Strings vazias (não tem caractere entre as aspas): False
É possível observar um exemplo disso na prática do Exercício 4
'''

# Exercício 5: Manipulação Avançada de Tipos e Objetos
x = 100
tipo_x = type(x)
print(tipo_x)
print(type(tipo_x)) # type também é uma classe, no caso dessa variável que serviu para guardar a verificação de um tipo