import funcoes as f

# ==================================================
# Exercício 1:
# você tem o seguinte problema: todo ano acontece a 
# vacinação da gripe H1N1 e, por isso, todas as
# pessoas deveriam se vacinar. Contudo, há uma ordem
# de prioridade para tomar as vacinas: primeiro, os
# idosos acima de 75 anos; depois, idosos entre 60 
# e 74 anos; e, por último, as pessoas abaixo de 60 
# anos. Então, como criar uma função que receba como
# argumento uma lista de idades e retorne uma lista 
# filtrada de acordo com a fase?
# ==================================================

lista = [1,3,5,7,9,60,61,62,63,80,99,103,78,75,59]
print('BAIXA PRIORIDADE:', f.filtrar(lista, f.terceira_fase))
print('MEDIA PRIORIDADE:', f.filtrar(lista, f.segunda_fase))
print('ALTA PRIORIDADE:', f.filtrar(lista, f.primeira_fase))

# ==================================================
# Exercício 2:
'''Você foi chamado para trabalhar como novo programador
   Python para o aplicativo Spotify, analisando as
   avaliações de músicas pelos usuários. O seu chefe
   está muito entusiasmado com a sua chegada e já pensou
   em várias perguntas para você responder. Ele coletou
   diversas avaliações dos gêneros musicais Rock e Pop.

   Em cada avaliação o usuário pode dar uma nota em 
   quantidade de estrelas para uma música, de 1 a 5. Ele 
   quer que você mapeie as avaliações numéricas em 
   categorias: entre 0 e 1 estrelas é uma música ruim, 
   entre 2 e 3 é uma música mediana e entre 4 e 5 são para 
   as músicas boas. O seu papel é dizer para o seu chefe 
   quantas músicas ruins, medianas e boas existem para 
   cada gênero: Rock e Pop.

   Além disso, ele quer saber se existe alguma música 
   mediana de Rock e se todas as músicas de Pop são boas. 
   Por fim, quer saber qual gênero musical teve uma maior 
   quantidade de músicas boas. Abaixo seguem as notas de 
   cada gênero.

   notas_rock = [5, 1, 4, 0, 2, 5, 2, 1, 0, 5, 5, 3, 5, 2, 5, 5, 3, 5, 4, 4]
   notas_pop = [3, 2, 5, 1, 2, 1, 4, 1, 5, 0, 4, 2, 1, 2, 5, 2, 4, 4, 0, 1]

    Pronto, com essas informações você pode começar a 
    desenvolver um programa em Python capaz de responder
    as perguntas do seu chefe.
'''
# ==================================================


notas_rock = [5, 1, 4, 0, 2, 5, 2, 1, 0, 5, 5, 3, 5, 2, 5, 5, 3, 5, 4, 4]
notas_pop = [3, 2, 5, 1, 2, 1, 4, 1, 5, 0, 4, 2, 1, 2, 5, 2, 4, 4, 0, 1]

print('\n', 'Alternativa com função 01:', '\n')

ruins_rock = len(list(filter(lambda x: x <= 1, notas_rock)))
medianas_rock = len(list(filter(lambda x: 2 <= x <= 3, notas_rock)))
boas_rock = len(list(filter(lambda x: 4 <= x <= 5, notas_rock)))

ruins_pop = len(list(filter(lambda x: x <= 1, notas_pop)))
medianas_pop = len(list(filter(lambda x: 2 <= x <= 3, notas_pop)))
boas_pop = len(list(filter(lambda x: 4 <= x <= 5, notas_pop)))

print('Genero Rock:')
print('Músicas ruins de Rock:', ruins_rock)
print('Músicas medianas de Rock:', medianas_rock)
print('Músicas boas de Rock:', boas_rock)
print('Genero Pop:')
print('Músicas ruins de Pop:', ruins_pop)
print('Músicas medianas de Pop:', medianas_pop)
print('Músicas boas de Pop:', boas_pop)

mediana_rock = any(map(lambda x: 2 <= x <= 3, notas_rock))
todas_boas_pop = all(map(lambda x: 4 <= x <= 5, notas_pop))

print('Existe alguma música mediana de Rock?', mediana_rock)
print('Todas as músicas de Pop são boas?', todas_boas_pop)

if boas_rock > boas_pop:
    print('O gênero musical com maior quantidade de músicas boas é Rock.')
else:
    print('O gênero musical com maior quantidade de músicas boas é Pop.')

# ou 

print('\n', 'Alternativa com função 02:', '\n')

def classificacao(notas):
    ruins = len(list(filter(lambda x: x <= 1, notas)))
    medianas = len(list(filter(lambda x: 2 <= x <= 3, notas)))
    boas = len(list(filter(lambda x: 4 <= x <= 5, notas)))
    return ruins, medianas, boas

for genero, notas in [('Rock', notas_rock), ('Pop', notas_pop)]:
    ruins, medianas, boas = classificacao(notas)
    print(f'Genero {genero}:')
    print(f'Músicas ruins de {genero}:', ruins)
    print(f'Músicas medianas de {genero}:', medianas)
    print(f'Músicas boas de {genero}:', boas)

    if boas_rock > boas_pop:
        print('O gênero musical com maior quantidade de músicas boas é Rock.')
    else:
        print('O gênero musical com maior quantidade de músicas boas é Pop.')

# ou

print('\n', 'Alternativa com função 03:', '\n')

def classificacao_nota(nota):
    if nota <= 1:
        return 'ruim'
    elif nota <= 3:
        return 'mediana'
    else:
        return 'boa'

musicas_rock = list(map(classificacao_nota, notas_rock))
musicas_pop = list(map(classificacao_nota, notas_pop))

