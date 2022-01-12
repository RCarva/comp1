import questao_02_servico
from questao_02_interface import coletaDados
def main():
    """Função que executa a interface e a função de serviços juntas;
    None -> Tuple"""
    lista = coletaDados()
    if lista[0] == 1:
        print("A área do Trapézio é:")
        print(questao_02_servico.areaTrapezio(lista[1],lista[2],lista[3]))
    if lista[0] == 2:
        print("O quadrado de A, B e C é:")
        print(questao_02_servico.quadrado(lista[1],lista[2],lista[3]))
    if lista[0] == 3:
        print("A média aritmética dos elementos é:")
        print(questao_02_servico.mediaAritmetica(lista[1],lista[2],lista[3]))
    if lista[0] == 4:
        print("A soma dos inteiros, de A até B, pulando de C em C é:")
        print(questao_02_servico.SomaInteiros(lista[1],lista[2],lista[3]))
    if lista[0] not in [1,2,3,4]:
        print("número inválido!")
main()
