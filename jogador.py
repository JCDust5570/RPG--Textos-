from enum import *
from status import *

class Jogador():
    
    def Atributos(self, const, forca, destreza, intel):
        self.const = const
        self.forca = forca
        self.destreza = destreza
        self.intel = intel
    
            
    def Status(self,nome, classe, vida, mana, ataque, defesa, iniciativa):
        self.nome = nome
        self.classe = classe
        self.vida = vida
        self.vidaMax = vida        
        self.mana = mana
        self.manaMax = mana
        self.ataque = ataque
        self.defesa = defesa
        self.iniciativa = iniciativa
        self.nivel = 1
        self.exp = 0
        self.expMax = self.nivel * 10
        self.vivo = True
        self.critico = False  
        self.condicao = "Normal"
        
    def __init__(self):
        nome = input("Digite o nome do personagem: ")
        total = 0
        
        print("Aqui usaremos um sisteminha de atributos aonde você usará pontos para personalizar seu personagem")
        print("lembrabdo que os atributos são os seguintes: Constituição, Força, Destreza e Inteligencia, a forma de distribuição é a seguinte:")
        print("Vida = 5 + Constituição")
        print("Mana = 5 + Inteligencia")
        print("Ataque = 1 + Força")
        print("Defesa = 1 + (Destreza + Constituição)/2")
        print("Iniciativa = 1 + Destreza")
        
        while total != 10:
            print("\nVocê tem 10 pontos para distribuir entre os atributos")
            print("Digite a quantidade de pontos que deseja colocar em cada atributo")
            print("Constituição: ")
            const = int(input())
            print("Força: ")
            forca = int(input())
            print("Destreza: ")
            destreza = int(input())
            print("Inteligencia: ")
            intel = int(input())
            total = const + forca + destreza + intel
        
        
        print("Escolha a classe do personagem: ")
        print("1 - Mago +3 de Inteligencia / -1 de Constituição")
        print("2 - Guerreiro +2 de Força / +1 Constitução / -1 de Inteligencia")
        print("3 - Ladino +2 de Destreza / +1 de Inteligencia / -1 de Constituição")
        print("4 - Paladino +1 de Força / +1 de Inteligência +1 de Constituição / -1 de Destreza")
        print("5 - Bardo +2 de Inteligência / +1 de Destreza / -1 de Força")
        print("6 - Druida +2 de Constituição / +1 de Inteligência / -1 de Força")
        classe = input("Digite a classe do personagem: ")
        
        print("Personagem criado com sucesso!")
        classe  = self.ClasseConfig(classe, const, forca, destreza, intel)  
        defesa = 1 + (destreza + const)/2
        defesa = int(defesa)
        
        self.Atributos(const, forca, destreza, intel)           
        self.Status(nome, classe, 5 + const, 5 + intel, 1 + forca, defesa, 1 + destreza)
        self.StatusView()
        
        
        
        
        
        
        
    def StatusView(self):
        print("Nome: ", self.nome)
        print("Classe: ", self.classe)
        print("Vida: ", self.vida)
        print("Mana: ", self.mana)
        print("Ataque: ", self.ataque)
        print("Defesa: ", self.defesa)
        print("Iniciativa: ", self.iniciativa)
        print("Condicao: ", self.condicao)
        print("Nivel: ", self.nivel)
        print("Experiencia: ", self.exp, "/", self.expMax)
    
    def ClasseConfig(self, classe, const, forca, destreza, intel):
        if classe == 1:
            const = const - 1
            intel = intel + 3
            classe = "Mago"
        elif classe == 2:
            forca = forca + 2
            const = const + 1
            intel = intel - 1
            classe = "Guerreiro"
        elif classe == 3:
            destreza = destreza + 2
            intel = intel + 1
            const = const - 1
            classe = "Ladino"
        elif classe == 4:
            forca = forca + 1
            intel = intel + 1
            const = const + 1
            destreza = destreza - 1
            classe = "Paladino"
        elif classe == 5:
            intel = intel + 2
            destreza = destreza + 1
            forca = forca - 1
            classe = "Bardo"
        elif classe == 6:
            const = const + 2
            intel = intel + 1
            forca = forca - 1
            classe = "Druida"
        return classe
    
    def SubiuDeNivel(self):
        if self.exp >= self.expMax:
            if self.exp > self.expMax:
                self.exp = self.exp - self.expMax
            else:
                self.exp = 0
            
            self.nivel = self.nivel + 1
            self.expMax = self.nivel * 10
            self.vidaMax += self.const
            self.vida = self.const
            self.ataque += self.forca
            defesa = (self.destreza + self.const)/2
            self.defesa = int(defesa)
            self.iniciativa += self.destreza
            self.manaMax += self.intel
            self.mana += self.intel
    
    
      