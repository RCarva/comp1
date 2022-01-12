# Questão 1 letra b
def media(a, b, c):
    """Função que calcula e Retorna a média de a, b e c"""
    return (a+b+c)/3
# Questão 1 letra C
def diferencaMedia(a, b ,c):
    """Retorna a subtração do maior numero de entrada pela média
    de todos valores de entrada"""
    return max(a,b,c) - media(a,b,c)
def somaMedia(a,b,c):
    """Retorna a soma do menor número de entrada, pela média
    de todos valores de entrada"""
    return min(a,b,c) + media(a,b,c)
# Questão 2 letra A
def delta(a,b,c):
    """Retorna o descriminante de um polinomio de segundo grau"""
    return (b**2)-(4*a*c)
# Questão 2 letra B
from math import sqrt
def raiz1(a,b,c):
    """Retorna a primeira raiz real de uma equação de segundo grau"""
    return (-b+sqrt(delta(a,b,c)))/(2*a)
# Questão 2 letra C
from math import sqrt
def raiz2(a,b,c):
    """Retorna a segunda raiz real de uma equação de segundo grau"""
    return (-b-sqrt(delta(a,b,c)))/(2*a)
# Questão 3 Letra B
def termoGeral(an,a1,r):
    """Calcula e retorna o numero de termos de uma PA"""
    return (an-(a1+ r*-1))/r
#Questão 3 Letra C
def somaPa(a1,an,r):
    """Calcula e retorna a soma de uma PA"""
    return termogeral(a1,an,r)*(a1+an)/2
#Questão 4 Letra A
from math import sqrt
def hipotenusa(c1,c2):
    """Calcula e retorna a hipotenusa de um triângulo retângulo,dados os catetos"""
    return sqrt(pow(c1,2) + pow(c2, 2))
#Questão 4 Letra B
from math import sqrt
def dist2pontos(xA,yA,xB,yB):
    """Calcula e retorna a distancia entra 2 pontos, sendo eles A e B"""
    return sqrt((pow(xB-xA,2))+ (pow(yB-yA,2)))
#Questão 4 Letra C
def perimetro(c1,c2):
    """calcula e retorna o perimetro de um triangulo, dados os catetos"""
    return hipotenusa(c1,c2) + c1 + c2
#Questão 4 Letra D
def somaSenCos(a1):
    """Calcula e retorna a soma do quadrado do seno e do cosseno,
    sendo a1=angulo em graus"""
    import math
    return pow(math.sin(a1),2) + pow(math.cos(a1),2)
#Questão 4 Letra E
from math import pi
def compCirculo(r):
    """Calcula e retorna o comprimento de uma circunferência"""
    return 2*pi*r
#Questão 5
from math import pi
def setorCirc(r,a1=360):
    """ Calcula e retorna a área do setor circular, a1 -> angulo(em graus)"""
    return a1*pi*r**2/360
#Questão 6
from math import floor
def bombons(x,y):
    """Calcula e Retorna a quantidade de bombons que podem ser compradas,
    dados o valor do bombom(x) e o dinheiro que pode ser gasto(y)"""
    return floor(y/x)
#Questão 7
def imc(altura,peso):
    """Calcula e Retorna o IMC, sendo que
    é preciso colocar a altura em metros e o peso em kilogramas"""
    return peso/pow(altura,2)
#Questão 8
from math import ceil
def carros(x,y=5):
    """Calcula e Retorna o numero de carros que um grupo de pessoas vai precisar
    para viajar levando em conta a legislação brasileira"""
    return ceil(x/y)
#Questão 9
def distanciaAtleta(r,d):
    """Calcula a quantidade de voltas que um atleta deu em uma pista cirular,
    sendo r = raio e d = distancia percorrida"""
    return d/compCirculo(r)
#Questão 10
def receitaBolo(FarinhaTrigo,Ovo,Colheres_de_Leite):
    """Calcula e retorna a quantidade máxima de bolos que podem ser feitos,
    dados os ingredintes"""
    return min(FarinhaTrigo//2,Ovo//3,Colheres_de_Leite//5)

