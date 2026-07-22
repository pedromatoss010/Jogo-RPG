# Função utilitária de limpar o terminal (multiplataforma)
import os

def limpa():
    os.system('cls' if os.name == 'nt' else 'clear')


