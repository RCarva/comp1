def coletaDados():
    """Função que guia o usuario a como colocar os dados corretamente"""
    print("Primeiramente, Informe a quantidade de funcionários que deseja procurar")
    linhas = int(input("quantos funcionários serão inseridos ?\n"))
    print("Insira os dados de cada funcionario na seguinte ordem:\nNome\nRegistro\nSetor\nCelular\n")
    matriz=[]
    for i in range(linhas):
        num = []
        print("Informações do funcionario "+str(i+1)+" abaixo:")
        for j in range(4):
            final=input("dados:")
            num.append(final)
        matriz.append(num)
    return matriz
