# Tabuleiro do Jogo da Velha
tabuleiro = [
    ["1", "2", "3"],
    ["4", "5", "6"],
    ["7", "8", "9"]
]

# Função que, dado um tabuleiro, exibe esse tabuleiro de Jogo da Velha no console.
def exibir_tabuleiro(tabuleiro):
    for linha in tabuleiro:
        print(" | ".join(linha))
        print("-" * 9)

# Função que, dado um tabuleiro e jogador, verifica se esse jogador venceu o jogo.
def verificar_vencedor(tabuleiro, jogador):
    # Verificar linhas
    for linha in tabuleiro:
        if all([posicao == jogador for posicao in linha]):
            return True

    # Verificar colunas
    for coluna in range(3):
        if all([tabuleiro[linha][coluna] == jogador for linha in range(3)]):
            return True

    # Verificar diagonais
    if all([tabuleiro[i][i] == jogador for i in range(3)]) or \
       all([tabuleiro[i][2 - i] == jogador for i in range(3)]):
        return True

    return False

# Função que, dado um tabuleiro, verifica se o jogo terminou em empate.
def verificar_empate(tabuleiro):
    for linha in tabuleiro:
        if any([posicao.isdigit() for posicao in linha]):
            return False
    return True

# Função principal que implementa o jogo da velha.
def jogo_da_velha():
    tabuleiro = [
        ["1", "2", "3"],
        ["4", "5", "6"],
        ["7", "8", "9"]
    ]
    jogador_atual = "X"

    while True:
        exibir_tabuleiro(tabuleiro)

        # Solicitar a jogada do jogador
        try:
            jogada = int(input(f"Jogador {jogador_atual}, escolha uma posição (1-9): ")) - 1
        except ValueError:
            print("Entrada inválida. Por favor, insira um número entre 1 e 9.")
            continue

        # Verificar se a jogada é válida
        if jogada < 0 or jogada > 8:
            print("Posição inválida. Escolha um número entre 1 e 9.")
            continue

        linha = jogada // 3
        coluna = jogada % 3

        if tabuleiro[linha][coluna] in ["X", "O"]:
            print("Posição já ocupada. Escolha outra posição.")
            continue

        # Fazer a jogada
        tabuleiro[linha][coluna] = jogador_atual

        # Verificar se o jogador atual venceu
        if verificar_vencedor(tabuleiro, jogador_atual):
            exibir_tabuleiro(tabuleiro)
            print(f"Parabéns! O jogador {jogador_atual} venceu!")
            break

        # Verificar se o jogo terminou em empate
        if verificar_empate(tabuleiro):
            exibir_tabuleiro(tabuleiro)
            print("O jogo terminou em empate!")
            break

        # Alternar entre os jogadores
        jogador_atual = "O" if jogador_atual == "X" else "X"

# Iniciar o jogo
jogo_da_velha()