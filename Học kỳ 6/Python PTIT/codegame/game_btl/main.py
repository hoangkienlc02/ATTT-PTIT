import pygame
import os
import time
import random
from pygame import mixer
from Ship import Ship
from laser import Laser
from Enemy import Enemy
from Player import Player
from Healing import Healing
from Heart import Heart
from laser_up import Laser_up
from Button import Button
from bt import Button1
from Bot import Bot
from meteor import Meteor
pygame.mixer.init()
pygame.font.init()
WIDTH, HEIGHT = 750,750
WIN = pygame.display.set_mode((WIDTH,HEIGHT))
#đặt tên cho cửa sổ
pygame.display.set_caption("BÀI TẬP LỚN PYTHON")
 # load anh

explosions = [pygame.image.load(os.path.join("Icon","explosion1.png")), pygame.image.load(os.path.join("Icon","explosion2.png")), pygame.image.load(os.path.join("Icon","explosion3.png")),
              pygame.image.load(os.path.join("Icon","explosion4.png")), pygame.image.load(os.path.join("Icon","explosion5.png")),pygame.image.load(os.path.join("Icon","explosion6.png")),pygame.image.load(os.path.join("Icon","explosion7.png")),
              pygame.image.load(os.path.join("Icon","explosion8.png")),pygame.image.load(os.path.join("Icon","explosion9.png")),pygame.image.load(os.path.join("Icon","explosion10.png")),pygame.image.load(os.path.join("Icon","explosion11.png")),pygame.image.load(os.path.join("Icon","explosion12.png"))]
Bexplosions = [pygame.image.load(os.path.join("Icon","Bexplosion1.png")), pygame.image.load(os.path.join("Icon","Bexplosion2.png")), pygame.image.load(os.path.join("Icon","Bexplosion3.png")),
              pygame.image.load(os.path.join("Icon","Bexplosion4.png")), pygame.image.load(os.path.join("Icon","Bexplosion5.png")),pygame.image.load(os.path.join("Icon","Bexplosion6.png")),pygame.image.load(os.path.join("Icon","Bexplosion7.png")),
              pygame.image.load(os.path.join("Icon","Bexplosion8.png")),pygame.image.load(os.path.join("Icon","Bexplosion9.png")),pygame.image.load(os.path.join("Icon","Bexplosion10.png")),pygame.image.load(os.path.join("Icon","Bexplosion11.png")),pygame.image.load(os.path.join("Icon","Bexplosion12.png"))]
start1_img = pygame.image.load(os.path.join("Icon","start_btn1.png"))
start2_img = pygame.image.load(os.path.join("Icon","start_btn2.png"))
exit_img = pygame.image.load(os.path.join("Icon","exit_btn.png"))
Thien_Thach2 = pygame.image.load(os.path.join("Icon","grey_big_2.png"))
Thien_Thach3 = pygame.image.load(os.path.join("Icon","brown_medium_2.png"))
#Background
BG = pygame.transform.scale(pygame.image.load(os.path.join("assets","background-black.png")), (WIDTH,HEIGHT)) # đặt kich thuoc background bằng kích thước màn hình
BG1 = pygame.transform.scale(pygame.image.load(os.path.join("assets","bg1.jpg")), (WIDTH,HEIGHT))
overlap = pygame.transform.scale(pygame.image.load(os.path.join("assets","background-black.png")), (WIDTH,HEIGHT))

#cham nhau ?
def collide(obj1, obj2):
    #coi nhu vecto 2 thanh phan offerX offerY
    offset_x = obj2.x - obj1.x # phần bù X
    offset_y = obj2.y - obj1.y # phần bù Y
    return obj1.mask.overlap(obj2.mask,(offset_x,offset_y)) != None
#exploition
def explosion_animation(x, y):
    for explosion in explosions:
        
        WIN.blit(explosion, (x, y))
        pygame.display.update()
        if explosion == explosions[11]:
            break
        
def Bexplosion_animation(x, y):
    for explosion in Bexplosions:
        
        WIN.blit(explosion, (x, y))
        pygame.display.update()
        if explosion == Bexplosions[11]:
            break
def pause():
    clock = pygame.time.Clock()
    main_font = pygame.font.SysFont("comicsans", 50)
    paused = True
    while paused:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c:
                    paused = False
                #elif event.key == pygame.K_q:
                    #pygame.quit()

                    
        WIN.blit(BG, (0,0))
        live_label = main_font.render("         Press C to continue ", 1, (255,255,255))
        WIN.blit(live_label, (30,350))
        pygame.display.update()
        clock.tick(5)
