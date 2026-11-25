import pygame
import random
import sys
import os

pygame.init()

# --- Configuración de tablero ---
BLOCK_SIZE = 30
GRID_WIDTH = 10
GRID_HEIGHT = 20
SCREEN_WIDTH = BLOCK_SIZE * (GRID_WIDTH + 6)
SCREEN_HEIGHT = BLOCK_SIZE * GRID_HEIGHT

# --- Colores ---
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (128, 128, 128)
CYAN = (0, 255, 255)
BLUE = (0, 0, 255)
ORANGE = (255, 165, 0)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
PURPLE = (128, 0, 128)
RED = (255, 0, 0)

# --- Formas de las piezas ---
SHAPES = [
    [[0,0,0,0],
     [1,1,1,1],
     [0,0,0,0],
     [0,0,0,0]],   # I (Cyan)

    [[0,0,1],
     [1,1,1],
     [0,0,0]],     # L (Orange)

    [[1,0,0],
     [1,1,1],
     [0,0,0]],     # J (Blue)

    [[1,1],
     [1,1]],       # O (Yellow)

    [[0,1,1],
     [1,1,0],
     [0,0,0]],     # Z (Red)

    [[0,1,0],
     [1,1,1],
     [0,0,0]],     # T (Purple)

    [[1,1,0],
     [0,1,1],
     [0,0,0]]      # S (Green)
]

COLORS = [CYAN, ORANGE, BLUE, YELLOW, RED, PURPLE, GREEN]

# --- Clase Pieza ---
class Piece:
    def __init__(self):
        self.shape_idx = random.randint(0, len(SHAPES)-1)
        self.shape = [row[:] for row in SHAPES[self.shape_idx]]
        self.color = COLORS[self.shape_idx]
        self.x = GRID_WIDTH // 2 - len(self.shape[0]) // 2
        self.y = 0

    def rotate(self):
        self.shape = [[self.shape[y][x] for y in range(len(self.shape)-1, -1, -1)]
                      for x in range(len(self.shape[0]))]

