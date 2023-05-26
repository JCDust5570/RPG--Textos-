

class Bardo():
    
    def __init__(self) -> None:
        pass
    
    def MelodiaCurativa():
        NomeHabilidade = "Melodia Curativa"
        descrição = "Uma melodia que cura o alvo em 1d4 durante 4 turnos\n(no nivel 5 e a cada nivel impar você pode gastar +2 de mana para aumentar a cura em +1d8)"
        dano = 1
        dAtaque = 4
        custoMana = 2
        passivo = True
        nivel = 1
        
    def MelodiaAssustadora():
        NomeHabilidade = "Melodia Assustadora"
        descrição = "Uma melodia que assusta o inimigo e o faz perder 1d4 de defesa durante 4 turnos\n(no nivel 5 e a cada nivel impar você pode gastar +2 de mana para aumentar a perda de defesa em +1d4)"
        dano = 1 
        dAtaque = 4
        custoMana = 2
        passivo = True
        nivel = 3  
        
    def MelodiaInspiradora():
        NomeHabilidade = "Melodia Inspiradora"
        descrição = "Uma melodia que aumenta o deu ataque em 1d4 durante 4 turnos\n(no nivel 5 e a cada nivel impar você pode gastar +2 de mana para aumentar o ataque em +1d4)"
        dano = 1
        dAtaque = 4
        custoMana = 2
        passivo = True
        nivel = 5    
        
        
    def MelodiaPesada():
        NomeHabilidade = "Melodia Pesada"
        descrição = "Uma melodia que causa 1d6 de dano durante 4 turnos\n(no nivel 5 e a cada nivel impar você pode gastar +2 de mana para aumentar o dano em +1d6)"
        dano = 1
        dAtaque = 4
        custoMana = 2
        passivo = True
        nivel = 7
        
    def GrandiFinali():
        NomeHabilidade = "Grandi Finali"
        descrição = "uma melodia que deixa o inimigo dormindo por 1d4 turnos\n(o inimigo tem direito a um teste de resistencia a cada turno para acordar)"
        dano = 1
        dAtaque = 4
        custoMana = 20
        passivo = True
        nivel = 9