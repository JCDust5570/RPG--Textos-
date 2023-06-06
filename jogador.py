from enum import *
from status import *


class Jogador():
    
    def Atributos(self, const, forca, destreza, intel):
        self.const = const
        self.forca = forca
        self.destreza = destreza
        self.intel = intel
    
            
    def Status(self,nome,vida, mana, ataque, defesa, iniciativa):
        self.nome = nome
        self.classe
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
        nome = input("Digite o nome do personagem: \n")
        total = 0
        
        print("Aqui usaremos um sisteminha de atributos aonde você usará pontos para personalizar seu personagem")
        print("lembrabdo que os atributos são os seguintes: Constituição, Força, Destreza e Inteligencia, a forma de distribuição é a seguinte:")
        print("Vida = 5 + Constituição")
        print("Mana = 5 + Inteligencia")
        print("Ataque = 1 + Força")
        print("Defesa = 1 + Destreza + Constituição/2")
        print("Iniciativa = 1 + Destreza")
        
        fim = False
        total = 0
        
        while fim == False:
            while total != 10:
                print("\nVocê tem 10 pontos para distribuir entre os atributos")
                print("Digite a quantidade de pontos que deseja colocar em cada atributo")
                print("Constituição: ")
                const = int(input())
                
                while const > 10 or const < 0:
                    print("Você não pode colocar mais pontos do que o permitido, digite novamente o valor de Constitução: ")
                    const = int(input())
                total = const
                
                
                print("Força: ")
                forca = int(input())
                while forca + const > 10 or forca < 0:
                    print("Você não pode colocar mais pontos do que o permitido, digite novamente o valor de Força: ")
                    forca = int(input())
                total += forca
                
                
                print("Destreza: ")
                destreza = int(input())
                while destreza + forca + const > 10 or destreza < 0:
                    print("Você não pode colocar mais pontos do que o permitido, digite novamente o valor de Destreza: ")
                    destreza = int(input())
                total += destreza
               
                    
                print("Inteligencia: ")
                intel = int(input())
                while intel + destreza + forca + const > 10 or intel < 0:
                    print("Você não pode colocar mais pontos do que o permitido, digite novamente o valor de Inteligência: ")
                    intel = int(input())
                total += intel
                
            print("Deseja confirmar a distribuição de pontos? (S/N)")
            confirm = input()
            if confirm == "S" or confirm == "s":
                fim = True
            else:
                fim = False
            
        classe = 0
        
        while classe == 0 and classe != 6 and classe !=5 and classe != 4 and classe != 3 and classe != 2 and classe != 1:
            print("Escolha a classe do personagem: ")
            print("1 - Mago +3 de Inteligencia / -1 de Constituição")
            print("2 - Guerreiro +2 de Força / +1 Constitução / -1 de Inteligencia")
            print("3 - Ladino +2 de Destreza / +1 de Inteligencia / -1 de Constituição")
            print("4 - Paladino +1 de Força / +1 de Inteligência +1 de Constituição / -1 de Destreza")
            print("5 - Bardo +2 de Inteligência / +1 de Destreza / -1 de Força")
            print("6 - Atirador +2 em Destreza / +1 em Inteligência / -1 em Constituição")
            classe = input("Digite a classe do personagem: \n")
        
        # Atribuido os valores baseados na classe escolhida
        if classe == "1":
            intel += 3
            const -= 1
            self.classe = "Mago"
        elif classe == "2":
            forca += 2
            const += 1
            intel -= 1
            self.classe = "Guerreiro"
        elif classe == "3":
            destreza += 2
            intel += 1
            const -= 1
            self.classe = "Ladino"
        elif classe == "4":
            forca += 1
            intel += 1
            const += 1
            destreza -= 1
            self.classe = "Paladino"
        elif classe == "5":
            intel += 2
            destreza += 1
            forca -= 1
            self.classe = "Bardo"
        elif classe == "6":
            destreza += 2
            intel += 1
            const -= 1
            self.classe = "Atirador"
        
        defesa = 1 + (destreza + const/2)
        defesa = int(defesa)
        self.Atributos(const, forca, destreza, intel)           
        self.Status(nome, 5 + const, 5 + intel, 1 + forca, defesa, 1 + destreza)
        self.StatusView()
        
        
        
        
        
        
        
    def StatusView(self):
        print("Nome: ", self.nome)
        print("Classe: ", self.classe)
        print("Vida: ", self.vida ,"/", self.vidaMax)
        print("Mana: ", self.mana, "/", self.manaMax)
        print("Ataque: ", self.ataque)
        print("Defesa: ", self.defesa)
        print("Iniciativa: ", self.iniciativa)
        print("Condicao: ", self.condicao)
        print("Nivel: ", self.nivel)
        print("Experiencia: ", self.exp, "/", self.expMax)
    
                
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
    
    
      