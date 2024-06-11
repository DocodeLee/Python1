import pygame
import sys

from random import randint
random_number1 = randint(1,14)
random_number2 = randint(1,14)

pygame.init()

width, height = 800, 600
screen = pygame.display.set_mode((width,height))
pygame.display.set_caption("Start grid")

star_image = pygame.image.load("images/star-158502_1280.webp")
star_image = pygame.transform.scale(star_image,(50,50))
grid_width, grid_height = random_number1, random_number2
spacing = 50
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    screen.fill((13,20,13))
    
    for row in range(grid_height):
        for col in range(grid_width):
            x = col * spacing
            y = row * spacing
            screen.blit(star_image,(x,y))
    pygame.display.flip()