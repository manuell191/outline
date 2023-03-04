import pygame
import sys

button1 = pygame.Rect(200, 250, 150, 50)
button2 = pygame.Rect(450, 250, 150, 50)

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

def logic(event):
    if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    elif event.type == pygame.MOUSEBUTTONDOWN:
            # Check if a button was clicked
            if button1.collidepoint(event.pos):
                return 1
            elif button2.collidepoint(event.pos):
                return 2

def graphics(screen, font):
    text0 = font.render("Click a button to change the screen", True, BLACK)
    button1_text = font.render("Black", True, WHITE)
    button2_text = font.render("White", True, WHITE)

    screen.fill(WHITE)
    pygame.draw.rect(screen, BLACK, button1)
    pygame.draw.rect(screen, BLACK, button2)
    screen.blit(text0, (200, 200))
    screen.blit(button1_text, (215, 260))
    screen.blit(button2_text, (470, 260))