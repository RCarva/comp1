#Questão 1
def SIGA(t1):
    """Função que ao receber uma tupla como parâmetro, retorna outra tupla
    com o nome do aluno, a média e a situação do aluno;
    tupla -> tupla"""
    nome = t1[0]
    n1 = t1[1] 
    n2 = t1[2]
    n3 = t1[3]
    media = round((n1+n2+n3)/3,1)
    if media >= 7:
        return (nome,media,'aprovado', 'Parabéns!')
    elif media < 7 and media >= 5:
        return (nome, media,'aprovado')
    else:
        return (nome,media,'reprovado')
#Questão 2
from math import pi

def quadrante(angulo,graus):
    """Função que dado um ângulo, retorna o quadrante no qual este ângulo
    se encontra;
    float, bool -> int"""
    if graus == False:
        angulo = angulo*180/pi
    angulo = angulo%360
    if angulo <= 90:
        return 1
    elif angulo > 90 and angulo <= 180:
        return 2
    elif angulo > 180 and angulo <= 270:
        return 3
    else:
        return 4
        
        
