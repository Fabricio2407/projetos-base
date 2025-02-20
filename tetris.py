import pygame
import random

# Inicializa o Pygame
pygame.init()

# Definir dimensões da tela e do grid
LARGURA_TELA, ALTURA_TELA = 300, 600
LARGURA_BLOCO = 30
COLUNAS, LINHAS = LARGURA_TELA // LARGURA_BLOCO, ALTURA_TELA // LARGURA_BLOCO

# Cores
CORES = [
    (0, 0, 0),  # Preto
    (0, 255, 255),  # Ciano
    (255, 165, 0),  # Laranja
    (0, 0, 255),  # Azul
    (255, 255, 0),  # Amarelo
    (0, 255, 0),  # Verde
    (128, 0, 128),  # Roxo
    (255, 0, 0)  # Vermelho
]

# Formatos das peças (Tetrominos)
PECAS = [
    [[1, 1, 1, 1]],
    [[1, 1], [1, 1]],
    [[0, 1, 0], [1, 1, 1]],
    [[1, 0, 0], [1, 1, 1]],
    [[0, 0, 1], [1, 1, 1]],
    [[1, 1, 0], [0, 1, 1]],
    [[0, 1, 1], [1, 1, 0]]
]


# Função para criar uma nova peça
def nova_peca():
    return {'forma': random.choice(PECAS), 'x': COLUNAS // 2 - 2, 'y': 0, 'cor': random.randint(1, len(CORES) - 1)}


# Função para desenhar o grid
def desenha_grid(tela, grid):
    for y in range(LINHAS):
        for x in range(COLUNAS):
            pygame.draw.rect(tela, CORES[grid[y][x]],
                             (x * LARGURA_BLOCO, y * LARGURA_BLOCO, LARGURA_BLOCO, LARGURA_BLOCO), 0)


# Função para desenhar a peça atual
def desenha_peca(tela, peca):
    forma = peca['forma']
    for y, linha in enumerate(forma):
        for x, valor in enumerate(linha):
            if valor:
                pygame.draw.rect(tela, CORES[peca['cor']],
                                 ((peca['x'] + x) * LARGURA_BLOCO,
                                  (peca['y'] + y) * LARGURA_BLOCO,
                                  LARGURA_BLOCO, LARGURA_BLOCO), 0)


# Função para verificar colisão
def colidiu(grid, peca):
    forma = peca['forma']
    for y, linha in enumerate(forma):
        for x, valor in enumerate(linha):
            if valor and (
                    y + peca['y'] >= LINHAS or x + peca['x'] < 0 or x + peca['x'] >= COLUNAS or grid[y + peca['y']][
                    x + peca['x']]):
                return True
    return False


# Função para fixar a peça no grid
def fixa_peca(grid, peca):
    forma = peca['forma']
    for y, linha in enumerate(forma):
        for x, valor in enumerate(linha):
            if valor:
                grid[peca['y'] + y][peca['x'] + x] = peca['cor']


# Função para remover linha completa
def remove_linhas(grid):
    linhas_removidas = 0
    for y in range(LINHAS - 1, -1, -1):
        if 0 not in grid[y]:
            del grid[y]
            grid.insert(0, [0 for _ in range(COLUNAS)])
            linhas_removidas += 1
    return linhas_removidas


# Função principal
def main():
    tela = pygame.display.set_mode((LARGURA_TELA, ALTURA_TELA))
    pygame.display.set_caption("Tetris")

    relogio = pygame.time.Clock()
    grid = [[0 for _ in range(COLUNAS)] for _ in range(LINHAS)]

    peca_atual = nova_peca()
    proxima_peca = nova_peca()

    trocou_peca = False
    velocidade = 500
    tempo_passado = 0
    rodando = True

    while rodando:
        tela.fill((0, 0, 0))
        tempo_passado += relogio.get_rawtime()
        relogio.tick()

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                rodando = False
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_LEFT:
                    peca_atual['x'] -= 1
                    if colidiu(grid, peca_atual):
                        peca_atual['x'] += 1
                elif evento.key == pygame.K_RIGHT:
                    peca_atual['x'] += 1
                    if colidiu(grid, peca_atual):
                        peca_atual['x'] -= 1
                elif evento.key == pygame.K_DOWN:
                    peca_atual['y'] += 1
                    if colidiu(grid, peca_atual):
                        peca_atual['y'] -= 1
                elif evento.key == pygame.K_UP:
                    peca_atual['forma'] = list(zip(*reversed(peca_atual['forma'])))
                    if colidiu(grid, peca_atual):
                        peca_atual['forma'] = list(zip(*reversed(peca_atual['forma']))[::-1])

        if tempo_passado > velocidade:
            peca_atual['y'] += 1
            if colidiu(grid, peca_atual):
                peca_atual['y'] -= 1
                fixa_peca(grid, peca_atual)
                peca_atual = proxima_peca
                proxima_peca = nova_peca()
                remove_linhas(grid)
            tempo_passado = 0

        desenha_grid(tela, grid)
        desenha_peca(tela, peca_atual)  # Adiciona esta linha para desenhar a peça atual
        pygame.display.update()


if __name__ == "__main__":
    main()
