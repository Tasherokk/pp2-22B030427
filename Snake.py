import pygame
from pygame.locals import *
import random, time
pygame.init()

path = "C:\\Users\\Nitro\\Desktop\\PP2\\lab8\\"
BLUE  = (0, 0, 255)
RED   = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

SCREEN_WIDTH = 400
SCREEN_HEIGHT = 400
SPEED1 = 2
SPEED2 = 2
SPEED = 5
SCORE = 0
LEVEL = 1
BLOCK = 10
SNAKE_LENGHT = 1
snake_list = []
DIRECTION = "right"

#Setting up Fonts
font = pygame.font.SysFont("Verdana", 60)
font_small = pygame.font.SysFont("Verdana", 20)
GAME_OVER = font.render("Game Over", True, BLACK)

FPS = pygame.time.Clock()
DISPLAY = pygame.display.set_mode((400, 400))
DISPLAY.fill(BLUE)
pygame.display.set_caption("Snake")

###
class Snake_Head(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.rect = pygame.Rect(280, 280, BLOCK, BLOCK)

    def move(self):
        if DIRECTION == "right":
            self.rect.move_ip(BLOCK, 0)
        if DIRECTION == "left":
            self.rect.move_ip(-BLOCK, 0)
        if DIRECTION == "up":
            self.rect.move_ip(0, -BLOCK)
        if DIRECTION == "down":
            self.rect.move_ip(0, BLOCK)

        #cheking boundaries
        if self.rect[0] < 0: self.rect[0] = 390
        if self.rect[0] >= 400: self.rect[0] = 0
        if self.rect[1] < 0: self.rect[1] = 390
        if self.rect[1] >= 400: self.rect[1] = 0

    def draw(self):
        pygame.draw.rect(DISPLAY, GREEN, self.rect)
        
###
class Food(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.rect = pygame.Rect(random.randint(0, 39) * 10, random.randint(0, 39) * 10, BLOCK, BLOCK)

    def draw(self):
        pygame.draw.rect(DISPLAY, RED, self.rect)

###
def Draw():
    for snake in snake_list:
        pygame.draw.rect(DISPLAY, GREEN, snake)

###
#Setting up Sprites
S1 = Snake_Head()
F1 = Food()

#Creating Sprites Groups
all_sprites = pygame.sprite.Group()
all_sprites.add(F1)
all_sprites.add(S1)



while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT and DIRECTION != "left":
                DIRECTION = "right"
            if event.key == pygame.K_LEFT and DIRECTION != "right":
                DIRECTION = "left"
            if event.key == pygame.K_DOWN and DIRECTION != "up":
                DIRECTION = "down"
            if event.key == pygame.K_UP and DIRECTION != "down":
                DIRECTION = "up"

    
    
    DISPLAY.fill(BLUE)
    SCORES = font_small.render("Score: " + str(SCORE), True, BLACK)
    LEVELS = font_small.render("Level: " + str(LEVEL), True, BLACK)
    DISPLAY.blit(SCORES, (10, 10))
    DISPLAY.blit(LEVELS, (300, 10))

    #Increasing Level
    LEVEL = int(1 + SCORE / 4)
    SPEED2 = SPEED1 * LEVEL 


    #old positions of head and tail
    (x1, y1) = S1.rect.topleft
    if len(snake_list) > 0: last = snake_list[len(snake_list) - 1]

    #Moving Snake
    S1.move()

    #Update positions of blocks of snake
    for i in range(len(snake_list) - 1, 0, -1):
        snake_list[i] = snake_list[i - 1]
    if len(snake_list) > 0:
        snake_list[0] = (x1, y1, BLOCK, BLOCK)

    #Cheking collide between Head and Tail
    for tail in snake_list:
        if tail == S1.rect:
            DISPLAY.fill(RED)
            DISPLAY.blit(GAME_OVER, ((400 - GAME_OVER.get_width()) / 2, (400 - GAME_OVER.get_height()) / 2))
            pygame.display.update()
            time.sleep(3)
            pygame.quit()
            exit()
            

    #To be run if collision occurs between Player and Food
    if pygame.sprite.collide_rect(S1, F1):
        SCORE += 1
        if len(snake_list) > 0:
            snake_list.append(last)
        else:
            snake_list.append((x1, y1, BLOCK, BLOCK))
        
        F1.rect = pygame.Rect(random.randint(0, 39) * 10, random.randint(0, 39) * 10, BLOCK, BLOCK)
        while pygame.sprite.collide_rect(S1, F1):
            F1.rect = pygame.Rect(random.randint(0, 39) * 10, random.randint(0, 39) * 10, BLOCK, BLOCK)

    #print(snake_list)
    
    #Re-draws all Sprites
    for entity in all_sprites:
        entity.draw()
    Draw()
    
    

        
    pygame.display.update()
    FPS.tick(SPEED + SPEED2)
