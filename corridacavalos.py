import turtle
import random

# Configuração da janela
window = turtle.Screen()
window.title("Corrida de Cavalos")
window.setup(width=800, height=400)

# Lista de cavalos
cavalos = ["Cavalo 1", "Cavalo 2", "Cavalo 3", "Cavalo 4"]

# Dicionário para armazenar a posição de cada cavalo
posicoes = {}

# Configuração dos cavalos
for cavalo in cavalos:
    posicoes[cavalo] = turtle.Turtle()
    posicoes[cavalo].shape("turtle")
    posicoes[cavalo].speed(2)
    posicoes[cavalo].penup()
    posicoes[cavalo].goto(-350, random.randint(-150, 150))

# Configuração do objeto de mensagem
mensagem = turtle.Turtle()
mensagem.hideturtle()
mensagem.penup()
mensagem.goto(0, 0)


# Função para mover um cavalo
def mover_cavalo(cavalo):
    posicoes[cavalo].forward(random.randint(1, 20))


# Função para verificar se um cavalo chegou à linha de chegada
def verificar_vencedor():
    for cavalo in cavalos:
        if posicoes[cavalo].xcor() > 350:
            return cavalo
    return None


# Função para realizar a aposta
def fazer_aposta():
    cavalo_aposta = window.textinput("Apostar", "Escolha o cavalo para apostar (1 a 4):")

    if cavalo_aposta.isdigit() and 1 <= int(cavalo_aposta) <= 4:
        cavalo_aposta = f"Cavalo {cavalo_aposta}"
    else:
        print("Escolha inválida. A aposta foi cancelada.")
        return None, 0

    valor_aposta = window.numinput("Apostar", f"Quanto dinheiro você quer apostar no {cavalo_aposta}?")

    return cavalo_aposta, valor_aposta


# Fazer aposta antes da corrida
cavalo_aposta, valor_aposta = fazer_aposta()
if not cavalo_aposta or not valor_aposta:
    exit()

# Loop principal do jogo
while True:
    for cavalo in cavalos:
        mover_cavalo(cavalo)

    vencedor = verificar_vencedor()
    if vencedor:
        print(f"{vencedor} venceu!")

        mensagem.color("black")
        mensagem.goto(0, 0)
        mensagem.write(f"{vencedor} venceu!", align="center", font=("Verdana", 16, "normal"))

        if cavalo_aposta == vencedor:
            valor_ganho = valor_aposta * 5
            mensagem.color("green")
            mensagem.goto(0, -50)
            mensagem.write(f"Parabéns! Você ganhou {valor_ganho} dinheiro!", align="center",
                           font=("Verdana", 16, "normal"))
        else:
            mensagem.color("red")
            mensagem.goto(0, -50)
            mensagem.write("Você perdeu. Mais sorte da próxima vez.", align="center", font=("Verdana", 16, "normal"))

        break

# Fechar a janela ao clicar
window.exitonclick()
