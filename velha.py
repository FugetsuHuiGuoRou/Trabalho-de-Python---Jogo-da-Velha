
#Primeiro,  criei ma lista para representar o tabuleiro do jogo.
tabuleiro = [" ", " ", " ", " ", " ", " ", " ", " ", " "]


# Segundo, defini uma função para exibir o tabuleiro do jogo. 
# Essa função irá imprimir o estado atual do tabuleiro na tela, 
# mostrando as posições ocupadas pelos jogadores e as posições vazias.

#Quando você chamar a função feche com () para deixar claro que é uma função, e não uma variável.
# Dois pontos : serve para indicar o início do bloco de código que pertence à função.

def exibir_tabuleiro():
    print("┌───┬───┬───┐")
    print(f"│ {tabuleiro[0]} │ {tabuleiro[1]} │ {tabuleiro[2]} │") 
    print("├───┼───┼───┤")
    print(f"│ {tabuleiro[3]} │ {tabuleiro[4]} │ {tabuleiro[5]} │")
    print("├───┼───┼───┤")
    print(f"│ {tabuleiro[6]} │ {tabuleiro[7]} │ {tabuleiro[8]} │")
    print("└───┴───┴───┘")
    #Tudo o que está entre chaves {} é uma expressão que será avaliada e seu resultado será convertido em string e inserido no lugar das chaves.



jogador_atual = "X"

while True:
    exibir_tabuleiro()  # Chama sua função para mostrar o jogo
    print(f"Vez do jogador: {jogador_atual}")
    
    # Recebe a jogada do usuário
    jogada = int(input("Escolha uma posição (1-9)"))  
    
    # Diminui 1 da jogada para ajustar ao índice da lista (0-8) Pro jogador não precisar digitar 0.
    tabuleiro[jogada - 1] = jogador_atual




