import sys
import pygame
import random
import game_interface
import flight
import store_system
import NPC
pygame.init()  # 初始化
screen = pygame.display.set_mode((600, 900))  # 游戏界面大小为600*900
screen_rect = screen.get_rect()  # 得到屏幕的rect
pygame.display.set_caption('flight fighting')  # 游戏命名
interface = game_interface.interface(screen)  # 创建游戏界面interface对象
bg_color1 = (0, 128, 128)  # 初始化颜色
bg_color2 = (255, 0, 0)
bg_color3 = (255, 0, 0)
store = store_system.store_system()
moving_left = False  # 初始化我方飞机移动方向判定变量
moving_right = False
moving_up = False
moving_down = False
shield = False
shield_time0 = pygame.time.get_ticks()
self_bullets = pygame.sprite.Group()  # 创建我方子弹精灵组
enemy_bullets = pygame.sprite.Group()  # 创建敌方飞机子弹精灵组
enemies = pygame.sprite.Group()  # 创建敌方飞机精灵组
bomb_2s = pygame.sprite.Group()
bomb_1s = pygame.sprite.Group()
bullets_enemy = pygame.sprite.Group()  # 111111111111111111111111
bullets_Max_enemy = pygame.sprite.Group()  # 1111111111111111111
Max_enemies = pygame.sprite.Group()  # 11111111111111111111111
booms = pygame.sprite.Group()  # 1111111111111111111
color_ready = "black"  # 111111111111111111
color_boom = "red"  # 111111111111111111
flight_1 = flight.flight([300, 950])  # 创建我方飞机对象
enemy_1 = flight.enemy([300, -50])
boss_1 = flight.Boss_1([300, -150], screen)
boss2 = flight.Boss_2([300, -150], screen)
game_while_0 = True
flight_move = True
adjutant_move = False
text_1 = True
boss_1_exist = True
adjutant_1 = NPC.adjutant([700, 750])
text_time0 = pygame.time.get_ticks()
game_while_1 = True
while game_while_1:  # 游戏界面循环
    interface.game_interface()  # 显示游戏界面
    text_time1 = pygame.time.get_ticks()
    for event in pygame.event.get():  # 与外界交互
        if event.type == pygame.QUIT:  # 添加结束游戏按钮
            pygame.quit()
            sys.exit()
        if interface.button_pause.is_over() and event.type == pygame.MOUSEBUTTONDOWN:
            # 调用interface中的按钮类判断是否鼠标暂停按到按钮
            pause_while = True
            while pause_while:  # 暂停界面循环
                interface.pause_interface()  # 显示暂停界面
                for event in pygame.event.get():  # 与外界交互
                    if event.type == pygame.QUIT:  # 添加结束游戏按钮
                        pygame.quit()
                        sys.exit()
                    if interface.button_pause_home.is_over() and event.type == pygame.MOUSEBUTTONDOWN:
                        # 调用interface中的按钮类判断是否鼠标按到返回主界面按钮
                        pause_while = False
                        game_while_1 = False
                    if interface.button_pause_game.is_over() and event.type == pygame.MOUSEBUTTONDOWN:
                        # 调用interface中的按钮类判断是否鼠标按到返回游戏按钮
                        pause_while = False
                    # if interface.button_pause_restart.is_over() and event.type == pygame.MOUSEBUTTONDOWN:
                pygame.display.flip()
        elif event.type == pygame.KEYDOWN:  # 若按下上下左右键分别将判断我方飞机上下左右移动的变量改为true
            if event.key == pygame.K_LEFT:
                moving_left = True
            if event.key == pygame.K_RIGHT:
                moving_right = True
            if event.key == pygame.K_UP:
                moving_up = True
            if event.key == pygame.K_DOWN:
                moving_down = True
            if event.key == pygame.K_SPACE and flight_1.blood > 0:  # 若按下空格键、飞机血量大于0并且屏幕中子弹数量小于2则产生子弹
                if len(self_bullets) < 2:
                    # 生成精灵
                    new_bullet = pygame.sprite.Sprite()
                    # 生成精灵形状
                    new_bullet.rect = pygame.Rect(0, 0, 4, 15)
                    # 绑定位置  精灵中间底部 = 图片顶部
                    new_bullet.rect.midbottom = flight_1.rect.midtop
                    # 精灵放入 盒中
                    self_bullets.add(new_bullet)
            if event.key == pygame.K_1 and store.blood:
                flight_1.blood_max += 50
                flight_1.blood += 50
                store.blood -= 1
            if event.key == pygame.K_2 and store.fix and flight_1.blood < flight_1.blood_max:
                if flight_1.blood <= flight_1.blood_max-50:
                    flight_1.blood += 50
                else:
                    flight_1.blood = flight_1.blood_max
                store.fix -= 1
            if event.key == pygame.K_3 and store.shield:
                shield = True
                shield_time0 = pygame.time.get_ticks()
                store.shield -= 1
            if event.key == pygame.K_4 and store.bomb_1:
                new_bomb_1 = flight.bomb_1()
                new_bomb_1.rect.midbottom = flight_1.rect.midtop
                new_bomb_1.bomb_rect.center = new_bomb_1.rect.center
                bomb_1s.add(new_bomb_1)
                new_bomb_1.draw(screen)
                store.bomb_1 -= 1
            if event.key == pygame.K_5 and store.bomb_2:
                new_bomb_2 = flight.bomb_2()
                new_bomb_2.rect.midbottom = flight_1.rect.midtop
                bomb_2s.add(new_bomb_2)
                new_bomb_2.draw(screen)
                store.bomb_2 -= 1
        elif event.type == pygame.KEYUP:  # 若放开上下左右键分别将判断我方飞机上下左右移动的变量改为false
            if event.key == pygame.K_LEFT:
                moving_left = False
            if event.key == pygame.K_RIGHT:
                moving_right = False
            if event.key == pygame.K_UP:
                moving_up = False
            if event.key == pygame.K_DOWN:
                moving_down = False
    if moving_left and flight_1.rect.left:  # 若判断我方飞机上下左右移动的变量为true且飞机在屏幕范围内，则让飞机上下左右移动
        flight_1.position[0] -= 10
        flight_1.rect.center = flight_1.position  # 更新飞机的rect
    if moving_right and flight_1.rect.right < screen_rect.right:
        flight_1.position[0] += 10
        flight_1.rect.center = flight_1.position
    if moving_up and flight_1.rect.top:
        flight_1.position[1] -= 10
        flight_1.rect.center = flight_1.position
    if moving_down and flight_1.rect.bottom < screen_rect.bottom:
        flight_1.position[1] += 10
        flight_1.rect.center = flight_1.position
    if flight_1.blood > 0:  # 如果飞机血量大于0，则打印飞机
        flight_1.draw(screen)
    if flight_1.blood <= 0:
        gameover_while = True
        while gameover_while:
            interface.gameover_interface()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if interface.gameover_home.is_over() and event.type == pygame.MOUSEBUTTONDOWN:
                    gameover_while = False
                    game_while_1 = False
            pygame.display.flip()
    if shield:
        shield_time1 = pygame.time.get_ticks()
        if shield_time1-shield_time0 <= 5000:
            flight_1.draw_shield(screen)
        else:
            shield = False
    for bullet in self_bullets:  # 遍历我方子弹组中所有子弹
        pygame.draw.rect(screen, bg_color2, bullet.rect)  # 画出子弹
        bullet.rect.y -= 10  # 将子弹向上移动
        if bullet.rect.top <= 0:
            self_bullets.remove(bullet)  # 若子弹处屏幕则将子弹移出精灵组
    for bomb_1 in bomb_1s:
        bomb_1.rect.y -= 10
        bomb_1.bomb_rect.center = bomb_1.rect.center
        bomb_1.draw(screen)
        if bomb_1.rect.bottom <= 0:
            bomb_1s.remove(bomb_1)
    for bomb_2 in bomb_2s:
        bomb_2.rect.y -= 10
        bomb_2.draw(screen)
        if bomb_2.rect.bottom <= 0:
            bomb_2s.remove(bomb_2)
    if len(enemies) < 5 and not boss_1_exist:  # 若敌机数量小于五，则打印敌机
        new_enemy = flight.enemy([random.randint(100, 500), -100])
        enemies.add(new_enemy)
    boss2.move_1()
    boss2.move_2()
    boss2.move_3()
    #boss2.SHOOT_1()
    #boss2.SHOOT_2()
    boss2.SHOOT_3()
    boss2.SHOOT_5()
    boss2.draw(screen)
    # boss2.SHOOT_1()
    # boss2.SHOOT_2()
    # boss2.SHOOT_3()
    interface.game_interface_button()
    flight_1.draw_blood(screen, [25, 750])
    f = pygame.font.Font('C:/Windows/Fonts/simhei.ttf', 50)
    text_blood = f.render(str(store.blood), True, (255, 0, 0), (255, 255, 255))
    textRect = text_blood.get_rect()
    textRect.topleft = (75, 815)
    screen.blit(text_blood, textRect)
    text_fix = f.render(str(store.fix), True, (255, 0, 0), (255, 255, 255))
    textRect = text_fix.get_rect()
    textRect.topleft = (195, 815)
    screen.blit(text_fix, textRect)
    text_shield = f.render(str(store.shield), True, (255, 0, 0), (255, 255, 255))
    textRect = text_shield.get_rect()
    textRect.topleft = (315, 815)
    screen.blit(text_shield, textRect)
    text_bomb_1 = f.render(str(store.bomb_1), True, (255, 0, 0), (255, 255, 255))
    textRect = text_bomb_1.get_rect()
    textRect.topleft = (435, 815)
    screen.blit(text_bomb_1, textRect)
    text_bomb_2 = f.render(str(store.bomb_2), True, (255, 0, 0), (255, 255, 255))
    textRect = text_bomb_2.get_rect()
    textRect.topleft = (555, 815)
    screen.blit(text_bomb_2, textRect)
    text_money = f.render(str(store.money), True, (255, 0, 0), (255, 255, 255))
    textRect = text_money.get_rect()
    textRect.topleft = (80, 35)
    screen.blit(text_money, textRect)
    pygame.display.flip()