musicas_ruins_rock = list(filter(lambda x: x == 'ruim', musicas_rock))
musicas_medianas_rock = list(filter(lambda x: x == 'mediana', musicas_rock))
musicas_boas_rock = list(filter(lambda x: x == 'boa', musicas_rock))

musicas_ruins_pop = list(filter(lambda x: x == 'ruim', musicas_pop))
musicas_medianas_pop = list(filter(lambda x: x == 'mediana', musicas_pop))
musicas_boas_pop = list(filter(lambda x: x == 'boa', musicas_pop))

mediana_rock = map(lambda x: x == 'mediana', musicas_rock)
boas_pop = map(lambda x: x == 'boa', musicas_pop)

print('Genero Rock:')
print('Músicas ruins de Rock:', len(musicas_ruins_rock))
print('Músicas medianas de Rock:', len(musicas_medianas_rock))
print('Músicas boas de Rock:', len(musicas_boas_rock))

print('Genero Pop:')
print('Músicas ruins de Pop:', len(musicas_ruins_pop))
print('Músicas medianas de Pop:', len(musicas_medianas_pop))
print('Músicas boas de Pop:', len(musicas_boas_pop))

print(mediana_rock)
print('Existe alguma música mediana de Rock?', any(mediana_rock))
print('Todas as músicas de Pop são boas?', all(boas_pop))

# ==================================================
# Exercício 3:
# Crie mensagens de log sem precisar fazer muitas configurações. 
# ==================================================

import logging

#Criação e configuração do objeto logger
logging.basicConfig(filename = 'logs.log')
logger = logging.getLogger()

#Testando o logger
logger.debug('depuração')
logger.info('informação')
logger.warning('aviso')
logger.error('erro')
logger.critical('critico')

# ==================================================
# Exercício 4:
#  Usando o parâmetro level no basicConfig(), você
#  deve definir o nível de mensagens de log que deseja registrar. 
# ==================================================

import logging

#Criação e configuração do objeto logger
FORMATACAO_MSG = "%(asctime)s | %(levelname)s -> %(message)s"
logging.basicConfig(filename = 'logs.log',
level = logging.DEBUG,
format = FORMATACAO_MSG)
logger = logging.getLogger()

#Testando o logger
logger.debug('depuração')
logger.info('informação')
logger.warning('aviso')
logger.error('erro')
logger.critical('critico')

# ==================================================
# Exercício 5:
# Defina a data e hora de um evento ocorrido em 16/07/2014 às 23:00;
# Obtenha a data e hora atual do sistema;
# Calcule o tempo decorrido entre as duas datas;
# Apresente o resultado em anos, meses, dias, horas, minutos e segundos.
# ==================================================

import datetime
d1 = datetime.datetime(2014,7,16,23)
d2 = datetime.datetime.now()
diff = d1 - d2
days = diff.days
years, days = days // 365, days % 365
months, days = days // 30, days % 30
seconds = diff.seconds
hours, seconds = seconds // 3600, seconds % 3600
minutes, seconds = seconds // 60, seconds % 60
print("Desde {} passaram {} anos, {} meses, {} dias" \
", {} horas, {} minutos e {} segundos"
.format(d1, years, months, days, hours, minutes, seconds))

# ==================================================
# Exercício 6:
# Utilize o método de Monte Carlo para estimar a probabilidade de dois dados,
# lançados simultaneamente, apresentarem o mesmo lado voltado para cima.
# Realize vários lançamentos aleatórios dos dois dados;
# Conte quantas vezes os dois dados apresentaram o mesmo resultado;
# Calcule a probabilidade estimada a partir da quantidade de ocorrências
# em relação ao número total de lançamentos;
# Apresente o resultado da probabilidade encontrada.
# ==================================================

import random

numero_de_tentativas = 2000000
quantidade_de_acertos = 0

for _ in range(numero_de_tentativas):
  dado_1 = random.randint(1,6)
  dado_2 = random.randint(1,6)

  if (dado_1 == dado_2):
    quantidade_de_acertos += 1

print(quantidade_de_acertos/numero_de_tentativas) 

# ============================================================
#  Exercício 6: - OFICINA AULA 2 - PEDRA, PAPEL E TESOURA
# ============================================================

# ETAPA 1
# ------------------------------------------------------------
# Pedra, papel e tesoura é um jogo que possui um elemento de
# aleatoriedade.
#
# Escreva um código que utilize a biblioteca Random para
# recriar esse jogo.
#
# O jogo deve apresentar as opções:
# 1 - Pedra
# 2 - Papel
# 3 - Tesoura
# 4 - Sair
#
# O jogador pode escolher qualquer uma das opções, mas o jogo
# somente deve finalizar quando a opção "Sair" for escolhida.
#
# A máquina deve escolher sua jogada de forma aleatória.
#
#
# ETAPA 2
# ------------------------------------------------------------
# Agora, melhore o jogo fazendo com que a máquina aprenda
# com as jogadas anteriores do jogador utilizando Machine
# Learning.
#
# Para isso, utilize o algoritmo ZeroR.
#
# O ZeroR deve identificar qual foi a jogada mais utilizada
# pelo jogador e, a partir disso, a máquina deve escolher a
# jogada que vence essa escolha.
#
# Como a máquina não possui histórico no início da partida,
# as primeiras jogadas devem continuar sendo aleatórias.
#
# Após o quinto turno, a máquina deve começar a utilizar o
# histórico das jogadas do jogador para identificar sua
# jogada mais frequente.


# ============================================================
# IMPORTAÇÃO DA BIBLIOTECA
# ============================================================

# A biblioteca random será utilizada para que a máquina possa
# realizar suas primeiras jogadas de forma aleatória.

import funcoes

funcoes.jogo_pedra_papel_tesoura()