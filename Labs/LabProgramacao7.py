#Questão 1
import random
def dados():
    """Função que simula um jogo de dois dados, retornando qauntas vezes os dados foram
    jogados até que saiam 2 números repitidos;
    none -> int"""
    dado1 = 1
    dado2 = 2
    contador = 0
    while dado1 != dado2:
        dado1 = random.randint(1,6)
        dado2 = random.randint(1,6)
        contador +=1
    return contador
def testaDados():
    """Retorna o Dado 1 , o Dado 2 e quantas vezes foram jogados para cair
    números iguais."""
    dado1 = 1
    dado2 = 2
    contador = 0
    while dado1 != dado2:
        dado1 = random.randint(1,6)
        dado2 = random.randint(1,6)
        contador +=1
    return dado1,dado2,contador

#Questão 2
def buscaContatos(listaContatos,nome):
    """Função que busca os dados de um contato salvo, ao receber uma lista e um nome,
    retorna uma lista de contatos que tem o nome buscado;
    list, str -> list"""
    contatinhos = list()
    i = 0
    while i < len(listaContatos):
        if str.lower(nome) in str.lower(listaContatos[i][0]):
            contatinhos.append(listaContatos[i])
        i += 1
    return contatinhos
def testaBuscaContatos():
    return (buscaContatos([["Bruno Campos",
            ['2199112233', '2133992211'], 'brunoc91@emailquente.com.br', '@brunocampos91'], ['Julia Fields',
            ['2198145233'], "", '@juju.fields']],"julia") == [['Julia Fields', ['2198145233'], '', '@juju.fields']],
            buscaContatos([["Luan Camargo",
            ['2199112233', '2133992211'], 'luancar@emailquente.com.br', '@camargoluan91'], ['Luan Silva',
            ['2198145233'], "luanss98@gmail.com", '@luanss']],"luan") == [['Luan Camargo', ['2199112233', '2133992211'],
            'luancar@emailquente.com.br', '@camargoluan91'], ['Luan Silva', ['2198145233'], 'luanss98@gmail.com', '@luanss']],
            buscaContatos([["Bruno Campos",
            ['2199112233', '2133992211'], 'brunoc91@emailquente.com.br', '@brunocampos91'], ['Julia Fields',
            ['2198145233'], "", '@juju.fields']],"Leonardo") == [],
            buscaContatos([["Bruno Campos",
            ['2199112233', '2133992211'], 'brunoc91@emailquente.com.br', '@brunocampos91'], ['Julia Fields',
            ['2198145233'], "", '@juju.fields']],"JULIA") == [['Julia Fields', ['2198145233'], '', '@juju.fields']])
    
