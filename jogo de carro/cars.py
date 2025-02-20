import pygame
from pygame.locals import *
from sys import exit
from random import randint
import random

pygame.init()

# musica do jogo
pygame.mixer.music.set_volume(0.3)
musica_de_fundo = ['Top Gear Soundtrack - Track 3(MP3_160K).mp3', 'Top-Gear-Soundtrack-Track-1_M4A_128K_.mp3', 'Top-Gear-Soundtrack-Track-4_M4A_128K_.mp3']
musica_escolhida = random.choice(musica_de_fundo)

pygame.mixer.music.load(musica_escolhida)
pygame.mixer.music.play(-1)

explosao = pygame.mixer.Sound('WhatsApp-Audio-2024-04-07-at-15.12.54.wav')
explosao.set_volume(1)

carro_passando = pygame.mixer.Sound('WhatsApp-Audio-2024-04-07-at-15.41.21.wav')
carro_passando.set_volume(0.5)

policia_som = pygame.mixer.Sound('WhatsApp-Audio-2024-04-07-at-15.54.27.wav')
policia_som.set_volume(1)

#tamanho da tela
largura = pygame.display.Info().current_w
altura = pygame.display.Info().current_h

venceu1 = False
venceu2 = False

#variáveis do jogador
x1 = 295
y1 = altura-300
x2 = largura-310
y2 = altura-300

#NPC PADRÂO pista 1
#145, 295, 445
carro1 = random.choice([145, 295, 445])
carro2 = random.choice([145, 295, 445])
caminhao1 = random.choice([145, 295, 445])
carroD1 = random.choice([145, 295, 445])
ladraox = random.choice([145, 295, 445])
polix = -100

velo1E = randint(-3000, -10)
velo1M = randint(-3000, -10)
velo1CV = randint(-10000, -5000)
veloD = randint(-5000, -1000)
car_direction = random.choice([3, -3])
ladraoy = randint(10000, 50000)
poliy = 100000

#npc pista 2 ☺
carroV1x = random.choice([largura-155, largura-300, largura-455])
carroV2x = random.choice([largura-155, largura-300, largura-455])
caminhao2x = random.choice([largura-155, largura-300, largura-455])
carroD2x = random.choice([largura-155, largura-300, largura-455])
car_direction2 = random.choice([3, -3])
ladraox1 = random.choice([largura-155, largura-300, largura-455])
polix1 = -100

carroV1y = randint(-3000, -10)
carroV2y = randint(-3000, -10)
caminhao2y = randint(-10000, -5000)
carroD2y = randint(-5000, -1000)
ladraoy1 = randint(10000, 50000)
poliy1 = 100000

#cores
branco = (255, 255, 255)
blue = (0, 0, 200)
red = (200, 0, 0)
amarelo = (255, 255, 0)
cinza = (70, 70, 70)
preto = (0, 0, 0)
cinza_claro = (150, 150, 150)
azul_claro = (0, 0, 255)

#variáveis da pista 1
morto1 = False
vel_faixa1_E1 = 0
vel_faixa1_E2 = 350
vel_faixa1_E3 = 700
vel_faixa1_E4 = 1050
vel_faixa1_D1 = 0
vel_faixa1_D2 = 350
vel_faixa1_D3 = 700
vel_faixa1_D4 = 1050

#variáveis da pista 2
morto2 = False
vel_faixa2_E1 = 0
vel_faixa2_E2 = 350
vel_faixa2_E3 = 700
vel_faixa2_E4 = 1050
vel_faixa2_D1 = 0
vel_faixa2_D2 = 350
vel_faixa2_D3 = 700
vel_faixa2_D4 = 1050

#gasolina/coletavel
cole1x = random.choice([145, 295, 445])
cole1y = randint(-2000, -10)

gasosa1 = 795

gasosa2 = largura - 530
cole2x = random.choice([largura - 155,largura - 300,largura - 455])
cole2y = randint(-2000, -10)

#variáveis de texto
fonte = pygame.font.SysFont('arial', 35, True, False)
fonte1 = pygame.font.SysFont('arial', 100, True, False)
pontos_distancia1 = 0
pontos_distancia2 = 0

# variavel vida
vida1 = 3
vida2 = 3

clock = pygame.time.Clock()
screen = pygame.display.set_mode((largura, altura), pygame.FULLSCREEN)
pygame.display.set_caption('projeto 0')

