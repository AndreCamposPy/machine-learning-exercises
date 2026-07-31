import funcoes as f

# ==================================================
# Exercício 1:
# Criar uma função que calcule a média dos valores
# de uma lista recebida como parâmetro.
# ==================================================

lista = [1,3,5,7,9,60,61,62,63,80,99,103,78,75,59]
print('BAIXA PRIORIDADE:', f.filtrar(lista, 'BAIXA PRIORIDADE'))
print('MEDIA PRIORIDADE:', f.filtrar(lista, 'MEDIA PRIORIDADE'))
print('ALTA PRIORIDADE:', f.filtrar(lista, 'ALTA PRIORIDADE'))
