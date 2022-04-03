import pygame
import os 

pygame.init() 

clock = pygame.time.Clock()

screen_width = 680 #가로크기
screen_height = 480 #세로 크기
screen = pygame.display.set_mode((screen_width, screen_height))

pygame.display.set_caption('Bubble Bobble')

character = pygame.image.load('C:\\Users\\WINDOWS10\\Desktop\\python_projects\\pygame\\bubble bobble\\character.png')
character_size = character.get_rect().size
character_width  = character_size[0]
character_height = character_size[1]
character_x_pos = (screen_width/2)- (character_width/2)
character_y_pos = screen_height - character_height 

character_to_y = 0
character_to_x = 0
character_speed = 5


running = True
while running :
    dt = clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT : #창이 닫히는 이벤트가 발생하였는가?
            running = False # 게임이 진행중이 아님
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                character_to_x -= character_speed
            elif event.key == pygame.K_RIGHT:
                character_to_x += character_speed
            


        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                character_to_x = 0

    character_x_pos += character_to_x 

    if character_x_pos <=0:
        character_x_pos=0
    elif character_x_pos >= screen_width-character_width:
        character_x_pos = screen_width-character_width

    screen.fill((0,0,0))
    screen.blit(character, (character_x_pos,character_y_pos))


    pygame.display.update()


pygame.quit()