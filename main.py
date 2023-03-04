import pygame
import sys
import menu, scene1, scene2

# Initialize Pygame
pygame.init()

# Set up the display
screen = pygame.display.set_mode((800, 600))

# Define some colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Scene is to know what scene to show
scene = 0

# Define some fonts
font = pygame.font.SysFont(None, 48)

# Define some text
text0 = font.render("Click a button to change the screen", True, BLACK)
text1 = font.render("Welcome to scene 1", True, BLACK)
text2 = font.render("Welcome to scene 2", True, WHITE)

# Define some buttons
button1 = pygame.Rect(200, 250, 150, 50)
button2 = pygame.Rect(450, 250, 150, 50)

# Define some button text
button1_text = font.render("Black", True, WHITE)
button2_text = font.render("White", True, WHITE)
button3_text = font.render("Back", True, BLACK)
button4_text = font.render("Back", True, WHITE)

# Set up the game loop
while True:

    # Handle events
    for event in pygame.event.get():
        if scene == 0:
            menu.logic(event)
        elif scene == 1:
            scene1.logic(event)
        elif scene == 2:
            scene2.logic(event)

    # Draw the menu
    if scene == 0:
        menu.graphics(scene, font)
    elif scene == 1:
        screen.fill(BLACK)
        pygame.draw.rect(screen, WHITE, button1)
        screen.blit(text1, (200, 200))
        screen.blit(button3_text, (215, 260))
    elif scene == 2:
        screen.fill(WHITE)
        pygame.draw.rect(screen, BLACK, button1)
        screen.blit(text2, (200, 200))
        screen.blit(button4_text, (215, 260))

    # Update the display
    pygame.display.flip()