import pygame  
import random  

class MovendoTexto:  
    def __init__(self, texto, fonte_tamanho, largura, altura):  
        self.fonte = pygame.font.SysFont(None, fonte_tamanho)
        self.texto = texto  # Define o texto a ser exibido.
        self.largura = largura  # Define a largura da tela.
        self.altura = altura  # Define a altura da tela.
        self.texto_surf = self.fonte.render(texto, True, (255, 255, 255))  # Renderiza o texto na tela.
        self.rect = self.texto_surf.get_rect(center=(largura / 2, altura / 2))  # Obtém o retângulo que envolve o texto e centraliza na tela.

        # Define as velocidades inicialmente como valores aleatórios não nulos.
        self.velocidade_x = self.gerar_numero_nao_zero()  
        self.velocidade_y = self.gerar_numero_nao_zero()

    def gerar_numero_nao_zero(self):  # Define um método para gerar um número aleatório não nulo.
        numero = 0  # Inicializa o número como zero.
        while numero == 0:  # Enquanto o número gerado for zero, continue gerando.
            numero = random.randint(-1, 1)  # Gera um número aleatório entre -1 e 1.
        return numero  # Retorna o número gerado.

    def move(self):  # Define um método para mover o texto.
        # Atualiza as coordenadas do retângulo do texto com base nas velocidades.
        self.rect.x += self.velocidade_x
        self.rect.y += self.velocidade_y

        # Verifica se o texto atingiu as bordas da tela e atualiza as velocidades e cores do texto, se necessário.
        if self.rect.left <= 0:
            self.velocidade_x = random.randint(0, 1)
            self.velocidade_y = random.randint(-1, 1)
            self.change_color()

        if self.rect.right >= self.largura:
            self.velocidade_x = random.randint(-1, 0)
            self.velocidade_y = random.randint(-1, 1)
            self.change_color()

        if self.rect.top <= 0:
            self.velocidade_x = random.randint(-1, 1)
            self.velocidade_y = random.randint(0, 1)
            self.change_color()

        if self.rect.bottom >= self.altura:
            self.velocidade_x = random.randint(-1, 1)
            self.velocidade_y = random.randint(-1, 0)
            self.change_color()

    def change_color(self):  # Define um método para mudar a cor do texto.
        # Gera uma nova cor aleatória.
        cor_texto = (
            random.randint(0, 255),
            random.randint(0, 255),
            random.randint(0, 255),
        )
        # Renderiza o texto com a nova cor.
        self.texto_surf = self.fonte.render(self.texto, True, cor_texto)
