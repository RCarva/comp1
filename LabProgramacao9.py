#Questão 1
def multiplicaMatriz(matriz,n):
    """Função que ao receber uma matriz e um número positivo, retorna
    o produto da multiplicação desse número pela matriz;
    list, float -> list"""
    resultado=[]
    for i in range(len(matriz)):
        linha=[]
        for j in range(len(matriz[0])):
            linha.append(matriz[i][j]*n)
        resultado.append(linha)
    return resultado
#Questão 2
def quem_ligou(numero,lista):
    """Função que ao receber um número de telefone e uma lista de contatos,
    retorna as informações de quem ligou;
    int, list -> list"""
    contato = []
    for i in range(len(lista)):
        for j in range(len(lista[0])):
            if numero in lista[i][j]:
                contato.append(lista[i])
    return contato
    
