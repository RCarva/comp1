#[DRE]       [Estudantes]
#[120123277] [Pedro Seco Barreto]
#[120123706] [Rafael de Carvalho Henriques do Nascimento]
#[120124493] [Victor de Oliveira Ernesto da Silva]

#Disciplina: Computação I - [CMT 3]
#Laboratório 11 IDLE - Jogo da Velha
#Módulo - Serviço

from Lab11_apresentacao import vez_jogador_1, vez_jogador_2, jogar_novamente


def jogo_da_velha():
    '''Função que não recebe parâmetro e retorna uma matriz no formato 4x4 de entrada: none -> list(list)'''
    tabuleiro = []
    for i in range(4):
        linha = []
        for j in range(4):
            linha.append('-')
        tabuleiro.append(linha)
    return tabuleiro


def formata_tabuleiro(matriz):
    '''Função que envia o tabuleiro do jogo para jogador, de entrada: list(list) -> print'''
    for i in range(len(matriz)):
        print(matriz[i][0] + " " + matriz[i][1] + " " + matriz[i][2] + " " + matriz[i][3])


def jogador1(jogada, tabuleiro):
    '''Função que recebe a posição escolhida pelo jogador 1, atualizando o tabuleiro com "X" após a jogada, de entrada: list,list(list) -> list(list)'''
    linha = jogada[0]
    coluna = jogada[1]

    tabuleiro[linha][coluna] = 'X'
    return formata_tabuleiro(tabuleiro)


def jogador2(jogada, tabuleiro):
    '''Função que recebe a posição escolhida pelo jogador 2, atualizando o tabuleiro com "O" após a jogada, de entrada: list,list(list) -> list(list)'''
    
    linha = jogada[0]
    coluna = jogada[1]

    tabuleiro[linha][coluna] = 'O'
    return formata_tabuleiro(tabuleiro)


def verifica_vitoria(tabuleiro):
    '''Função que verifica os casos de vitória do jogador, de entrada: list(list)-> Boolean'''
    
    #quadrados
    for i in range(3):
        for j in range(3):
            if ((tabuleiro[i][j]=='X' and tabuleiro[i][j+1]=='X' and tabuleiro[i+1][j]=='X' and tabuleiro[i+1][j+1]=='X') or
                (tabuleiro[i][j]=='O' and tabuleiro[i][j+1]=='O' and tabuleiro[i+1][j]=='O' and tabuleiro[i+1][j+1]=='O')):
                return True
    #linhas
    for i in range(4):
        if ((tabuleiro[i][0] == 'X' and tabuleiro[i][1] == 'X' and tabuleiro[i][2] == 'X' and tabuleiro[i][3] == 'X') or
            (tabuleiro[i][0] == 'O' and tabuleiro[i][1] == 'O' and tabuleiro[i][2] == 'O' and tabuleiro[i][3] == 'O')):
            return True

    #colunas
    for i in range(4):
        if ((tabuleiro[0][i] == 'X' and tabuleiro[1][i] == 'X' and tabuleiro[2][i] == 'X' and tabuleiro[3][i] == 'X') or
            (tabuleiro[0][i] == 'O' and tabuleiro[1][i] == 'O' and tabuleiro[2][i] == 'O' and tabuleiro[3][i] == 'O')):
            return True

    #diagonais
    if ((tabuleiro[0][0] == 'X' and tabuleiro[1][1] == 'X' and tabuleiro[2][2] == 'X' and tabuleiro[3][3] == 'X') or
        (tabuleiro[0][0] == 'O' and tabuleiro[1][1] == 'O' and tabuleiro[2][2] == 'O' and tabuleiro[3][3] == 'O')):
        return True

    if ((tabuleiro[3][0] == 'X' and tabuleiro[2][1] == 'X' and tabuleiro[1][2] == 'X' and tabuleiro[0][3] == 'X') or
        (tabuleiro[3][0] == 'O' and tabuleiro[2][1] == 'O' and tabuleiro[1][2] == 'O' and tabuleiro[0][3] == 'O')):
        return True

