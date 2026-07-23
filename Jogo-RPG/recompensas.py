# Sistema de baú: sorteio ponderado por raridade + frases variadas

import random
import time
from utils import limpa
from cores import VERDE, AMARELO, VERMELHO, ROXO, RESET


frases_moedas = [
    "Você ganhou " + AMARELO + "{moedas}" + RESET + " moedas de ouro!",
    "O baú brilha! Você encontrou " + AMARELO + "{moedas}" + RESET + " moedas de ouro!",
    "Um punhado de moedas reluzentes! +" + AMARELO + "{moedas}" + RESET + " de ouro."
]

frases_pocao = [
    "Você encontrou uma " + VERDE + "poção de cura" + RESET + "!",
    "Um frasco borbulhante estava escondido no baú — " + VERDE + "poção de cura" + RESET + " adquirida!",
    "Cheiro de ervas medicinais... você ganhou uma " + VERDE + "poção" + RESET + "!"
]

frases_vida = [
    "Uma energia reconfortante te envolve! Você recuperou " + VERDE + "{valor}" + RESET + " de HP.",
    "O baú emana uma luz curativa — HP restaurado em " + VERDE + "{valor}" + RESET + "!",
    "Você sente suas forças voltarem! +" + VERDE + "{valor}" + RESET + " de HP."
]

frases_bomba = [
    "Uma " + VERMELHO + "bomba" + RESET + "! Cuidado ao manuseá-la, mas ela é sua agora.",
    "Você encontrou uma " + VERMELHO + "bomba explosiva" + RESET + " escondida no fundo do baú!",
    "Pólvora e pavio... você ganhou uma " + VERMELHO + "bomba" + RESET + "!"
]

frases_espada = [
    "Uma " + ROXO + "espada encantada" + RESET + " reluz dentro do baú! Seu ataque aumentou permanentemente!",
    "Lâmina antiga, mas ainda afiada — " + ROXO + "bônus de ataque" + RESET + " conquistado!",
    "Você sente o poder da lâmina fluir por suas mãos! Ataque +" + ROXO + "{valor}" + RESET + "."
]

frases_escudo = [
    "Um " + ROXO + "escudo antigo" + RESET + ", resistente ao tempo! Sua defesa aumentou permanentemente!",
    "Placas de metal reforçado — " + ROXO + "bônus de defesa" + RESET + " conquistado!",
    "Você se sente mais protegido ao empunhar este escudo! Defesa +" + ROXO + "{valor}" + RESET + "."
]

def abrir_bau(player):
    itens_bau = ["moedas", "pocao", "vida", "bomba", "espada", "escudo"]
    pesos_bau = [30, 25, 20, 15, 6, 4]

    item_sorteado = random.choices(itens_bau, weights=pesos_bau, k=1)[0]

    limpa()
    print("Abrindo baú...")
   

    match item_sorteado:
        case "moedas":
            moedas = random.randint(20,50)
            player['ouro'] += moedas
            frase = random.choice(frases_moedas)
            print(frase.format(moedas=moedas))
            time.sleep(2.5)
            return
        case "pocao":
            player["pocoes"] += 1
            frase = random.choice(frases_pocao)
            print(frase)
            time.sleep(2.5)
            return
        case "vida":
            cura = random.randint(20, 35)
            player["hp"] = min(player["hp_max"], player["hp"] + cura)
            frase = random.choice(frases_vida)
            print(frase.format(valor=cura))
            time.sleep(2.5)
            return
        case "bomba":
            player['bomba'] += 1
            frase = random.choice(frases_bomba)
            print(frase)
            time.sleep(2.5)
            
            return
        case "espada":
            bonus_ataque = random.randint(3, 5)
            player["bonus_ataque"] += bonus_ataque
            frase = random.choice(frases_espada)
            print(frase.format(valor=bonus_ataque))
            time.sleep(2.5)
            return
        case "escudo":
            bonus_defesa = random.randint(3, 5)
            player["bonus_defesa"] += bonus_defesa
            frase = random.choice(frases_escudo)
            print(frase.format(valor=bonus_defesa))
            time.sleep(2.5)
            return

    

