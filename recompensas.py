import random
import time
from utils import limpa
frases_moedas = [
    "Você ganhou {moedas} moedas de ouro!",
    "O baú brilha! Você encontrou {moedas} moedas de ouro!",
    "Um punhado de moedas reluzentes! +{moedas} de ouro."
]

frases_pocao = [
    "Você encontrou uma poção de cura!",
    "Um frasco borbulhante estava escondido no baú — poção de cura adquirida!",
    "Cheiro de ervas medicinais... você ganhou uma poção!"
]

frases_vida = [
    "Uma energia reconfortante te envolve! Você recuperou {valor} de HP.",
    "O baú emana uma luz curativa — HP restaurado em {valor}!",
    "Você sente suas forças voltarem! +{valor} de HP."
]

frases_bomba = [
    "Uma bomba! Cuidado ao manuseá-la, mas ela é sua agora.",
    "Você encontrou uma bomba explosiva escondida no fundo do baú!",
    "Pólvora e pavio... você ganhou uma bomba!"
]

frases_espada = [
    "Uma espada encantada reluz dentro do baú! Seu ataque aumentou permanentemente!",
    "Lâmina antiga, mas ainda afiada — bônus de ataque conquistado!",
    "Você sente o poder da lâmina fluir por suas mãos! Ataque +{valor}."
]

frases_escudo = [
    "Um escudo antigo, resistente ao tempo! Sua defesa aumentou permanentemente!",
    "Placas de metal reforçado — bônus de defesa conquistado!",
    "Você se sente mais protegido ao empunhar este escudo! Defesa +{valor}."
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
            player["hp"] = min(150, player["hp"] + cura)
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

    

