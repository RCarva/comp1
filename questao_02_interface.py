def coletaDados():
    """Função que recebe todos os códigos i, sendo que quando i = 1 é calculado a área do trapezio,
    i = 2 calcula o quadrado de cada numero, i = 3 calcula a média aritmética dos números,
    e quando i = 4 calcula a soma dos inteiros de A até B, pulando de C em C;
    None -> None"""
    i = int(input("Defina qual codigo(i) será utilizado:\nsendo que quando i = 1 é calculado a área do trapezio,i = 2 calcula \no quadrado de cada numero, i = 3 calcula a média aritmética dos números,\ne quando i = 4 calcula a soma dos inteiros de A até B, pulando de C em C.\n"))
    print("Defina os 3 valores inteiros positivos, sendo o primeiro menor que o segundo")
    a = int(input("Defina o primeiro valor:\n"))
    b = int(input("Defina o segundo valor:\n"))
    c = int(input("Defina o terceiro valor:\n"))
    lista=[]
    lista.append(i)
    lista.append(a)
    lista.append(b)
    lista.append(c)
    return lista
    
