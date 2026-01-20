import pygame
import random
import sys

pygame.init()
WIDTH, HEIGHT = 800,600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Matriix Digital Rain")
clock = pygame.time.Clock()

FONT_SIZE = 20
COLUMNS = WIDTH // FONT_SIZE
font = pygame.font.Font(None, FONT_SIZE)

CHARS = "ﾊﾐﾋｰｳｼﾅﾓﾆｻﾜﾂｵﾘｱﾎﾃﾏｹﾒｴｶｷﾑﾕﾗｾﾈｽﾀﾇﾍ012345789Z:・.\"=*+-<>¦｜çﾘｸ"

class Stream:
    def __init__(self, x):
        self.x = x
        self.y = random.randint(-50, 0)
        self.speed = random.uniform(3,8)
        self.chars = [random.choice(CHARS) for _ in range(20)]
    def update(self):
        self.y += self.speed
        if self.y > HEIGHT:
            self.y = random.randint(-50, 0)
            self.speed = random.uniform(3,8)
    def draw(self, screen):
        for i, char in enumerate(self.chars):
            y_pos = self.y + (1*FONT_SIZE)
            if 0 <= y_pos < HEIGHT:
                alpha = max(0, 255 -(i *12))
                color = (0, alpha, 0)
                if i == 0:
                    color = (200, 255, 200)
                text = font.render(char, True, color)
                screen.blit(text, (self.x * FONT_SIZE, y_pos))

streams = [Stream(i) for i in range(COLUMNS)]
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    s= pygame.Surface((WIDTH, HEIGHT))
    s.set_alpha(25)
    s.fill((0,0,0))
    screen.blit(s, (0,0))

    for stream in streams:
        stream.update()
        stream.draw(screen)

    pygame.display.flip()
    clock.tick(30)
pygame.quit()
sys.exit()