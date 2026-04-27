# 1. Tabuleiro inicial
tabuleiro = [" ", " ", " ", " ", " ", " ", " ", " ", " "]

def exibir_tabuleiro(jogada = None):
    print("┌───┬───┬───┐")
    print(f"│ {tabuleiro[0]} │ {tabuleiro[1]} │ {tabuleiro[2]} │") 
    print("├───┼───┼───┤")
    print(f"│ {tabuleiro[3]} │ {tabuleiro[4]} │ {tabuleiro[5]} │")
    print("├───┼───┼───┤")
    print(f"│ {tabuleiro[6]} │ {tabuleiro[7]} │ {tabuleiro[8]} │")
    print("└───┴───┴───┘")
    if jogada: 
        print(f"Última jogada na posição: {jogada}")

input("Bem-vindo ao Jogo da Velha, aperte Enter para começar!")

jogador_atual = "X"


while True:
    exibir_tabuleiro()   
    
    escolha = int(input(f"Jogador {jogador_atual}, escolha uma posição (1-9): ")) -1

    while escolha < 0 or escolha > 8:

         print ("Posição inválida! Tente novamente.")
         escolha = int(input(f"Jogador {jogador_atual}, escolha uma posição (1-9): ")) -1
         
         

    if tabuleiro[escolha] == " ":
        tabuleiro[escolha] = jogador_atual



        # --- VERIFICAÇÃO DE VITÓRIA ---
        # Definimos todas as sequências que ganham o jogo
        vitoria = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8], # Linhas

            [0, 3, 6], [1, 4, 7], [2, 5, 8], # Colunas

            [0, 4, 8], [2, 4, 6]             # Diagonais
        ]


#---------------------------------------------------
        
        venceu = False
        for v in vitoria:
            # Se as 3 posições da sequência forem iguais ao jogador atual
            if tabuleiro[v[0]] == tabuleiro[v[1]] == tabuleiro[v[2]] == jogador_atual:
                exibir_tabuleiro()
                print(f"PARABÉNS! O Jogador {jogador_atual} venceu o jogo!")
                venceu = True
                break
        
        if venceu:
            break # Encerra o While True
            
        # --- VERIFICAÇÃO DE EMPATE ---
        if " " not in tabuleiro:
            exibir_tabuleiro()
            print("DEU VELHA! O jogo empatou.")
            break

#--------------------------------------------------


        # Alterna o jogador
        if jogador_atual == "X":
            jogador_atual = "O"
        else:
            jogador_atual = "X"
    else:
        print("Essa posição já está ocupada! Tente novamente.")
        input("Aperte Enter para continuar...")