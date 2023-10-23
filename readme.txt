O script implementa uma versão do clássico jogo da velha, onde o usuário pode jogar contra uma inteligência artificial (IA) simples. A IA é projetada para fazer o melhor movimento possível, bloqueando o jogador ou tentando vencer.

Além disso, o jogo possui um recurso de histórico que salva todas as jogadas feitas durante a partida em um arquivo. (Este recurso pode ser útil para análises posteriores)

Funcionalidades do jogo:

1. Exibição do Tabuleiro
A cada turno, o tabuleiro é exibido para o jogador, mostrando as posições de 'X', 'O' e espaços vazios.

2. Escolha qual lado deseja jogar
No início da partida, o jogador pode escolher entre jogar como 'X' ou 'O'.

3. Jogada do Usuário
O jogador é solicitado a fornecer coordenadas (linha, coluna) para sua jogada. O jogo verifica se a entrada é válida (dentro do tabuleiro e em uma célula vazia).

4. Jogada da IA
A IA verifica o tabuleiro para encontrar o melhor movimento. Ela primeiro procura por movimentos que permitiriam a ela vencer na próxima jogada. Se não houver, ela verifica se precisa bloquear o jogador de vencer na próxima jogada. Se nenhum desses cenários estiver presente, a IA faz uma jogada aleatória.

5. Verificação de Vitória ou Empate
Após cada jogada, o jogo verifica se há um vencedor ou se todas as células do tabuleiro estão ocupadas, resultando em um empate.

6. Histórico de Jogadas
Todas as jogadas são registradas em uma lista durante o jogo. Ao final da partida, o jogador pode escolher salvar esse histórico em um arquivo de texto.

Estrutura do Código

Funções:
exibe_tabuleiro(): Exibe o tabuleiro atualizado.

verifica_vencedor(simbolo): Verifica se o símbolo fornecido ('X' ou 'O') venceu.

melhor_movimento(): Determina o melhor movimento para a IA.

salvar_historico(): Salva o histórico das jogadas em um arquivo.

jogo(): Função principal que coordena o fluxo do jogo.

Variáveis:
tabuleiro: Representa o tabuleiro 3x3 do jogo.

historico_jogadas: Lista que mantém o registro de todas as jogadas.

COMO JOGAR?
Execute o script.
Escolha o símbolo com o qual deseja jogar ('X' ou 'O').
Siga as instruções na tela para fazer suas jogadas.
Ao final da partida, você pode optar por salvar o histórico de jogadas.