
import random   #For generating random numbers
import sys   #use sys.exit to exit the game
import pygame
from pygame.locals import *   #Basic pygame import

#Global variables for the game

FPS = 30
SCREENWIDTH = 289
SCREENHEIGHT = 511
SCREEN = pygame.display.set_mode((SCREENWIDTH,SCREENHEIGHT))
GROUNDY = int(SCREENHEIGHT * 0.8)
GAME_SPRITES = {}
GAME_SOUNDS = {}
PLAYER = 'Galleries/sprites/bird.png'
BACKGROUND = 'Galleries/sprites/background.png'
PIPE = 'Galleries/sprites/pipe.png'

def welcomescreen():

    # Show welcome images on the screen
    playerx = int(SCREENWIDTH/5)
    playery = int((SCREENHEIGHT-GAME_SPRITES['player'].get_height())/2)
    messagex = int((SCREENWIDTH-GAME_SPRITES['message'].get_width())/2)
    messagey = int(SCREENHEIGHT*0.13)
    basex = 0
    while True:
        for event in pygame.event.get():
            # if user click on cross button close the game
            if event.type == QUIT or (event.type==KEYDOWN and event.key==K_ESCAPE):
                pygame.quit()
                sys.exit()
            elif event.type==KEYDOWN and (event.key==K_UP or event.key==K_SPACE):
                return
            else:
                SCREEN.blit(GAME_SPRITES['background'],(0,0))
                SCREEN.blit(GAME_SPRITES['player'],(playerx,playery))
                SCREEN.blit(GAME_SPRITES['message'],(messagex,messagey))
                SCREEN.blit(GAME_SPRITES['base'],(basex,GROUNDY))
                pygame.display.update()
                FPSCLOCK.tick(FPS)
def maingame():
    score = 0
    playerx = int(SCREENWIDTH/5)
    playery = int(SCREENHEIGHT/2)
    basex = 0
    # Create two pipes for blitting on the screen
    newpipe1 = getrandompipe()
    newpipe2 = getrandompipe()
    #My list of upper pipes
    upperpipe = [
        {"x":SCREENWIDTH+200,"y":newpipe1[0]['y']},
        {"x":SCREENWIDTH+200+int(SCREENWIDTH/2),"y":newpipe2[0]['y']}
    ]
    #My list of lower pipes
    lowerpipe = [
        {"x":SCREENWIDTH+200,"y":newpipe1[1]['y']},
        {"x":SCREENWIDTH+200+int(SCREENWIDTH/2),"y":newpipe2[1]['y']}
    ]
    pipevelx = -4
    playervely = -9
    playermaxvely = 10
    playerminvely = -8
    playeraccy = 1

    playerFlapaccv = -8 #velocity while flapping
    playerflapped = False  # It is true only when the bird is flapping

    while True:
        for event in pygame.event.get():
            if event.type==QUIT or (event.type==KEYDOWN and event.key==K_ESCAPE):
                pygame.quit()
                sys.exit()
            if event.type==KEYDOWN and (event.key==K_SPACE or event.key==K_UP):
                if playery>0:
                    playervely = playerFlapaccv
                    playerflapped = True
                    GAME_SOUNDS['wing'].play()
        # This function will return true if the player is crashed
        crashtest = isCollide(playerx,playery,upperpipe,lowerpipe)
        if crashtest:
           return
        playermidpos = playerx + int(GAME_SPRITES['player'].get_width())
        for pipe in upperpipe:
            pipemidpos = pipe['x'] + int(GAME_SPRITES['pipe'][0].get_width()/2)
            if pipemidpos<=playermidpos < pipemidpos+4:
                score+=1
                print(f"Your score is {score}")
                GAME_SOUNDS['point'].play()
        if playervely < playermaxvely and not playerflapped:
            playervely += playeraccy
        if playerflapped:
            playerflapped = False
        playerheight = GAME_SPRITES['player'].get_height()
        playery = playery + min(playervely,GROUNDY-playery-playerheight)

        # Move pipes to the left
        for up,lp in zip(upperpipe,lowerpipe):
            up['x'] += pipevelx
            lp['x'] += pipevelx


        # Add a new pipe when the first is about to cross the leftmost part of the screen
        if 0<upperpipe[0]['x']<5:
            newpipe = getrandompipe()
            upperpipe.append(newpipe[0])
            lowerpipe.append(newpipe[1])

        # If the pipe is out of the screen,remove it
        if upperpipe[0]['x'] < -GAME_SPRITES['pipe'][0].get_width():
            upperpipe.pop(0)
            lowerpipe.pop(0)
        SCREEN.blit(GAME_SPRITES['background'],(0,0))
        for up,lp in zip(upperpipe,lowerpipe):
            SCREEN.blit(GAME_SPRITES['pipe'][0],(up['x'],up['y']))
            SCREEN.blit(GAME_SPRITES['pipe'][1],(lp['x'],lp['y']))
        SCREEN.blit(GAME_SPRITES['base'],(basex,GROUNDY))
        SCREEN.blit(GAME_SPRITES['player'],(playerx,playery))

        mydigits = [int(x) for x in list(str(score))]
        width = 0
        for digit in mydigits:
            width += GAME_SPRITES['numbers'][digit].get_width()
        xoffset = int((SCREENWIDTH - width)/2)

        for digit in mydigits:
            SCREEN.blit(GAME_SPRITES['numbers'][digit],(xoffset,int(SCREENHEIGHT*0.12)))
            xoffset += GAME_SPRITES['numbers'][digit].get_width()

        pygame.display.update()
        FPSCLOCK.tick(FPS)


