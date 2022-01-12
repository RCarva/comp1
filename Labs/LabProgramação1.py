# Questao 1
def mult(x, y):
    """Retorna o produto de X por Y"""
    return x*y
# Questao 2
def areacubo(c):
    """Retorna área de superfície do cubo, c elevado a 2"""
    return 6*c**2
# Questao 3
def areacoroa(R, r):
    """ Calcula formula da coroa circular, retornando sua área(R>r)"""
    return (R**2-r**2)*3.14
# Questao 4
def media(x, y):
    """retorna a média de X e Y"""
    return (x+y)/2
# Questao 5
def funcao(x,a,b,c):
    """retorna a ordenada da função representada por um polinomio de segundo grau"""
    return a*x**2+b*x+c
# Questao 6
def mediaponderada(x1,p1,x2,p2):
    """Calcula a média ponderada, onde x1 é a nota 1 e p1 o peso 1, x2 nota 2 e p2 peso2 """
    return (x1*p1+x2*p2)/(p1+p2)
# Questao 7
def pg(q,n):
    """retorna o erro entre um PG infinita a partir de 1.0 e
    a soma dos n primeiros numeros"""
    return (1/(1 -q)) - (1*(q**n-1)/ q - 1)
# Questao 8
def gorjeta10porcento(total_conta):
    """Retorna 10% do valor total da conta, o valor de entrada"""
    return total_conta*0.1
# Questao 9
def gorjetaGarcom(valor_conta,porcentagem):
    """Retorna a gorjeta do garçom,sendo que a porcentagem deve ser informada em
    número decimal, como 0.1 pra 10%, 0.12 para 12%..."""
    return valor_conta*porcentagem
# Questao 10
def juros(saldo_inicial, juros, meses):
    """Retorna o saldo final, com juros(colocar a taxa, como 10 = 10% de juros),
    de acordo com os meses"""
    return saldo_inicial*(1+(juros/100)*meses)
# Questao 11
def correnteza(vel_correnteza,vel_barco, largura_rio):
    """Calcula a distância em que a correnteza arrasta um barco na travessia de um rio"""
    return vel_correnteza*(largura_rio/vel_barco)

