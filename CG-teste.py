import sys
import pygame

pygame.init()

#Configura tela
largura = 800
altura = 600

tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Pygame")

PRETO =(0, 0, 0)
BRANCO = (255, 255, 255)

tamnho_fonte = 50
fonte = pygame.font.SysFont(None, tamnho_fonte)

texto = fonte.render("Mateus", True, BRANCO)
# texto_rect = texto.get_rect(center=(largura / 2, altura / 2)) centro
# texto_rect = texto.get_rect(center=(80, 55))  # top esquerdo
# texto_rect = texto.get_rect(center=(700, 55)) #top direito
# texto_rect = texto.get_rect(center=(largura / 2, 25)) #TOP
# texto_rect = texto.get_rect(center=(80, 300)) #centro esquerda
# texto_rect = texto.get_rect(center=(700, 300)) #centro direita
# texto_rect = texto.get_rect(center=(80, 550)) #inferior esquerdo
# texto_rect = texto.get_rect(center=(400, 550)) #inferior centro
# texto_rect = texto.get_rect(center=(700, 550)) #inferior direito 

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    tela.fill(PRETO)
    tela.blit(texto, texto_rect)
    pygame.display.flip()
