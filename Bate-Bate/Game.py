import pygame  
import sys  
from MecMovimento import MovendoTexto 

class Game: 
    def __init__(self):  
        pygame.init()  
        self.largura = 800  # Define a largura da tela do jogo.
        self.altura = 600  # Define a altura da tela do jogo.
        self.tela = pygame.display.set_mode((self.largura, self.altura))  # Cria a tela do jogo com as dimensões especificadas.
        pygame.display.set_caption("Bate-Bate")  # Define o título da janela do jogo.
        self.clock = pygame.time.Clock()  # Cria um objeto clock para controlar a taxa de quadros do jogo.
        self.MovendoTexto = MovendoTexto("Mateus", 50, self.largura, self.altura)  # Cria um objeto da classe MovendoTexto.

    def run(self):  # Define o método run da classe Game.
        rodando = True  # Define a variável rodando como True, indicando que o jogo está em execução.
        while rodando:  # Inicia um loop enquanto o jogo estiver em execução.
            for evento in pygame.event.get():  # Itera sobre os eventos pygame.
                if evento.type == pygame.QUIT:  # Verifica se o evento é de fechar a janela.
                    rodando = False  # Define rodando como False para sair do loop.

            self.MovendoTexto.move()  # Chama o método move do objeto MovendoTexto para atualizar sua posição.
            self.tela.fill((0, 0, 0))  # Preenche a tela com a cor preta.
            self.tela.blit(self.MovendoTexto.texto_surf, self.MovendoTexto.rect)  # Desenha o texto na tela.
            pygame.display.flip()  # Atualiza a tela para exibir as mudanças.
            self.clock.tick(60)  # Limita a taxa de quadros do jogo para 60 quadros por segundo.

        pygame.quit()  
        sys.exit()  

        pygame.quit()
        sys.exit()
