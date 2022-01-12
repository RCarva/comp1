#Questão 1 Letra A
def funcao(n):
    """Função que ao receber um número, calcula a soma da série até esse número;
    int -> float"""
    somaf = 0
    for i in range(n + 1):
        somaf = somaf + ((-1)**i) / (2*i+1)
    return somaf
def testefuncao():
    return (funcao(5) == 0.7440115440115441,
            funcao(10) == 0.8080789523513985,
            funcao(15) == 0.769788348549357,
            funcao(20) == 0.797296195569399)
#Questão 1 Letra B
#Professor, no meu IDLE essa função, as vezes simplesmente não acontecia nada(não aparecia mensagem de erro e nem um retorno),
#por esse motivo caso no seu idle dê erro pode ser por causa disso, não sei do porque está acontecendo isso,
#estou há horas tentando resolver e nada, simplesmente as vezes funciona, mas as vezes não.
import math
def erroDeSoma():
    """Função que não recebe parâmetro e calcula a soma da série com erro inferior a
    0.01, e retorna uma tupla com a soma da série e o número de termos necessários;
    None -> tuple"""
    i = 0
    while math.fabs(funcao(i) - math.pi/4) > 0.01:
        i = i + 1
    return funcao(i),i
def testaErro():
    return (erroDeSoma() == (0.7953941713587581, 24))
#Questão 2
def buscaContatos(listaContatos,nome):
    """Função que busca os dados de um contato salvo, ao receber uma lista e um nome,
    retorna uma lista de contatos que tem o nome buscado;
    list, str -> list"""
    contatinhos = list()
    for i in range(len(listaContatos)):
        if str.lower(nome) in str.lower(listaContatos[i][0]):
            contatinhos.append(listaContatos[i])
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
