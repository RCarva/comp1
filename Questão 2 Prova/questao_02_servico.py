def areaTrapezio(a,b,c):
    """Função que ao receber 3 números inteiros positivos, retorna a área do trapézio,
    sendo A < B e esses são as bases e C a altura;
    int, int, int -> tuple"""
    return ((a+b)*c)/2,["valores lidos ->",a,b,c] 
def quadrado(a,b,c):
    """Função que calcula o quadrado de A, B e C;
    int, int, int -> tuple"""
    return a**2,b**2,c**2,["valores lidos ->", a,b,c]
def mediaAritmetica(a,b,c):
    """"Calcula a média aritmetica dos valores a,b,c;
    int, int, int -> tuple"""
    return (a+b+c)/3, ["Valores lidos ->",a,b,c]
def SomaInteiros(a,b,c):
    """Função que ao receber 3 números inteiros positivos, sendo A < B, retorna a soma dos números
     que estão entre A e B, pulando de C em C;
     int, int, int -> tuple"""
    int = range(a,b,c)
    somaFinal = sum(int)
    return somaFinal+b, ["valores lidos ->", a,b,c]