def isCollide(playerx,playery,upperpipe,lowerpipe):

    if playery > GROUNDY - 25 or playery<0:
        GAME_SOUNDS['hit'].play()
        return True

    for pipe in upperpipe:
        pipeheight = GAME_SPRITES['pipe'][0].get_height()
        if (playery < pipeheight+pipe['y'] and abs(playerx-pipe['x']) < GAME_SPRITES['pipe'][0].get_width()):
            GAME_SOUNDS['hit'].play()
            return True
    for pipe in lowerpipe:
        if(playery + GAME_SPRITES['player'].get_height() > pipe['y'] and abs(playerx - pipe['x']) < GAME_SPRITES['pipe'][0].get_width()):
            GAME_SOUNDS['hit'].play()
            return True
    return False



def getrandompipe():
    '''
    Generates the position of two pipes for blitting on the screen
    '''
    pipeheight = GAME_SPRITES['pipe'][0].get_height()
    offset = int(SCREENHEIGHT/3)
    y2 = offset+random.randrange(0,int(SCREENHEIGHT-GAME_SPRITES['base'].get_height()-1.2*offset))
    pipex = SCREENWIDTH+10
    y1 = pipeheight-y2+offset
    pipe = [
        {"x":pipex,"y":-y1}, #Upper pipe
        {"x":pipex,"y":y2}  #Lower pipe
    ]
    return pipe
if __name__ == '__main__':
    # This is the main point where the game will start
    pygame.init()
    FPSCLOCK = pygame.time.Clock()
    pygame.display.set_caption("Flappy Bird game by Tahmid")
    GAME_SPRITES['numbers'] = (
        pygame.image.load('Galleries/sprites/0.png').convert_alpha(),
        pygame.image.load('Galleries/sprites/1.png').convert_alpha(),
        pygame.image.load('Galleries/sprites/2.png').convert_alpha(),
        pygame.image.load('Galleries/sprites/3.png').convert_alpha(),
        pygame.image.load('Galleries/sprites/4.png').convert_alpha(),
        pygame.image.load('Galleries/sprites/5.png').convert_alpha(),
        pygame.image.load('Galleries/sprites/6.png').convert_alpha(),
        pygame.image.load('Galleries/sprites/7.png').convert_alpha(),
        pygame.image.load('Galleries/sprites/8.png').convert_alpha(),
        pygame.image.load('Galleries/sprites/9.png').convert_alpha()

    )
    GAME_SPRITES['message'] = pygame.image.load('Galleries/sprites/message.png').convert_alpha()
    GAME_SPRITES['base'] = pygame.image.load('Galleries/sprites/base.png').convert_alpha()
    GAME_SPRITES['pipe'] = (
        pygame.transform.rotate(pygame.image.load(PIPE).convert_alpha(),180),  #Upper pipe
        pygame.image.load(PIPE).convert_alpha()   # Lower pipe

    )
    GAME_SPRITES['player'] = pygame.image.load(PLAYER).convert_alpha()
    GAME_SPRITES['background'] = pygame.image.load(BACKGROUND).convert()

    #Game Sounds
    GAME_SOUNDS['die'] = pygame.mixer.Sound('Galleries/audio/die.wav')
    GAME_SOUNDS['hit'] = pygame.mixer.Sound('Galleries/audio/hit.wav')
    GAME_SOUNDS['point'] = pygame.mixer.Sound('Galleries/audio/point.wav')
    GAME_SOUNDS['swoosh'] = pygame.mixer.Sound('Galleries/audio/swoosh.wav')
    GAME_SOUNDS['wing'] = pygame.mixer.Sound('Galleries/audio/wing.wav')

    while True:
        welcomescreen() # this is a welcome screen and this will show untill player press a button
        maingame()