def jogo():
    '''Função que executa o jogo e suas regras, de entrada: none -> none'''

    jogador = 1
    rodada = True

    print('[Jogo da Velha 4x4]' + ('-='*22),'\n')
    tabuleiro = jogo_da_velha()
    formata_tabuleiro(tabuleiro)

    while rodada:
        vazio = False
        for i in range(len(tabuleiro)):
            for j in range(len(tabuleiro[i])):
                if '-' in tabuleiro[i][j]:
                    vazio = True
                    if jogador == 1:
                        posicao_1 = vez_jogador_1(tabuleiro)
                        jogador1(posicao_1, tabuleiro)
                        jogador = 2
                    
                        if verifica_vitoria(tabuleiro) == True:
                            print('Jogador 1 venceu o jogo!')
                            limpa_tabuleiro(tabuleiro)
                            return jogar_novamente()
                    else:
                        posicao_2 = vez_jogador_2(tabuleiro)
                        jogador2(posicao_2, tabuleiro)
                        jogador = 1
                        
                        if verifica_vitoria(tabuleiro) == True:
                            print('Jogador 2 venceu o jogo!')
                            limpa_tabuleiro(tabuleiro)
                            return jogar_novamente()                     
        if vazio == False:
            print('Empate')
            limpa_tabuleiro(tabuleiro)
            return jogar_novamente() 

def resetar_jogo():
    '''Função que reseta o jogo dependendo da escolha do jogador, de entrada: none -> none'''

    reiniciar = "S"

    while reiniciar == "S":
        reiniciar = jogo()

def limpa_tabuleiro(tabuleiro):
    '''Função que reseta o tabuleiro para reiniciar o jogo, de entrada: list(list) -> list(list)'''
    for i in range(len(tabuleiro)):
        for j in range(len(tabuleiro[i])):
            tabuleiro[i][j] = '-'
    return tabuleiro

#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
#[Funções de teste]

def testa_jogador1():
    print(jogador1([1,3],[['X','-','-','-'],['X','O','X','-'],['O','O','X','X'],['-','-','-','-']]) == formata_tabuleiro([['X','-','-','-'],['X','O','X','X'],['O','O','X','X'],['-','-','-','-']]))
    
    print(jogador1([2,0],[['-','-','-','-'],['-','-','-','-'],['-','-','-','-'],['-','-','-','-']]) == formata_tabuleiro([['-','-','-','-'],['-','-','-','-'],['X','-','-','-'],['-','-','-','-']]))
    
    print(jogador1([3,2],[['X','O','O','X'],['O','X','O','X'],['X','O','X','O'],['X','O','-','-']]) == formata_tabuleiro([['X','O','O','X'],['O','X','O','X'],['X','O','X','O'],['X','O','X','-']]))


def testa_jogador2():
    print(jogador1([0,3],[['O','O','O','-'],['-','X','-','-'],['-','X','X','-'],['X','-','-','-']]) == formata_tabuleiro([['O','O','O','O'],['-','X','-','-'],['-','X','X','-'],['X','-','-','-']]))
    
    print(jogador1([1,2],[['-','-','-','-'],['-','-','-','-'],['-','-','-','-'],['-','-','-','-']]) == formata_tabuleiro([['-','-','-','-'],['-','-','O','-'],['-','-','-','-'],['-','-','-','-']]))
    
    print(jogador1([1,1],[['O','X','X','O'],['X','-','X','X'],['O','O','X','O'],['X','X','O','X']]) == formata_tabuleiro([['O','X','X','O'],['X','O','X','X'],['O','O','X','O'],['X','X','O','X']]))
    
def testa_verifica_vitoria():
#Algumas situações de vitória
    print(verifica_vitoria([['-','-','-','-'],['-','X','X','-'],['-','X','X','-'],['-','-','-','-']]) == True)
    
    print(verifica_vitoria([['-','-','-','O'],['-','-','-','O'],['-','-','-','O'],['-','-','-','O']]) == True)
    
    print(verifica_vitoria([['X','O','X','O'],['O','X','O','O'],['X','O','O','X'],['O','O','X','O']]) == True)

#Algumas situações de empate
    print(verifica_vitoria([['O','O','X','X'],['O','X','O','O'],['X','O','O','X'],['O','O','X','O']]) != True)
    
    print(verifica_vitoria([['O','O','X','O'],['O','X','X','O'],['X','O','O','X'],['O','O','X','O']]) != True)
    
    print(verifica_vitoria([['O','O','X','O'],['O','X','O','O'],['X','X','O','X'],['O','O','X','O']]) != True)
    
def testa_limpatabuleiro():
    print(limpa_tabuleiro([['X','O','X','O'],['O','X','O','O'],['X','O','O','X'],['O','O','X','O']]) == [['-','-','-','-'],['-','-','-','-'],['-','-','-','-'],['-','-','-','-']])
    
    print(limpa_tabuleiro([['O','O','O','-'],['-','X','-','-'],['-','X','X','-'],['X','-','-','-']]) == [['-','-','-','-'],['-','-','-','-'],['-','-','-','-'],['-','-','-','-']])
   
    print(limpa_tabuleiro([['X','O','O','X'],['O','X','O','X'],['X','O','X','O'],['X','O','-','O']]) == [['-','-','-','-'],['-','-','-','-'],['-','-','-','-'],['-','-','-','-']])