ok = 0
ck_laser_up = 0
def main():
    global ck_laser_up
    ck_laser_up = 0
    #chose()
    hlFILE = open("heighscore.txt",'r')
    highLevel = int(hlFILE.read())
    run = True
    #Background sound
    mixer.music.load(os.path.join("sound","background.wav"))#os.path.join("Icon","background.wav")
    mixer.music.play(-1)
    FPS = 144 # con so nay cang cao thi game chayj cang nhanh (hieenr thi 60 khung hinh 1s)
    level = 0
    lives = 5
    main_font = pygame.font.SysFont("comicsans", 30)
    lost_font = pygame.font.SysFont("comicsans", 60)
    enemies = []
    hearts = []
    healings = []
    bots = []
    laser_ups = []
    meteors = []
    wave_length = 5 #có 5 tầu mới dc tạo ra ----có thể hiểu có 5 leveel mỗi level sẽ có các chuyến tàu rơi tự do xuống
    enemy_vel = 3 # tốc độ di chuyển của tầu địch là 1pixel trên dây
    heart_cnt = 1
    healing_cnt = 1
    player_vel = 9 # mỗi lần nhấn phím di chuyển 5pixel
    laser_vel = 6 # tốc độ laser
    player = Player(300, 650)
    if ok == 1:
        player.ship_img = YELLOW_SPACE_SHIP
    elif ok == 2: player.ship_img = MY_SHIP
    else: player.ship_img = MY_SHIP4
    #bot = Bot(310,-80)
    clock = pygame.time.Clock()
    ck = 0 #kiem tra xoa bot
    lost = False
    lost_count = 0
    #Vẽ mọi thứ lên màn hình
    
    def redraw_window():
        #WIN.blit(BG, (0,0)) #vex background (kichs thuoc bang destop), góc trên bên trái có tọa độ (0,0)
        #vẽ text

        live_label = main_font.render(f"Lives: {lives}", 1, (255,255,255))
        level_label = main_font.render(f"Level: {level}", 1, (255,255,255))
        
        WIN.blit(live_label, (10,10))
        WIN.blit(level_label, (WIDTH-level_label.get_width()-10,10))
        # kẻ địch pahir dduocj vẽ trước người choi --hiểu đơn giản 
        for meteor in meteors:
            meteor.draw(WIN)
        for bot in bots:
            bot.draw(WIN)
        for healing in healings:
            healing.draw(WIN)
        for heart in hearts:
            heart.draw(WIN)
        for enemy in enemies:
            enemy.draw(WIN)
        for laser_up in laser_ups:
            laser_up.draw(WIN)
        player.draw(WIN)
        
        if lost:
            
            level_label = lost_font.render(f'Your Level: {level}', 1, (249,215,28))
            maxlevel_label = lost_font.render(f'High Level: {highLevel}', 1, (249,215,28))
            WIN.blit(level_label, (WIDTH/2-level_label.get_width()/2,350))
            WIN.blit(maxlevel_label, (WIDTH/2-maxlevel_label.get_width()/2,450))
            hlFILE = open("heighscore.txt",'w')
            hlFILE.write(str(highLevel))
            hlFILE.close()
        
        pygame.display.update()
    b_pos = -750
    o_pos = 0
    speed = 4
    while run:
        clock.tick(FPS) # đảm bảo trò chơi nhất quán trên mọi thiết bị chạy trên máy nahnh hay chậm thì đều chạy cùng tốc độ
        if b_pos >= HEIGHT:
            b_pos = -HEIGHT
        if o_pos >= HEIGHT:
            o_pos = -HEIGHT

        b_pos += speed
        o_pos += speed
        WIN.blit(BG, (0,o_pos))
        WIN.blit(overlap, (0,b_pos))
        redraw_window() # vẽ lại màn hình

        if lives <= 0 or player.health <= 0:
            lost = True
            lost_count += 1

        if lost:
            if lost_count > FPS * 3: # mỗi FPS thực hiện trong 1s neen nếu lost_count > 3 (s)
                run = False
            else:
                continue # để game ko chạy nữa
        
        if len(enemies) == 0:
            level+=1 #nếu như ta bắn hết số mấy bay sainh ra thì tăng level
            if level > highLevel: highLevel = level
            wave_length += 1 # sinh theem 5 tauf địch cho level tiếp theo
            if heart_cnt < 3:
                heart_cnt += 1
            else: heart_cnt=1
            if healing_cnt < 3:
                healing_cnt+=1
            else: healing_cnt = 1
            if level % 3 == 0:
                bot = Bot(310, -80,100+10*level)
                if level % 2 == 0: bot.ship_img = pygame.image.load(os.path.join("Icon","bot1.png"))
                bots.append(bot)
            
            #sinh thien thach
            for i in range(1,6):
                meteor = Meteor(random.randrange(50,WIDTH-100), random.randrange(-1500,-100))
                if i % 3 == 1: meteor.img = Thien_Thach2
                elif i %3 ==  2: meteor.img = Thien_Thach3
                meteors.append(meteor)
            #sinh nang cap dan
            if level % 3 == 0:
                laser_up = Laser_up(random.randrange(50,WIDTH-100), random.randrange(-10,-5))
                laser_ups.append(laser_up)
            for i in range(wave_length):
                #sinh random ngẫu nhiên vị trí tầu địch từ tòa đô x,y (y < 0) sinh độ cao ngẫu nhiên để nó không rơi cùng nhau rơi đọ cao khác nhau
                enemy = Enemy(random.randrange(50,WIDTH-100), random.randrange(-1500,-100),random.choice(["red","blue","green"]) ) # cem video 1:03 đê biết ideal tăng đọ khó level
                enemies.append(enemy)
            for i in range(heart_cnt):
                #sinh random ngẫu nhiên vị trí tầu địch từ tòa đô x,y (y < 0) sinh độ cao ngẫu nhiên để nó không rơi cùng nhau rơi đọ cao khác nhau
                heart = Heart(random.randrange(50,WIDTH-100), random.randrange(-1500,-100))  # cem video 1:03 đê biết ideal tăng đọ khó level
                hearts.append(heart)
            for i in range(healing_cnt):
                healing = Healing(random.randrange(50,WIDTH-100), random.randrange(-1500,-100))
                healings.append(healing)
        for event in pygame.event.get():
             if event.type == pygame.QUIT: # thoat game
                quit()
             if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    pause()
                if event.key == pygame.K_q:
                    run = False
        
        #phím điều khiển tàu
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a] and player.x - player_vel > 0: # left
            player.x -= player_vel #toc độ mỗi lần di chuyển la 5picxel
        if keys[pygame.K_d] and player.x + player_vel + player.get_width()< WIDTH: #right
            player.x += player_vel
        if keys[pygame.K_w] and player.y - player_vel > 0: #  up
            player.y -= player_vel
        if keys[pygame.K_s] and player.y+player_vel + player.get_height() + 15< HEIGHT: #down --- ta cộng thêm 15 là lúc sau thêm thanh máu cao 10 pixel đảm bảo thanh sức khỏe hiện thị
            player.y += player_vel 
        if keys[pygame.K_SPACE]:
            if ck_laser_up == 1:
                player.shoot1()
            else: player.shoot()
            # sound_shoot = mixer.Sound(os.path.join("sound","lasers.wav"))#os.path.join("Icon","laser.wav")
            # sound_shoot.play()
       
        for bot in bots:
            bot.move()
            x = player.health
            bot.move_lasers(5, player)
            if x != player.health: ck_laser_up = 0
            if random.randrange(0,3*60) == 1: # 60FPS --. 60 anhr treen 1 s ,nên random trên ra 1 là lớn trong 2s
                bot.shoot1()
            for ls in player.lasers:
                if collide(bot, ls) : # ==40 (dang fix)   and bot.y >= 40
                    bot.health-=10
                    
                    if bot.health <= 0:
                        try:
                            bot_x = bot.x
                            bot_y = bot.y
                            bots.remove(bot)
                            Bexplosion_animation(bot_x, bot_y)
                            Bexplosion_animation(bot_x, bot_y)
                            Bexplosion_animation(bot_x, bot_y)
                        except: print('No')
                    
                    try: player.lasers.remove(ls)
                    except: print('No')
            #if bot.health == 0: bots.remove(bot)
        for enemy in enemies[:]: # cho địch dịch chuyển tốc độ enemy_vel
            enemy.move(enemy_vel)
            x = player.health
            enemy.move_lasers(laser_vel,player) # tia laser di chuyển tốc độ 4 và kiểm tra xem có trúng người chơi ko
            if player.health != x: ck_laser_up = 0
            if random.randrange(0,5*60) == 1: # 60FPS --. 60 anhr treen 1 s ,nên random trên ra 1 là lớn trong 2s
                enemy.shoot()
            #if player.health > 20: ok = 1
            if collide(enemy, player):
                player.health-=10
                ck_laser_up = 0
                enemy_1x = enemy.x
                enemy_1y = enemy.y
                enemies.remove(enemy)
                explosion_animation(enemy_1x, enemy_1y)
            if enemy.y + enemy.get_height() > HEIGHT and enemy in enemies:
                lives-=1 # nếu quân địch đi tới cuối màn hình thì mạng sống -=1
                enemies.remove(enemy)
        for heart in hearts[:]:
            heart.move(1)
            if collide(heart, player):
                lives+=1
                try:
                    hearts.remove(heart)
                except: print("No")
            if heart.y +  heart.get_height() > HEIGHT and heart in hearts:
                try: hearts.remove(heart)
                except: print("No")
        for healing in healings:
            healing.move(1)
            if collide(healing, player):
                if  player.health <= 100-5:
                    player.health += 5
                try:
                    healings.remove(healing)
                except: print("No")
            if healing.y +  healing.get_height() > HEIGHT and healing in healings:
                healings.remove(healing)
        for laser_up in laser_ups[:]:
            laser_up.move(1)
            if collide(laser_up, player):
                ck_laser_up = 1
                try:
                    laser_ups.remove(laser_up)
                except:
                    print("no")
                #laser_ups.remove(laser_up)
        for meteor in meteors[:]:
            meteor.move()
            if collide(meteor, player):
                player.health-=10
                meteor_x = meteor.x
                meteor_y = meteor.y
                try:
                    meteors.remove(meteor)
                except:
                    print("No")
                explosion_animation(meteor_x, meteor_y)
            for laser in player.lasers:
                if collide(laser, meteor):
                    meteor_x = meteor.x
                    meteor_y = meteor.y
                    try:
                        meteors.remove(meteor)
                    except:
                        print("No")
                    explosion_animation(meteor_x, meteor_y)
        player.move_lasers1(-9,enemies) # enimies danh sách kẻ địch, vận tốc âm để tia laser player đi lên
        player.mvb(bots)
       
