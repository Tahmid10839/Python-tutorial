import pygame
pygame.init()

# Create window
gameWindow = pygame.display.set_mode((1200,720))
pygame.display.set_caption("Tahmid")

# Game Specific Variables
exit_game = False
game_over = False

# Creating game loop
while not exit_game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit_game = True

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                print("You have presssed the right key")

pygame.quit()
quit()
