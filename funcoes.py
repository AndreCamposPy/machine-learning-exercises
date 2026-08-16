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


def contar_casas_decimais(valor):
  """Retorna o número de casas decimais de `valor`.

  Aceita `int`, `float`, `decimal.Decimal` ou `str`.
  - Para `int` retorna 0.
  - Para `Decimal` respeita os zeros finais (usa o expoente diretamente).
  - Para `float` converte para `Decimal(str(valor))` (evita precisão binária).
  - Para `str` conta os dígitos após o ponto decimal (preserva zeros finais).
  """
  from decimal import Decimal, InvalidOperation

  # inteiro
  if isinstance(valor, int):
    return 0

  # Decimal: use o expoente (preserva zeros finais)
  if isinstance(valor, Decimal):
    exp = valor.as_tuple().exponent
    return max(0, -exp)

  # Float ou outros: tente converter para Decimal via string
  try:
    d = Decimal(str(valor))
    exp = d.as_tuple().exponent
    return max(0, -exp)
  except (InvalidOperation, ValueError, TypeError):
    # Fallback para strings ou valores estranhos: conte após '.'
    try:
      s = str(valor)
      if '.' in s:
        return len(s.split('.')[-1])
      return 0
    except Exception:
      return 0


def jogada_mais_usada(historico):
    """Identifica a jogada mais frequente no histórico do jogador."""
    contagem = {}

    for jogada in historico:
        if jogada not in contagem:
            contagem[jogada] = 0
        contagem[jogada] += 1

    return max(contagem, key=contagem.get)


def jogada_que_ganha(jogada_jogador):
    """Retorna a jogada que vence a escolha do jogador."""
    if jogada_jogador == "Pedra":
        return "Papel"
    elif jogada_jogador == "Papel":
        return "Tesoura"
    elif jogada_jogador == "Tesoura":
        return "Pedra"


def jogo_pedra_papel_tesoura():
    """Executa o jogo Pedra, Papel e Tesoura com placar final."""
    import random

    jogadas = ["Pedra", "Papel", "Tesoura"]
    historico_jogador = []
    turno = 0
    placar = {
        "jogador": 0,
        "maquina": 0,
        "empates": 0,
    }

    while True:
        print("\nEscolha uma opção (1, 2, 3 ou 4):")
        print("1 - Pedra")
        print("2 - Papel")
        print("3 - Tesoura")
        print("4 - Sair")

        opcao = input("Digite sua escolha: ")

        if opcao == "4":
            print("\nJogo encerrado!")
            print("\nPlacar final:")
            print(f"Você: {placar['jogador']}")
            print(f"Máquina: {placar['maquina']}")
            print(f"Empates: {placar['empates']}")
            return placar

        if opcao not in ["1", "2", "3"]:
            print("\nOpção inválida! Escolha 1, 2, 3 ou 4.")
            continue

        if opcao == "1":
            jogada_jogador = "Pedra"
        elif opcao == "2":
            jogada_jogador = "Papel"
        else:
            jogada_jogador = "Tesoura"

        historico_jogador.append(jogada_jogador)
        turno += 1

        if turno <= 5:
            jogada_maquina = random.choice(jogadas)
            metodo = "aleatoriedade"
        else:
            jogada_mais_frequente = jogada_mais_usada(historico_jogador)
            jogada_maquina = jogada_que_ganha(jogada_mais_frequente)
            metodo = "ZeroR"

        print(f"\nSua jogada -> {jogada_jogador}")
        print(f"Jogada da máquina -> {jogada_maquina}")
        print(f"Método utilizado pela máquina -> {metodo}")

        if jogada_jogador == jogada_maquina:
            print("Empate!")
            placar["empates"] += 1
        elif (
            (jogada_jogador == "Pedra" and jogada_maquina == "Tesoura")
            or
            (jogada_jogador == "Papel" and jogada_maquina == "Pedra")
            or
            (jogada_jogador == "Tesoura" and jogada_maquina == "Papel")
        ):
            print("Você ganhou!")
            placar["jogador"] += 1
        else:
            print("A máquina ganhou!")
            placar["maquina"] += 1