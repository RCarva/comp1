def zodiaco(ano):
    """Função que ao receber o ano de nascimento de uma pessoa, retorna o signo
    aproximado do indivíduo(zodíaco chinês);
    int -> str"""
    signo = ['Macaco','Galo', 'Cão', 'Porco', 'Rato', 'Boi', 'Tigre',
              'Coelho', 'Dragão', 'Serpente', 'Cavalo', 'Carneiro']
    return signo[ano%12]
