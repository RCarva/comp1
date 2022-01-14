
class UFRJ:
    def __init__(self, nome, dre, matricula="Ativa"):
        """Cria objetos da calsse UFRJ com os atributos nome, dre e matricula"""
        self.nome = nome
        self.dre = dre
        self.matricula = matricula
    
    def setmatricula(self, matricula):
        
        if self.matricula == matricula:
            print("A matricula ja esta " + matricula)
        else:
            self.matricula = matricula
            print("Matricula atualizada para " + matricula)
    
    def __str__(self):
        print("{}\t{}\tmatricula {}".format(self.nome, str(self.dre), self.matricula))



class Materia:
    def __init__(self, nome, vagas=0):
        self.nome = nome
        self.vagas = vagas
        self.alunos = []
    
    def InscreverAluno(self, aluno):
        if len(self.alunos) < self.vagas and aluno not in self.alunos:
            self.alunos.append(aluno)
        elif aluno in self.alunos:
            print("O aluno ja esta inscrito!")
        else:
            print("Vagas insuficientes!")
    
    def ConsultarVagas(self):
        print("Vagas Totais: {} Vagas Livres {}".format(self.vagas, self.vagas - len(self.alunos)))
    
    def __str__(self):
        if len(self.alunos) <= 0:
            print("A Disciplina {} ".format(self.nome, self.vagas))
            print("Vagas Totais: {} Vagas Livres {}".format(self.vagas, self.vagas - len(self.alunos)))
        else:
            print("Alunos inscritos em {}:\n".format(self.nome))

            for i in range (len(self.alunos)):
                print("Nome: {}, DRE: {}, Matricula: {}".format(self.alunos[i].nome, self.alunos[i].dre, self.alunos[i].matricula)) 
                                                
                                            
            print("Vagas Totais: {} Vagas Livres {}".format(self.vagas, self.vagas - len(self.alunos)))


    
mab = Materia("COMP1",10)
carva = UFRJ("rafael", 12346)
lc = UFRJ("Luccas", 12478,"trancada")
mab.InscreverAluno(lc)
mab.InscreverAluno(carva)
mab.__str__()