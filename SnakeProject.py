import pygame
import time
import random

snakeSpeed = 24

# Size of window
width = 720
height = 480

# Colors
black = pygame.Color(0, 0, 0)
white = pygame.Color(255, 255, 255)
red = pygame.Color(255, 0, 0)
green = pygame.Color(0, 255, 0)
blue = pygame.Color(0, 0, 255)

# Initializing
pygame.init()

# Game window
pygame.display.set_caption("Snake Project")
window = pygame.display.set_mode((width, height))

# fps
FPS = pygame.time.Clock()

# Default snake position
snakePOS = [100, 50]

# Block of snake body
snakeBody = [[100, 50], [90, 50], [80, 50], [70, 50]]

fruitPOS = [random.randrange(1, (width // 10 )) * 10, random.randrange(1, height // 10) * 10]

spawn = True

direction = 'RIGHT'
changeTo = direction

score = 0 # Initial score

def showScore(choice, color, font, size):
    scoreFont = pygame.font.SysFont(font, size)
    scoreSurface = scoreFont.render('Score:' + str(score), True, color)
    scoreRect = scoreSurface.get_rect()
    window.blit(scoreSurface, scoreRect)

def gameOver():
    font = pygame.font.SysFont('times new roman', 50)

    #Surface for gamveover
    gameOverSurface = font.render('Score is:' + str(score), True, red)
    gameOverRect = gameOverSurface.get_rect()
    gameOverRect.midtop = (width / 2, height / 4)

    window.blit(gameOverSurface, gameOverRect)
    pygame.display.flip()

    time.sleep(2)
    pygame.quit()

    quit()

# Main code
while True:

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                changeTo = 'UP'
            if event.key == pygame.K_DOWN:
                changeTo = 'DOWN'
            if event.key == pygame.K_LEFT:
                changeTo = 'LEFT'
            if event.key == pygame.K_RIGHT:
                changeTo = 'RIGHT'

    if changeTo == 'UP' and direction != 'DOWN':
        direction = 'UP'
    if changeTo == 'DOWN' and direction != 'UP':
        direction = 'DOWN'
    if changeTo == 'LEFT' and direction != 'RIGHT':
        direction = 'LEFT'
    if changeTo == 'RIGHT' and direction != 'LEFT':
        direction = 'RIGHT'

    if direction == 'UP':
        snakePOS[1] -= 10
    if direction == 'DOWN':
        snakePOS[1] += 10
    if direction == 'LEFT':
        snakePOS[0] -= 10
    if direction == 'RIGHT':
        snakePOS[0] += 10

    snakeBody.insert(0, list(snakePOS))
    if snakePOS[0] == fruitPOS[0] and snakePOS[1] == fruitPOS[1]:
        score += 10
        spawn = False
    else:
        snakeBody.pop()

    if not spawn:
        fruitPOS = [random.randrange(1, (width // 10)) * 10, random.randrange(1, (height // 10)) * 10]

    spawn = True
    window.fill(black)

    for pos in snakeBody:
        pygame.draw.rect(window, green, pygame.Rect(pos[0], pos[1], 10, 10))

        pygame.draw.rect(window, white, pygame.Rect(fruitPOS[0], fruitPOS[1], 10, 10))

    if snakePOS[0] < 0 or snakePOS[0] > width - 10:
        gameOver()
    if snakePOS[1] < 0 or snakePOS[1] > height - 10:
        gameOver()

    for block in snakeBody[1:]:
        if snakePOS [0] == block[0] and snakePOS[1] == block[1]:
            gameOver()

    showScore(1, white, 'times new roman', 20)

    pygame.display.update()
    FPS.tick(snakeSpeed)