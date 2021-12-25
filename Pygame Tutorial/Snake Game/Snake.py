import pygame
import random


pygame.init()
pygame.mixer.init()

# Colors
white = (255,255,255)
red = (255,0,0)
black = (0,0,0)

# Creating window
screen_width = 900
screen_height = 600
gameWindow = pygame.display.set_mode((screen_width,screen_height))

# Background Image
bgimg = pygame.image.load("image/bg2.jpg")
bgimg = pygame.transform.scale(bgimg,(screen_width,screen_height)).convert_alpha()
intro = pygame.image.load("image/intro.png")
intro = pygame.transform.scale(intro,(screen_width,screen_height)).convert_alpha()
outro = pygame.image.load("image/outro.png")
outro = pygame.transform.scale(outro,(screen_width,screen_height)).convert_alpha()

# Game Title
pygame.display.set_caption("Snake Game")
pygame.display.update()



clock = pygame.time.Clock()
font = pygame.font.SysFont(None,30)    # (style,size)


def text_screen(text,color,x,y):
    screen_text = font.render(text,True,color)
    gameWindow.blit(screen_text,[x,y])

def plot_snake(gameWindow,color,snk_list,snake_size):
    for x,y in snk_list:
        pygame.draw.rect(gameWindow, color, [x, y, snake_size, snake_size])

def welcome():
    exit_game = False
    while not exit_game:
        gameWindow.fill((233,210,229))
        gameWindow.blit(intro,(0,0))
        #text_screen("Welcome to Snake Game",black,300,250)
        #text_screen("Press Enter to start the game",black,290,290)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit_game = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    gameloop()
        pygame.display.update()
        clock.tick(30)

# Game loop
def gameloop():
    # Game Specific Variables
    exit_game = False
    game_over = False
    snake_x = 45
    snake_y = 55
    snake_size = 10
    velocity_x = 0
    velocity_y = 0
    pygame.mixer.music.load('music/bgm.mp3')
    pygame.mixer.music.play()
    with open("highscore.txt", "r") as f:
        highscore = f.read()
    food_x = random.randint(20, screen_width / 2)
    food_y = random.randint(20, screen_height / 2)
    score = 0
    fps = 30

    snk_list = []
    snk_length = 1
    while not exit_game:
        if game_over:
            with open("highscore.txt","w") as f:
                f.write(str(highscore))
            gameWindow.fill(white)
            gameWindow.blit(outro,(0,0))
            text_screen("Score: " + str(score) + "      High Score: "+str(highscore), red, 320, 350)
            #text_screen("Game Over! Press enter to continue",red,260,250)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        gameloop()
        else:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        velocity_x = 3
                        velocity_y = 0
                    if event.key == pygame.K_LEFT:
                        velocity_x = -3
                        velocity_y = 0
                    if event.key == pygame.K_UP:
                        velocity_y = -3
                        velocity_x = 0
                    if event.key == pygame.K_DOWN:
                        velocity_y = 3
                        velocity_x = 0
                    # Cheat Codes
                    if event.key == pygame.K_q:
                        score +=10
            snake_x += velocity_x
            snake_y += velocity_y

            if abs(snake_x-food_x)<11 and abs(snake_y-food_y)<11:
                score += 10
                food_x = random.randint(20, screen_width / 2)
                food_y = random.randint(20, screen_height / 2)
                snk_length += 5
            if score > int(highscore):
                highscore = score
            gameWindow.fill(white)
            gameWindow.blit(bgimg,(0,0))
            text_screen("Score: " + str(score) + "      High Score: "+ str(highscore), red, 5, 5)
            pygame.draw.circle(gameWindow, red, [food_x, food_y],6)

            head = []
            head.append(snake_x)
            head.append(snake_y)
            snk_list.append(head)

            if len(snk_list) > snk_length:
                del snk_list[0]

            if head in snk_list[:-1]:
                game_over = True
                pygame.mixer.music.load('music/gameover.mp3')
                pygame.mixer.music.play()

            if snake_x<0 or snake_x>screen_width or snake_y<0 or snake_y>screen_height:
                game_over = True
                pygame.mixer.music.load('music/gameover.mp3')
                pygame.mixer.music.play()

            plot_snake(gameWindow,black,snk_list,snake_size)
        pygame.display.update()
        clock.tick(fps)

    pygame.quit()
    quit()

welcome()

