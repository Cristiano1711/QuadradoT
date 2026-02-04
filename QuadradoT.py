import turtle as t

## Configurações da Janela
janela = t.Screen()
altura_janela = 900
largura_janela = 900
janela.setup(width= largura_janela, height= altura_janela)
janela.title("Quadrado T")

## Configurações da tartaruga
tartaruga = t.Turtle()
tartaruga.speed(0)
tartaruga.hideturtle()
tartaruga.pensize(1)


def quadrado(turt, tamanho, cor):
    turt.color(cor)
    turt.begin_fill()
    for _ in range(4):
        turt.forward(tamanho)
        turt.left(90)
        
    turt.end_fill()    


def quadradoT(turt ,tamQ, nivel, posX, posY, cor, nvl_max):
    if nivel > nvl_max:
        return
    else:
        
        turt.pu()
        turt.goto(posX - tamQ / 2, posY - tamQ / 2)
        turt.pd()
        quadrado(turt, tamQ, cor)
        novo_tamQ = tamQ / 2

        # Quadrado canto superior esquerdo
        quadradoT(turt, novo_tamQ, nivel + 1, (posX - novo_tamQ), (posY + novo_tamQ), cor, nvl_max)

        # Quadrado canto superior direito
        quadradoT(turt, novo_tamQ, nivel + 1, (posX + novo_tamQ) , (posY + novo_tamQ), cor, nvl_max)

        # Quadrado canto inferior esquerdo
        quadradoT(turt, novo_tamQ, nivel + 1, (posX - novo_tamQ), (posY - novo_tamQ), cor, nvl_max)

        # Quadrado canto inferior direito
        quadradoT(turt, novo_tamQ, nivel + 1, (posX + novo_tamQ), (posY - novo_tamQ), cor, nvl_max)

def main():
    print("Escolha o nivel do fractal, sendo 0 o mais básico: \n")
    nvl_max = int(input())
    print("Escolha a cor do quadrado (em ingles por favor): \n")
    cor = (input())
    quadradoT(tartaruga, 300, 0, 0, 0, cor, nvl_max)
    t.done()

main()
   
