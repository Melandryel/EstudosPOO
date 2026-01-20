#Definição de classe
class Gafanhoto:
    def __init__ (self): #Método construtor
        #Atributos de instância
        self.nome = ""
        self.idade = 0

    #Métodos de instância
    def aniversario (self):
        self.idade += 1

    def mensagem (self):
        return f"{self.nome} é Gafanhoto(a) e tem {self.idade} anos de idade."

#Declaração de objetos

g1 = Gafanhoto()
g1.nome = 'José'
g1.idade = 36

g2 = Gafanhoto()
g2.nome = 'Nilton'
g2.idade = 27

g1.aniversario()
print(g1.mensagem(), g2.mensagem())