def busca(setor,matriz):
    """Essa funcao recebe uma matriz e faz uma busca por setor, ou seja,
    dado um nome de um setor da empresa, a funcao retorna os dados de todos os funcionarios daquele setor; str, list-> list"""
    listaf=[]
    for i in range(len(matriz)):
        if setor==matriz[i][2]:
            listaf.append(matriz[i][:2]+matriz[i][3:])
    if listaf==[]:
        return "Nenhum registro encontrado!"
    return listaf
