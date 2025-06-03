# autor: Michel
# data: 03/06/2025

# revisão sobre funções

#######################  1  ######################
print("#######################  1  ######################")

# definição de funções em python.
# Funções são blocos de código que realizam uma tarefa específica.
# Elas podem receber entradas (parâmetros) e retornar saídas (valores).
# As funções são definidas com a palavra-chave 'def', seguida pelo nome da função,
# parênteses com os parâmetros (se houver) e dois pontos.
# A sintaxe básica é:
# def nome_da_funcao(parametro1, parametro2):
#     # bloco de código
#     return valor_de_retorno
# A função pode ser chamada pelo nome, passando os argumentos necessários.
# Exemplo de função simples:
print("Exemplo de função simples:")
def saudacao(nome):
    return f"Olá, {nome}!"
# Chamada da função
print(saudacao("Maria"))  # Saída: Olá, Maria!

#####################################################

#######################  2  ######################
print("#######################  2  ######################")

# palavra chave: def, parâmetros, (), return

#ex0, procedimento com retorno None e uma variável local
def nome_procedimento(): # -> None
  local = 1 # variável local 
  print("Este é um procedimento sem retorno.")

# variável global
global_var = 1  # variável global, acessível em todo o escopo do módulo

# ex1, função com retorno None e uma variável local
def nome_funcao1(): # -> None
  local =1
  print()
  
# ex2, função com retorno e uma variável local
# entrada -> parâmetro # saída -> retorno
def nome_funcao2(entrada): # parâmetro = argumento
  entrada += entrada
  saida = entrada # variável local 
  return saida # 

# ex3, função com vários parâmetros e retorno de múltiplos valores
# entrada -> parâmetros # saída -> retorno
# varias (entrada1, entrada2, entrada3, ...)
def nome_funcao3(entrada1, entrada2):
  # variáveis locais
  soma = entrada1 + entrada2 # x+y soma é uma variável local
  subtracao = entrada1 - entrada2 # x-y
  multiplica = entrada1 * entrada2 # x*y
  divisao = entrada1 / entrada2 # x/y
  pot = entrada1 ** entrada2 # x^y
  return soma, subtracao, multiplica, divisao, pot # tupla (soma, subtração, multiplica, divisao, pot)


# chamada de funções # procedimento
# chamada de procedimento
valor_procedimento = nome_procedimento()
# chamada de funções
valor_funcao1 = nome_funcao1()

# chamada de funções com argumentos
valor_funcao2 = nome_funcao2(1)  # argumento -> 1
valor_funcao3 = nome_funcao3(1,2) # argumentos -> 1 e 2
soma, subtracao, maria, dani, davi = nome_funcao3(1,2)

# printando os valores retornados
print(f"valor procedimento = {valor_procedimento}")
print(f"valor função1 = {valor_funcao1}")
print(f"valor função2 = {valor_funcao2}")
print(f"valor função3 = {valor_funcao3}, que é uma {type(valor_funcao3)}")
print(f"entrada1 + entrada2 = {soma}, que é uma {type(soma)}")
print(f"entrada1 - entrada2 = {subtracao}, que é uma {type(subtracao)}")
print(f"entrada1 * entrada2 = {maria}, que é uma {type(maria)}")
print(f"entrada1 / entrada2 = {dani}, que é uma {type(dani)}")
print(f"entrada1 ^ entrada2 = {davi}, que é uma {type(davi)}")


##################################################

#######################  3  ######################
print("#######################  3  ######################")

# escopo da variável (local, global)
def nome_funcao4():
  #variável local
  nome = input("informe seu nome: ") # variável local
  # exemplo uso global
  print(f"data = {data}")
  return f"bom dia, {nome}"

# global
data = "03/06/2025"

# chamada da função 
print(f"{nome_funcao4()}, hoje é {data}") 

##################################################