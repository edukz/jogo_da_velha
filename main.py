import random

# Tabuleiro 3x3
tabuleiro = [[' ' for _ in range(3)] for _ in range(3)]
historico_jogadas = []

def exibe_tabuleiro():
    print("\n" * 50)
    for linha in tabuleiro:
        for _ in range(3):
            print('|'.join([' ' * 3 + celula + ' ' * 3 for celula in linha]))
        if linha != tabuleiro[-1]:
            print('-' * 33)

def verifica_vencedor(simbolo):
    for i in range(3):
        if all(tabuleiro[i][j] == simbolo for j in range(3)) or \
           all(tabuleiro[j][i] == simbolo for j in range(3)):
           return True
    
    if all(tabuleiro[i][i] == simbolo for i in range(3)) or \
       all(tabuleiro[i][2 - i] == simbolo for i in range(3)):
       return True

    return False

def melhor_movimento():
    for i in range(3):
        for j in range(3):
            if tabuleiro[i][j] == ' ':
                tabuleiro[i][j] = 'O'
                if verifica_vencedor('O'):
                    return (i, j)
                tabuleiro[i][j] = ' '

    for i in range(3):
        for j in range(3):
            if tabuleiro[i][j] == ' ':
                tabuleiro[i][j] = 'X'
                if verifica_vencedor('X'):
                    tabuleiro[i][j] = 'O'
                    return (i, j)
                tabuleiro[i][j] = ' '

    while True:
        i, j = random.randint(0, 2), random.randint(0, 2)
        if tabuleiro[i][j] == ' ':
            return (i, j)

def salvar_historico():
    nome_arquivo = "historico_jogadas.txt"
    with open(nome_arquivo, 'a') as f:
        for jogada in historico_jogadas:
            f.write(f"{jogada[0]} jogou na posição {jogada[1]}, {jogada[2]}\n")
    print(f"Histórico adicionado ao arquivo {nome_arquivo}!")

def jogo():
    simbolo_jogador = ''
    while simbolo_jogador not in ['X', 'O']:
        simbolo_jogador = input("Você deseja ser 'X' ou 'O'? ").upper()
    turno = 'X'

    while True:
        exibe_tabuleiro()
        if turno == simbolo_jogador:
            while True:
                x, y = map(int, input("Digite sua jogada (linha, coluna): ").split(','))
                if 0 <= x < 3 and 0 <= y < 3 and tabuleiro[x][y] == ' ':
                    break
                else:
                    print("Coordenada inválida. Por favor, tente novamente.")
            tabuleiro[x][y] = simbolo_jogador
            historico_jogadas.append((turno, x, y))
        else:
            x, y = melhor_movimento()
            tabuleiro[x][y] = 'O' if simbolo_jogador == 'X' else 'X'
            historico_jogadas.append(('O' if simbolo_jogador == 'X' else 'X', x, y))

        if verifica_vencedor(turno):
            exibe_tabuleiro()
            print(f"{turno} venceu!")
            break

        if all(celula != ' ' for linha in tabuleiro for celula in linha):
            exibe_tabuleiro()
            print("Empate!")
            break

        turno = 'O' if turno == 'X' else 'X'

    if input("Deseja salvar o histórico desta partida? (s/n) ").lower() == 's':
        salvar_historico()

if __name__ == "__main__":
    jogo()