#jogo ativo em geral
while True:
    clock.tick(60)  # Controla a taxa de quadros
    screen.fill((0, 0, 0))

    #pontuação dos jogadores
    pontuacao1 = 'pontuação'
    pontos_P1 = f'{pontos_distancia1}'
    pontuacao2 = 'pontuação'
    pontos_P2 = f'{pontos_distancia2}'
    vidap1 = 'vida'
    vidap2 = 'vida'
    texto_pontuacao1 = fonte.render(pontuacao1, False, branco)
    texto_pontos_p1 = fonte.render(pontos_P1, False, branco)
    texto_pontuacao_p2 = fonte.render(pontuacao2, False, branco)
    texto_pontos_p2 = fonte.render(pontos_P2, False, branco)
    texto_vidap1 = fonte.render(vidap1, False, branco)
    texto_vidap2 = fonte.render(vidap2, False, branco)

    for event in pygame.event.get():
        if event.type == QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_p):
            pygame.quit()
            exit()

    dt = clock.tick()  # Captura o tempo desde a última chamada de tick()

    #estrada cinza ambas pistas
    pygame.draw.rect(screen, cinza, (100, 0, 450, 1500))
    pygame.draw.rect(screen, cinza, (largura-500, 0, 450, 1500))

    #cantos da pista 1
    canto_EA = pygame.draw.line(screen, branco, (100, 0), (100, 1500), 5)
    canto_DA = pygame.draw.line(screen, branco, (550, 0), (550, 1500), 5)

    #carros da pista 1
    carro_C1A = pygame.draw.rect(screen, branco, (carro1, velo1E, 70, 100))
    carro_C2A = pygame.draw.rect(screen, branco, (carro2, velo1M, 70, 100))
    carro_CVA = pygame.draw.rect(screen, cinza_claro, (caminhao1, velo1CV, 70, 200))
    pygame.draw.rect(screen, preto, (caminhao1, velo1CV, 70, 50))
    carroDA = pygame.draw.rect(screen, amarelo, (carroD1, veloD, 70, 100))
    ladrao = pygame.draw.rect(screen, red, (ladraox, ladraoy, 70, 100))
    policia = pygame.draw.rect(screen, azul_claro, (polix, poliy, 70, 100))

    #faixa amarela da esquerda da pista 1
    pygame.draw.rect(screen, amarelo, (250, vel_faixa1_E1, 5, 200))
    pygame.draw.rect(screen, amarelo, (250, vel_faixa1_E2, 5, 200))
    pygame.draw.rect(screen, amarelo, (250, vel_faixa1_E3, 5, 200))
    pygame.draw.rect(screen, amarelo, (250, vel_faixa1_E4, 5, 200))

    #faixa amarela da direita da pista 1
    pygame.draw.rect(screen, amarelo, (400, vel_faixa1_D1, 5, 200))
    pygame.draw.rect(screen, amarelo, (400, vel_faixa1_D2, 5, 200))
    pygame.draw.rect(screen, amarelo, (400, vel_faixa1_D3, 5, 200))
    pygame.draw.rect(screen, amarelo, (400, vel_faixa1_D4, 5, 200))

    player1 = pygame.draw.rect(screen, blue, (x1, y1, 80, 100))

    #elementos da pista 2

    #cantos da pista 2
    canto_DV = pygame.draw.line(screen, branco, (largura-50, 0), (largura-50, 1500), 5)
    canto_EV = pygame.draw.line(screen, branco, (largura-500, 0), (largura-500, 1500), 5)

    #carros da pista 2
    carroV1 = pygame.draw.rect(screen, branco, (carroV1x, carroV1y, 70, 100))
    carroV2 = pygame.draw.rect(screen, branco, (carroV2x, carroV2y, 70, 100))
    caminhao2 = pygame.draw.rect(screen, cinza_claro, (caminhao2x, caminhao2y, 70, 200))
    pygame.draw.rect(screen, preto, (caminhao2x, caminhao2y, 70, 50))
    carroD2 = pygame.draw.rect(screen, amarelo, (carroD2x, carroD2y, 70, 100))
    ladrao2 = pygame.draw.rect(screen, red, (ladraox1, ladraoy1, 70, 100))
    poli2 = pygame.draw.rect(screen, azul_claro, (polix, poliy, 70, 100))

    #faixa amarela da esquerda da pista 2
    pygame.draw.rect(screen, amarelo, (largura - 350, vel_faixa2_E1, 5, 200))
    pygame.draw.rect(screen, amarelo, (largura - 350, vel_faixa2_E2, 5, 200))
    pygame.draw.rect(screen, amarelo, (largura - 350, vel_faixa2_E3, 5, 200))
    pygame.draw.rect(screen, amarelo, (largura - 350, vel_faixa2_E4, 5, 200))

    #faixa amarela da direita da pista 2
    pygame.draw.rect(screen, amarelo, (largura - 200, vel_faixa2_D1, 5, 200))
    pygame.draw.rect(screen, amarelo, (largura - 200, vel_faixa2_D2, 5, 200))
    pygame.draw.rect(screen, amarelo, (largura - 200, vel_faixa2_D3, 5, 200))
    pygame.draw.rect(screen, amarelo, (largura - 200, vel_faixa2_D4, 5, 200))

    player2 = pygame.draw.rect(screen, red, (x2, y2 , 80, 100))

        #policia pista 1
    if ladraoy < 5000 and ladraoy > -200:
        if ladraox == 145:
            polix = 145
            poliy = 4200
            pygame.draw.rect(screen, red, (145, altura - 100, 60, 60))
        elif ladraox == 295:
            polix = 295
            poliy = 4200
            pygame.draw.rect(screen, red, (295, altura - 100, 60, 60))
        elif ladraox == 445:
            polix = 445
            poliy = 4200
            pygame.draw.rect(screen, red, (445, altura - 100, 60, 60))
    if ladraoy < altura + 3300 and ladraoy > altura + 3270:
        carro_passando.play()
    if poliy < altura + 3000 and poliy > 3000:
        policia_som.play()

        #policia pista 2
    if ladraoy1 < 5000 and ladraoy1 > -200:
        if ladraox == largura - 155:
            polix1 = largura - 155
            poliy1 = 4200
            pygame.draw.rect(screen, red, (largura - 155, altura - 100, 60, 60))
        elif ladraox1 == largura - 300:
            polix1 = largura - 300
            poliy1 = 4200
            pygame.draw.rect(screen, red, (largura - 300, altura - 100, 60, 60))
        elif ladraox1 == largura - 455:
            polix1 = largura - 455
            poliy1 = 4200
            pygame.draw.rect(screen, red, (largura - 455, altura - 100, 60, 60))
    if ladraoy1 < altura + 3300 and ladraoy1 > altura + 3299:
        carro_passando.play()
    if poliy1 < altura + 3000 and poliy1 > 3000:
        policia_som.play()

    # colisao entre npcs pista 1
    if veloD >= altura/2 - 300:
        carroD1 = carroD1 + car_direction

    if player1.colliderect(policia) or player1.colliderect(ladrao):
        vida1 -= 1
        ladraox = random.choice([145, 295, 445])
        polix = -100
        ladraoy = randint(10000, 50000)
        poliy = 100000
        explosao.play()

    if carroDA.colliderect(canto_EA) or carroDA.colliderect(canto_DA):
        veloD = randint(-5000, -1000)
        carroD1 = random.choice([145, 295, 445])
        car_direction = random.choice([3, -3])
        explosao.play()

    if carroDA.colliderect(carro_C1A):
        velo1E = randint(-3000, -10)
        veloD = randint(-5000, -1000)
        carroD1 = random.choice([145, 295, 445])
        carro1 = random.choice([145, 295, 445])
        car_direction = random.choice([3, -3])
        explosao.play()

    if carro_CVA.colliderect(carro_C1A):
        velo1E = randint(-3000, -10)
        carro1 = random.choice([145, 295, 445])
        velo1CV = randint(-10000, -5000)
        caminhao1 = random.choice([145, 295, 445])

    elif carro_CVA.colliderect(carro_C2A):
        velo1M = randint(-3000, -10)
        carro2 = random.choice([145, 295, 445])
        caminhao1 = random.choice([145, 295, 445])
        velo1CV = randint(-10000, -5000)

    elif carro_CVA.colliderect(carroDA):
        veloD = randint(-5000, -1000)
        velo1CV = randint(-10000, -5000)
        caminhao1 = random.choice([145, 295, 445])
        carroD1 = random.choice([145, 295, 445])
        car_direction = random.choice([3, -3])
        explosao.play()


    # colisao entre npcs pista 2
    if player2.colliderect(ladrao2) or player2.colliderect(poli2):
        vida2 -= 1
        carroV1x = random.choice([largura - 155, largura - 300, largura - 455])
        carroV2x = random.choice([largura - 155, largura - 300, largura - 455])
        caminhao2x = random.choice([largura - 155, largura - 300, largura - 455])
        carroD2x = random.choice([largura - 155, largura - 300, largura - 455])
        car_direction2 = random.choice([3, -3])
        ladraox1 = random.choice([largura - 155, largura - 300, largura - 455])
        polix1 = -100
        carroV1y = randint(-3000, -10)
        carroV2y = randint(-3000, -10)
        caminhao2y = randint(-10000, -5000)
        carroD2y = randint(-5000, -1000)
        ladraoy1 = randint(10000, 50000)
        poliy1 = 100000
        explosao.play()

    if carroD2y >= altura/2 - 300:
        carroD2x = carroD2x + car_direction2

    if carroD2.colliderect(carroV1):
        carroD2x = random.choice([largura - 155, largura - 300, largura - 455])
        carroV1x = random.choice([largura - 155, largura - 300, largura - 455])
        carroD2y = randint(-5000, -1000)
        carroV1y = randint(-3000, -10)
        car_direction2 = random.choice([3, -3])
        explosao.play()

    elif carroD2.colliderect(carroV2):
        carroV2x = random.choice([largura - 155, largura - 300, largura - 455])
        carroD2x = random.choice([largura - 155, largura - 300, largura - 455])
        carroV2y = randint(-3000, -10)
        carroD2y = randint(-5000, -1000)
        car_direction2 = random.choice([3, -3])
        explosao.play()

    elif carroD2.colliderect(caminhao2):
        caminhao2x = random.choice([largura - 155, largura - 300, largura - 455])
        carroD2x = random.choice([largura - 155, largura - 300, largura - 455])
        caminhao2y = randint(-10000, -5000)
        carroD2y = randint(-5000, -1000)
        car_direction2 = random.choice([3, -3])
        explosao.play()

    elif carroD2.colliderect(canto_EV) or carroD2.colliderect(canto_DV):
        carroD2x = random.choice([largura - 155, largura - 300, largura - 455])
        carroD2y = randint(-5000, -1000)
        car_direction2 = random.choice([3, -3])
        explosao.play()

    if carroV1.colliderect(carroV2):
        carroV1x = random.choice([largura - 155, largura - 300, largura - 455])
        carroV2x = random.choice([largura - 155, largura - 300, largura - 455])
        carroV1y = randint(-3000, -10)
        carroV2y = randint(-3000, -10)

    elif carroV1.colliderect(caminhao2):
        carroV1x = random.choice([largura - 155, largura - 300, largura - 455])
        caminhao2x = random.choice([largura - 155, largura - 300, largura - 455])
        carroV1y = randint(-3000, -10)
        caminhao2y = randint(-10000, -5000)

    elif carroV2.colliderect(caminhao2):
        carroV2x = random.choice([largura - 155, largura - 300, largura - 455])
        caminhao2x = random.choice([largura - 155, largura - 300, largura - 455])
        carroV2y = randint(-3000, -10)
        caminhao2y = randint(-10000, -5000)

    #colisão mortal ambos players
    if player1.colliderect(canto_EA) or player1.colliderect(canto_DA) or player1.colliderect(carro_C1A) or player1.colliderect(carro_C2A) or player1. colliderect(carro_CVA) or player1.colliderect(carroDA):
        vida1 -= 1
        x1 = 295
        y1 = altura - 300
        velo1E = randint(-3000, -10)
        velo1M = randint(-3000, -10)
        velo1CV = randint(-10000, -5000)
        veloD = randint(-1000, -100)
        ladraox = random.choice([145, 295, 445])
        polix = -100
        ladraoy = randint(10000, 50000)
        poliy = 100000
        explosao.play()

    if vida1 == 3:
        pygame.draw.rect(screen, red, (580, 270, 50, 50))
        pygame.draw.rect(screen, red, (631, 270, 50, 50))
        pygame.draw.rect(screen, red, (682, 270, 50, 50))

    elif vida1 == 2:
        pygame.draw.rect(screen, red, (631, 270, 50, 50))
        pygame.draw.rect(screen, red, (580, 270, 50, 50))

    elif vida1 == 1:
        pygame.draw.rect(screen, red, (580, 270, 50, 50))

    if vida1 == 0:
        morto1 = True

    if player2.colliderect(canto_DV) or player2.colliderect(canto_EV) or player2.colliderect(carroV1) or player2.colliderect(carroV2) or player2.colliderect(caminhao2) or player2.colliderect(carroD2):
        vida2 -= 1
        x2 = largura - 310
        y2 = altura - 300
        carroV1x = random.choice([largura - 155, largura - 300, largura - 455])
        carroV2x = random.choice([largura - 155, largura - 300, largura - 455])
        caminhao2x = random.choice([largura - 155, largura - 300, largura - 455])
        carroD2x = random.choice([largura - 155, largura - 300, largura - 455])
        car_direction2 = random.choice([3, -3])
        ladraox1 = random.choice([largura - 155, largura - 300, largura - 455])
        polix1 = -100
        carroV1y = randint(-3000, -10)
        carroV2y = randint(-3000, -10)
        caminhao2y = randint(-10000, -5000)
        carroD2y = randint(-5000, -1000)
        ladraoy1 = randint(10000, 50000)
        poliy1 = 100000
        explosao.play()

    if vida2 == 3:
        pygame.draw.rect(screen, red, (largura-580, 270, 50, 50))
        pygame.draw.rect(screen, red, (largura - 631, 270, 50, 50))
        pygame.draw.rect(screen, red, (largura - 682, 270, 50, 50))

    elif vida2 == 2:
        pygame.draw.rect(screen, red, (largura - 631, 270, 50, 50))
        pygame.draw.rect(screen, red, (largura - 580, 270, 50, 50))

    elif vida2 == 1:
        pygame.draw.rect(screen, red, (largura - 580, 270, 50, 50))

    if vida2 == 0:
        morto2 = True

    #movimento do jogador 1
    if morto1:
        pass
    else:
        key = pygame.key.get_pressed()
        if key[K_a]:
            x1 -= 10
        elif key[K_d]:
            x1 += 10
        if key[K_w]:
            vel_faixa1_E1 += 15
            vel_faixa1_E2 += 15
            vel_faixa1_E3 += 15
            vel_faixa1_E4 += 15
            vel_faixa1_D1 += 15
            vel_faixa1_D2 += 15
            vel_faixa1_D3 += 15
            vel_faixa1_D4 += 15
            velo1E += 10
            velo1M += 10
            velo1CV += 15
            veloD += 10
            poliy -= 0
            ladraoy -= 0
        elif key[K_s]:
            vel_faixa1_E1 -= 5
            vel_faixa1_E2 -= 5
            vel_faixa1_E3 -= 5
            vel_faixa1_E4 -= 5
            vel_faixa1_D1 -= 5
            vel_faixa1_D2 -= 5
            vel_faixa1_D3 -= 5
            vel_faixa1_D4 -= 5
            velo1E += 1
            velo1M += 1
            velo1CV += 3
            veloD += 1
            poliy -= 15
            ladraoy -= 15

        if vel_faixa1_E1 > 1050:
            vel_faixa1_E1 = -350
        if vel_faixa1_E2 > 1050:
            vel_faixa1_E2 = -350
        if vel_faixa1_E3 > 1050:
            vel_faixa1_E3 = -350
        if vel_faixa1_E4 > 1050:
            vel_faixa1_E4 = -350

        if vel_faixa1_D1 > 1050:
            vel_faixa1_D1 = -350
        if vel_faixa1_D2 > 1050:
            vel_faixa1_D2 = -350
        if vel_faixa1_D3 > 1050:
            vel_faixa1_D3 = -350
        if vel_faixa1_D4 > 1050:
            vel_faixa1_D4 = -350

        #movimento da pista1
        vel_faixa1_E1 += 15
        vel_faixa1_E2 += 15
        vel_faixa1_E3 += 15
        vel_faixa1_E4 += 15
        vel_faixa1_D1 += 15
        vel_faixa1_D2 += 15
        vel_faixa1_D3 += 15
        vel_faixa1_D4 += 15

        velo1E += 7
        velo1M += 7
        velo1CV += 5
        veloD += 7
        poliy -= 10
        ladraoy -= 10
        if velo1E > altura + 50:
            velo1E = randint(-3000, -10)
            carro1 = random.choice([145, 295, 445])
        if velo1CV > altura + 50:
            velo1CV = randint(-3000, -10)
            caminhao1 = random.choice([145, 295, 445])
        if velo1M > altura + 50:
            velo1M = randint(-3000, -10)
            carro2 = random.choice([145, 295, 445])
        if veloD > altura + 50:
            carroD1 = random.choice([145, 295, 445])
            veloD = randint(-5000, -1000)
            car_direction = random.choice([5, -5])
        if ladraoy < -200:
            ladraox = random.choice([145, 295, 445])
            ladraoy = randint(10000, 50000)
        if poliy < -200:
            poliy = 50000

    #movimento do jogador 2
    if morto2 == True:
        pass
    else:
        key = pygame.key.get_pressed()
        if key[K_LEFT]:
            x2 -= 10
        elif key[K_RIGHT]:
            x2 += 10
        if key[K_UP]:
            vel_faixa2_E1 += 15
            vel_faixa2_E2 += 15
            vel_faixa2_E3 += 15
            vel_faixa2_E4 += 15
            vel_faixa2_D1 += 15
            vel_faixa2_D2 += 15
            vel_faixa2_D3 += 15
            vel_faixa2_D4 += 15
            carroV2y += 10
            carroV1y += 10
            carroD2y += 10
            caminhao2y += 15
            poliy1 -= 0
            ladraoy1 -= 0

        elif key[K_DOWN]:
            vel_faixa2_E1 -= 5
            vel_faixa2_E2 -= 5
            vel_faixa2_E3 -= 5
            vel_faixa2_E4 -= 5
            vel_faixa2_D1 -= 5
            vel_faixa2_D2 -= 5
            vel_faixa2_D3 -= 5
            vel_faixa2_D4 -= 5
            carroV2y += 1
            carroV1y += 1
            carroD2y += 1
            caminhao2y += 3
            poliy1 -= 15
            ladraoy1 -= 15

            # faixa esquerda pista 2 movimento
        if vel_faixa2_E1 > 1050:
            vel_faixa2_E1 = -350
        if vel_faixa2_E2 > 1050:
            vel_faixa2_E2 = -350
        if vel_faixa2_E3 > 1050:
            vel_faixa2_E3 = -350
        if vel_faixa2_E4 > 1050:
            vel_faixa2_E4 = -350

            # faixa direita pista 2 movimento
        if vel_faixa2_D1 > 1050:
            vel_faixa2_D1 = -350
        if vel_faixa2_D2 > 1050:
            vel_faixa2_D2 = -350
        if vel_faixa2_D3 > 1050:
            vel_faixa2_D3 = -350
        if vel_faixa2_D4 > 1050:
            vel_faixa2_D4 = -350

        #movimento da pista2
        vel_faixa2_E1 += 15
        vel_faixa2_E2 += 15
        vel_faixa2_E3 += 15
        vel_faixa2_E4 += 15
        vel_faixa2_D1 += 15
        vel_faixa2_D2 += 15
        vel_faixa2_D3 += 15
        vel_faixa2_D4 += 15

        carroV2y += 7
        carroV1y += 7
        carroD2y += 7
        caminhao2y += 9
        poliy1 -= 10
        ladraoy1 -= 10

        if carroV2y > altura + 50:
            carroV2y = randint(-3000, -10)
        if carroV1y > altura + 50:
            carroV1y = randint(-3000, -10)
        if carroD2y > altura + 50:
            carroD2y = randint(-5000, -1000)
        if caminhao2y > altura + 50:
            caminhao2y = randint(-10000, -5000)
        if ladraoy1 < -200:
            ladraoy1 = randint(10000, 50000)
        if poliy1 < -200:
            poliy1 = 100000


    if gasosa1 == 580:
        morto1 = True
        pygame.draw.line(screen, branco, (575, 150), (800, 150), 20)
        pass
    else:
        if key[K_w]:
            if vel_faixa1_E1 > 1040 or vel_faixa1_E2 > 1040 or vel_faixa1_E3 > 1040 or vel_faixa1_E4 > 1040:
                pontos_distancia1 += 1
                gasosa1 -= 1.5
        elif key[K_s]:
            if vel_faixa1_E1 > 1055 or vel_faixa1_E2 > 1055 or vel_faixa1_E3 > 1055 or vel_faixa1_E4 > 1055:
                pontos_distancia1 += 1
                gasosa1 -= 1
        else:
            if vel_faixa1_E1 > 1050 or vel_faixa1_E2 > 1050 or vel_faixa1_E3 > 1050 or vel_faixa1_E4 > 1050:
                pontos_distancia1 += 1
                gasosa1 -= 0.5


    if gasosa2 == largura-745:
        morto2 = True
        pygame.draw.line(screen, (255, 255, 255), (largura - 750, 150), (largura - 525, 150), 20)
        pass
    else:
        if key[K_UP]:
            if vel_faixa2_D1 > 1040 or vel_faixa2_D2 > 1040 or vel_faixa2_D3 > 1040 or vel_faixa2_D4 > 1040:
                pontos_distancia2 += 1
                gasosa2 -= 1.5
        elif key[K_DOWN]:
            if vel_faixa2_D1 > 1055 or vel_faixa2_D2 > 1055 or vel_faixa2_D3 > 1055 or vel_faixa2_D4 > 1055:
                pontos_distancia2 += 1
                gasosa2 -= 1
        else:
            if vel_faixa2_D1 > 1050 or vel_faixa2_D2 > 1050 or vel_faixa2_D3 > 1050 or vel_faixa2_D4 > 1050:
                pontos_distancia2 += 1
                gasosa2 -= 0.5

    screen.blit(texto_pontuacao1, (580, 20))
    screen.blit(texto_pontos_p1, (580, 70))
    screen.blit(texto_pontuacao_p2, (largura-700, 20))
    screen.blit(texto_pontos_p2, (largura-700, 70))
    screen.blit(texto_vidap1, (580, 220))
    screen.blit(texto_vidap2, (largura-600, 220))

    # gasosa carro 1

    pygame.draw.line(screen, branco, (575, 150), (800, 150), 20)
    pygame.draw.line(screen, (255, 0, 0), (580, 150), (gasosa1, 150), 10)

    gaso1 = pygame.draw.rect(screen, (0, 0, 255), (cole1x, cole1y, 40, 40))
    cole1y += 5

    if cole1y > 1500:
        cole1y = randint(-13000, -6000)
    cole1y += 5

    # gasosa carro 2

    pygame.draw.line(screen, (255, 255, 255), (largura - 750, 150), (largura - 525, 150), 20)
    pygame.draw.line(screen, (255, 0, 0), (largura - 745, 150), (gasosa2, 150), 10)

    gaso2 = pygame.draw.rect(screen, (0, 0, 255), (cole2x, cole2y, 40, 40))
    if cole2y > 1500:
        cole2y = randint(-13000, -6000)
    cole2y += 5

    if player2.colliderect(gaso2):
        cole2y = randint(-13000, -6000)
        gasosa2 = min(gasosa2 + 50, max([largura - 530]))

    if player1.colliderect(gaso1):
        cole1y = randint(-13000, -6000)
        gasosa1 = min(gasosa1 + 50, max([795]))

    # aumento carro1
    if pontos_distancia1 > 50:
        veloD += 1
        velo1M += 1
        velo1E += 1
    if pontos_distancia1 > 100:
        veloD += 1
        velo1M += 1
        velo1E += 1
    if pontos_distancia1 > 150:
        veloD += 1
        velo1M += 1
        velo1E += 1
    if pontos_distancia1 > 200:
        veloD += 2
        velo1M += 2
        velo1E += 2
    if pontos_distancia1 > 300:
        veloD += 2
        velo1M += 2
        velo1E += 2
    if pontos_distancia1 > 400:
        veloD += 2
        velo1M += 2
        velo1E += 2
    if pontos_distancia1 > 500:
        veloD += 5
        velo1M += 5
        velo1E += 5

    # aumento carro2
    if pontos_distancia2 > 50:
        velo1E += 1
        velo1M += 1
        velo1CV += 1
        veloD += 1
    if pontos_distancia2 > 100:
        velo1E += 1
        velo1M += 1
        velo1CV += 1
        veloD += 1
    if pontos_distancia2 > 150:
        velo1E += 1
        velo1M += 1
        velo1CV += 1
        veloD += 1
    if pontos_distancia2 > 200:
        velo1E += 1
        velo1M += 1
        velo1CV += 1
        veloD += 1
    if pontos_distancia2 > 300:
        velo1E += 1
        velo1M += 1
        velo1CV += 1
        veloD += 1
    if pontos_distancia2 > 400:
        velo1E += 1
        velo1M += 1
        velo1CV += 1
        veloD += 1
    if pontos_distancia2 > 500:
        velo1E += 1
        velo1M += 1
        velo1CV += 1
        veloD += 1

    # gasosa carro 1

    pygame.draw.line(screen, branco, (575, 150), (800, 150), 20)
    pygame.draw.line(screen, (255, 0, 0), (580, 150), (gasosa1, 150), 10)

    # gasosa carro 2

    pygame.draw.line(screen, (255, 255, 255), (largura - 750, 150), (largura - 525, 150), 20)
    pygame.draw.line(screen, (255, 0, 0), (largura - 745, 150), (gasosa2, 150), 10)

    gaso2 = pygame.draw.rect(screen, (0, 0, 255), (cole2x, cole2y, 40, 40))
    if cole2y > 1500:
        cole2y = randint(-13000, -6000)
    cole2y += 5

    if player2.colliderect(gaso2):
        cole2y = randint(-13000, -6000)
        gasosa2 = min(gasosa2 + 50, max([largura - 530]))

    if player1.colliderect(gaso1):
        cole1y = randint(-13000, -6000)
        gasosa1 = min(gasosa1 + 50, max([795]))

    # aumento carro1
    if pontos_distancia1 > 50:
        carroV1y += 1
        carroV2y += 1
        caminhao2y += 1
        carroD2y += 1
    if pontos_distancia1 > 100:
        carroV1y += 1
        carroV2y += 1
        caminhao2y += 1
        carroD2y += 1
    if pontos_distancia1 > 150:
        carroV1y += 1
        carroV2y += 1
        caminhao2y += 1
        carroD2y += 1
    if pontos_distancia1 > 200:
        carroV1y += 1
        carroV2y += 1
        caminhao2y += 1
        carroD2y += 1
    if pontos_distancia1 > 300:
        carroV1y += 1
        carroV2y += 1
        caminhao2y += 1
        carroD2y += 1
    if pontos_distancia1 > 400:
        veloD += 2
        velo1M += 2
        velo1E += 2
    if pontos_distancia1 > 500:
        veloD += 5
        velo1M += 5
        velo1E += 5

    # aumento carro2
    if pontos_distancia2 > 50:
        carroV1y += 1
        carroV2y += 1
        caminhao2y += 1
        carroD2y += 1
    if pontos_distancia2 > 100:
        carroV1y += 1
        carroV2y += 1
        caminhao2y += 1
        carroD2y += 1
    if pontos_distancia2 > 150:
        carroV1y += 1
        carroV2y += 1
        caminhao2y += 1
        carroD2y += 1
    if pontos_distancia2 > 200:
        carroV1y += 1
        carroV2y += 1
        caminhao2y += 1
        carroD2y += 1
    if pontos_distancia2 > 300:
        carroV1y += 1
        carroV2y += 1
        caminhao2y += 1
        carroD2y += 1
    if pontos_distancia2 > 400:
        carroV1y += 1
        carroV2y += 1
        caminhao2y += 1
        carroD2y += 1
    if pontos_distancia2 > 500:
        carroV1y += 1
        carroV2y += 1
        caminhao2y += 1
        carroD2y += 1

    # coletavel

    # esquema de pontuação
    if morto1 == True and morto2 == True:
        if pontos_distancia1 > pontos_distancia2:
            venceu1 = True
            while True:
                screen.fill((cinza_claro))
                mensagem = ("player 1 venceu!")
                mensagem1 = f'player 1 ganhou com {pontos_distancia1} pontos'
                mensagem2 = f'player 2 perdeu com {pontos_distancia2} pontos'
                texto_formatado = fonte1.render(mensagem, True, preto)
                texto_formatado1 = fonte.render(mensagem1, True, azul_claro)
                texto_formatado2 = fonte.render(mensagem2, True, red)
                ret_texto = texto_formatado.get_rect()
                ret_texto1 = texto_formatado1.get_rect()
                ret_texto2 = texto_formatado2.get_rect()
                ret_texto.center = (largura // 2, altura // 2 - 150)
                ret_texto1.center = (largura // 2, altura // 2)
                ret_texto2.center = (largura // 2, altura // 2 + 50)
                screen.blit(texto_formatado, ret_texto)
                screen.blit(texto_formatado1, ret_texto1)
                screen.blit(texto_formatado2, ret_texto2)
                pygame.mixer_music.stop()
                for event in pygame.event.get():
                    if event.type == QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_p):
                        pygame.quit()
                        exit()

                pygame.display.update()

    if morto1 == True and morto2 == True:
        if pontos_distancia1 < pontos_distancia2:
            venceu2 = True
            while True:
                screen.fill((cinza_claro))
                mensagem = ("player 2 venceu!")
                mensagem1 = f'player 1 perdeu com {pontos_distancia1} pontos'
                mensagem2 = f'player 2 ganhou com {pontos_distancia2} pontos'
                texto_formatado = fonte1.render(mensagem, True, preto)
                texto_formatado1 = fonte.render(mensagem1, True, azul_claro)
                texto_formatado2 = fonte.render(mensagem2, True, red)
                ret_texto = texto_formatado.get_rect()
                ret_texto1 = texto_formatado1.get_rect()
                ret_texto2 = texto_formatado2.get_rect()
                ret_texto.center = (largura // 2, altura // 2 - 150)
                ret_texto1.center = (largura // 2, altura // 2)
                ret_texto2.center = (largura // 2, altura // 2 + 50)
                screen.blit(texto_formatado, ret_texto)
                screen.blit(texto_formatado1, ret_texto1)
                screen.blit(texto_formatado2, ret_texto2)
                pygame.mixer_music.stop()
                for event in pygame.event.get():
                    if event.type == QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_p):
                        pygame.quit()
                        exit()
                pygame.display.update()
    pygame.display.update()
