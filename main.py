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
pygame.mixer.init()
pygame.mixer.music.load("music/Graze the Roof.mp3")
pygame.mixer.music.play(5)
pygame.mixer.music.set_volume(0.5)
pass_game_1 = False
pass_game_2 = False
while True:  # 游戏主循环
    interface.main_interface()  # 显示主循环界面
    for event in pygame.event.get():  # 与外界交互
        if event.type == pygame.QUIT:  # 添加结束游戏按钮
            pygame.quit()
            sys.exit()
        if interface.button_start.is_over() and event.type == pygame.MOUSEBUTTONDOWN:  # 调用interface中的按钮类判断是否鼠标按到开始游戏按钮
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
            bullets_enemy = pygame.sprite.Group()
            bullets_Max_enemy = pygame.sprite.Group()
            Max_enemies = pygame.sprite.Group()
            booms = pygame.sprite.Group()
            boss_bullets = pygame.sprite.Group()
            boss_bullets_left = pygame.sprite.Group()
            boss_bullets_right = pygame.sprite.Group()
            bosses = pygame.sprite.Group()
            boss_screen_blacks = pygame.sprite.Group()
            boss_booms = pygame.sprite.Group()
            flight_1 = flight.flight([300, 950])  # 创建我方飞机对象
            enemy_1 = flight.enemy([300, -50])
            boss_1 = flight.Boss_1([350, -200], screen)
            boss2 = flight.Boss_2([350, -200], screen)
            boss_c = flight.Boss([350, -200])
            bosses.add_internal(boss_c)
            game_while_0 = True
            game_while_1 = True
            game_while_2 = True
            game_while_3 = True
            win_game = True
            if not pass_game_1 and not pass_game_2:
                game_while_0 = True
                game_while_1 = True
                game_while_2 = True
                game_while_3 = True
            if pass_game_1:
                game_while_0 = False
                game_while_1 = False
                game_while_2 = True
                game_while_3 = True
            if pass_game_2:
                game_while_0 = False
                game_while_1 = False
                game_while_2 = False
                game_while_3 = True
            flight_move = True
            adjutant_move = False
            text_1 = True
            enemy_exist = True
            boss_1_exist = False
            boss_2_exist = False
            boss_3_exist = False
            max_enemy_exist = False
            color_ready = "black"
            color_boom = "red"
            adjutant_1 = NPC.adjutant([700, 750])
            text_time0 = pygame.time.get_ticks()
            pygame.mixer.init()
            pygame.mixer.music.load("music/Graze the Roof.mp3")
            pygame.mixer.music.play(5)
            pygame.mixer.music.set_volume(0.5)
            while game_while_0:
                interface.game_interface()
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
                if flight_move:
                    flight_1.position[1] -= 1
                    flight_1.rect.center = flight_1.position
                if adjutant_move:
                    adjutant_1.position[0] -= 1
                    adjutant_1.rect.center = adjutant_1.position
                if flight_1.position[1] == 650:
                    flight_move = False
                    adjutant_move = True
                if adjutant_1.position[0] == 550:
                    text_time0 = pygame.time.get_ticks()
                if adjutant_1.position[0] == 500:
                    adjutant_move = False
                if not flight_move and not adjutant_move:
                    pygame.draw.rect(screen, (0, 128, 128), (0, 700, 600, 200))
                    text_time1 = pygame.time.get_ticks()
                    if 1000 <= text_time1-text_time0 <= 4000:
                        adjutant_1.draw_text_1(screen)
                    if 4000 <= text_time1-text_time0 <= 7000:
                        adjutant_1.draw_text_2(screen)
                    if text_time1-text_time0 >= 7000:
                        text_time0 = pygame.time.get_ticks()
                        game_while_0 = False
                flight_1.draw(screen)
                adjutant_1.draw(screen)
                enemy_1.draw(screen)
                pygame.display.flip()
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
                                    game_while_2 = False
                                    game_while_3 = False
                                    win_game = False
                                if interface.button_pause_game.is_over() and event.type == pygame.MOUSEBUTTONDOWN:
                                    # 调用interface中的按钮类判断是否鼠标按到返回游戏按钮
                                    pause_while = False
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
                            if len(self_bullets) < 50:
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
                                game_while_2 = False
                                game_while_3 = False
                                win_game = False
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
                if len(enemies) < 5 and enemy_exist:  # 若敌机数量小于五，则打印敌机
                    new_enemy = flight.enemy([random.randint(100, 500), -100])
                    enemies.add(new_enemy)
                for enemy_1 in enemies:  # 遍历敌机组中的所有敌机
                    enemy_1.draw(screen)  # 画出敌机
                    if pygame.sprite.collide_rect(flight_1, enemy_1) and not shield:  # 如果敌方飞机碰到我方飞机，则让我方飞机扣血
                        flight_1.blood -= 10
                    for bullet in self_bullets:
                        if pygame.sprite.collide_rect(bullet, enemy_1):  # 如果我方飞机子弹碰到敌方飞机，则让敌方飞机消失
                            enemies.remove(enemy_1)
                            self_bullets.remove(bullet)
                            store.money += 5
                    for bomb_1 in bomb_1s:
                        if pygame.sprite.collide_rect(bomb_1, enemy_1):
                            bomb_1.draw_bomb_effect(screen)
                            for enemy_2 in enemies:
                                if bomb_1.bomb_rect.left < enemy_2.rect.x < bomb_1.bomb_rect.right and bomb_1.bomb_rect.top < enemy_2.rect.y < bomb_1.bomb_rect.bottom:
                                    enemies.remove(enemy_2)
                                    bomb_1s.remove(bomb_1)
                    for bomb_2 in bomb_2s:
                        if pygame.sprite.collide_rect(bomb_2, enemy_1):
                            enemies.remove(enemy_1)
                            store.money += 5
                    if enemy_1.rect.left < screen_rect.left:  # 如果敌方飞机出界，则改变其速度使其飞回
                        enemy_1.speed_x = 1
                    if enemy_1.rect.right > screen_rect.right:
                        enemy_1.speed_x = -1
                    if enemy_1.rect.top < screen_rect.top:
                        enemy_1.speed_y = 1
                    if enemy_1.rect.bottom > screen_rect.bottom:
                        enemy_1.speed_y = -1
                    if pygame.time.get_ticks() % 100 == 0:  # 敌机每0.5秒随机改变一次速度
                        enemy_1.speed_x = random.randint(-1, 1)
                        enemy_1.speed_y = random.randint(-1, 1)
                    enemy_1.position[0] += enemy_1.speed_x  # 更新敌机的位置和rect
                    enemy_1.position[1] += enemy_1.speed_y
                    enemy_1.rect.center = enemy_1.position
                    if pygame.time.get_ticks() % 200 == 0:  # 敌机每2秒发一次子弹
                        # 生成精灵
                        new_bullet = pygame.sprite.Sprite()
                        # 生成精灵形状
                        new_bullet.rect = pygame.Rect(0, 0, 4, 15)
                        # 绑定位置  精灵中间底部 = 图片顶部
                        new_bullet.rect.midtop = enemy_1.rect.midbottom
                        # 精灵放入 盒中
                        enemy_bullets.add(new_bullet)
                for enemy_bullet in enemy_bullets:  # 遍历敌机子弹组中的所有子弹
                    pygame.draw.rect(screen, bg_color2, enemy_bullet.rect)  # 画出敌机子弹
                    enemy_bullet.rect.y += 2
                    if enemy_bullet.rect.bottom >= screen_rect.bottom:  # 若子弹出界，则让该子弹移出子弹组
                        enemy_bullets.remove(enemy_bullet)
                    if pygame.sprite.collide_rect(enemy_bullet, flight_1) and not shield:
                        # 若敌方飞机子弹碰到我方飞机，则让我方飞机扣血并让子弹消失
                        flight_1.blood -= 10
                        enemy_bullets.remove(enemy_bullet)
                # ---------------------------------------------------------------------------------
                if len(Max_enemies) < 3 and pygame.time.get_ticks() >= 1000 and max_enemy_exist:
                    new_Max_enemy = flight.Max_Enemy([random.randint(50, 450), -50], screen_rect)
                    Max_enemies.add_internal(new_Max_enemy)
                for Max_enemy in Max_enemies:
                    Max_enemy.Max_draw(screen)
                    Max_enemy.Max_move()
                    if pygame.sprite.collide_rect(flight_1, Max_enemy) and not shield:  # 如果敌方飞机碰到我方飞机，则让我方飞机扣血
                        flight_1.blood -= 10
                    if pygame.time.get_ticks() % 300 == 0:
                        Max_bullet_new1 = flight.Bullets_enemy(
                            [Max_enemy.rect.center[0] + Max_enemy.image.get_width() / 2,
                             Max_enemy.rect.center[1] + Max_enemy.image.get_height() / 2])
                        Max_bullet_new2 = flight.Bullets_enemy(
                            [Max_enemy.rect.center[0] - Max_enemy.image.get_width() / 2,
                             Max_enemy.rect.center[1] + Max_enemy.image.get_height() / 2])
                        bullets_Max_enemy.add_internal(Max_bullet_new1)
                        bullets_Max_enemy.add_internal(Max_bullet_new2)
                    for bullet_1 in self_bullets:
                        if pygame.sprite.collide_rect(Max_enemy, bullet_1):
                            Max_enemy.HP -= 50
                            self_bullets.remove_internal(bullet_1)
                    for bomb_1 in bomb_1s:
                        if pygame.sprite.collide_rect(bomb_1, Max_enemy):
                            bomb_1.draw_bomb_effect(screen)
                            for Max_enemy in Max_enemies:
                                if bomb_1.bomb_rect.left < Max_enemy.rect.x < bomb_1.bomb_rect.right and bomb_1.bomb_rect.top < Max_enemy.rect.y < bomb_1.bomb_rect.bottom:
                                    Max_enemy.HP -= 50
                                    bomb_1s.remove(bomb_1)
                    for bomb_2 in bomb_2s:
                        if pygame.sprite.collide_rect(bomb_2, Max_enemy):
                            Max_enemy.HP -= 50
                            store.money += 5
                    if Max_enemy.HP <= 0:
                        Max_enemies.remove_internal(Max_enemy)
                        store.money += 10
                        boom = flight.Boom(flight_1.rect.center[0], flight_1.rect.center[1], Max_enemy.rect.centerx,
                                           Max_enemy.rect.centery)
                        booms.add_internal(boom)
                for Max_enemy_bullet in bullets_Max_enemy:
                    Max_enemy_bullet.rect.y += 2
                    Max_enemy_bullet.draw(screen)
                    if Max_enemy_bullet.rect.top > screen_rect.bottom:
                        bullets_Max_enemy.remove_internal(Max_enemy_bullet)
                    if pygame.sprite.collide_rect(Max_enemy_bullet, flight_1) and flight_1.blood > 0 and not shield:
                        bullets_Max_enemy.remove_internal(Max_enemy_bullet)
                        flight_1.blood -= 10
                for boom in booms:
                    boom_now = pygame.time.get_ticks()
                    if boom.now_positiony <= boom.rect.centery - boom.dead_flight.get_height() / 2 - 50:
                        screen.blit(boom.dead_flight, [boom.now_positionx, boom.now_positiony])
                    if pygame.time.get_ticks() % 1 == 0:
                        if boom.rect.centerx - boom.dead_flight.get_width() / 2 < boom.now_positionx:
                            boom.now_positionx -= 5
                        if boom.rect.centerx - boom.dead_flight.get_width() / 2 > boom.now_positionx:
                            boom.now_positionx += 5
                        if boom.rect.centery - boom.dead_flight.get_height() / 2 < boom.now_positiony:
                            boom.now_positiony -= 5
                        if boom.rect.centery - boom.dead_flight.get_height() / 2 > boom.now_positiony:
                            boom.now_positiony += 5
                    if boom.now_positiony >= boom.rect.centery - boom.dead_flight.get_height() / 2 - 50 and boom.now_positiony <= boom.rect.centery - boom.dead_flight.get_height() / 2 + 50:
                        if boom_now - boom.ready >= boom.wait:
                            # pygame.draw.rect(screen, color_boom, boom.rect)
                            boom.boom(screen)
                        if boom_now - boom.ready <= boom.wait:
                            # pygame.draw.rect(screen, color_ready, boom.rect)
                            boom.boom_ready(screen)
                        if boom_now - boom.ready >= boom.wait + boom.boom_time:
                            booms.remove_internal(boom)
                        if pygame.sprite.collide_rect(boom,flight_1) and boom_now - boom.ready >= boom.wait and boom_now - boom.ready <= boom.wait + 10 and flight_1.blood > 0 and not shield:
                            flight_1.blood -= 20
                if boss_1_exist:
                    boss_1.move_1()
                    boss_1.move_2()
                    boss_1.move_4()
                    boss_1.SHOOT_1()
                    boss_1.SHOOT_2()
                    boss_1.SHOOT_3()
                    boss_1.SHOOT_4()
                    boss_1.SHOOT_5()
                    for enemy_bullet in boss_1.bullets_1:
                        if pygame.sprite.collide_rect(enemy_bullet, flight_1) and not shield:
                            flight_1.blood -= 10
                            boss_1.bullets_1.remove_internal(enemy_bullet)
                    for enemy_bullet in boss_1.bullets_2:
                        if pygame.sprite.collide_rect(enemy_bullet, flight_1) and not shield:
                            flight_1.blood -= 10
                            boss_1.bullets_2.remove_internal(enemy_bullet)
                    for enemy_bullet in boss_1.bullets_3:
                        if pygame.sprite.collide_rect(enemy_bullet, flight_1) and not shield:
                            flight_1.blood -= 10
                            boss_1.bullets_3.remove_internal(enemy_bullet)
                    for enemy_bullet in boss_1.bullets_5:
                        if pygame.sprite.collide_rect(enemy_bullet, flight_1) and not shield:
                            flight_1.blood -= 10
                            boss_1.bullets_5.remove_internal(enemy_bullet)
                    for bullet in self_bullets:
                        if pygame.sprite.collide_rect(bullet, boss_1):  # 如果我方飞机子弹碰到敌方飞机，则让敌方飞机消失
                            boss_1.HP -= 100
                            self_bullets.remove(bullet)
                            store.money += 5
                    for bomb_1 in bomb_1s:
                        if pygame.sprite.collide_rect(bomb_1, boss_1):
                            bomb_1.draw_bomb_effect(screen)
                            if bomb_1.bomb_rect.left < boss_1.rect.x < bomb_1.bomb_rect.right and bomb_1.bomb_rect.top < boss_1.rect.y < bomb_1.bomb_rect.bottom:
                                boss_1.HP -= 100
                                bomb_1s.remove(bomb_1)
                    for bomb_2 in bomb_2s:
                        if pygame.sprite.collide_rect(bomb_2, boss_1):
                            boss_1.HP -= 100
                            bomb_2s.remove(bomb_2)
                            store.money += 5
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
                if 2000 <= text_time1-text_time0 <= 7000:
                    pygame.draw.rect(screen, (0, 128, 128), (0, 700, 600, 200))
                    adjutant_1.draw_text_3(screen)
                    adjutant_1.draw(screen)
                if 2050 <= text_time1-text_time0 <= 7000:
                    pygame.time.wait(5000)
                if 10000 <= text_time1-text_time0 <= 15000:
                    pygame.draw.rect(screen, (0, 128, 128), (0, 700, 600, 200))
                    adjutant_1.draw_text_4(screen)
                    adjutant_1.draw(screen)
                if 10050 <= text_time1-text_time0 <= 15000:
                    pygame.time.wait(5000)
                if 16000 <= text_time1-text_time0 <= 19000:
                    pygame.draw.rect(screen, (0, 128, 128), (0, 700, 600, 200))
                    adjutant_1.draw_text_6(screen)
                    adjutant_1.draw(screen)
                if 16050 <= text_time1-text_time0 <= 19000:
                    pygame.time.wait(3000)
                if 30000 <= text_time1-text_time0 <= 33000:
                    pygame.draw.rect(screen, (0, 128, 128), (0, 700, 600, 200))
                    adjutant_1.draw_text_5(screen)
                    adjutant_1.draw(screen)
                if 30050 <= text_time1-text_time0 <= 33000:
                    pygame.time.wait(3000)
                if text_time1-text_time0 >= 30000:
                    max_enemy_exist = True
                if 60000 <= text_time1-text_time0 <= 63000:
                    pygame.draw.rect(screen, (0, 128, 128), (0, 700, 600, 200))
                    adjutant_1.draw_text_7(screen)
                    adjutant_1.draw(screen)
                if 60050 <= text_time1-text_time0 <= 63000:
                    pygame.time.wait(3000)
                if text_time1-text_time0 >= 63000:
                    boss_1_exist = True
                    enemy_exist = False
                    max_enemy_exist = False
                    if text_time1 - text_time0 <= 64000:
                        pygame.mixer.init()
                        pygame.mixer.music.load("music/Block City Wars OST - Summer.mp3")
                        pygame.mixer.music.play(5)
                        pygame.mixer.music.set_volume(0.5)
                if boss_1.HP <= 0:
                    boss_1_exist = False
                    pass_game_1 = True
                    game_while_1 = False
                    pygame.mixer.init()
                    pygame.mixer.music.load("music/Graze the Roof.mp3")
                    pygame.mixer.music.play(5)
                    pygame.mixer.music.set_volume(0.5)
                pygame.display.flip()
            text_time0 = pygame.time.get_ticks()
            while game_while_2:
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
                                    game_while_2 = False
                                    game_while_3 = False
                                    win_game = False
                                if interface.button_pause_game.is_over() and event.type == pygame.MOUSEBUTTONDOWN:
                                    # 调用interface中的按钮类判断是否鼠标按到返回游戏按钮
                                    pause_while = False
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
                            if len(self_bullets) < 50:
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
                            if flight_1.blood <= flight_1.blood_max - 50:
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
                                game_while_2 = False
                                game_while_3 = False
                                win_game = False
                        pygame.display.flip()
                if shield:
                    shield_time1 = pygame.time.get_ticks()
                    if shield_time1 - shield_time0 <= 5000:
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
                if len(enemies) < 5 and enemy_exist:  # 若敌机数量小于五，则打印敌机
                    new_enemy = flight.enemy([random.randint(100, 500), -100])
                    enemies.add(new_enemy)
                for enemy_1 in enemies:  # 遍历敌机组中的所有敌机
                    enemy_1.draw(screen)  # 画出敌机
                    if pygame.sprite.collide_rect(flight_1, enemy_1) and not shield:  # 如果敌方飞机碰到我方飞机，则让我方飞机扣血
                        flight_1.blood -= 10
                    for bullet in self_bullets:
                        if pygame.sprite.collide_rect(bullet, enemy_1):  # 如果我方飞机子弹碰到敌方飞机，则让敌方飞机消失
                            enemies.remove(enemy_1)
                            self_bullets.remove(bullet)
                            store.money += 5
                    for bomb_1 in bomb_1s:
                        if pygame.sprite.collide_rect(bomb_1, enemy_1):
                            bomb_1.draw_bomb_effect(screen)
                            for enemy_2 in enemies:
                                if bomb_1.bomb_rect.left < enemy_2.rect.x < bomb_1.bomb_rect.right and bomb_1.bomb_rect.top < enemy_2.rect.y < bomb_1.bomb_rect.bottom:
                                    enemies.remove(enemy_2)
                                    bomb_1s.remove(bomb_1)
                    for bomb_2 in bomb_2s:
                        if pygame.sprite.collide_rect(bomb_2, enemy_1):
                            enemies.remove(enemy_1)
                            store.money += 5
                    if enemy_1.rect.left < screen_rect.left:  # 如果敌方飞机出界，则改变其速度使其飞回
                        enemy_1.speed_x = 1
                    if enemy_1.rect.right > screen_rect.right:
                        enemy_1.speed_x = -1
                    if enemy_1.rect.top < screen_rect.top:
                        enemy_1.speed_y = 1
                    if enemy_1.rect.bottom > screen_rect.bottom:
                        enemy_1.speed_y = -1
                    if pygame.time.get_ticks() % 100 == 0:  # 敌机每0.5秒随机改变一次速度
                        enemy_1.speed_x = random.randint(-1, 1)
                        enemy_1.speed_y = random.randint(-1, 1)
                    enemy_1.position[0] += enemy_1.speed_x  # 更新敌机的位置和rect
                    enemy_1.position[1] += enemy_1.speed_y
                    enemy_1.rect.center = enemy_1.position
                    if pygame.time.get_ticks() % 200 == 0:  # 敌机每2秒发一次子弹
                        # 生成精灵
                        new_bullet = pygame.sprite.Sprite()
                        # 生成精灵形状
                        new_bullet.rect = pygame.Rect(0, 0, 4, 15)
                        # 绑定位置  精灵中间底部 = 图片顶部
                        new_bullet.rect.midtop = enemy_1.rect.midbottom
                        # 精灵放入 盒中
                        enemy_bullets.add(new_bullet)
                for enemy_bullet in enemy_bullets:  # 遍历敌机子弹组中的所有子弹
                    pygame.draw.rect(screen, bg_color2, enemy_bullet.rect)  # 画出敌机子弹
                    enemy_bullet.rect.y += 2
                    if enemy_bullet.rect.bottom >= screen_rect.bottom:  # 若子弹出界，则让该子弹移出子弹组
                        enemy_bullets.remove(enemy_bullet)
                    if pygame.sprite.collide_rect(enemy_bullet, flight_1) and not shield:
                        # 若敌方飞机子弹碰到我方飞机，则让我方飞机扣血并让子弹消失
                        flight_1.blood -= 10
                        enemy_bullets.remove(enemy_bullet)
                # ---------------------------------------------------------------------------------
                if len(Max_enemies) < 3 and pygame.time.get_ticks() >= 1000 and max_enemy_exist:
                    new_Max_enemy = flight.Max_Enemy([random.randint(50, 450), -50], screen_rect)
                    Max_enemies.add_internal(new_Max_enemy)
                for Max_enemy in Max_enemies:
                    Max_enemy.Max_draw(screen)
                    Max_enemy.Max_move()
                    if pygame.sprite.collide_rect(flight_1, Max_enemy) and not shield:  # 如果敌方飞机碰到我方飞机，则让我方飞机扣血
                        flight_1.blood -= 10
                    if pygame.time.get_ticks() % 300 == 0:
                        Max_bullet_new1 = flight.Bullets_enemy(
                            [Max_enemy.rect.center[0] + Max_enemy.image.get_width() / 2,
                             Max_enemy.rect.center[1] + Max_enemy.image.get_height() / 2])
                        Max_bullet_new2 = flight.Bullets_enemy(
                            [Max_enemy.rect.center[0] - Max_enemy.image.get_width() / 2,
                             Max_enemy.rect.center[1] + Max_enemy.image.get_height() / 2])
                        bullets_Max_enemy.add_internal(Max_bullet_new1)
                        bullets_Max_enemy.add_internal(Max_bullet_new2)
                    for bullet_1 in self_bullets:
                        if pygame.sprite.collide_rect(Max_enemy, bullet_1):
                            Max_enemy.HP -= 50
                            self_bullets.remove_internal(bullet_1)
                    for bomb_1 in bomb_1s:
                        if pygame.sprite.collide_rect(bomb_1, Max_enemy):
                            bomb_1.draw_bomb_effect(screen)
                            for Max_enemy in Max_enemies:
                                if bomb_1.bomb_rect.left < Max_enemy.rect.x < bomb_1.bomb_rect.right and bomb_1.bomb_rect.top < Max_enemy.rect.y < bomb_1.bomb_rect.bottom:
                                    Max_enemy.HP -= 50
                                    bomb_1s.remove(bomb_1)
                    for bomb_2 in bomb_2s:
                        if pygame.sprite.collide_rect(bomb_2, Max_enemy):
                            Max_enemy.HP -= 50
                            store.money += 5
                    if Max_enemy.HP <= 0:
                        Max_enemies.remove_internal(Max_enemy)
                        store.money += 10
                        boom = flight.Boom(flight_1.rect.center[0], flight_1.rect.center[1], Max_enemy.rect.centerx,
                                           Max_enemy.rect.centery)
                        booms.add_internal(boom)
                for Max_enemy_bullet in bullets_Max_enemy:
                    Max_enemy_bullet.rect.y += 2
                    Max_enemy_bullet.draw(screen)
                    if Max_enemy_bullet.rect.top > screen_rect.bottom:
                        bullets_Max_enemy.remove_internal(Max_enemy_bullet)
                    if pygame.sprite.collide_rect(Max_enemy_bullet, flight_1) and flight_1.blood > 0 and not shield:
                        bullets_Max_enemy.remove_internal(Max_enemy_bullet)
                        flight_1.blood -= 10
                for boom in booms:
                    boom_now = pygame.time.get_ticks()
                    if boom.now_positiony <= boom.rect.centery - boom.dead_flight.get_height() / 2 - 50:
                        screen.blit(boom.dead_flight, [boom.now_positionx, boom.now_positiony])
                    if pygame.time.get_ticks() % 1 == 0:
                        if boom.rect.centerx - boom.dead_flight.get_width() / 2 < boom.now_positionx:
                            boom.now_positionx -= 5
                        if boom.rect.centerx - boom.dead_flight.get_width() / 2 > boom.now_positionx:
                            boom.now_positionx += 5
                        if boom.rect.centery - boom.dead_flight.get_height() / 2 < boom.now_positiony:
                            boom.now_positiony -= 5
                        if boom.rect.centery - boom.dead_flight.get_height() / 2 > boom.now_positiony:
                            boom.now_positiony += 5
                    if boom.now_positiony >= boom.rect.centery - boom.dead_flight.get_height() / 2 - 50 and boom.now_positiony <= boom.rect.centery - boom.dead_flight.get_height() / 2 + 50:
                        if boom_now - boom.ready >= boom.wait:
                            # pygame.draw.rect(screen, color_boom, boom.rect)
                            boom.boom(screen)
                        if boom_now - boom.ready <= boom.wait:
                            # pygame.draw.rect(screen, color_ready, boom.rect)
                            boom.boom_ready(screen)
                        if boom_now - boom.ready >= boom.wait + boom.boom_time:
                            booms.remove_internal(boom)
                        if pygame.sprite.collide_rect(boom,flight_1) and boom_now - boom.ready >= boom.wait and boom_now - boom.ready <= boom.wait + 10 and flight_1.blood > 0 and not shield:
                            flight_1.blood -= 20
                if boss_2_exist:
                    for boss_c in bosses:
                        boss_c.boss_draw(screen)
                        boss_c.boss_move()
                        if pygame.time.get_ticks() % 100 == 0 and boss_c.rect.centery == 100:
                            boss_bullet_new1 = flight.Bullets_enemy([boss_c.rect.center[0] + boss_c.image.get_width() / 2,
                                                              boss_c.rect.center[1] + boss_c.image.get_height() / 2])
                            boss_bullet_new1_left = flight.Bullets_enemy([boss_c.rect.center[0] + boss_c.image.get_width() / 2,
                                                                   boss_c.rect.center[
                                                                       1] + boss_c.image.get_height() / 2])
                            boss_bullet_new1_right = flight.Bullets_enemy(
                                [boss_c.rect.center[0] + boss_c.image.get_width() / 2,
                                 boss_c.rect.center[1] + boss_c.image.get_height() / 2])
                            boss_bullet_new2 = flight.Bullets_enemy([boss_c.rect.center[0] - boss_c.image.get_width() / 2,
                                                              boss_c.rect.center[1] + boss_c.image.get_height() / 2])
                            boss_bullet_new2_left = flight.Bullets_enemy([boss_c.rect.center[0] - boss_c.image.get_width() / 2,
                                                                   boss_c.rect.center[
                                                                       1] + boss_c.image.get_height() / 2])
                            boss_bullet_new2_right = flight.Bullets_enemy(
                                [boss_c.rect.center[0] - boss_c.image.get_width() / 2,
                                 boss_c.rect.center[1] + boss_c.image.get_height() / 2])
                            boss_bullet_new3 = flight.Bullets_enemy(
                                [boss_c.rect.center[0], boss_c.rect.center[1] + boss_c.image.get_height() / 2])
                            boss_bullet_new3_left = flight.Bullets_enemy(
                                [boss_c.rect.center[0], boss_c.rect.center[1] + boss_c.image.get_height() / 2])
                            boss_bullet_new3_right = flight.Bullets_enemy(
                                [boss_c.rect.center[0], boss_c.rect.center[1] + boss_c.image.get_height() / 2])
                            boss_bullets_left.add_internal(boss_bullet_new1_left)
                            boss_bullets_left.add_internal(boss_bullet_new2_left)
                            boss_bullets_left.add_internal(boss_bullet_new3_left)
                            boss_bullets_right.add_internal(boss_bullet_new1_right)
                            boss_bullets_right.add_internal(boss_bullet_new2_right)
                            boss_bullets_right.add_internal(boss_bullet_new3_right)
                            boss_bullets.add_internal(boss_bullet_new1)
                            boss_bullets.add_internal(boss_bullet_new2)
                            boss_bullets.add_internal(boss_bullet_new3)
                        if boss_c.HP <= 4000:
                            boss_c.image = pygame.image.load('image/sprite/boss_death_2.png')
                            boss_c.image = pygame.transform.rotozoom(boss_c.image, 0, 1.2)
                            if len(boss_screen_blacks) < 10 and pygame.time.get_ticks() % 100 == 0:
                                boss_screen_black = flight.screen_black(flight_1.rect.center[0], flight_1.rect.center[1], 0, 0)
                                boss_screen_blacks.add_internal(boss_screen_black)
                        if boss_c.HP <= 2000:
                            boss_c.image = pygame.image.load('image/sprite/boss_death_1.png')
                            boss_c.image = pygame.transform.rotozoom(boss_c.image, 0, 1.2)
                            if len(boss_booms) < 3 and pygame.time.get_ticks() % 200 == 0:
                                boss_boom = flight.Boom(flight_1.rect.center[0], flight_1.rect.center[1], 0, 0)
                                boss_booms.add_internal(boss_boom)
                        for bullet_1 in self_bullets:
                            if pygame.sprite.collide_rect(boss_c, bullet_1):
                                boss_c.HP -= 100
                                self_bullets.remove_internal(bullet_1)
                        for bomb_1 in bomb_1s:
                            if pygame.sprite.collide_rect(bomb_1, boss_c):
                                bomb_1.draw_bomb_effect(screen)
                                if bomb_1.bomb_rect.left < boss_c.rect.x < bomb_1.bomb_rect.right and bomb_1.bomb_rect.top < boss_c.rect.y < bomb_1.bomb_rect.bottom:
                                    boss_c.HP -= 50
                                    bomb_1s.remove(bomb_1)
                        for bomb_2 in bomb_2s:
                            if pygame.sprite.collide_rect(bomb_2, boss_c):
                                boss_c.HP -= 50
                                store.money += 5
                                bomb_2s.remove(bomb_2)
                        if boss_c.HP <= 0:
                            bosses.remove_internal(boss_c)
                        for boss_screen_black in boss_screen_blacks:
                            boss_screen_black_now = pygame.time.get_ticks()
                            if boss_screen_black_now - boss_screen_black.ready >= boss_screen_black.wait:
                                boss_screen_blacks.remove_internal(boss_screen_black)
                            if boss_screen_black_now - boss_screen_black.ready <= boss_screen_black.wait + boss_screen_black.boom_time:
                                boss_screen_black.screen_black_draw(screen)
                        for boss_bullet in boss_bullets:

                            boss_bullet.rect.y += 1
                            boss_bullet.draw(screen)
                            if boss_bullet.rect.top > screen_rect.bottom:
                                boss_bullets.remove_internal(boss_bullet)
                            if pygame.sprite.collide_rect(boss_bullet, flight_1) and flight_1.blood > 0 and not shield:
                                boss_bullets.remove_internal(boss_bullet)
                                flight_1.blood -= 10
                        for boss_bullet in boss_bullets_left:
                            boss_bullet.rect.y += 1
                            boss_bullet.rect.x -= 1
                            boss_bullet.draw(screen)
                            if boss_bullet.rect.top > screen_rect.bottom:
                                boss_bullets_left.remove_internal(boss_bullet)
                            if pygame.sprite.collide_rect(boss_bullet, flight_1) and flight_1.blood > 0 and not shield:
                                boss_bullets_left.remove_internal(boss_bullet)
                                flight_1.blood -= 10
                        for boss_bullet in boss_bullets_right:
                            boss_bullet.rect.y += 1
                            boss_bullet.rect.x += 1
                            boss_bullet.draw(screen)
                            if boss_bullet.rect.top > screen_rect.bottom:
                                boss_bullets_right.remove_internal(boss_bullet)
                            if pygame.sprite.collide_rect(boss_bullet, flight_1) and flight_1.blood > 0 and not shield:
                                boss_bullets_right.remove_internal(boss_bullet)
                                flight_1.blood -= 10
                        for boss_boom in boss_booms:
                            boss_boom_now = pygame.time.get_ticks()
                            if boss_boom_now - boss_boom.ready >= boss_boom.wait:
                                boss_boom.boom_boss_boom(screen)
                            if boss_boom_now - boss_boom.ready <= boss_boom.wait:
                                boss_boom.boom_boss(screen)
                            if boss_boom_now - boss_boom.ready >= boss_boom.wait + boss_boom.boom_time:
                                boss_booms.remove_internal(boss_boom)
                            if pygame.sprite.collide_rect(boss_boom,flight_1) and boss_boom_now - boss_boom.ready >= boss_boom.wait and boss_boom_now - boss_boom.ready <= boss_boom.wait + 1 and flight_1.blood > 0 and not shield:
                                flight_1.blood -= 20
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
                if 1000 <= text_time1 - text_time0 <= 4000:
                    pygame.draw.rect(screen, (0, 128, 128), (0, 700, 600, 200))
                    adjutant_1.draw_text_8(screen)
                    adjutant_1.draw(screen)
                if 1050 <= text_time1 - text_time0 <= 4000:
                    pygame.time.wait(3000)
                if 5000 <= text_time1 - text_time0 <= 10000:
                    pygame.draw.rect(screen, (0, 128, 128), (0, 700, 600, 200))
                    adjutant_1.draw_text_9(screen)
                    adjutant_1.draw(screen)
                    enemy_exist = True
                    max_enemy_exist = True
                if 5050 <= text_time1 - text_time0 <= 10000:
                    pygame.time.wait(5000)
                if 30000 <= text_time1 - text_time0 <= 33000:
                    pygame.draw.rect(screen, (0, 128, 128), (0, 700, 600, 200))
                    adjutant_1.draw_text_10(screen)
                    adjutant_1.draw(screen)
                if 30050 <= text_time1 - text_time0 <= 33000:
                    pygame.time.wait(3000)
                if text_time1-text_time0 >= 33000:
                    boss_2_exist = True
                    enemy_exist = False
                    max_enemy_exist = False
                    if text_time1 - text_time0 <= 34000:
                        pygame.mixer.init()
                        pygame.mixer.music.load("music/Block City Wars OST - Roofs.mp3")
                        pygame.mixer.music.play(5)
                        pygame.mixer.music.set_volume(0.5)
                if boss_c.HP <= 0:
                    boss_2_exist = False
                    pass_game_2 = True
                    game_while_2 = False
                    pygame.mixer.init()
                    pygame.mixer.music.load("music/Graze the Roof.mp3")
                    pygame.mixer.music.play(5)
                    pygame.mixer.music.set_volume(0.5)
                pygame.display.flip()
            text_time0 = pygame.time.get_ticks()
            while game_while_3:
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
                                    game_while_2 = False
                                    game_while_3 = False
                                    win_game = False
                                if interface.button_pause_game.is_over() and event.type == pygame.MOUSEBUTTONDOWN:
                                    # 调用interface中的按钮类判断是否鼠标按到返回游戏按钮
                                    pause_while = False
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
                            if len(self_bullets) < 50:
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
                            if flight_1.blood <= flight_1.blood_max - 50:
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
                                game_while_2 = False
                                game_while_3 = False
                                win_game = False
                        pygame.display.flip()
                if shield:
                    shield_time1 = pygame.time.get_ticks()
                    if shield_time1 - shield_time0 <= 5000:
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
                if len(enemies) < 5 and enemy_exist:  # 若敌机数量小于五，则打印敌机
                    new_enemy = flight.enemy([random.randint(100, 500), -100])
                    enemies.add(new_enemy)
                for enemy_1 in enemies:  # 遍历敌机组中的所有敌机
                    enemy_1.draw(screen)  # 画出敌机
                    if pygame.sprite.collide_rect(flight_1, enemy_1) and not shield:  # 如果敌方飞机碰到我方飞机，则让我方飞机扣血
                        flight_1.blood -= 10
                    for bullet in self_bullets:
                        if pygame.sprite.collide_rect(bullet, enemy_1):  # 如果我方飞机子弹碰到敌方飞机，则让敌方飞机消失
                            enemies.remove(enemy_1)
                            self_bullets.remove(bullet)
                            store.money += 5
                    for bomb_1 in bomb_1s:
                        if pygame.sprite.collide_rect(bomb_1, enemy_1):
                            bomb_1.draw_bomb_effect(screen)
                            for enemy_2 in enemies:
                                if bomb_1.bomb_rect.left < enemy_2.rect.x < bomb_1.bomb_rect.right and bomb_1.bomb_rect.top < enemy_2.rect.y < bomb_1.bomb_rect.bottom:
                                    enemies.remove(enemy_2)
                                    bomb_1s.remove(bomb_1)
                    for bomb_2 in bomb_2s:
                        if pygame.sprite.collide_rect(bomb_2, enemy_1):
                            enemies.remove(enemy_1)
                            store.money += 5
                    if enemy_1.rect.left < screen_rect.left:  # 如果敌方飞机出界，则改变其速度使其飞回
                        enemy_1.speed_x = 1
                    if enemy_1.rect.right > screen_rect.right:
                        enemy_1.speed_x = -1
                    if enemy_1.rect.top < screen_rect.top:
                        enemy_1.speed_y = 1
                    if enemy_1.rect.bottom > screen_rect.bottom:
                        enemy_1.speed_y = -1
                    if pygame.time.get_ticks() % 100 == 0:  # 敌机每0.5秒随机改变一次速度
                        enemy_1.speed_x = random.randint(-1, 1)
                        enemy_1.speed_y = random.randint(-1, 1)
                    enemy_1.position[0] += enemy_1.speed_x  # 更新敌机的位置和rect
                    enemy_1.position[1] += enemy_1.speed_y
                    enemy_1.rect.center = enemy_1.position
                    if pygame.time.get_ticks() % 200 == 0:  # 敌机每2秒发一次子弹
                        # 生成精灵
                        new_bullet = pygame.sprite.Sprite()
                        # 生成精灵形状
                        new_bullet.rect = pygame.Rect(0, 0, 4, 15)
                        # 绑定位置  精灵中间底部 = 图片顶部
                        new_bullet.rect.midtop = enemy_1.rect.midbottom
                        # 精灵放入 盒中
                        enemy_bullets.add(new_bullet)
                for enemy_bullet in enemy_bullets:  # 遍历敌机子弹组中的所有子弹
                    pygame.draw.rect(screen, bg_color2, enemy_bullet.rect)  # 画出敌机子弹
                    enemy_bullet.rect.y += 2
                    if enemy_bullet.rect.bottom >= screen_rect.bottom:  # 若子弹出界，则让该子弹移出子弹组
                        enemy_bullets.remove(enemy_bullet)
                    if pygame.sprite.collide_rect(enemy_bullet, flight_1) and not shield:
                        # 若敌方飞机子弹碰到我方飞机，则让我方飞机扣血并让子弹消失
                        flight_1.blood -= 10
                        enemy_bullets.remove(enemy_bullet)
                # ---------------------------------------------------------------------------------
                if len(Max_enemies) < 3 and pygame.time.get_ticks() >= 1000 and max_enemy_exist:
                    new_Max_enemy = flight.Max_Enemy([random.randint(50, 450), -50], screen_rect)
                    Max_enemies.add_internal(new_Max_enemy)
                for Max_enemy in Max_enemies:
                    Max_enemy.Max_draw(screen)
                    Max_enemy.Max_move()
                    if pygame.sprite.collide_rect(flight_1, Max_enemy) and not shield:  # 如果敌方飞机碰到我方飞机，则让我方飞机扣血
                        flight_1.blood -= 10
                    if pygame.time.get_ticks() % 300 == 0:
                        Max_bullet_new1 = flight.Bullets_enemy(
                            [Max_enemy.rect.center[0] + Max_enemy.image.get_width() / 2,
                             Max_enemy.rect.center[1] + Max_enemy.image.get_height() / 2])
                        Max_bullet_new2 = flight.Bullets_enemy(
                            [Max_enemy.rect.center[0] - Max_enemy.image.get_width() / 2,
                             Max_enemy.rect.center[1] + Max_enemy.image.get_height() / 2])
                        bullets_Max_enemy.add_internal(Max_bullet_new1)
                        bullets_Max_enemy.add_internal(Max_bullet_new2)
                    for bullet_1 in self_bullets:
                        if pygame.sprite.collide_rect(Max_enemy, bullet_1):
                            Max_enemy.HP -= 50
                            self_bullets.remove_internal(bullet_1)
                    for bomb_1 in bomb_1s:
                        if pygame.sprite.collide_rect(bomb_1, Max_enemy):
                            bomb_1.draw_bomb_effect(screen)
                            for Max_enemy in Max_enemies:
                                if bomb_1.bomb_rect.left < Max_enemy.rect.x < bomb_1.bomb_rect.right and bomb_1.bomb_rect.top < Max_enemy.rect.y < bomb_1.bomb_rect.bottom:
                                    Max_enemy.HP -= 50
                                    bomb_1s.remove(bomb_1)
                    for bomb_2 in bomb_2s:
                        if pygame.sprite.collide_rect(bomb_2, Max_enemy):
                            Max_enemy.HP -= 50
                            store.money += 5
                    if Max_enemy.HP <= 0:
                        Max_enemies.remove_internal(Max_enemy)
                        store.money += 10
                        boom = flight.Boom(flight_1.rect.center[0], flight_1.rect.center[1], Max_enemy.rect.centerx,
                                           Max_enemy.rect.centery)
                        booms.add_internal(boom)
                for Max_enemy_bullet in bullets_Max_enemy:
                    Max_enemy_bullet.rect.y += 2
                    Max_enemy_bullet.draw(screen)
                    if Max_enemy_bullet.rect.top > screen_rect.bottom:
                        bullets_Max_enemy.remove_internal(Max_enemy_bullet)
                    if pygame.sprite.collide_rect(Max_enemy_bullet, flight_1) and flight_1.blood > 0 and not shield:
                        bullets_Max_enemy.remove_internal(Max_enemy_bullet)
                        flight_1.blood -= 10
                for boom in booms:
                    boom_now = pygame.time.get_ticks()
                    if boom.now_positiony <= boom.rect.centery - boom.dead_flight.get_height() / 2 - 50:
                        screen.blit(boom.dead_flight, [boom.now_positionx, boom.now_positiony])
                    if pygame.time.get_ticks() % 1 == 0:
                        if boom.rect.centerx - boom.dead_flight.get_width() / 2 < boom.now_positionx:
                            boom.now_positionx -= 5
                        if boom.rect.centerx - boom.dead_flight.get_width() / 2 > boom.now_positionx:
                            boom.now_positionx += 5
                        if boom.rect.centery - boom.dead_flight.get_height() / 2 < boom.now_positiony:
                            boom.now_positiony -= 5
                        if boom.rect.centery - boom.dead_flight.get_height() / 2 > boom.now_positiony:
                            boom.now_positiony += 5
                    if boom.now_positiony >= boom.rect.centery - boom.dead_flight.get_height() / 2 - 50 and boom.now_positiony <= boom.rect.centery - boom.dead_flight.get_height() / 2 + 50:
                        if boom_now - boom.ready >= boom.wait:
                            # pygame.draw.rect(screen, color_boom, boom.rect)
                            boom.boom(screen)
                        if boom_now - boom.ready <= boom.wait:
                            # pygame.draw.rect(screen, color_ready, boom.rect)
                            boom.boom_ready(screen)
                        if boom_now - boom.ready >= boom.wait + boom.boom_time:
                            booms.remove_internal(boom)
                        if pygame.sprite.collide_rect(boom,flight_1) and boom_now - boom.ready >= boom.wait and boom_now - boom.ready <= boom.wait + 10 and flight_1.blood > 0 and not shield:
                            flight_1.blood -= 20
                if boss_3_exist:
                    boss2.move_1()
                    boss2.move_2()
                    boss2.move_3()
                    boss2.SHOOT_1()
                    boss2.SHOOT_2()
                    boss2.SHOOT_3()
                    boss2.SHOOT_5()
                    boss2.draw(screen)
                    for enemy_bullet in boss2.bullets_1:
                        if pygame.sprite.collide_rect(enemy_bullet, flight_1) and not shield:
                            flight_1.blood -= 10
                            boss2.bullets_1.remove(enemy_bullet)
                    for flight_bullet in self_bullets:
                        if pygame.sprite.collide_rect(boss2, flight_bullet):
                            boss2.HP -= 100
                            self_bullets.remove(flight_bullet)
                        for enemy in boss2.enemys_1:
                            if pygame.sprite.collide_rect(enemy, flight_bullet):
                                enemy.HP -= 100
                                self_bullets.remove(flight_bullet)
                        for enemy in boss2.enemys_2:
                            if pygame.sprite.collide_rect(enemy, flight_bullet):
                                enemy.HP -= 100
                                self_bullets.remove(flight_bullet)
                        for enemy in boss2.enemys_3:
                            if pygame.sprite.collide_rect(enemy, flight_bullet):
                                enemy.HP -= 100
                                self_bullets.remove(flight_bullet)
                    for bomb_1 in bomb_1s:
                        if pygame.sprite.collide_rect(bomb_1, boss2):
                            bomb_1.draw_bomb_effect(screen)
                            if bomb_1.bomb_rect.left < boss2.rect.x < bomb_1.bomb_rect.right and bomb_1.bomb_rect.top < boss2.rect.y < bomb_1.bomb_rect.bottom:
                                boss2.HP -= 100
                                bomb_1s.remove(bomb_1)
                            for enemy in boss2.enemys_1:
                                if bomb_1.bomb_rect.left < enemy.rect.x < bomb_1.bomb_rect.right and bomb_1.bomb_rect.top < enemy.rect.y < bomb_1.bomb_rect.bottom:
                                    enemy.HP -= 100
                                    bomb_1s.remove(bomb_1)
                            for enemy in boss2.enemys_2:
                                if bomb_1.bomb_rect.left < enemy.rect.x < bomb_1.bomb_rect.right and bomb_1.bomb_rect.top < enemy.rect.y < bomb_1.bomb_rect.bottom:
                                    enemy.HP -= 100
                                    bomb_1s.remove(bomb_1)
                            for enemy in boss2.enemys_3:
                                if bomb_1.bomb_rect.left < enemy.rect.x < bomb_1.bomb_rect.right and bomb_1.bomb_rect.top < enemy.rect.y < bomb_1.bomb_rect.bottom:
                                    enemy.HP -= 100
                                    bomb_1s.remove(bomb_1)
                    for bomb_2 in bomb_2s:
                        if pygame.sprite.collide_rect(boss2, bomb_2):
                            boss2.HP -= 100
                            bomb_2s.remove(bomb_2)
                        for enemy in boss2.enemys_1:
                            if pygame.sprite.collide_rect(enemy, bomb_2):
                                enemy.HP -= 100
                                bomb_2s.remove(bomb_2)
                        for enemy in boss2.enemys_2:
                            if pygame.sprite.collide_rect(enemy, bomb_2):
                                enemy.HP -= 100
                                bomb_2s.remove(bomb_2)
                        for enemy in boss2.enemys_3:
                            if pygame.sprite.collide_rect(enemy, bomb_2):
                                enemy.HP -= 100
                                bomb_2s.remove(bomb_2)
                    for enemy_bullet in boss2.bullets_2:
                        if pygame.sprite.collide_rect(enemy_bullet, flight_1) and not shield:
                            flight_1.blood -= 10
                            boss2.bullets_2.remove_internal(enemy_bullet)
                    for enemy_bullet in boss2.bullets_3:
                        if pygame.sprite.collide_rect(enemy_bullet, flight_1) and not shield:
                            flight_1.blood -= 10
                            boss2.bullets_3.remove_internal(enemy_bullet)
                    for enemy_bullet in boss2.bullets_4:
                        if pygame.sprite.collide_rect(enemy_bullet, flight_1) and not shield:
                            flight_1.blood -= 10
                            boss2.bullets_4.remove_internal(enemy_bullet)
                    for enemy_bullet in boss2.enemy_1_bullets:
                        if pygame.sprite.collide_rect(enemy_bullet, flight_1) and not shield:
                            flight_1.blood -= 10
                            boss2.enemy_1_bullets.remove_internal(enemy_bullet)
                    for enemy_bullet in boss2.enemy_2_bullets:
                        if pygame.sprite.collide_rect(enemy_bullet, flight_1) and not shield:
                            flight_1.blood -= 10
                            boss2.enemy_2_bullets.remove_internal(enemy_bullet)
                    for enemy_bullet in boss2.enemy_3_bullets:
                        if pygame.sprite.collide_rect(enemy_bullet, flight_1) and not shield:
                            flight_1.blood -= 10
                            boss2.enemy_3_bullets.remove_internal(enemy_bullet)
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
                if 1000 <= text_time1 - text_time0 <= 4000:
                    pygame.draw.rect(screen, (0, 128, 128), (0, 700, 600, 200))
                    adjutant_1.draw_text_11(screen)
                    adjutant_1.draw(screen)
                if 1050 <= text_time1 - text_time0 <= 4000:
                    pygame.time.wait(3000)
                if 5000 <= text_time1 - text_time0 <= 10000:
                    pygame.draw.rect(screen, (0, 128, 128), (0, 700, 600, 200))
                    adjutant_1.draw_text_12(screen)
                    adjutant_1.draw(screen)
                    enemy_exist = True
                    max_enemy_exist = True
                if 5050 <= text_time1 - text_time0 <= 10000:
                    pygame.time.wait(5000)
                if 30000 <= text_time1 - text_time0 <= 33000:
                    pygame.draw.rect(screen, (0, 128, 128), (0, 700, 600, 200))
                    adjutant_1.draw_text_13(screen)
                    adjutant_1.draw(screen)
                if 30050 <= text_time1 - text_time0 <= 33000:
                    pygame.time.wait(3000)
                if text_time1 - text_time0 >= 33000:
                    boss_3_exist = True
                    enemy_exist = False
                    max_enemy_exist = False
                    if text_time1 - text_time0 <= 34000:
                        pygame.mixer.init()
                        pygame.mixer.music.load("music/Block City Wars OST - Halloween.mp3.mp3")
                        pygame.mixer.music.play(5)
                        pygame.mixer.music.set_volume(0.5)
                if boss2.HP <= 0:
                    boss_3_exist = False
                    game_while_3 = False
                    pygame.mixer.init()
                    pygame.mixer.music.load("music/Graze the Roof.mp3")
                    pygame.mixer.music.play(5)
                    pygame.mixer.music.set_volume(0.5)
                pygame.display.flip()
            while win_game:
                interface.win_game_interface()
                for event in pygame.event.get():  # 与外界交互
                    if event.type == pygame.QUIT:  # 添加结束游戏按钮
                        pygame.quit()
                        sys.exit()
                    if interface.win_game_home.is_over() and event.type == pygame.MOUSEBUTTONDOWN:
                        # 调用interface中的按钮类判断是否鼠标按到返回主界面按钮
                        game_while_1 = False
                        game_while_2 = False
                        game_while_3 = False
                        win_game = False
                pygame.display.flip()
        if interface.button_store.is_over() and event.type == pygame.MOUSEBUTTONDOWN:  # 调用interface中的按钮类判断是否鼠标按到商店按钮
            pygame.mixer.init()
            pygame.mixer.music.load("music/our kingdom will fall.mp3")
            pygame.mixer.music.play(5)
            pygame.mixer.music.set_volume(0.5)
            store_while = True
            while store_while:  # 商店界面循环
                interface.store_interface()  # 显示商店界面
                for event in pygame.event.get():  # 与外界交互
                    if event.type == pygame.QUIT:  # 添加结束游戏按钮
                        pygame.quit()
                        sys.exit()
                    if interface.button_store_home.is_over() and event.type == pygame.MOUSEBUTTONDOWN:
                        pygame.mixer.init()
                        pygame.mixer.music.load("music/Graze the Roof.mp3")
                        pygame.mixer.music.play(5)
                        pygame.mixer.music.set_volume(0.5)
                        store_while = False
                    if interface.button_store_blood.is_over() and event.type == pygame.MOUSEBUTTONDOWN and store.money:
                        store.blood += 1
                        store.money -= 20
                    if interface.button_store_bomb_1.is_over() and event.type == pygame.MOUSEBUTTONDOWN and store.money:
                        store.bomb_1 += 1
                        store.money -= 15
                    if interface.button_store_bomb_2.is_over() and event.type == pygame.MOUSEBUTTONDOWN and store.money:
                        store.bomb_2 += 1
                        store.money -= 10
                    if interface.button_store_fix.is_over() and event.type == pygame.MOUSEBUTTONDOWN and store.money:
                        store.fix += 1
                        store.money -= 10
                    if interface.button_store_shield.is_over() and event.type == pygame.MOUSEBUTTONDOWN and store.money:
                        store.shield += 1
                        store.money -= 30
                f = pygame.font.Font('C:/Windows/Fonts/simhei.ttf', 50)
                text_blood = f.render(str(store.blood), True, (255, 0, 0), (255, 255, 255))
                textRect = text_blood.get_rect()
                textRect.topleft = (45, 360)
                screen.blit(text_blood, textRect)
                text_fix = f.render(str(store.fix), True, (255, 0, 0), (255, 255, 255))
                textRect = text_fix.get_rect()
                textRect.topleft = (165, 360)
                screen.blit(text_fix, textRect)
                text_shield = f.render(str(store.shield), True, (255, 0, 0), (255, 255, 255))
                textRect = text_shield.get_rect()
                textRect.topleft = (285, 360)
                screen.blit(text_shield, textRect)
                text_bomb_1 = f.render(str(store.bomb_1), True, (255, 0, 0), (255, 255, 255))
                textRect = text_bomb_1.get_rect()
                textRect.topleft = (405, 360)
                screen.blit(text_bomb_1, textRect)
                text_bomb_2 = f.render(str(store.bomb_2), True, (255, 0, 0), (255, 255, 255))
                textRect = text_bomb_2.get_rect()
                textRect.topleft = (525, 360)
                screen.blit(text_bomb_2, textRect)
                text_money = f.render(str(store.money), True, (255, 0, 0), (255, 255, 255))
                textRect = text_money.get_rect()
                textRect.topleft = (120, 110)
                screen.blit(text_money, textRect)
                pygame.display.flip()
        if interface.button_exit.is_over() and event.type == pygame.MOUSEBUTTONDOWN:
            pygame.quit()
            sys.exit()
    pygame.display.flip()
