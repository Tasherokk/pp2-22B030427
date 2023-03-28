import pygame
import datetime

pygame.init()
surface = pygame.Surface((100, 100))
screen = pygame.display.set_mode((700, 500))
done = False

clock = pygame.time.Clock()
image = pygame.image.load('mickeyclock.jpg')
image = pygame.transform.scale(image, (700, 500))


while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:            
            done = True

    
    left_hand = pygame.image.load('lefthand.png')
    right_hand = pygame.image.load('righthand.png')
    t = datetime.datetime.now()
    angle1 = -t.second * 6
    angle2 = -t.minute * 6 - t.second / 10 
    
    #left_hand = pygame.transform.scale(left_hand, (300, 300))

##    pos = (left_hand.get_width() / 2, left_hand.get_height() / 2)
##    origin_pos = (image.get_width() / 2, image.get_height() / 2)
##    image_rect = left_hand.get_rect(topleft = (origin_pos[0] - pos[0], origin_pos[1] - pos[1]))
##    offset_center_to_pivot = image_rect.center - pygame.math.Vector2(pos)
##    rotated_offset = offset_center_to_pivot.rotate(angle1)
##    rotated_image_center = (pos[0] + rotated_offset.x, pos[1] + rotated_offset.y)
##    left_hand = pygame.transform.rotate(left_hand, angle1)
##    rotated_image_rect = left_hand.get_rect(center = rotated_image_center)

    left_hand = pygame.transform.rotate(left_hand, angle1)
    right_hand = pygame.transform.rotate(right_hand, angle2)
    pos1 = (left_hand.get_width() / 2, left_hand.get_height() / 2)
    pos2 = (right_hand.get_width() / 2, right_hand.get_height() / 2)
    origin_pos = (image.get_width() / 2, image.get_height() / 2)

    
    screen.fill((255, 255, 255))
    screen.blit(image, (0, 0))
    screen.blit(left_hand, (origin_pos[0] - pos1[0], origin_pos[1] - pos1[1]))
    screen.blit(right_hand, (origin_pos[0] - pos2[0], origin_pos[1] - pos2[1]))
    pygame.display.flip()
    

    
    clock.tick(1)
pygame.quit()


#left_hand.get_width(), left_hand.get_height()
