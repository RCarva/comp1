from questao_03_servico import busca
from questao_03_interface import coletaDados
def main():
    """função que guia o usuario a colocar os dados corretamente, e executa a função"""
    x = coletaDados()
    setor = input("Para buscar um funcionário, digite abaixo o setor:\n")
    print(busca(setor,x))
main()
