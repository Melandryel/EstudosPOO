#Definição de classe
class Gafanhoto:
    def __init__ (self, nome, idade): #Método construtor
        #Atributos de instância
        self.nome = nome
        self.idade = idade

    #Métodos de instância
    def aniversario (self):
        self.idade += 1

    def mensagem (self):
        return f"{self.nome} é Gafanhoto(a) e tem {self.idade} anos de idade."

#Declaração de objetos

g1 = Gafanhoto("jose", 22)


g2 = Gafanhoto('Nilton', 27)


g1.aniversario()
print(g1.mensagem(), g2.mensagem())