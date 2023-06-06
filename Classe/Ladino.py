__package__ = "Classe"

class Ladino():
    
    def __init__(self) -> None:
        pass
    
    def AtaqueFurtivo(jogador):
        NomeHabilidade = "Ataque Furtivo"
        descrição = "Um ataque furtivo que causa 1d4 (+ nivel) de dano critico EXTRA(o dano dobra caso o inimigo tenha uma condição negativa)"
        dano = 1
        dAtaque = 4 + jogador.nivel
        custoMana = 4
        passivo = True
        nivel = 1
        
    def Furtividade(jogador):
        NomeHabilidade = "Furtividade"
        descrição = "O jogador se torna invisivel por 1d4 turnos(ou até atacar)\n(Durante a furtividade o jogador tem 50% de chance de desviar de ataques inimigos e ganha + 10% * (seu nivel) de chance de dano critico)"
        dano = 0
        dAtaque = 0
        custoMana = 8
        passivo = True
        nivel = 3
        
    def Veneno(jogador):
        NomeHabilidade = "Veneno"
        descrição = "O jogador envenena o inimigo, causando 5% da vida max de dano por 4 turnos\n(Se o inimigo ja estiver envenenado, o veneno é renovado e dano aumenta em +5%(limite de 15%))"
        dano = 1
        dAtaque = 4
        custoMana = 5
        passivo = False
        nivel = 5
        
    def BombaDeFumaca():
        NomeHabilidade = "Bomba de Fumaça"
        descrição = "O jogador joga uma bomba de fumaça, causando 1d8 de dano e cegando o inimigo por 1d4 turnos"
        dano = 1
        dAtaque = 8
        custoMana = 10
        passivo = False
        nivel = 7
    
    def Assassinar(jogador):
        NomeHabilidade = "Assassinar"
        descrição = "Todo os seus golpes são focados em pontos viteis por conta disso seus ataques agora passao a ter 100% de chance de dano crítico"
        dano = 0
        dAtaque = 0
        custoMana = 0
        passivo = True
        nivel = 9
        jogador.critico = True