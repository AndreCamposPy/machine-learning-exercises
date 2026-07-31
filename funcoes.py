def faixa(idade):
  if idade < 60:
    return 'BAIXA PRIORIDADE'
  elif idade < 75:
    return 'MEDIA PRIORIDADE'
  elif idade >= 75:
    return 'ALTA PRIORIDADE'

def filtrar(lista, faixa_esperada):
  nova_lista = []
  for elemento in lista:
    if faixa(elemento) == faixa_esperada:

      nova_lista.append(elemento)
  return nova_lista