import pygame
import psycopg2
from pygame.locals import *
import random, time


###
def connect(conn):
    #Connect to the PosgreSQL server
    try:
        conn = psycopg2.connect(
            host = "localhost",
            database = "postgres",
            user = "postgres",
            password = "Taukent2004",
            port = "5432")
        
        #create a cursor
        cur = conn.cursor()

        #execute a statement
        cur.execute('SELECT version()')

        #display the PostgreSQL database server version
        db_version = cur.fetchone()
        print(db_version)

        #Close the communication with the PostgreSQL
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            return conn
###
        
def createTable(cursor):
    #Create table in PostgreSQL database if such table not exists
    query = """
        CREATE TABLE IF NOT EXISTS postgres.snake.snake(
            "user" VARCHAR(255),
            "level" integer,
            "user_score" integer,
            "total_score" integer
        )
        """
    cursor.execute(query)
    conn.commit()
    
###

def insertData(cursor, user, level, user_score, total_score):
    #Insert data to our table snake
    cursor.execute(f"""SELECT "user"
        FROM postgres.snake.snake
        WHERE "user" = '{user}';
        """)
    row = cursor.fetchone()
    query = f"""
        INSERT INTO postgres.snake.snake("user", "level", "user_score", "total_score")
        VALUES('{user}', {level}, {user_score}, {total_score})
        ON CONFLICT DO NOTHING
        """

    if row == None:
        cursor.execute(query)
        conn.commit()
        return True

    else:
        return False
    

###

def updateData(cursor, user, level, user_score, total_score):
    #updating data by user
    query = f"""
            UPDATE postgres.snake.snake
            SET "level" = {level},
                "user_score" = {user_score},
                "total_score" = {total_score}
            WHERE "user" = '{user}';
            """
    cursor.execute(query)
    conn.commit()

###

def showLevel(cursor, user):
    query = f"""
        SELECT level
        FROM postgres.snake.snake
        WHERE "user" = '{user}'
        """
    cursor.execute(query)
    row = cursor.fetchone()
    conn.commit()
    return row

###

def showScore(cursor, user):
    query = f"""
        SELECT user_score
        FROM postgres.snake.snake
        WHERE "user" = '{user}'
        """
    cursor.execute(query)
    row = cursor.fetchone()
    conn.commit()
    return row


###

def showTotalScore(cursor, user):
    query = f"""
        SELECT total_score
        FROM postgres.snake.snake
        WHERE "user" = '{user}'
        """
    cursor.execute(query)
    row = cursor.fetchone()
    conn.commit()
    return row


###
        
conn = None
cursor = None
#connecting
conn = connect(conn)
cursor = conn.cursor()

#creating table
createTable(cursor)





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



#Asking for username
print("Please enter your name:")
name = input()
new = insertData(cursor, name, 1, 0, 0)
level = showLevel(cursor, name)
level = level[0]
LEVEL = level

user_score = showScore(cursor, name)
user_score = user_score[0]
SCORE = user_score

#if new player
if new:
    START = font_small.render("Good luck newbie!", True, BLACK)
    DISPLAY.blit(START, ((400 - START.get_width()) / 2, (400 - START.get_height()) / 2))
    pygame.display.update()
    time.sleep(2)

#if old player
else:
    START = font_small.render("Welcome back!", True, BLACK)
    DISPLAY.blit(START, ((400 - START.get_width()) / 2, (400 - START.get_height()) / 2))
    pygame.display.update()
    time.sleep(2)
    DISPLAY.fill(BLUE)
    START = font_small.render(f"Starting Game by your level {level}", True, BLACK)
    DISPLAY.blit(START, ((400 - START.get_width()) / 2, (400 - START.get_height()) / 2))
    pygame.display.update()
    time.sleep(3)


###

def UPD(startinglevel, score, earnedscores):
    #getting global score and updaiting table

    total_score = showTotalScore(cursor, name)
    total_score = total_score[0]
    updateData(cursor, name, startinglevel, score, total_score + earnedscores)

###
walls = pygame.sprite.Group()

