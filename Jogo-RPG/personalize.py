from utils import limpa
from player import criar_player
import time

def personalizando_heroi():
    limpa()
    print("=======================================")    
    print("                HERÓI                  ")
    print("=======================================")
    nome = input("Digite o nome do seu herói: ")
    print(f"Bem-vindo, {nome}!")
    time.sleep(2)
    limpa()

    player = criar_player(nome)

    while True:
        limpa()
        print("=======================================") # ESCOLHER SKIN
        print("       PERSONALIZE SEU HERÓI           ")
        print("=======================================\n")
        print('Escolha a skin do seu herói: ')
        print("1. Skin Vovô Casado")
        print("2. Skin Detetive")
        print("3. Skin Caçador") 
        try:
            roupa = int(input("Qual vai escolher? "))
        except ValueError:
            roupa = 0
        if roupa == 1:
            print("PARABÉNS! Sua skin é a do Vovô Casado!") 
            player["skin"] = "Vovô Casado"
            time.sleep(2) 
            break
           
        elif roupa == 2:
            print("PARABÉNS! Sua skin é do Detetive!") 
            player["skin"] = "Detetive"
            time.sleep(2)
            break
        elif roupa == 3:
            print("PARABÉNS! Sua skin é a do Caçador!")        
            player["skin"] = "Caçador"
            time.sleep(2)
            break
        else:
            print("NÃO TEMOS ESSA SKIN, Escolha uma das opções acima!")
            time.sleep(2)
        
    while True:
        limpa()
        print("=======================================") # ESCOLHER ESPADA
        print("        EQUIPAMENTO DE BATALHA         ")
        print("=======================================")
        print("Escolha sua espada: ")
        print("1. Espada de Madeira")
        print("2. Espada de Ferro")
        print("3. Espada de Diamante")
        try:
            espada = int(input("Qual espada você quer? "))
        except ValueError:
            espada = 0
            
        if espada == 1:
            print("BOA ESCOLHA! Espada de Madeira equipada!")
            player["bonus_ataque"] += 2
            time.sleep(2)
            break
            
        elif espada == 2:
            print("ÓTIMA ESCOLHA! Espada de Ferro equipada!")
            player["bonus_ataque"] += 3
            time.sleep(2)
            break
            
        elif espada == 3:
            print("EXCELENTE ESCOLHA! Espada de Diamante!")
            player["bonus_ataque"] += 4
            time.sleep(2)
            break
            
        else:
            print("NÃO TEMOS ESSA ESPADA, Escolha uma das opções acima!")
            time.sleep(2)

    return player
        
