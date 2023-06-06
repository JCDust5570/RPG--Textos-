__package__ = "Classe"


class Atirador():
    
    def __init__(self) -> None:
        self.balas = 6
        self.critico = False
        self.timerMira = 0
        self.danoCritico = 2
    
    def Recarga(self):
        descricao = "O jogador recarrega sua arma"
        self.balas = 6
        passivo = False
        nivel = 0
        
    
    def Mirar(self):
        Descricao = "O jogador mira no inimigo, aumentando a chance de acerto Crítico no seu proximo ataque"
        self.critico = True
        self.timerMira = 1
        passivo = False
        nivel = 1
        
    
    def TiroRapido(self):
        pass
    
    def TiroCerteiro(self):
        pass
    
    def ChuvaDeBalas(self):
        pass
    
    def MiraPrecisa(self):
        descricao = "O jogador aprende a mirar melhor, agora  o dano critico dele é multiplicado por 3x\ne tem 20% de chance de causar fraqueza"
        
    