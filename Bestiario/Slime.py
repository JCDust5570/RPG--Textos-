import random
__package__ = "Bestiario"

class Slime():
    
    def __init__(self) -> None:
        self.vida = 10
        self.vidaMax = 10
        self.mana = 5
        self.manaMax = 5
        self.ataque = 2
        self.defesa = 0
        self.iniciativa = 1
        self.condicao = "Normal"
        self.nivel = 1
        self.exp = 4
        self.moedas = random.randint(0, 3)
        
        print("\nUm Slime apareceu")
        
    def MetodoDeAtaque(self):
        if self.mana > 1 and self.vida < 3:
            print("\nO Slime usou Tiro de Gosma")
            dano = self.TiroDeGosma()
            print("\nO Slime causou", dano, "de dano")
        if self.vida < 3:
            print("\nO Slime usou Regenerar")
            self.Regenerar()
        else:
            print("\nO Slime usou Pancada")
            dano = self.Pancada()
            print("\nO Slime causou", dano, "de dano")
            
    
    def Pancada(self):
        return self.ataque + random.randint(1, 4)
    
    def TiroDeGosma(self):
        self.mana -= 2
        c = random.randint(1, 10)
        if c > 7:
            return self.ataque + random.randint(1, 4) + 2
        else:
            print("\nO Slime causou dando crítico")
            return self.ataque + random.randint(1, 4) + 4
    
    def Regenerar(self):
        v = random.randint(1, 4)
        m = random.randint(1, 2)
        self.vida += v
        print("\nO Slime se regenerou em", v, "de vida")
        if self.vida > self.vidaMax:
            self.vida = self.vidaMax
        self.mana += m
        print("\nO Slime recuperou", m, "de mana")
        if self.mana > self.manaMax:
            self.mana = self.manaMax
        
