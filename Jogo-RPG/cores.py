# Códigos ANSI para colorir o texto no terminal

VERMELHO = "\033[91m"   # dano recebido, HP baixo, Game Over
VERDE = "\033[92m"      # cura, vitória, mensagens positivas
CINZA = "\033[90m" 
BRANCO = "\033[97m"     # texto de destaque neutro, se precisar
AMARELO = "\033[93m"    # ouro, avisos
AZUL = "\033[94m"       # informações neutras, textos de sistema
ROXO = "\033[95m"       # itens raros (espada/escudo do baú), destaque especial
CIANO = "\033[96m"      # dano causado pelo jogador (ataque)
NEGRITO = "\033[1m"     # deixa o texto em negrito (combina com outras cores)
MARROM = "\033[38;2;139;69;19m"  
RESET = "\033[0m"       # sempre usar no final, "desliga" a cor