ok1 = 0
ok2 = 0
ck1_laser_up = 0
ck2_laser_up = 0
def main1():
    #chose1()
    #chose2()
    global ck1_laser_up
    global ck2_laser_up
    ck1_laser_up = 0
    ck2_laser_up = 0
    hlFILE = open("heighscore.txt",'r')
    highLevel = int(hlFILE.read())
    run = True
    #Background sound
    mixer.music.load(os.path.join("sound","background.wav"))#os.path.join("Icon","background.wav")
    mixer.music.play(-1)
    FPS = 60 # con so nay cang cao thi game chayj cang nhanh (hieenr thi 60 khung hinh 1s)
    level = 0
    lives = 5
    main_font = pygame.font.SysFont("comicsans", 30)
    lost_font = pygame.font.SysFont("comicsans", 60)
    enemies = []
    hearts = []
    healings = []
    bots = []
    laser_ups = []
    meteors = []
    wave_length = 5 #có 5 tầu mới dc tạo ra ----có thể hiểu có 5 leveel mỗi level sẽ có các chuyến tàu rơi tự do xuống
    enemy_vel = 4 # tốc độ di chuyển của tầu địch là 1pixel trên dây
    heart_cnt = 1
    healing_cnt = 1
    player_vel = 9 # mỗi lần nhấn phím di chuyển 5pixel
    laser_vel = 6 # tốc độ laser
    player1 = Player(250, 650)
    player2 = Player(350, 650)
    if ok1 == 1:
        player1.ship_img = YELLOW_SPACE_SHIP
    elif ok1 == 2: player1.ship_img = MY_SHIP
    else: player1.ship_img = MY_SHIP4
    if ok2 == 1:
        player2.ship_img = YELLOW_SPACE_SHIP
    elif ok2 == 2: player2.ship_img = MY_SHIP
    else: player2.ship_img = MY_SHIP4

    #bot = Bot(310,-80)
    clock = pygame.time.Clock()
    ck = 0 #kiem tra xoa bot
    lost = False
    lost_count = 0
    #Vẽ mọi thứ lên màn hình
    
    def redraw_window():
        #WIN.blit(BG, (0,0)) #vex background (kichs thuoc bang destop), góc trên bên trái có tọa độ (0,0)
        #vẽ text

        live_label = main_font.render(f"Lives: {lives}", 1, (255,255,255))
        level_label = main_font.render(f"Level: {level}", 1, (255,255,255))
        
        WIN.blit(live_label, (10,10))
        WIN.blit(level_label, (WIDTH-level_label.get_width()-10,10))
        # kẻ địch pahir dduocj vẽ trước người choi --hiểu đơn giản  
        
        for bot in bots:
            if bot.health > 0:
                bot.draw(WIN)
        for healing in healings:
            healing.draw(WIN)
        for heart in hearts:
            heart.draw(WIN)
        for enemy in enemies:
            enemy.draw(WIN)
        for meteor in meteors:
            meteor.draw(WIN)
        for laser_up in laser_ups:
            laser_up.draw(WIN)
        player1.draw(WIN)
        player2.draw(WIN)
        if lost:
            
            level_label = lost_font.render(f'Your Level: {level}', 1, (249,215,28))
            maxlevel_label = lost_font.render(f'High Level: {highLevel}', 1, (249,215,28))
            WIN.blit(level_label, (WIDTH/2-level_label.get_width()/2,350))
            WIN.blit(maxlevel_label, (WIDTH/2-maxlevel_label.get_width()/2,450))
            hlFILE = open("heighscore.txt",'w')
            hlFILE.write(str(highLevel))
            hlFILE.close()
        
        pygame.display.update()
    b_pos = -750
    o_pos = 0
    speed = 3
    while run:
        clock.tick(FPS) # đảm bảo trò chơi nhất quán trên mọi thiết bị chạy trên máy nahnh hay chậm thì đều chạy cùng tốc độ
        if b_pos >= HEIGHT:
            b_pos = -HEIGHT
        if o_pos >= HEIGHT:
            o_pos = -HEIGHT

        b_pos += speed
        o_pos += speed
        WIN.blit(BG, (0,o_pos))
        WIN.blit(overlap, (0,b_pos))
        redraw_window() # vẽ lại màn hình

        if lives <= 0 or (player1.health <= 0 and player2.health <= 0):
            lost = True
            lost_count += 1
        
        if lost:
            if lost_count > FPS * 3: # mỗi FPS thực hiện trong 1s neen nếu lost_count > 3 (s)
                run = False
            else:
                continue # để game ko chạy nữa
        
        if len(enemies) == 0:
            level+=1 #nếu như ta bắn hết số mấy bay sainh ra thì tăng level
            if level > highLevel: highLevel = level
            wave_length += 1 # sinh theem 5 tauf địch cho level tiếp theo
            if heart_cnt < 3:
                heart_cnt += 1
            else: heart_cnt=1
            if healing_cnt < 3:
                healing_cnt+=1
            else: healing_cnt = 1
            if level % 3 == 0:
                bot = Bot(310, -80,100+10*level)
                if level % 2 == 0: bot.ship_img = pygame.image.load(os.path.join("Icon","bot1.png"))
                bots.append(bot)
            #sinh thien thach
            for i in range(3):
                meteor = Meteor(random.randrange(50,WIDTH-100), random.randrange(-1000,-100))
                if i == 1: meteor.img = Thien_Thach2
                elif i == 2: meteor.img = Thien_Thach3
                meteors.append(meteor)
            #sinh nang cap dan
            if level % 3 == 0:
                laser_up = Laser_up(random.randrange(50,WIDTH-100), random.randrange(-10,-5))
                laser_ups.append(laser_up)
            
            for i in range(wave_length):
                #sinh random ngẫu nhiên vị trí tầu địch từ tòa đô x,y (y < 0) sinh độ cao ngẫu nhiên để nó không rơi cùng nhau rơi đọ cao khác nhau
                enemy = Enemy(random.randrange(50,WIDTH-100), random.randrange(-1500,-100),random.choice(["red","blue","green"]) ) # cem video 1:03 đê biết ideal tăng đọ khó level
                enemies.append(enemy)
            for i in range(heart_cnt):
                #sinh random ngẫu nhiên vị trí tầu địch từ tòa đô x,y (y < 0) sinh độ cao ngẫu nhiên để nó không rơi cùng nhau rơi đọ cao khác nhau
                heart = Heart(random.randrange(50,WIDTH-100), random.randrange(-1500,-100))  # cem video 1:03 đê biết ideal tăng đọ khó level
                hearts.append(heart)
            for i in range(healing_cnt):
                healing = Healing(random.randrange(50,WIDTH-100), random.randrange(-1500,-100))
                healings.append(healing)
        for event in pygame.event.get():
             if event.type == pygame.QUIT: # thoat game
                quit()
             if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    pause()
                if event.key == pygame.K_q:
                    run = False
        
        #phím điều khiển tàu
        if player1.health > 0:
            keys = pygame.key.get_pressed()
            if keys[pygame.K_a] and player1.x - player_vel > 0: # left
                player1.x -= player_vel #toc độ mỗi lần di chuyển la 5picxel
            if keys[pygame.K_d] and player1.x + player_vel + player1.get_width()< WIDTH: #right
                player1.x += player_vel
            if keys[pygame.K_w] and player1.y - player_vel > 0: #  up
                player1.y -= player_vel
            if keys[pygame.K_s] and player1.y+player_vel + player1.get_height() + 15< HEIGHT: #down --- ta cộng thêm 15 là lúc sau thêm thanh máu cao 10 pixel đảm bảo thanh sức khỏe hiện thị
                player1.y += player_vel 
            if keys[pygame.K_SPACE]:
                if ck1_laser_up == 0: player1.shoot()
                else: player1.shoot1()
                # sound_shoot = mixer.Sound(os.path.join("sound","lasers.wav"))#os.path.join("Icon","laser.wav")
                # sound_shoot.play()
        else: 
            player1 = Player(1000, 50)
            player1.health = 0
        if player2.health > 0:
            keys = pygame.key.get_pressed()
            if keys[pygame.K_LEFT] and player2.x - player_vel > 0: # left
                player2.x -= player_vel #toc độ mỗi lần di chuyển la 5picxel
            if keys[pygame.K_RIGHT] and player2.x + player_vel + player2.get_width()< WIDTH: #right
                player2.x += player_vel
            if keys[pygame.K_UP] and player2.y - player_vel > 0: #  up
                player2.y -= player_vel
            if keys[pygame.K_DOWN] and player2.y+player_vel + player2.get_height() + 15< HEIGHT: #down --- ta cộng thêm 15 là lúc sau thêm thanh máu cao 10 pixel đảm bảo thanh sức khỏe hiện thị
                player2.y += player_vel 
            if keys[pygame.K_KP0]:
                if ck2_laser_up == 0: player2.shoot()
                else: player2.shoot1()
                # sound_shoot = mixer.Sound(os.path.join("sound","lasers.wav"))#os.path.join("Icon","laser.wav")
                # sound_shoot.play()
        else: 
            player2 = Player(1000, 50)
            player2.health = 0
        '''if level == 2 or bot.health != 0:
            bot.move()'''
        for bot in bots:
            bot.move()
            x1 = player1.health
            x2 = player2.health
            bot.move_lasers(5, player1)
            bot.move_lasers(5, player2)
            if x1 != player1.health: ck1_laser_up = 0
            if x2 != player2.health: ck2_laser_up = 0
            if random.randrange(0,3*60) == 1: # 60FPS --. 60 anhr treen 1 s ,nên random trên ra 1 là lớn trong 2s
                bot.shoot1()

            for ls in player1.lasers:
                
                    if collide(bot, ls) :
                        bot.health-=10
                        try: player1.lasers.remove(ls)
                        except: print("No")
                        if bot.health <= 0: #and len(bots) > 0: 
                            try:
                                bot_x = bot.x
                                bot_y = bot.y
                                bots.remove(bot)

                                Bexplosion_animation(bot_x, bot_y)
                                Bexplosion_animation(bot_x, bot_y)
                                Bexplosion_animation(bot_x, bot_y)
                            except: print("No")
            for ls in player2.lasers:
                
                    if collide(bot, ls) :
                        bot.health-=10
                        try: player2.lasers.remove(ls)
                        except: prin("No")
                        if bot.health <= 0: #and len(bots) > 0: 
                            try:
                                bot_x = bot.x
                                bot_y = bot.y
                                bots.remove(bot)
                                Bexplosion_animation(bot_x, bot_y)
                                Bexplosion_animation(bot_x, bot_y)
                                Bexplosion_animation(bot_x, bot_y)
                            except: print("No")
        for enemy in enemies[:]: # cho địch dịch chuyển tốc độ enemy_vel
            enemy.move(enemy_vel)
            x = player1.health
            y = player2.health
            enemy.move_lasers(laser_vel,player1) # tia laser di chuyển tốc độ 4 và kiểm tra xem có trúng người chơi ko
            enemy.move_lasers(laser_vel,player2)
            if x != player1.health: ck1_laser_up = 0
            if y != player2.health: ck2_laser_up = 0
            if random.randrange(0,5*60) == 1: # 60FPS --. 60 anhr treen 1 s ,nên random trên ra 1 là lớn trong 2s
                enemy.shoot()
            #if player.health > 20: ok = 1
            if collide(enemy, player1):
                player1.health-=10
                ck1_laser_up = 0
                enemy_1x = enemy.x
                enemy_1y = enemy.y
                enemies.remove(enemy)
                explosion_animation(enemy_1x, enemy_1y)
            if collide(enemy, player2):
                player2.health-=10
                ck2_laser_up = 0
                enemy_1x = enemy.x
                enemy_1y = enemy.y
                try: enemies.remove(enemy)
                except: print("No")
                explosion_animation(enemy_1x, enemy_1y)
            if enemy.y + enemy.get_height() > HEIGHT and enemy in enemies:
                lives-=1 # nếu quân địch đi tới cuối màn hình thì mạng sống -=1
                try: enemies.remove(enemy)
                except: print("No")
        for heart in hearts[:]:
            heart.move(1)
            if collide(heart, player1):
                lives+=1
                try: hearts.remove(heart)
                except: print("No")
            if heart.y +  heart.get_height() > HEIGHT and heart in hearts:
                try: hearts.remove(heart)
                except: print("No")
        for heart in hearts[:]:
            heart.move(1)
            if collide(heart, player2):
                lives+=1
                try: hearts.remove(heart)
                except: print("No")
            if heart.y +  heart.get_height() > HEIGHT and heart in hearts:
                try: hearts.remove(heart)
                except: print("No")
        for healing in healings:
            healing.move(1)
            if collide(healing, player1):
                if  player1.health <= 100-5:
                    player1.health += 5
                try: healings.remove(healing)
                except: print("No")
            if healing.y +  healing.get_height() > HEIGHT and healing in healings:
                try: healings.remove(healing)
                except: print("No")
        for healing in healings:
            healing.move(1)
            if collide(healing, player2):
                if  player2.health <= 100-5:
                    player2.health += 5
                try: healings.remove(healing)
                except: print("No")
            if healing.y +  healing.get_height() > HEIGHT and healing in healings:
                healings.remove(healing)
        for laser_up in laser_ups[:]:
            laser_up.move(1)
            if collide(laser_up, player1):
                ck1_laser_up = 1
                try: laser_ups.remove(laser_up)
                except: print("No")
        for laser_up in laser_ups[:]:
            laser_up.move(1)
            if collide(laser_up, player2):
                ck2_laser_up = 1
                try: laser_ups.remove(laser_up)
                except: print("No")
        for meteor in meteors[:]:
            meteor.move()
            if collide(meteor, player1):
                player1.health-=10
                meteor_x = meteor.x
                meteor_y = meteor.y
                try:
                    meteors.remove(meteor)
                except:
                    print("No")
                explosion_animation(meteor_x, meteor_y)
            for laser in player1.lasers:
                if collide(laser, meteor):
                    meteor_x = meteor.x
                    meteor_y = meteor.y
                    try:
                        meteors.remove(meteor)
                    except:
                        print("No")
                    explosion_animation(meteor_x, meteor_y)
        for meteor in meteors[:]:
            meteor.move()
            if collide(meteor, player2):
                player2.health-=10
                meteor_x = meteor.x
                meteor_y = meteor.y
                try:
                    meteors.remove(meteor)
                except:
                    print("No")
                explosion_animation(meteor_x, meteor_y)
            for laser in player2.lasers:
                if collide(laser, meteor):
                    meteor_x = meteor.x
                    meteor_y = meteor.y
                    try:
                        meteors.remove(meteor)
                    except:
                        print("No")
                    explosion_animation(meteor_x, meteor_y)   
        player1.move_lasers1(-laser_vel,enemies) # enimies danh sách kẻ địch, vận tốc âm để tia laser player đi lên
        player1.mvb(bots)
        player2.move_lasers1(-laser_vel,enemies) # enimies danh sách kẻ địch, vận tốc âm để tia laser player đi lên
        player2.mvb(bots)
        
