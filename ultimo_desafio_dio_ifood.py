# -*- coding: utf-8 -*-
"""Ultimo_Desafio_DIO_Ifood.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1ZX0eXV7hfJfA7YCjHPdVCaBtO1scbb3n
"""

class Heroi:
    def __init__(self, nome, idade, tipo):
        self.nome = nome
        self.idade = idade
        self.tipo = tipo

    def atacar(self):
        ataque = ""
        if self.tipo == 'mago':
            ataque = 'usou magia'
        elif self.tipo == 'guerreiro':
            ataque = 'usou espada'
        elif self.tipo == 'monge':
            ataque = 'usou artes marciais'
        elif self.tipo == 'ninja':
            ataque = 'usou shuriken'

        print(f"O {self.tipo} atacou usando {ataque}")

# Criando uma lista de heróis
herois = [
    Heroi('Herói Mago', 30, 'mago'),
    Heroi('Herói Guerreiro', 25, 'guerreiro'),
    Heroi('Herói Monge', 35, 'monge'),
    Heroi('Herói Ninja', 28, 'ninja')
]

def mostrar_menu():
    print("\nMENU:")
    print("1: Escolher guerreiro para atacar")
    print("2: Sair do jogo")

def agradecer_por_jogar():
    print("\nObrigado por jogar!")

# Loop principal do jogo
while True:
    mostrar_menu()
    escolha = input("Escolha uma opção: ")

    if escolha == '1':
        print("Escolha o guerreiro para atacar:")
        for i, heroi in enumerate(herois):
            print(f"{i + 1}: {heroi.nome}")

        try:
            escolha_guerreiro = int(input("Digite o número do guerreiro para atacar (ou '0' para voltar ao menu): ")) - 1

            if escolha_guerreiro == -1:
                continue
            elif 0 <= escolha_guerreiro < len(herois):
                heroi_escolhido = herois[escolha_guerreiro]
                heroi_escolhido.atacar()
            else:
                print("Escolha inválida. Tente novamente.")
        except ValueError:
            print("Por favor, insira um número válido.")

    elif escolha == '2':
        agradecer_por_jogar()
        break

    else:
        print("Opção inválida. Tente novamente.")