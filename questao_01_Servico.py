def ContaSeries(lista):
    """Função que, ao receber uma lista com uma série de lançamentos de dados,
    retorna o número de ocorrências de séries de faces repitidas
    list -> list"""
    cont = 0
    for i in range(1,len(lista)-2):
        listaFinal = lista[i-1:i+2]
        if listaFinal[0] == listaFinal[1] and listaFinal[1] != listaFinal[2]:
            cont += 1
    if lista[-1] == lista[-2]:
        cont += 1
    return cont