YELLOW_SPACE_SHIP = pygame.image.load(os.path.join("Icon","tau_minh (1).png"))
MY_SHIP = pygame.image.load(os.path.join("Icon","Myship3.png"))
MY_SHIP4 = pygame.image.load(os.path.join("Icon","Myship5.png"))
def chose():
    run = True
    FPS = 60
    players = []
    clock = pygame.time.Clock()
    button1 = Button1('B52',100,40,(80,500),5)
    button2 = Button1('F22',100,40,(300,500),5)
    button3 = Button1('F55',100,40,(520,500),5)
    def redraw_window():
        WIN.blit(BG, (0,0))
        ngame_font = pygame.font.SysFont("comicsans", 80)
        play1_label = ngame_font.render('PLAY1', 1, (249,215,28))
        WIN.blit(play1_label, (WIDTH/2-play1_label.get_width()/2,200))
        button1.draw()
        button2.draw()
        button3.draw()
        WIN.blit(YELLOW_SPACE_SHIP, (90,380))
        WIN.blit(MY_SHIP, (310,380))
        WIN.blit(MY_SHIP4, (520,380))
        pygame.display.update()

    while run:
        clock.tick(FPS)
        redraw_window()
        global ok
        for event in pygame.event.get():
            if button1.ck == 1: # thoat game
                ok = 1
                run = False
            if button2.ck == 1:
                ok = 2
                run = False
            if button3.ck == 1:
                ok = 3
                run = False
           
