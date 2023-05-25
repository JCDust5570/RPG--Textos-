

class Mago(jogador):
    def __init__(self) -> None:
        Passiva = RaioArcano()
        
        
    def RaioArcano(self):
        NomeHabilidade = "Raio Arcano"
        descrição = "Um raio de energia arcano sai de suas mãos e atinge o inimigo\n(para cada 3 de mana gasta, o dano aumenta em 1d4)"
        dano = 1
        dAtaque = 8
        custoMana = 1
        passivo = False
        
    def BolaDeFogo(self):
        NomeHabilidade = "Bola de Fogo"
        descrição = "Uma bola de fogo sai de suas mãos e atinge o inimigo\n(20% de chance de queimar o inimigo, causando 5% de dano por 3 turnos)"
        dano = 2
        dAtaque = 10
        custoMana = 6
        passivo = False
    
    def ArmaduraArcana(self):
        pass
    
    
        