__package__ = "Classe"

class Mago():
    def __init__(self) -> None:
        pass
        
        
    def RaioArcano(self):
        NomeHabilidade = "Raio Arcano"
        descrição = "Um raio de energia arcano sai de suas mãos e atinge o inimigo\n(para cada 3 de mana gasta, o dano aumenta em 1d4)"
        dano = 1
        dAtaque = 8
        custoMana = 1
        passivo = False
        nivel = 1
        
    def ArmaduraArcana(self):
        NomeHabilidade = "Armadura Arcana"
        descrição = "Uma armadura de energia arcano cobre seu corpo\n(Para cada 3 de mana gasta, a armadura aumenta em 1d4 por 3 turnos)"
        dano = 1
        dAtaque = 4
        custoMana = 3
        passivo = True
        nivel = 3
        
    def BolaDeFogo(self):
        NomeHabilidade = "Bola de Fogo"
        descrição = "Uma bola de fogo sai de suas mãos e atinge o inimigo\n(20% de chance de queimar o inimigo, causando 5% de dano por 3 turnos)"
        dano = 2
        dAtaque = 10
        custoMana = 6
        passivo = False
        nivel = 5
    
    def Meteoro(self):
        NomeHabilidade = "Meteoro"
        descrição = "Um meteoro cai do céu e atinge o inimigo\n(Causa 3d12 de dano e 20% de chancde de queimar o inimigo, causando 5% de dano por 3 turnos)"
        dano = 3
        dAtaque = 12
        custoMana = 25
        passivo = False
        nivel = 7
    
    def TempestadeDeRaios(self):
        NomeHabilidade = "Tempestade de Raios"
        descrição = "Uma tempestade de raios cai do céu e atinge o inimigo\n(Causa 2d20 de dano e 35% de chance de paralizar o inimigo por 2 turnos)"
        dano = 2
        dAtaque = 20
        custoMana = 20
        passivo = False
        nivel = 9

    
    
        