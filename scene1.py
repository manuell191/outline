import pygame
import sys

button1 = pygame.Rect(200, 250, 150, 50)

def logic(event):
    if event.type == pygame.QUIT:
        pygame.quit()
        sys.exit()
    elif event.type == pygame.MOUSEBUTTONDOWN:
        # Check if a button was clicked
        if button1.collidepoint(event.pos):
            scene = 0