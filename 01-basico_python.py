print(f'Olá Mundo!')

## CONHECENDO A LINGUAGEM
# O QUE SAO TIPOS

# DEFINEM CARACTERISTICAS E COMPORTAMENTOS DE UM VALOR (OBJETO)

print(11+10)
print(21+int('11'))
print(True)
print(1.5 + 3)

str(1)

## MODO INTERATIVO 
# Existem duas formas de iniciar o modo interativo:
# chamando o interpretador (python)
# ou
# executando o scrit com a flag -i (python -i nomedoprograma.py)

## Função DIR e HELP

# DIR - retorna a lista de nomes no escopo local atual; 
# com argumento, retorna uma lista de atributos válidos para o objeto

# HELP - invoca sistema de ajuda integrado
# com argumento, informa o modulo, função, classe da variavel

### LINKS UTEIS - https://github.com/guicarvalho/trilha-python-dio
### REFERENCIAS - https://wiki.pthon.org.br/ModoInterativo


####### VARIAVEIS E CONSTANTES
# Variavel = valores que podem sofrer alterações
# Constantes = valores 'fixos' 

age, name = (72,'Sidnei')
print(f'Meu nome {name} e tenho {age} ano(s)de idade')

# alternativamente:
age = 25
name = 'Robson'
print(f'Meu nome é {name} e tenho {age} anos!')

## Python NÃO tem constantes; não existe uma palavra reservada pra informar que é uma constante como final (java) e const (C).
## Em Python, usa-se uma convenção com a variavel om o Nome Todo em Letras Maiusculas

CAMINHO_URL = 'https://x.com/home'
DEBUG = True
STATES = [
    'SP',
    'RJ',
    'MG',
]
AMOUNT = 30.2

### BOAS PRÁTICAS
# Padrão de nomes deve ser snake_case ; escolher nomes sugestivos; nome de consntates todo em maiusculo
# snake_case = nome_da_variavel

print(STATES)

### CONVERTENDO TIPOS
# Preciso para quando for fazer operações por exemplo

preco = 3
print('esse é int ',preco)
print('esse é float ',float(preco))
preconovo = preco/2
print(preconovo)

# Pra concatenar, precisa ser do mesmo tipo; exemplo:

texto = f'{str(preco)} {str(age)}'
# no caso, transformei preco e age em str
print(texto)

### FUNCOES DE ENTRADA (INPUT) E SAIDA (OUTPUT)
# input - lê dados da entrada padrão teclado na saida padrão tela.

nome = input('digita ai!')

# output - print; recebe 4 argumentos opcionais (SEP , END, FILE e FLUSH)

nome = 'Teste'
sobrenome = 'Testonildon'

print(nome,sobrenome)
print(nome,sobrenome, end='.... poxa \n')
print(nome,sobrenome,sep="#####")

## LINKS UTEIS:  
# https://docs.python.org/3/library/function.html#input
# https://docs.python.org/3/library/function.html#print
