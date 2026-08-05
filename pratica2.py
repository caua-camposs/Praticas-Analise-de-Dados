# Listas - Segunda Prática

# Exercício 1: Cópia vs. Referência
origem = [10 , 20 , 30]
copia = list(origem)
origem[0] = 99
print(origem)
print(copia)

# Exercício 2: Removendo Elementos com del
linguagens = ["Python", "Java", "C++", "JavaScript", "Ruby"]
del linguagens[2]
print(len(linguagens))

# Exercício 3: Concatenação de Listas Heterogêneas
dados_pessoais = ['ana' , 25]
status = [True, 'ativo']
perfil = dados_pessoais + status
for elemento in perfil: # 'elemento' é uma variável temporária, a qual foram atribuídos os valores de 'perfil'
    print(elemento)
    print(type(elemento))

# Exercício 4: Alterando Intervalos com Slicing
numeros = [1, 2, 99, 99, 5]
numeros[2:4] = [3 , 4]
print(numeros)

# Exercício 5: Desafio Combinado
compras = ["Maçã", "Banana", "Leite", "Pão", "Café"]
del compras[2]
compras = compras + ['Ovos' , 'Manteiga']
compras[0:2] = ['Maçã Verde' , 'Banana Prata']
print(compras)