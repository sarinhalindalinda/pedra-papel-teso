import random

def jogar():
    opcoes = ["pedra", "papel", "tesoura"]
    vitoria_jogador = 0
    vitoria_computador = 0
    empates = 0

    while True:
        escolha_jogador = input("Escolha pedra, papel ou tesoura: ").lower()
        escolha_computador = random.choice(opcoes)

        print(f"Você escolheu {escolha_jogador}, o computador escolheu {escolha_computador}.")

        if escolha_jogador == escolha_computador:
            print("Empate!")
            empates += 1
        elif (escolha_jogador == "pedra" and escolha_computador == "tesoura") or \
             (escolha_jogador == "papel" and escolha_computador == "pedra") or \
             (escolha_jogador == "tesoura" and escolha_computador == "papel"):
            print("Você venceu!")
            vitoria_jogador += 1
        else:
            print("Você perdeu!")
            vitoria_computador += 1

        print(f"Vitórias: {vitoria_jogador} | Derrotas: {vitoria_computador} | Empates: {empates}")

        continuar = input("Deseja continuar? (s/n): ").lower()
        if continuar != 's':
            break

if _name_ := "_main_":
    jogar()