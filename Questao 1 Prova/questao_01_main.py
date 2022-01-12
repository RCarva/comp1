from questao_01_Servico import ContaSeries
from questao_01_interface import coletaDados
def main():
    """executa, a função de serviço, juntamente com os dados da função de interface"""
    x = coletaDados()
    resultado = ContaSeries(x)
    print(str.format("Existem {} sequencias de faces iguais.",resultado))
main()
