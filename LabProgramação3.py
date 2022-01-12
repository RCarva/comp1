#Questão 1
def valorAbsoluto(x):
    """Calcula e retorna o valor absoluto de um número;
    complex -> complex"""
    if x < 0:
        return -1 * x
    else:
        return x

#Questão 2
def delta(a,b,c):
    """Retorna o descriminante de um polinomio de segundo grau;
    float, float, float -> float"""
    return (b**2)-(4*a*c)
def raizes(a, b, c):
    """Calcula e Retorna a quantidade de raízes reais de uma equação de segundo grau;
    float, float, float -> int"""
    if delta(a, b, c) < 0:
        return 0
    elif delta(a, b, c) == 0:
        return 1
    else:
        return 2
#Questão 3
def mensagem(frase,n):
    """Retorna a string inserida(colocar entre '...'), sendo que, essa string vai se repetir (n) vezes;
    str, int -> str"""
    return frase*n
#Questão 4
def data(dia,mes,ano):
    """Retorna a sequência de caracteres, formatadas no padrão usual de datas;
    int, int, int -> str"""
    if dia < 10 and mes >= 10:
        return str('0')+ str(int(dia)) + str('/')+str(int(mes))+str('/')+str(int(ano))
    elif dia >=10 and mes < 10:
        return str(int(dia)) + str('/')+str('0')+str(int(mes))+str('/')+str(int(ano))
    elif dia < 10 and mes < 10:
        return str('0')+ str(int(dia)) + str('/')+str('0')+str(int(mes))+str('/')+str(int(ano))
    else:
        return str(int(dia)) + str('/')+str(int(mes))+str('/')+str(int(ano))
#Questão 5
def numeroMinFuncao(x):
    """Calcula e retorna o número mínimo de casos de teste,
    garantindo que todas as linhas da função sejam executadas;
    float -> float"""
    if x <= 2:
        return x
    elif x > 2 and x <= 3.5:
        return 2
    elif x > 3.5 and x <= 5:
        return 3
    else:
        return pow(x,2) - 10*x + 28
#Questão 6 Letra A
def descontoINSS(salarioBruto):
    """Calcula a taxa de desconto de imposto de INSS,retornando o valor da taxa em Reais;
    float -> float"""
    if salarioBruto <= 2000:
        return salarioBruto*(6/100)
    elif salarioBruto > 2000 and salarioBruto <= 3000:
        return salarioBruto*(8/100)
    else:
        return salarioBruto*(10/100)
#Questão 6 Letra B
def descontoIR(salarioBruto):
    """Calcula a taxa de desconto de Imposto de Renda, retornando o valor da taxa em Reais;
    float -> float"""
    if salarioBruto <= 2500:
        return salarioBruto*(11/100)
    elif salarioBruto > 2500 and salarioBruto <= 5000:
        return salarioBruto*(15/100)
    else:
        return salarioBruto*(22/100)
#Questão 6 Letra B
def salarioLiquido(SalarioBruto):
    """Calcula e retorna o Valor do Salário Líquido;
    float -> float"""
    return SalarioBruto - (descontoINSS(SalarioBruto) + descontoIR(SalarioBruto))
        
def retira_pontuacao(frase):
    """Função que ao receber uma frase(str), retorna essa mesma frase,
    mas sem os caracteres de pontuação, que são substituídos por espeço;
    str -> str"""
    frasef = str.replace(str.replace(str.replace(str.replace(str.replace(frase, ',', ' '), '!',' '),'.',' '), '?', ' '),'-', ' ')
    return frasef
def inv(frase):
    frasef = str.split(frase, ' ')
    retira_pontuacao(frase) = str.join('', frase[::-1])
    return frasef
    
