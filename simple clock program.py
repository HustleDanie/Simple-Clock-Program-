import pygame
import time

pygame.init()

white = (255, 255, 255)
black = (0, 0, 0)

screen = pygame.display.set_mode((300, 300))
pygame.display.set_caption("Clock")

clock = pygame.time.Clock()

font = pygame.font.Font(None, 30)

def display_time(screen, font, x, y):
    current_time = time.strftime("%H:%M:%S")
    text = font.render(current_time, True, white)
    screen.blit(text, [x, y])

game_over = False
while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True

    screen.fill(black)
    display_time(screen, font, 100, 100)

    pygame.display.update()
    clock.tick(60)

pygame.quit()