# --- Clase TetrisGame ---
class TetrisGame:
    def __init__(self):
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption('Tetris con Imágenes')
        self.clock = pygame.time.Clock()
        self.grid = [[BLACK for _ in range(GRID_WIDTH)] for _ in range(GRID_HEIGHT)]
        self.current_piece = Piece()
        self.next_piece = Piece()
        self.game_over = False
        self.score = 0
        self.fall_time = 0
        self.fall_speed = 500
        self.font = pygame.font.Font(None, 36)

        # --- Cargar imágenes ---
        self.images = {
            ORANGE: pygame.image.load("assets/bloque_orange.png").convert_alpha(),
            PURPLE: pygame.image.load("assets/bloque_purple.png").convert_alpha(),
            YELLOW: pygame.image.load("assets/bloque_yellow.png").convert_alpha(),
            BLUE: pygame.image.load("assets/bloque_blue.png").convert_alpha(),
            CYAN: pygame.image.load("assets/bloque_cyan.png").convert_alpha(),
            RED: pygame.image.load("assets/bloque_red.png").convert_alpha(),
            GREEN: pygame.image.load("assets/bloque_green.png").convert_alpha()
        }

        # Escalar todas las imágenes al tamaño del bloque
        for key in self.images:
            self.images[key] = pygame.transform.scale(self.images[key], (BLOCK_SIZE, BLOCK_SIZE))

    def valid_move(self, piece, x, y):
        for i in range(len(piece.shape)):
            for j in range(len(piece.shape[i])):
                if piece.shape[i][j]:
                    if (x+j < 0 or x+j >= GRID_WIDTH or
                        y+i >= GRID_HEIGHT or
                        (y+i >=0 and self.grid[y+i][x+j] != BLACK)):
                        return False
        return True

    def lock_piece(self):
        for i in range(len(self.current_piece.shape)):
            for j in range(len(self.current_piece.shape[i])):
                if self.current_piece.shape[i][j]:
                    if self.current_piece.y + i < 0:
                        self.game_over = True
                        return
                    self.grid[self.current_piece.y + i][self.current_piece.x + j] = self.current_piece.color
        self.clear_lines()
        self.current_piece = self.next_piece
        self.next_piece = Piece()
        if not self.valid_move(self.current_piece, self.current_piece.x, self.current_piece.y):
            self.game_over = True

    def clear_lines(self):
        new_grid = []
        lines_cleared = 0
        for row in self.grid:
            if all(cell != BLACK for cell in row):
                lines_cleared += 1
            else:
                new_grid.append(row)
        for _ in range(lines_cleared):
            new_grid.insert(0, [BLACK for _ in range(GRID_WIDTH)])
        self.grid = new_grid
        self.score += lines_cleared * 100

    def draw_grid(self):
        self.screen.fill(BLACK)

        # Dibujar tablero con imágenes
        for i in range(GRID_HEIGHT):
            for j in range(GRID_WIDTH):
                color = self.grid[i][j]
                if color != BLACK:
                    self.screen.blit(self.images[color], (j * BLOCK_SIZE, i * BLOCK_SIZE))
                pygame.draw.rect(self.screen, GRAY, (j*BLOCK_SIZE, i*BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE), 1)

        # Dibujar pieza actual
        for i in range(len(self.current_piece.shape)):
            for j in range(len(self.current_piece.shape[i])):
                if self.current_piece.shape[i][j]:
                    color = self.current_piece.color
                    self.screen.blit(self.images[color], ((self.current_piece.x+j)*BLOCK_SIZE, (self.current_piece.y+i)*BLOCK_SIZE))

        # Dibujar siguiente pieza
        next_text = self.font.render("Siguiente", True, WHITE)
        self.screen.blit(next_text, (GRID_WIDTH*BLOCK_SIZE + 20, 20))
        for i in range(len(self.next_piece.shape)):
            for j in range(len(self.next_piece.shape[i])):
                if self.next_piece.shape[i][j]:
                    color = self.next_piece.color
                    self.screen.blit(self.images[color],
                                     (GRID_WIDTH*BLOCK_SIZE + 20 + j*BLOCK_SIZE, 80 + i*BLOCK_SIZE))

        # Puntaje
        score_text = self.font.render(f"Puntaje: {self.score}", True, WHITE)
        self.screen.blit(score_text, (GRID_WIDTH*BLOCK_SIZE + 20, 200))

    def show_game_over(self):
        dark_surface = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
        dark_surface.fill(BLACK)
        dark_surface.set_alpha(180)
        self.screen.blit(dark_surface, (0,0))
        texts = [
            self.font.render("JUEGO TERMINADO", True, WHITE),
            self.font.render(f"Puntaje final: {self.score}", True, WHITE),
            self.font.render("Presiona X para salir", True, WHITE)
        ]
        text_y = SCREEN_HEIGHT//2 - 60
        for text in texts:
            text_x = SCREEN_WIDTH//2 - text.get_width()//2
            self.screen.blit(text, (text_x, text_y))
            text_y += 40
        pygame.display.flip()

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN and event.key == pygame.K_x:
                    pygame.quit()
                    sys.exit()
            self.clock.tick(15)

    def run(self):
        while not self.game_over:
            dt = self.clock.tick(60)
            self.fall_time += dt

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT and self.valid_move(self.current_piece, self.current_piece.x-1, self.current_piece.y):
                        self.current_piece.x -= 1
                    elif event.key == pygame.K_RIGHT and self.valid_move(self.current_piece, self.current_piece.x+1, self.current_piece.y):
                        self.current_piece.x += 1
                    elif event.key == pygame.K_DOWN and self.valid_move(self.current_piece, self.current_piece.x, self.current_piece.y+1):
                        self.current_piece.y += 1
                    elif event.key == pygame.K_UP:
                        original = [row[:] for row in self.current_piece.shape]
                        self.current_piece.rotate()
                        if not self.valid_move(self.current_piece, self.current_piece.x, self.current_piece.y):
                            self.current_piece.shape = original

            if self.fall_time >= self.fall_speed:
                if self.valid_move(self.current_piece, self.current_piece.x, self.current_piece.y+1):
                    self.current_piece.y += 1
                else:
                    self.lock_piece()
                self.fall_time = 0

            self.draw_grid()
            pygame.display.flip()

            if self.score >= 1000:
                pygame.quit()
                sys.exit()
        self.show_game_over()

if __name__ == "__main__":
    TetrisGame().run()
