import pygame
from pygame.locals import *
from sys import exit
from random import randint

pygame.init()

largura = 640
altura = 480

x = largura/2
y = altura/2
x1 = randint(40, 600)
y1 = randint(40, 440)
x_c = 3
y_c = 0
velocidade = 3
morto = False

fonte = pygame.font.SysFont('arial', 40, True, False)
pontos = 0

screen = pygame.display.set_mode((largura, altura))
pygame.display.set_caption('refazendo o jogo')

clock = pygame.time.Clock()

lista_cobra = []
comprimento_inicial = 15
def aumenta_cobra(lista_cabeca):
    for XeY in lista_cobra:
        pygame.draw.rect(screen, (0, 200, 0), (XeY[0], XeY[1], 20, 20))
def restart_game():
    global pontos, comprimento_inicial, x, y, lista_cobra, lista_cabeca, x1, y1, morto
    pontos = 0
    comprimento_inicial = 15
    x = int(largura/2)
    y = int(altura/2)
    lista_cobra = []
    lista_cabeca = []
    x1 = randint(40, 600)
    y1 = randint(40, 440)
    morto = False

# Loop principal do jogo
while True:
    clock.tick(60)
    screen.fill((0, 0, 0))
    mensagem = f'pontos: {pontos}'
    texto_formatado = fonte.render(mensagem, True, (255, 255, 255))
    aumenta_cobra(lista_cobra)

    # Lógica de movimento
    x += x_c
    y += y_c

    cobra = pygame.draw.rect(screen, (0, 200, 0), (x, y, 20, 20))
    maca = pygame.draw.rect(screen, (200, 0, 0), (x1, y1, 20, 20))
    canto_superior = pygame.draw.line(screen, (0, 0, 0), (0, 0), (640, 0), 1)
    canto_inferior = pygame.draw.line(screen, (0, 0, 0), (0, 480), (640, 480), 1)
    canto_direito = pygame.draw.line(screen, (0, 0, 0), (640, 0), (640, 480), 1)
    canto_esquerdo = pygame.draw.line(screen, (0, 0, 0), (-1, 0), (-1, 480), 1)

    if cobra.colliderect(canto_superior):
        morto = True
    if cobra.colliderect(canto_inferior):
        morto = True
    if cobra.colliderect(canto_direito):
        morto = True
    if cobra.colliderect(canto_esquerdo):
        morto = True

    # Verificar colisão entre a cobra e a maçã
    if cobra.colliderect(maca):
        x1 = randint(40, 600)
        y1 = randint(40, 440)
        pontos += 1
        comprimento_inicial += 5
        velocidade += 0.1

    # Atualizar a lista de partes da cobra
    lista_cabeca = []
    lista_cabeca.append(x)
    lista_cabeca.append(y)
    lista_cobra.append(lista_cabeca)
    if len(lista_cobra) > comprimento_inicial:
        del lista_cobra[0]
    if lista_cobra.count(lista_cabeca) > 1:
        fonte2 = pygame.font.SysFont('arial', 20, True, False)
        pontuacao = f'{pontos}, pontos'
        mensagem = 'gameover! pressione a tecla R para jogar novamente'
        mensagem1 = 'ou P para sair do jogo'
        texto_formatado = fonte2.render(mensagem, True, (255, 255, 255))
        texto_formatado1 = fonte2.render(mensagem1, True, (255, 255, 255))
        texto_pontos = fonte2.render(pontuacao, True, (255, 255, 255))
        ret_texto = texto_formatado.get_rect()
        ret_texto1 = texto_formatado1.get_rect()
        ret_pontos = texto_pontos.get_rect()
        morto = True
        while morto:
            screen.fill((0, 0, 0))
            for event in pygame.event.get():
                if event.type == QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_p):
                    pygame.quit()
                    exit()
                if event.type == KEYDOWN:
                    if event.key == pygame.K_r:
                        restart_game()

            ret_texto.center = (largura//2, altura//2)
            ret_texto1.center = (largura//2, altura//2 + 40)
            ret_pontos.center = (largura//2, altura//2 - 40)
            screen.blit(texto_formatado, ret_texto)
            screen.blit(texto_formatado1, ret_texto1)
            screen.blit(texto_pontos, ret_pontos)
            pygame.display.update()

    # Detecção de eventos
    for event in pygame.event.get():
        if event.type == QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_p):
            pygame.quit()
            exit()

        if event.type == KEYDOWN:
            if event.key == K_a:
                if x_c == velocidade:
                    pass
                else:
                    x_c = -velocidade
                    y_c = 0
            if event.key == K_d:
                if x_c == -velocidade:
                    pass
                else:
                    x_c = velocidade
                    y_c = 0
            if event.key == K_w:
                if y_c == velocidade:
                    pass
                else:
                    x_c = 0
                    y_c = -velocidade
            if event.key == K_s:
                if y_c == -velocidade:
                    pass
                else:
                    x_c = 0
                    y_c = velocidade

    screen.blit(texto_formatado, (450, 40))
    pygame.display.update()
