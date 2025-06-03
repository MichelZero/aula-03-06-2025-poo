# autor: Michel
# data: 03/06/2025

# revisão sobre funções

#######################  1  ######################
print("#######################  1  ######################")

# definição de funções em python
# palavra chave: def, parâmetros, (), return

#ex01
def nome_procedimento(): 
  local =1
  print()

local =1

def nome_funcao1(): # -> None
  local =1
  print()
  

# entrada -> parâmetro
def nome_funcao2(entrada): # parâmetro = argumento
  entrada += entrada
  saida = entrada
  return saida # qqcoisa

# varias (entrada1, entrada2, entrada3, ...)
def nome_funcao3(entrada1, entrada2):
  soma = entrada1 + entrada2 # x+y
  subtracao = entrada1 - entrada2 # x-y
  multiplica = entrada1 * entrada2 # x*y
  divisao = entrada1 / entrada2 # x/y
  pot = entrada1 ** entrada2 # x^y
  return soma, subtracao, multiplica, divisao, pot # tupla (soma, subtração, multiplica, divisao, pot)

# chamada das funções
valor_procedimento = nome_procedimento()
valor_funcao1 = nome_funcao1()
valor_funcao2 = nome_funcao2(1)  # argumento -> 1
valor_funcao3 = nome_funcao3(1,2) # argumentos -> 1 e 2
soma, subtracao, maria, dani, davi = nome_funcao3(1,2)

# printar
print(f"valor procedimento = {valor_procedimento}")
print(f"valor função1 = {valor_funcao1}")
print(f"valor função2 = {valor_funcao2}")
print(f"valor função3 = {valor_funcao3}, que é uma {type(valor_funcao3)}")
print(f"entrada1 + entrada2 = {soma}, que é uma {type(soma)}")
print(f"entrada1 - entrada2 = {subtracao}, que é uma {type(subtracao)}")
print(f"entrada1 * entrada2 = {maria}, que é uma {type(maria)}")
print(f"entrada1 / entrada2 = {dani}, que é uma {type(dani)}")
print(f"entrada1 ^ entrada2 = {davi}, que é uma {type(davi)}")


# escopo da variável (local, global)
def nome_funcao4():
  #variável local
  nome = input("informe seu nome: ")
  # exemplo uso global
  print(f"data = {data}")
  return f"bom dia, {nome}"

# global
data = "03/06/2025"

print(f"{nome_funcao4()}, hoje é {data}")

##################################################