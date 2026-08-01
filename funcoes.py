def primeira_fase(idade):
  return idade >= 75

def segunda_fase(idade):
  return 60 <= idade <= 74

def terceira_fase(idade):
  return idade <= 59

def filtrar(lista, fase_esperada):
  nova_lista = []
  for elemento in lista:
    if fase_esperada(elemento):
      nova_lista.append(elemento)
  return nova_lista