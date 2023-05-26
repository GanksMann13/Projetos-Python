import random
import time

opcoes_jogo = ["Pedra", "Papel", "Tesoura"]

def menu():
    print("Bem-vindo ao jankenpo!")
    
    while True:
        deseja_continuar = input("\nDeseja iniciar uma nova partida (s/n)? ")
        if deseja_continuar != "s":
            break
        jogo(opcoes_jogo)
        print("-" * 35)

    print("Obrigado e volte sempre!!!")


def falar_jankenpo(lista_falas, tempo_espera):
    for i in range(len(lista_falas)):
        print(lista_falas[i], end="")
        time.sleep(tempo_espera)
    
    
def jogo(opcoes):
    mensagem = ""

    for i in range(len(opcoes_jogo)):
        mensagem += str(i + 1) + " - " + opcoes[i] + "\n"

    mensagem += "Escolha uma das opções para jogar: "

    escolha_jogador = opcoes_jogo[int(input(mensagem)) - 1]
    escolha_computador = random.choice(opcoes_jogo)

    print()

    falar_jankenpo(["jan...", "ken...", "pô!"], 1)

    print("\nSua escolha: " + escolha_jogador)
    print("Escolha do computador: " + escolha_computador + "\n")

    regras(escolha_jogador, escolha_computador)
    

def regras(jogador, computador):
    if jogador == "Pedra" and computador == "Pedra" or \
       jogador == "Papel" and computador == "Papel" or \
       jogador == "Tesoura" and computador == "Tesoura":
        print("Essa partida terminou empatada!")

    elif jogador == "Pedra" and computador == "Tesoura" or \
        jogador == "Papel" and computador == "Pedra" or \
        jogador == "Tesoura" and computador == "Papel":
        print("Você ganhou a partida!")

    else:
        print("O computador ganhou a partida!")
    

menu()
