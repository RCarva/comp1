#[DRE]       [Estudantes]
#[120123277] [Pedro Seco Barreto]
#[120123706] [Rafael de Carvalho Henriques do Nascimento]
#[120124493] [Victor de Oliveira Ernesto da Silva]

#Disciplina: Computação I - [CMT 3]
#Laboratório 11 IDLE - Jogo da Velha
#Módulo - Apresentação

def vez_jogador_1(tabuleiro):
    '''Função que retorna a as coordenadas [X,Y] inseridas pelo jogador 1 de entrada: list(list) -> list'''

    conferir_jogador_1 = False

    while conferir_jogador_1 == False:

        print ('\n' + '-='*32)
        jogador_1 = input('[Jogador 1] \n' + 'Escolha uma posição [x,y]: \n')
        jogada_1 = str.split(str.strip(jogador_1,'[]'),',')
        
        if '[' and ',' and ']' in jogador_1 and (len(jogada_1) == 2):
            jogada_1[0] = int(jogada_1[0])
            jogada_1[1] = int(jogada_1[1])
            linha = jogada_1[0]
            coluna = jogada_1[1]
            if(linha >= 0 and coluna >= 0) and (linha <= 3 and coluna <= 3) and (tabuleiro[linha][coluna] == '-'):
                conferir_jogador_1 = True
            else:
                print('\n' + '-='*32)
                print('Posição ocupada! Jogador 1 escolha outra posição [x,y]')
                print('-='*32)
        else:
            print('Comando Inválido')
    
    return jogada_1

def vez_jogador_2(tabuleiro):
    '''Função que retorna a as coordenadas [X,Y] inseridas pelo jogador 2 de entrada: list(list) -> list'''

    conferir_jogador_2 = False

    while conferir_jogador_2 == False:
        print ('\n' + '-='*32)
        jogador_2 = input('[Jogador 2]\n' + 'Escolha uma posição [x,y]: \n')
        jogada_2 = str.split(str.strip(jogador_2,'[]'),',')
        
        if '[' and ',' and ']' in jogador_2 and (len(jogada_2) == 2):
            jogada_2[0] = int(jogada_2[0])
            jogada_2[1] = int(jogada_2[1])
            linha = jogada_2[0]
            coluna = jogada_2[1]
            if(linha >= 0 and coluna >= 0) and (linha <= 3 and coluna <= 3) and (tabuleiro[linha][coluna] == '-'):
                conferir_jogador_2 = True
            else:
                print('\n' + '-='*32)
                print('Posição ocupada! Jogador 2 escolha outra posição [x,y]')
                print('-='*32)
        else:   
            print('Comando Inexistente')
    
    return jogada_2

def jogar_novamente():   
    '''Função que reinicia o jogo da velha dependendo do usuário de entrada: none -> none'''
   
    print ('\n' + '-='*32)
    nova_partida = input("Deseja iniciar uma nova partida (S/N)? \n")
    if nova_partida == "S":
        print("-="*32)
        print("Partida reiniciada!")
        print("-="*32 + "\n")
        return "S"
    elif nova_partida == "N":
        print("X="*32)
        print("Jogo encerrado!")
        print("X="*32 + "\n")
        return "N"
    else:
        print("\n" + "!="*32)
        print("Comando inválido! Tente novamente!")
        print("!="*32)
        return jogar_novamente()