def chose1():
    run = True
    FPS = 60
    players = []
    clock = pygame.time.Clock()
    button1 = Button1('B52',100,40,(80,500),5)
    button2 = Button1('F22',100,40,(300,500),5)
    button3 = Button1('F55',100,40,(520,500),5)
    def redraw_window():
        WIN.blit(BG, (0,0))
        ngame_font = pygame.font.SysFont("comicsans", 80)
        play1_label = ngame_font.render('PLAY1', 1, (249,215,28))
        WIN.blit(play1_label, (WIDTH/2-play1_label.get_width()/2,200))
        button1.draw()
        button2.draw()
        button3.draw()
        WIN.blit(YELLOW_SPACE_SHIP, (90,380))
        WIN.blit(MY_SHIP, (310,380))
        WIN.blit(MY_SHIP4, (520,380))
        pygame.display.update()

    while run:
        clock.tick(FPS)
        redraw_window()
        global ok1
        for event in pygame.event.get():
            if button1.ck == 1: # thoat game
                ok1 = 1
                run = False
            if button2.ck == 1:
                ok1 = 2
                run = False
            if button3.ck == 1:
                ok1 = 3
                run = False
def chose2():
    run = True
    FPS = 60
    players = []
    clock = pygame.time.Clock()
    button1 = Button1('B52',100,40,(80,500),5)
    button2 = Button1('F22',100,40,(300,500),5)
    button3 = Button1('F55',100,40,(520,500),5)

    def redraw_window():
        WIN.blit(BG, (0,0))
        ngame_font = pygame.font.SysFont("comicsans", 80)
        play1_label = ngame_font.render('PLAY2', 1, (249,215,28))
        WIN.blit(play1_label, (WIDTH/2-play1_label.get_width()/2,200))
        button1.draw()
        button2.draw()
        button3.draw()
        WIN.blit(YELLOW_SPACE_SHIP, (90,380))
        WIN.blit(MY_SHIP, (310,380))
        WIN.blit(MY_SHIP4, (520,380))
        pygame.display.update()

    while run:
        clock.tick(FPS)
        redraw_window()
        global ok2
        for event in pygame.event.get():
            if button1.ck == 1: # thoat game
                ok2 = 1
                run = False
            if button2.ck == 1:
                ok2 = 2
                run = False
            if button3.ck == 1:
                ok2 = 3
                run = False
            
