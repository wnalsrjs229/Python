import pygame
import os
#######################################################
# 기본 초기화 (반드시 필요한 것들)
pygame.init() 

#화면 크기 설정
screen_width = 680 #가로크기
screen_height = 480 #세로 크기
screen = pygame.display.set_mode((screen_width, screen_height))

#화면 타이틀 설정
pygame.display.set_caption('GAME') #게임 이름


#FPS
clock = pygame.time.Clock()
######################################################

# 1. 사용자 게임 초기화 (배경 화면, 게임 이미지, 좌표, 속도, 폰트 등)
current_path = os.path.dirname(__file__) #현재 파일의 위치 변환
image_path = os.path.join(current_path, "images") #images 폴더 위치 반환


#배경 이미지 불러오기
background = pygame.image.load(os.path.join(image_path, "background.png"))

#스테이지 만들기
stage = pygame.image.load(os.path.join(image_path, "stage.png"))
stage_size = stage.get_rect().size
stage_height = stage_size[1] #스테이지의 높이 위에 캐릭터를 두기 위해 사용


#캐릭터(스프라이트) 불러오기
character = pygame.image.load(os.path.join(image_path, "character.png"))
character_size = character.get_rect().size
character_width  = character_size[0]
character_height = character_size[1]
character_x_pos = (screen_width/2)- (character_width/2)
character_y_pos = screen_height - character_height - stage_height

#캐릭터 이동 방향
character_to_x = 0

#이동 속도
character_speed = 5

#무기 만들기
weapon = pygame.image.load(os.path.join(image_path, "weapon.png"))
weapon_size = weapon.get_rect().size
weapon_width = weapon_size[0]

# 무기는 한번에 여러 발 발사 가능
weapons = []

#무기 이동속도
weapon_speed = 10

#폰트 정의
game_font = pygame.font.Font(None, 40) #폰트 객체 생성 (폰트, 크기)

#총 시간


#시작 시간
 #현재 tick 을 받아옴

# 2. 이벤트 처리 (키보드, 마우스 등)
running = True #게임이 진행중인가?
while running:
    dt = clock.tick(60) #게임화면의 초당 프레임 수를 설정
    for event in pygame.event.get(): # 어떤 이벤트가 발생하였는가?
        if event.type == pygame.QUIT : #창이 닫히는 이벤트가 발생하였는가?
            running = False # 게임이 진행중이 아님
        
        if event.type  == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                character_to_x -= character_speed
            elif event.key == pygame.K_RIGHT:
                character_to_x += character_speed
            elif event.key == pygame.K_SPACE:
                weapon_x_pos = character_x_pos + (character_width/2) - (weapon_width/2)
                weapon_y_pos = character_y_pos 
                weapons.append([weapon_x_pos, weapon_y_pos])

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                character_to_x = 0
    
    #3. 게임 캐릭터 위치 정의
    character_x_pos += character_to_x

    #가로 경계값 처리
    if character_x_pos <0:
        character_x_pos = 0
    elif character_x_pos > screen_width - character_width:
        character_x_pos =  screen_width - character_width

    #무기 위치 조정
    weapons = [[w[0], w[1] - weapon_speed] for w in weapons] #무기 위치를 위로

    #천장에 닿은 무기 없애기
    weapons = [ [w[0],w[1]] for w in weapons if w[1]>0 ]
    #4. 충돌 처리

    #충돌 처리를 위한 rect 정보 업데이트
   
  
    #충돌 체크
  

    #5. 화면에 그리기

    #screen.fill((0,0,255))
    screen.blit(background, (0,0)) #배경 그리기

    for weapon_x_pos, weapon_y_pos in weapons :
        screen.blit(weapon, (weapon_x_pos,weapon_y_pos))

    screen.blit(stage, (0,screen_height - stage_height)) #캐릭터 그리기
    screen.blit(character, (character_x_pos,character_y_pos))

    
    #타이머 집어 넣기
    #경과 시간 계산
    
    #경과시간(ms)을 1000으로 나눠서 초(s) 단위로 표시

   
    # 출력할 글자, True, 글자 색상
    

    # 만약 시간이 0 이하이면 게임 종료
   

    pygame.display.update() #게임 화면을 다시 그리기

# 잠시 대기

#pygame 종료
pygame.quit()