class Wall(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.rect = None

    def draw(self):
        pygame.draw.rect(DISPLAY, BLACK, self.rect)
###

def loadLevel(level):
    #updaiting walls
    for wall in walls:
        wall.kill()
    #updaiting snake
    snake_list.clear()
    S1.rect = pygame.Rect(10, 10, BLOCK, BLOCK)
    global DIRECTION
    DIRECTION = "right"    


    if(level == 2 or level == 3):
        DISPLAY.fill(BLUE)
        LOAD = font_small.render("Loading next level", True, BLACK)
        DISPLAY.blit(LOAD, ((400 - LOAD.get_width()) / 2, (400 - LOAD.get_height()) / 2))
        pygame.display.update()
        time.sleep(3)

    if(level > 3):
        #update scores
        UPD(1, 0, SCORE)
        
        DISPLAY.fill(BLUE)
        CONG = font_small.render("Congratulations!", True, BLACK)
        DISPLAY.blit(CONG, ((400 - CONG.get_width()) / 2, (400 - CONG.get_height()) / 2))
        pygame.display.update()
        time.sleep(3)
        pygame.quit()
        exit()
        
    if(level == 1):
        loadLevel1()
    if(level == 2):
        loadLevel2()
    if(level == 3):
        loadLevel3()

###

def loadLevel1():
    w1 = Wall()
    w1.rect = pygame.Rect(30, 170, BLOCK * 35, BLOCK)
    walls.add(w1)
    w2 = Wall()
    w2.rect = pygame.Rect(30, 220, BLOCK * 35, BLOCK)
    walls.add(w2)

    
###

def loadLevel2():
    w1 = Wall()
    w1.rect = pygame.Rect(170, 30, BLOCK, BLOCK * 34)
    walls.add(w1)
    w2 = Wall()
    w2.rect = pygame.Rect(220, 30, BLOCK, BLOCK * 34)
    walls.add(w2)

###

def loadLevel3():
    w1 = Wall()
    w1.rect = pygame.Rect(30, 170, BLOCK * 35, BLOCK)
    walls.add(w1)
    w2 = Wall()
    w2.rect = pygame.Rect(30, 220, BLOCK * 35, BLOCK)
    walls.add(w2)
    w3 = Wall()
    w3.rect = pygame.Rect(190, 30, BLOCK * 2, BLOCK * 34)
    walls.add(w3)

###
    
def endgame():
    #update scores and starts from begining
    UPD(LEVEL, 0, SCORE)

    #end of game
    conn.commit()
    cursor.close()
    conn.close()
    DISPLAY.fill(RED)
    DISPLAY.blit(GAME_OVER, ((400 - GAME_OVER.get_width()) / 2, (400 - GAME_OVER.get_height()) / 2))
    pygame.display.update()
    time.sleep(3)
    pygame.quit()
    exit()
    

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
        if self.rect[0] < 0:
            if self.rect[1] >= 180 and self.rect[1] <= 220: self.rect[0] = 390
            else: endgame()
        if self.rect[0] >= 400:
            if self.rect[1] >= 180 and self.rect[1] <= 220: self.rect[0] = 0
            else: endgame()
        if self.rect[1] < 0:
            if self.rect[0] >= 180 and self.rect[0] <= 220: self.rect[1] = 390
            else: endgame()
        if self.rect[1] >= 400:
            if self.rect[0] >= 180 and self.rect[0] <= 220: self.rect[1] = 0
            else: endgame()
    def draw(self):
        pygame.draw.rect(DISPLAY, GREEN, self.rect)
        
###
class Food(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.upd()

    def draw(self):
        pygame.draw.rect(DISPLAY, RED, self.rect)

    def upd(self):
        self.weight = random.randint(5, 10)
        self.rect = pygame.Rect(random.randint(1, 38) * 10, random.randint(1, 38) * 10, BLOCK, BLOCK)
        while pygame.sprite.collide_rect(self, S1) or pygame.sprite.spritecollideany(self, walls):
            self.rect = pygame.Rect(random.randint(1, 38) * 10, random.randint(1, 38) * 10, BLOCK, BLOCK)
        

###
def Draw():
    for snake in snake_list:
        pygame.draw.rect(DISPLAY, GREEN, snake)

###


#Setting up Sprites
S1 = Snake_Head()
F1 = Food()

#Loading start Level
loadLevel(LEVEL)

#Creating Sprites Groups
all_sprites = pygame.sprite.Group()
all_sprites.add(F1)
all_sprites.add(S1)


#Adding new user event for food
TIME = pygame.USEREVENT + 1
pygame.time.set_timer(TIME, 1000)


while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            conn.commit()
            cursor.close()
            conn.close()
            pygame.quit()
            exit()

        #for timer
        if event.type == TIME:
            F1.weight -= 1
            if F1.weight == 0:
                F1.upd()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT and DIRECTION != "left":
                DIRECTION = "right"
            if event.key == pygame.K_LEFT and DIRECTION != "right":
                DIRECTION = "left"
            if event.key == pygame.K_DOWN and DIRECTION != "up":
                DIRECTION = "down"
            if event.key == pygame.K_UP and DIRECTION != "down":
                DIRECTION = "up"
            if event.key == K_ESCAPE:
                UPD(LEVEL, SCORE, 0)
                time.sleep(3)
                
                

    
    DISPLAY.fill(BLUE)
    pygame.draw.rect(DISPLAY, BLACK, (0, 0, 400, 400))
    pygame.draw.rect(DISPLAY, BLUE, (3, 3, 394, 394))
    pygame.draw.rect(DISPLAY, BLUE, (180, 0, 40, 3))
    pygame.draw.rect(DISPLAY, BLUE, (180, 397, 40, 3))
    pygame.draw.rect(DISPLAY, BLUE, (0, 180, 3, 40))
    pygame.draw.rect(DISPLAY, BLUE, (397, 180, 3, 40))
    SCORES = font_small.render("Score: " + str(SCORE), True, BLACK)
    LEVELS = font_small.render("Level: " + str(LEVEL), True, BLACK)
    DISPLAY.blit(SCORES, (10, 10))
    DISPLAY.blit(LEVELS, (300, 10))

    #Increasing Level
    if SCORE / 20 >= 1:
        UPD(LEVEL + 1, 0, SCORE)
        SCORE = 0
        LEVEL += 1
        SPEED2 = SPEED1 * LEVEL
        loadLevel(LEVEL)


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
            endgame()

    #Cheking collide between Head and Walls
    if pygame.sprite.spritecollideany(S1, walls):
        endgame()
            

    #To be run if collision occurs between Player and Food
    if pygame.sprite.collide_rect(S1, F1):
        SCORE += F1.weight
        if len(snake_list) > 0:
            snake_list.append(last)
        else:
            snake_list.append((x1, y1, BLOCK, BLOCK))
        
        F1.upd()

    #print(snake_list)
    
    #Re-draws all Sprites
    for entity in all_sprites:
        entity.draw()
    for entity in walls:
        entity.draw()
    Draw()
    
    

        
    pygame.display.update()
    FPS.tick(SPEED + SPEED2)