def main_menu():
    start_button1 = Button(WIDTH // 2 - 200, HEIGHT // 2 + 50, start1_img)
    start_button2 = Button(WIDTH // 2 - 200, HEIGHT // 2 + 150, start2_img)
    exit_button = Button(WIDTH // 2 -100, HEIGHT // 2 + 250, exit_img)
    
    ngame_font = pygame.font.SysFont("comicsans", 80)
    run = True
    while run:
        WIN.blit(BG1, (0,0))
        ngame_label = ngame_font.render('GAME', 1, (249,215,28))
        WIN.blit(ngame_label, (WIDTH/2-ngame_label.get_width()/2,200))
        ngame_label1 = ngame_font.render('SPACE INVADERS', 1, (249,215,28))
        WIN.blit(ngame_label1, (WIDTH/2-ngame_label1.get_width()/2,300))
        start_button1.draw()
        start_button2.draw()
        exit_button.draw()
        pygame.display.update() #update de cap nhap mới
        for event in pygame.event.get():
            if exit_button.draw():
                run = False
            if start_button1.draw():# neeus ấn chuột thì game bắt đầu lại
                ck_laser_up=0
                chose()
                main()
            if start_button2.draw():
                
                chose1()
                chose2()
                main1()
    pygame.quit()

main_menu()