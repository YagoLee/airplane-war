import random
import pygame
import sys


class bomb_1(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('image/store/bomb_1_upward.png')
        self.bomb_effect_image = pygame.image.load('image/store/bomb_effect.png')
        self.rect = self.image.get_rect()
        self.bomb_effect_image_rect = self.bomb_effect_image.get_rect()
        self.bomb_rect = pygame.Rect(0, 0, 400, 400)

    def draw(self, surface):
        surface.blit(self.image, self.rect)

    def draw_bomb_effect(self, surface):
        self.bomb_effect_image_rect.center = self.bomb_rect.center
        surface.blit(self.bomb_effect_image, self.bomb_effect_image_rect)


class bomb_2(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('image/store/bomb_2_upward.png')
        self.rect = self.image.get_rect()

    def draw(self, surface):
        surface.blit(self.image, self.rect)


class flight(pygame.sprite.Sprite):  # 我方飞机类

    def __init__(self,position):  # 构造函数：导入我方飞机图片、获取飞机的rect、初始化飞机血量、初始化飞机位置
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.image.load('image/sprite/flight.png')
        self.rect=self.image.get_rect()
        self.rect.center=position
        self.position=position
        self.blood=100
        self.blood_max = 100
        self.shield = pygame.image.load('image/sprite/shield.png')
        self.shield_rect = self.shield.get_rect()
        self.shield_rect.center = self.rect.center

    def draw(self,surface):  # draw函数打印飞机
        surface.blit(self.image, self.rect)

    def draw_blood(self,surface,position):
        pygame.draw.rect(surface, (255, 255, 255), (position[0]-10, position[1]-10, self.blood_max*2+20, 50), 0)
        pygame.draw.rect(surface, (0, 0, 0), (position[0] - 10, position[1] - 10, self.blood_max * 2 + 20, 50), 10)
        pygame.draw.rect(surface, (255, 0, 0),(position[0], position[1], self.blood*2, 30), 0)

    def draw_shield(self,surface):
        self.shield_rect.center = self.rect.center
        surface.blit(self.shield, self.shield_rect)
        # self.shield = pygame.transform.rotate(self.shield, 1)

    pass


class enemy(pygame.sprite.Sprite):  # 敌方飞机类

    def __init__(self,position,speed_x=random.randint(-1,1),speed_y=random.randint(-1,1)):  # 构造函数：导入敌方飞机图片、获取飞机的rect、初始化飞机位置、初始化飞机速度
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('image/sprite/enemy_1.png')
        self.rect = self.image.get_rect()
        self.rect.center = position
        self.position = position
        self.speed_x=speed_x
        self.speed_y=speed_y

    def draw(self,surface):  # draw函数打印飞机
        surface.blit(self.image,self.rect)

    pass


class BULLET(pygame.sprite.Sprite):
    #子弹类也得先传入一个posiiton来标记区域的中心
    def __init__(self,position):
        pygame.sprite.Sprite.__init__(self)
        self.speed=20
        self.image=pygame.Surface((4,15))
        self.image = pygame.image.load('image/sprite/bullet1.png')
        self.image = pygame.transform.rotozoom(self.image,270,0.6)
        self.rect=self.image.get_rect()
        self.speed_x = 0.8
        self.speed_y = 2.0
        self.rect.midtop = position
        self.position = position
        #boss_1的相关变量
        self.shoot4_rect = pygame.Rect(0, 0, 100, 900)
        self.random_speed_x = random.randint(-20,20)/10
        #boss_2的相关变量



    def draw(self,surface):
        surface.blit(self.image,self.rect)
   #BOSS1的属性


class Boss_1(pygame.sprite.Sprite):
    def __init__(self, position, surface):
        pygame.sprite.Sprite.__init__(self)
        self.HP = 5000
        self.image = pygame.image.load('image/sprite/boss1.png')
        self.image = pygame.transform.rotozoom(self.image, 180, 0.4)
        self.rect = self.image.get_rect()
        self.rect.midtop = position
        self.position = position
        self.speed_x = 2
        self.speed_y = 2

        self.timer = pygame.time.get_ticks()
        self.judge_1 = True
        self.judge_2 = False
        self.judge_3 = True
        self.num = 1
        # 我的玩家变量
        # self.player = player([self.rect.center[0], HIGHT - 150])
        # SHOOT1里面的子弹组
        self.bullets_1 = pygame.sprite.Group()

        # SHOOT2里面的子弹组
        self.bullets_2 = pygame.sprite.Group()

        # 子弹射击SHOOT3的子弹组
        self.bullets_3 = pygame.sprite.Group()

        # SHOOT4里面的子弹变量
        self.shoot4 = BULLET([0, 0])

        # SHOOT5里面的子弹组
        self.bullets_5 = pygame.sprite.Group()

        # 图片的展示
        self.surface = surface

    def draw(self, surface):
        surface.blit(self.image, self.rect)

        # 移动方式1：从屏幕上方移动到屏幕的上方

    def move_1(self):
        if self.judge_3:
            self.position[1] += self.speed_y
            self.rect.center = self.position
            if self.position[1] == 150:
                self.judge_3 = False
            self.draw(self.surface)

    # 移动方式2：简单的左右移动
    def move_2(self):
        if self.judge_1:
            if self.rect.centery == 150:
                self.position[0] += self.speed_x
                self.position[1] = self.rect.center[1]
                self.rect.center = self.position
                if self.rect.left < 0:
                    self.rect.left = 0
                    if self.rect.left == 0:
                        self.speed_x = 2
                if self.rect.right > 600:
                    self.rect.right = 600
                    if self.rect.right == 600:
                        self.speed_x = -2
                self.draw(self.surface)
        if self.HP < 2500:
            self.judge_1 = False

        # 移动方式2

    def move_3(self):
        self.speed_x = 5
        if self.timer % 50000 == 0:
            if self.timer % 2 == 0:
                self.rect.x += self.speed_x
                if self.rect.right > screen_rect.right:
                    self.rect.right = screen_rect.right
                    self.speed_x = -self.speed_x
                if self.rect.left < 0:
                    self.rect.left = 0
                    self.speed_x = -self.speed_x
            self.draw(self.surface)

    def move_4(self):
        if self.judge_2:
            # 血量低的时候开启狂暴模式
            if self.HP < 2500:
                self.position[0] += self.speed_x
                self.position[1] += self.speed_y
                # 对第三阶段的boss移动撞墙处理
                if self.rect.right > 600:
                    self.rect.right = 600
                    self.speed_x = -1
                if self.rect.left < 0:
                    self.rect.left = 0
                    self.speed_x = 1
                if self.rect.y < 0:
                    self.rect.y = 0
                    self.speed_y = 1
                if self.rect.y > 900 / 2 - self.rect.height:
                    self.rect.y = 900 / 2 - self.rect.height
                    self.speed_y = -1
                self.rect.center = self.position
                self.draw(self.surface)
        if self.HP < 2500:
            self.judge_2 = True
        # BOSS的攻击方式1

    def SHOOT_1(self):
        if self.rect.top == 150 - (self.rect.height / 2):
            if len(self.bullets_1) < 20:
                # 控制子弹生成的频率，子弹组的长度的控制可以满足不同的视觉效果
                if pygame.time.get_ticks() % 50 == 0:
                    bullet_1 = BULLET([self.rect.midbottom[0], self.rect.midbottom[1]])
                    self.bullets_1.add_internal(bullet_1)
            for bullet1 in self.bullets_1:
                bullet1.position[0] -= 0.8
                bullet1.position[1] += 2
                bullet1.rect.center = bullet1.position
                if bullet1.rect.bottom > 900:
                    self.bullets_1.remove_internal(bullet1)
                bullet1.draw(self.surface)

    def SHOOT_2(self):
        if self.rect.top == 150 - (self.rect.height / 2):
            if len(self.bullets_2) < 20:
                if pygame.time.get_ticks() % 50 == 0:
                    bullet_2 = BULLET([self.rect.midbottom[0], self.rect.midbottom[1]])
                    self.bullets_2.add_internal(bullet_2)
            for bullet2 in self.bullets_2:
                # bullet2.position[0] = self.rect.center[0]
                bullet2.position[1] += 2
                bullet2.rect.center = bullet2.position
                if bullet2.rect.bottom > 900:
                    self.bullets_2.remove_internal(bullet2)
                bullet2.draw(self.surface)

    def SHOOT_3(self):
        if self.rect.top == 150 - (self.rect.height / 2):
            if len(self.bullets_3) < 20:
                if pygame.time.get_ticks() % 50 == 0:
                    bullet_3 = BULLET([self.rect.midbottom[0], self.rect.midbottom[1]])
                    self.bullets_3.add_internal(bullet_3)
            for bullet3 in self.bullets_3:
                bullet3.position[0] += 0.8
                bullet3.position[1] += 2
                bullet3.rect.center = bullet3.position
                if bullet3.rect.bottom > 900:
                    self.bullets_3.remove_internal(bullet3)
                bullet3.draw(self.surface)

    def SHOOT_4(self):
        if self.HP > 2000 and self.HP < 2500 and self.HP > 500 and self.HP < 700:
            self.shoot4.shoot4_rect.midtop = self.rect.midbottom
            pygame.draw.rect(self.surface, (255, 0, 0), self.shoot4.shoot4_rect)

    def SHOOT_5(self):
        if self.HP < 2500:
            if len(self.bullets_5) < 30:
                if pygame.time.get_ticks() % 20 == 0:
                    bullet_5 = BULLET([self.rect.midbottom[0], self.rect.midbottom[1]])
                    self.bullets_5.add_internal(bullet_5)
            for bullet5 in self.bullets_5:
                bullet5.position[0] += bullet5.random_speed_x
                bullet5.position[1] += 2
                bullet5.rect.midtop = bullet5.position
                if bullet5.rect.y > 900:
                    self.bullets_5.remove_internal(bullet5)
                bullet5.draw(self.surface)
            for bullet1 in self.bullets_1:
                bullet1.position[0] -= 0.8
                bullet1.position[1] += 2
                bullet1.rect.center = bullet1.position
                if bullet1.rect.bottom > 900:
                    self.bullets_1.remove_internal(bullet1)
                bullet1.draw(self.surface)
            for bullet2 in self.bullets_2:
                # bullet2.position[0] = self.rect.center[0]
                bullet2.position[1] += 2
                bullet2.rect.center = bullet2.position
                if bullet2.rect.bottom > 900:
                    self.bullets_2.remove_internal(bullet2)
                bullet2.draw(self.surface)
            for bullet3 in self.bullets_3:
                bullet3.position[0] += 0.8
                bullet3.position[1] += 2
                bullet3.rect.center = bullet3.position
                if bullet3.rect.bottom > 900:
                    self.bullets_3.remove_internal(bullet3)
                bullet3.draw(self.surface)


class Boom(pygame.sprite.Sprite):
    def __init__(self,x,y,positionx,positiony):
      pygame.sprite.Sprite.__init__(self)
      self.image_ready = pygame.image.load('image/sprite/大飞机死亡2.png')
      self.image_ready = pygame.transform.rotozoom(self.image_ready, 0,0.82)
      self.image = pygame.image.load('image/sprite/爆炸.png')
      self.image_boss_boom =pygame.transform.rotozoom(self.image, 0, 6.0)
      self.image = pygame.transform.rotozoom(self.image, 0, 1.6)
      self.image_boss = pygame.image.load('image/sprite/smoke.png')
      self.rect = pygame.Rect(0,0,150,150)
      self.x1 = x+random.randint(0, 10)
      if self.x1 >= 700 :
         self.x1 = x
      self.y1 = y+random.randint(0, 10)
      if self.y1 >= 900:
         self.y1 = y
      self.position = [self.x1,self.y1]
      self.rect.center = self.position
      self.ready = pygame.time.get_ticks()
      self.wait = 3000
      self.boom_time = 500
      self.now_positionx = positionx
      self.now_positiony = positiony
      self.dead_flight = pygame.image.load('image/sprite/enemy_2.png')
    def boom_boss_boom(self,surface):
       surface.blit(self.image_boss_boom, self.rect)
    def boom_boss(self,surface):
       surface.blit(self.image_boss, self.rect)
    def boom_ready(self,surface):
       surface.blit(self.image_ready, self.rect)
    def boom(self,surface):
       surface.blit(self.image, self.rect)


class Max_Enemy(pygame.sprite.Sprite):
   def __init__(self, position, screen_rect):
      pygame.sprite.Sprite.__init__(self)
      self.HP = 200
      # self.image=pygame.Surface((50,50))#定义敌人图像的大小
      self.image = pygame.image.load('image/sprite/enemy_2.png')
      self.rect = self.image.get_rect()
      self.rect.center = position
      self.position = position
      tuple(self.position)
      self.speed_x = 1
      self.speed_y = 1  # 飞机飞来的速度
      self.timer = 0  # 初始化计时器
      self.change_interval = 1000  # 设置移动时间的间隔
      self.screen_rect = screen_rect

   def Max_move(self):
      self.timer = pygame.time.get_ticks()  # 计时器
      # 每隔一秒飞机的速度方向和大小将会重置以完成敌机的随机移动
      if self.timer % 1000 == 0:
         self.speed_x = random.randint(-1, 1)
         self.speed_y = random.randint(-1, 1)
      # 通过敌机区域和屏幕区域边缘的判定来实现敌机的碰墙反弹
      if self.rect.left < 0:
         self.speed_x = 1
      if self.rect.right > 600:
         self.speed_x = -1
      if self.rect.top < 0:
         self.speed_y = 1
      if self.rect.bottom > 900 / 2:
         self.speed_y = -1
      self.position[0] += self.speed_x
      self.position[1] += self.speed_y
      self.rect.center = self.position


   def Max_draw(self, surface):
      surface.blit(self.image, self.rect)


class Bullets_enemy(pygame.sprite.Sprite):
   def __init__(self, position1, speed=1):

      pygame.sprite.Sprite.__init__(self)
      self.speed = speed
      self.rect = pygame.Rect(0,0,4,15)
      self.rect.center = position1
      self.position = position1
      self.color = "red"

   def draw(self, surface):
      pygame.draw.rect(surface, self.color, self.rect)


class Boss(pygame.sprite.Sprite):
   def __init__(self, position):
      pygame.sprite.Sprite.__init__(self)
      self.HP = 7000
      self.image = pygame.image.load('image/sprite/boss濒死.png')
      self.image = pygame.transform.rotozoom(self.image,0,1.2)
      self.rect = self.image.get_rect()
      self.rect.center = position
      self.position = position
      self.speed_x = 0
      self.speed_y = 0
      self.timer = 0  # 初始化计时器
      self.change_interval = 1000  # 设置移动时间的间隔
   def boss_move(self):
      self.timer = pygame.time.get_ticks()  # 计时器
      if self.rect.centery != 100:
         self.speed_y = 1
      if self.rect.centery == 100:
         self.speed_y = 0
      if self.timer % 1000 == 0 and self.rect.centery == 100:
         self.speed_x = random.randint(-1, 1)
      if self.rect.left < 0:
         self.speed_x = 1
      if self.rect.right > 600:
         self.speed_x = -1
      if self.rect.centery != 100:
         self.position[1] += self.speed_y
      if self.rect.centery == 100:
         self.position[0] += self.speed_x
      self.rect.center = self.position



   def boss_draw(self,surface):
      surface.blit(self.image, self.rect)

class screen_black(pygame.sprite.Sprite):
    def __init__(self, x, y, positionx, positiony):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('image/sprite/smoke.png')
        self.rect = self.image.get_rect()
        self.x1 = x + random.randint(0, 10)
        if self.x1 >= 600:
            self.x1 = x
        self.y1 = y + random.randint(0, 10)
        if self.y1 >= 900:
            self.y1 = y
        self.position = [self.x1, self.y1]
        self.rect.center = self.position
        self.ready = pygame.time.get_ticks()
        self.wait = 3000
        self.boom_time = 500
        self.now_positionx = positionx
        self.now_positiony = positiony


    def screen_black_draw(self, surface):
        surface.blit(self.image, self.rect)


class Enemy(pygame.sprite.Sprite):
    def __init__(self,position):
        pygame.sprite.Sprite.__init__(self)
        self.HP=600
        #self.image=pygame.Surface((50,50))#定义敌人图像的大小
        self.image=pygame.image.load('image/sprite/boss3.png')
        self.image = pygame.transform.rotozoom(self.image,0,0.6)
        self.rect=self.image.get_rect()
        self.rect.center = position
        self.position=position
        self.bullets_1 = pygame.sprite.Group()
        tuple(self.position)
        self.speed_x=2
        self.speed_y=2#飞机飞来的速度
        self.timer=0#初始化计时器
        self.change_interval=1000#设置移动时间的间隔
    def move(self):
        self.timer=pygame.time.get_ticks()# 计时器
        #每隔一秒飞机的速度方向和大小将会重置以完成敌机的随机移动
        if self.timer % 200 == 0:
            self.speed_x=random.randint(-2,2)
            self.speed_y=random.randint(-2,2)
        #通过敌机区域和屏幕区域边缘的判定来实现敌机的碰墙反弹
        if self.rect.left < 0:
            self.speed_x = 2
        if self.rect.right > 600:
            self.speed_x = -2
        if self.rect.top < 0:
            self.speed_y = 2
        if self.rect.bottom > 900/2:
            self.speed_y = -2
        #if pygame.time.get_ticks() % 1 == 0:
        self.position[0] += self.speed_x
        self.position[1] += self.speed_y
        self.rect.center = self.position

    def draw(self,surface):
        surface.blit(self.image,self.rect)


class Boss_2(Enemy):
    def __init__(self,position,screen):
        pygame.sprite.Sprite.__init__(self)
        #pygame.sprite.Sprite__init__(self)
        self.HP = 8000
        self.speed_x = 2
        self.speed_y = 2
        self.position = position
        self.center = position
        self.image = pygame.image.load('image/sprite/boss3 (2).png')
        self.image = pygame.transform.rotozoom(self.image, 180, 0.7)
        self.rect = self.image.get_rect()
        self.screen = screen
        #函数中的计时器
        self.timer = pygame.time.get_ticks()
        #函数中的判定变量
        #SHOOT1-3里面的
        self.judge_1 = True
        self.judge_2 = False
        self.judge_3 = True
        self.judge_4 = False
        self.judge_5 = True
        self.judge_12 = True
        self.judge_13 = False
        #SHOOT4中的判定变量
        self.judge_6 = True
        self.judge_7 = False
        self.judge_8 = False
        self.counter = 0
        #SHOOT_5中的变量
        self.enemys = pygame.sprite.Group()
        self.judge_9 = True
        self.judge_10 = True
        self.judge_11 = True
        self.judge_14 = False



        #SHOOT_1中的子弹组
        self.bullets_1 = pygame.sprite.Group()
        self.bullets_2 = pygame.sprite.Group()
        self.bullets_3 = pygame.sprite.Group()
        self.bullets_4 = pygame.sprite.Group()
        self.bullets_5 = pygame.sprite.Group()

        #SHOOT5里面的子弹组
        self.enemys_1 = pygame.sprite.Group()
        self.enemys_2 = pygame.sprite.Group()
        self.enemys_3 = pygame.sprite.Group()

        #SHOOT4中的东西
        self.shoot4_bullet_1 =BULLET([0,0])
        #爆炸炸弹中的组
        #SHOOT5里面的东西
        self.enemy_1_bullets = pygame.sprite.Group()
        self.enemy_2_bullets = pygame.sprite.Group()
        self.enemy_3_bullets = pygame.sprite.Group()

    def draw(self,surface):
        surface.blit(self.image, self.rect)


    def move_1(self):
        if self.judge_5:
            self.position[1] += self.speed_y
            self.rect.center = self.position
            self.draw(self.screen)
            if self.position[1] == 150:
                self.judge_5 = False
    def move_2(self):
        if not self.judge_5 and self.judge_12:
            self.position[0] += self.speed_x
            self.position[1] = self.rect.centery
            self.rect.center = self.position
            if self.rect.right > 600:
                self.rect.right = 600
                if self.rect.right == 600:
                    self.speed_x = -2
            if self.rect.left < 0:
                self.rect.left = 0
                if self.rect.left == 0:
                    self.speed_x = 2
            self.draw(self.screen)

    def move_3(self):
        if self.HP < 3500 and self.HP > 0:
            self.judge_12 = False
            self.judge_14 = True
            if self.rect.centerx > 300:
                self.position[0] -= 2
                self.rect.center =self.position
            if self.rect.centerx < 300:
                self.position[0] += 2
                self.rect.center = self.position
            if self.rect.centerx == 300:
                self.rect.centerx = 300
                self.judge_13 =True
            self.draw(self.screen)



    def SHOOT_1(self):
        if not self.judge_5 and self.judge_12:
            m_1 = [1, 0.9, 0.8, 0.7, 0.6, 0.5, 0.4, 0.3, 0.2, 0.1, 0,-0.1,-0.2,-0.3,-0.4,-0.5,-0.6,-0.7,-0.8,-0.9,-1]
            x_1 = [1.5,1.6,1.7,1.8,1.9,2.0, 2.1, 2.2, 2.3, 2.4, 2.5, 2.4, 2.3, 2.2, 2.1, 2.0,1.9,1.8,1.7,1.6,1.5]
            n_1 = 0
            if self.judge_3:
                bullet_1 = BULLET([self.rect.midbottom[0] - 75, self.rect.midbottom[1]])
                bullet_1.image = pygame.image.load("image/sprite/bullet2.png")
                bullet_1.image = pygame.transform.rotozoom(bullet_1.image, 0, 0.3)
                self.bullets_1.add(bullet_1)
            # 加入的判定条件即只有在所有子弹都射出屏幕外子弹组才会自动加入子弹
            if len(self.bullets_1) == 0:
                self.judge_4 = False
                self.judge_3 = True
            if len(self.bullets_1) == 21:
                self.judge_4 = True
                self.judge_3 = False
            if self.judge_4 and self.judge_1:
                for bullet1 in self.bullets_1:
                    bullet1.position[0] -= m_1[n_1]
                    bullet1.position[1] += x_1[n_1]
                    bullet1.rect.center = bullet1.position
                    n_1 += 1
                    if bullet1.rect.top > 900:
                        self.bullets_1.remove_internal(bullet1)
                    bullet1.draw(self.screen)
    def SHOOT_2 (self) :
        if not self.judge_5 and self.judge_12:
            m_2 = [1, 0.9, 0.8, 0.7, 0.6, 0.5, 0.4, 0.3, 0.2, 0.1, 0,-0.1,-0.2,-0.3,-0.4,-0.5,-0.6,-0.7,-0.8,-0.9,-1]
            x_2 = [1.5,1.6,1.7,1.8,1.9,2.0, 2.1, 2.2, 2.3, 2.4, 2.5, 2.4, 2.3, 2.2, 2.1, 2.0,1.9,1.8,1.7,1.6,1.5]
            n_2 = 0
            if self.judge_2:
                bullet_2 = BULLET([self.rect.midbottom[0]+75,self.rect.midbottom[1]])
                bullet_2.image = pygame.image.load("image/sprite/bullet2.png")
                bullet_2.image = pygame.transform.rotozoom(bullet_2.image,0,0.3)
                self.bullets_2.add(bullet_2)
            #加入的判定条件即只有在所有子弹都射出屏幕外子弹组才会自动加入子弹
            #但是有个缺点就是等所有子弹移除，那这个时间间隔有点长
            if len(self.bullets_2) == 0:
                self.judge_1 = False
                self.judge_2 = True
            if len(self.bullets_2) ==21:
                self.judge_1 = True
                self.judge_2 =False
            if self.judge_1 and self.judge_4:
                for bullet2 in self.bullets_2:
                    bullet2.position[0] += m_2[n_2]
                    bullet2.position[1] += x_2[n_2]
                    bullet2.rect.center = bullet2.position
                    n_2 += 1
                    if bullet2.rect.top > 900:
                        self.bullets_2.remove_internal(bullet2)
                    bullet2.draw(self.screen)
    #子弹的任意方向的发射
    def SHOOT_3(self):
        if self.rect.centery == 150 :
            if len(self.bullets_3) < 16:
                if pygame.time.get_ticks() % 12 ==0:
                    bullet_3 = BULLET([self.rect.midbottom[0]+75,self.rect.midbottom[1]])
                    bullet_3.image = pygame.image.load("image/sprite/bullet2.png")
                    bullet_3.image = pygame.transform.rotozoom(bullet_3.image,0,0.3)
                    self.bullets_3.add(bullet_3)
            for bullet3 in self.bullets_3:
                bullet3.position[0] += bullet3.random_speed_x
                bullet3.position[1] += 2
                bullet3.rect.center = bullet3.position
                if bullet3.rect.top > 900:
                    self.bullets_3.remove(bullet3)
                bullet3.draw(self.screen)
            if len(self.bullets_4) < 16:
                if pygame.time.get_ticks() % 12 == 0:
                    bullet_4 = BULLET([self.rect.midbottom[0]-75,self.rect.midbottom[1]])
                    bullet_4.image = pygame.image.load("image/sprite/bullet2.png")
                    bullet_4.image = pygame.transform.rotozoom(bullet_4.image,0,0.3)
                    bullet_4.rect = bullet_4.image.get_rect()
                    self.bullets_4.add(bullet_4)
            for bullet4 in self.bullets_4:
                bullet4.position[0] += bullet4.random_speed_x
                bullet4.position[1] += 2
                bullet4.rect.center = bullet4.position
                if bullet4.rect.top > 900:
                    self.bullets_4.remove(bullet4)
                bullet4.draw(self.screen)

    def SHOOT_5(self):
        if self.judge_13:
            m_2 = [1, 0.9, 0.8, 0.7, 0.6, 0.5, 0.4, 0.3, 0.2, 0.1, 0, -0.1, -0.2, -0.3, -0.4, -0.5, -0.6, -0.7, -0.8,
                   -0.9, -1]
            x_2 = [1.5, 1.6, 1.7, 1.8, 1.9, 2.0, 2.1, 2.2, 2.3, 2.4, 2.5, 2.4, 2.3, 2.2, 2.1, 2.0, 1.9, 1.8, 1.7, 1.6,
                   1.5]
            n_2 = 0
            m_1 = [1, 0.9, 0.8, 0.7, 0.6, 0.5, 0.4, 0.3, 0.2, 0.1, 0, -0.1, -0.2, -0.3, -0.4, -0.5, -0.6, -0.7, -0.8,
                   -0.9, -1]
            x_1 = [1.5, 1.6, 1.7, 1.8, 1.9, 2.0, 2.1, 2.2, 2.3, 2.4, 2.5, 2.4, 2.3, 2.2, 2.1, 2.0, 1.9, 1.8, 1.7, 1.6,
                   1.5]
            n_1 = 0
            for bullet1 in self.bullets_1:
                bullet1.position[0] -= m_1[n_1]
                bullet1.position[1] += x_1[n_1]
                bullet1.rect.center = bullet1.position
                n_1 += 1
                if bullet1.rect.top > 900:
                    self.bullets_1.remove_internal(bullet1)
                self.bullets_1.draw(self.screen)
            for bullet2 in self.bullets_2:
                bullet2.position[0] += m_2[n_2]
                bullet2.position[1] += x_2[n_2]
                bullet2.rect.center = bullet2.position
                n_2 += 1
                if bullet2.rect.top > 900:
                    self.bullets_2.remove_internal(bullet2)
                self.bullets_2.draw(self.screen)
            if self.rect.centerx == 300:
                if len(self.enemys_1) < 2:
                    enemy_1 = Enemy([self.rect.midleft[0]-30,self.rect.midleft[1]])
                    self.enemys_1.add(enemy_1)
                for enemy in self.enemys_1:
                    enemy.move()
                    enemy.draw(self.screen)
                    if enemy.HP < 0:
                        self.enemys_1.remove(enemy)
                    if len(self.enemy_1_bullets) < 50:
                        if pygame.time.get_ticks() % 50 == 0:
                            bullet_1 = BULLET([enemy.rect.midleft[0]-30, enemy.rect.midleft[1]])
                            self.enemy_1_bullets.add_internal(bullet_1)
                    for bullet in self.enemy_1_bullets:
                        bullet.position[1] += 1.5
                        bullet.rect.center = bullet.position
                        bullet.draw(self.screen)
                        if bullet.rect.midbottom[1] > 900:
                            self.enemy_1_bullets.remove_internal(bullet)
                if len(self.enemys_2) < 1:
                    enemy_2 = Enemy([self.rect.midbottom[0],self.rect.midbottom[1]+30])
                    self.enemys_2.add(enemy_2)
                for enemy in self.enemys_2:
                    enemy.move()
                    enemy.draw(self.screen)
                    if enemy.HP < 0:
                        self.enemys_2.remove(enemy)
                    if len(self.enemy_2_bullets) < 50:
                        if pygame.time.get_ticks() % 50 == 0:
                            bullet_2 = BULLET([enemy.rect.midbottom[0], enemy.rect.midbottom[1]+30])
                            self.enemy_2_bullets.add_internal(bullet_2)
                    for bullet in self.enemy_2_bullets:
                        bullet.position[1] += 1.5
                        bullet.rect.center = bullet.position
                        bullet.draw(self.screen)
                        if bullet.rect.midbottom[1] > 900:
                            self.enemy_2_bullets.remove_internal(bullet)
                if len(self.enemys_3) < 2:
                    enemy_3 = Enemy([self.rect.midright[0]+30, self.rect.midright[1] ])
                    self.enemys_3.add(enemy_3)
                for enemy in self.enemys_3:
                    enemy.move()
                    enemy.draw(self.screen)
                    if enemy.HP < 0:
                        self.enemys_3.remove(enemy)
                    if len(self.enemy_3_bullets) < 50:
                        if pygame.time.get_ticks() % 50 == 0:
                            bullet_3 = BULLET([enemy.rect.midright[0]+30, enemy.rect.midright[1]])
                            self.enemy_3_bullets.add_internal(bullet_3)
                    for bullet in self.enemy_3_bullets:
                        bullet.position[1] += 1.5
                        bullet.rect.center = bullet.position
                        bullet.draw(self.screen)
                        if bullet.rect.midbottom[1] > 900:
                            self.enemy_3_bullets.remove_internal(bullet)





            '''if len(self.enemys_2) < 2:
                enemy_2 = Enemy([self.rect.midright[0]+30, self.rect.midright[1]])
                self.enemys_2.add(enemy_2)
            for enemy in self.enemys_2:
                if pygame.time.get_ticks() % 1000 == 0:
                    enemy.speed_x = random.randint(-2, 2)
                    enemy.speed_y = random.randint(-2, 2)
                if pygame.time.get_ticks() % 2 ==0:
                    enemy.position[0] += enemy.speed_x
                    enemy.position[1] += enemy.speed_y
                    enemy.rect.center = enemy.position
                if enemy.rect.left < self.rect.midright[1]+30:
                    enemy.rect.left = 0
                    enemy.position[0] += enemy.speed_x
                    enemy.rect.center = enemy.position
                if enemy.rect.bottom > 450:
                    enemy.rect.bottom = 450
                    enemy.position[1] -= enemy.speed_y
                    enemy.rect.center = enemy.position
                if enemy.rect.right > 600:
                    enemy.rect.right = 600
                    enemy.position[0] -= enemy.speed_x
                    enemy.rect.center = enemy.position
                if enemy.rect.top < 0:
                    enemy.rect.top = 0
                    enemy.position[1] += enemy.speed_y
                    enemy.rect.center = enemy.position


                enemy.draw(self.screen)


                if len(self.enemys_3) < 2:
                    enemy_3 = Enemy([self.rect.midbottom[0], self.rect.midbottom[1]+30])
                    self.enemys_2.add(enemy_3)
                for enemy in self.enemys_3:
                    if pygame.time.get_ticks() % 1000 == 0:
                        enemy.speed_x = random.randint(-2, 2)
                        enemy.speed_y = random.randint(-2, 2)
                    if pygame.time.get_ticks() % 2 == 0:
                        enemy.position[0] += enemy.speed_x
                        enemy.position[1] += enemy.speed_y
                        enemy.rect.center = enemy.position
                    if enemy.rect.left < 0:
                        enemy.rect.left = 0
                        enemy.position[0] += enemy.speed_x
                        enemy.rect.center = enemy.position
                    if enemy.rect.bottom > 450:
                        enemy.rect.bottom = 450
                        enemy.position[1] -= enemy.speed_y
                        enemy.rect.center = enemy.position
                    if enemy.rect.right > 600:
                        enemy.rect.right = 600
                        enemy.position[0] -= enemy.speed_x
                        enemy.rect.center = enemy.position
                    if enemy.rect.top < self.rect.midbottom[1]+30:
                        enemy.rect.top = 0
                        enemy.position[1] += enemy.speed_y
                        enemy.rect.center = enemy.position
                    enemy.draw(self.screen)'''





            '''enemy_1 = Enemy([self.rect.centerx-50, self.rect.centery])
            enemy_2 = Enemy([self.rect.centerx, self.rect.centery+30])
            enemy_3 = Enemy([self.rect.centerx+50, self.rect.centery])
            enemy_1.HP = 500
            enemy_2.HP = 500
            enemy_3.HP = 500
            if self.judge_9 and self.judge_10 and self.judge_11:
                self.enemys.add(enemy_1)
                self.enemys.add(enemy_2)
                self.enemys.add(enemy_3)
                self.judge_9 = False
                self.judge_10 = False
                self.judge_11 = False
            if not self.judge_9 or not self.judge_10 or not self.judge_11:
                if not self.judge_9:
                    enemy_1.timer = pygame.time.get_ticks()  # 计时器
                    # 每隔一秒飞机的速度方向和大小将会重置以完成敌机的随机移动
                    if pygame.time.get_ticks() % 2 == 0:
                        enemy_1.speed_x = random.randint(-1, 1) / 10
                        enemy_1.speed_y = random.randint(-1, 1) / 10
                    # 通过敌机区域和屏幕区域边缘的判定来实现敌机的碰墙反弹
                    if enemy_1.rect.left < 0:
                        enemy_1.speed_x = 0.1
                    if enemy_1.rect.right > 600:
                        enemy_1.speed_x = -0.1
                    if enemy_1.rect.top < 0:
                        enemy_1.speed_y = 0.1
                    if enemy_1.rect.bottom > 900 / 2:
                        enemy_1.speed_y = -0.1
                    if pygame.time.get_ticks() % 2 ==0:
                        enemy_1.position[0] += enemy_1.speed_x
                        enemy_1.position[1] += enemy_1.speed_y
                        enemy_1.rect.center = enemy_1.position
                        enemy_1.draw(self.screen)
                    if len(self.enemy_1_bullets) < 10:
                        if len(self.enemy_1_bullets) % 4 == 0:
                            if  pygame.time.get_ticks() % 350 == 0:
                                enemy_1_bullet = BULLET([enemy_1.rect.midbottom[0],enemy_1.rect.midbottom[1]])
                        else:
                            enemy_1_bullet = BULLET([enemy_1.rect.midbottom[0],enemy_1.rect.midbottom[1]])
                            self.enemy_1_bullets.add_internal(enemy_1_bullet)
                        for bullet in self.enemy_1_bullets:
                            bullet.position[1] += 2
                            bullet.rect.midtop = bullet.position
                            if bullet.rect.midtop[1] > 900:
                                self.enemy_1_bullets.remove_internal(bullet)
                            bullet.draw(self.screen)
                if self.judge_9:
                    if pygame.time.get_ticks() % 1500 == 0:
                        enemy_1 = Enemy([self.rect.centerx-50, self.rect.centery])
                        self.enemys.add(enemy_1)
                        self.judge_9 = False
    
                if not self.judge_10:
                    enemy_2.timer = pygame.time.get_ticks()  # 计时器
                    # 每隔一秒飞机的速度方向和大小将会重置以完成敌机的随机移动
                    if pygame.time.get_ticks() % 2 == 0:
                        enemy_2.speed_x = random.randint(-1, 1) / 10
                        enemy_2.speed_y = random.randint(-1, 1) / 10
                    # 通过敌机区域和屏幕区域边缘的判定来实现敌机的碰墙反弹
                    if enemy_2.rect.left < 0:
                        enemy_2.speed_x = 0.1
                    if enemy_2.rect.right > 600:
                        enemy_2.speed_x = -0.1
                    if enemy_2.rect.top < 0:
                        enemy_2.speed_y = 0.1
                    if enemy_2.rect.bottom > 900 / 2:
                        enemy_2.speed_y = -0.1
                    #if pygame.time.get_ticks() % 2 == 0:
                    enemy_2.position[0] += enemy_2.speed_x
                    enemy_2.position[1] += enemy_2.speed_y
                    enemy_2.rect.center = enemy_2.position
                        enemy_2.draw(self.screen)
                    if len(self.enemy_2_bullets) < 10:
                        if len(self.enemy_2_bullets) % 4 == 0:
                            if pygame.time.get_ticks() % 350 == 0:
                                enemy_2_bullet = BULLET([enemy_2.rect.midbottom[0], enemy_2.rect.midbottom[1]])
                                self.enemy_2_bullets.add(enemy_2_bullet)
                        else:
                            enemy_2_bullet = BULLET([enemy_2.rect.midbottom[0], enemy_2.rect.midbottom[1]])
                            self.enemy_2_bullets.add(enemy_2_bullet)
                        for bullet in self.enemy_2_bullets:
                            bullet.position[1] += 2
                            bullet.rect.midtop = bullet.position
                            if bullet.rect.midtop[1] > 900:
                                self.enemy_2_bullets.remove_internal(bullet)
                            bullet.draw(self.screen)
                if self.judge_10:
                    if pygame.time.get_ticks() %1500 == 0:
                        enemy_2 = Enemy([self.rect.centerx,self.rect.centery+50])
                        self.enemys.add(enemy_2)
                        self.judge_10 = False


                if not  self.judge_11:
                    enemy_3.timer = pygame.time.get_ticks()  # 计时器
                    # 每隔一秒飞机的速度方向和大小将会重置以完成敌机的随机移动
                    if pygame.time.get_ticks() % 1000 == 0:
                        enemy_3.speed_x = random.randint(-10, 10) / 10
                        enemy_3.speed_y = random.randint(-10, 10) / 10
                    # 通过敌机区域和屏幕区域边缘的判定来实现敌机的碰墙反弹
                    if enemy_3.rect.left < 0:
                        enemy_3.speed_x = 0.1
                    if enemy_3.rect.right > 600:
                        enemy_3.speed_x = -0.1
                    if enemy_3.rect.top < 0:
                        enemy_3.speed_y = 0.1
                    if enemy_3.rect.bottom > 900 / 2:
                        enemy_3.speed_y = -0.1
                    #if pygame.time.get_ticks() % 2 == 0:
                    enemy_3.move()
                    enemy_3.draw(self.screen)
                    if len(self.enemy_3_bullets) < 10:
                        if len(self.enemy_3_bullets) % 4 == 0:
                            if pygame.time.get_ticks() % 50 == 0:
                                enemy_3_bullet = BULLET([enemy_3.rect.midbottom[0], enemy_3.rect.midbottom[1]])
                                self.enemy_3_bullets.add(enemy_3_bullet)
                        else:
                            enemy_3_bullet = BULLET([enemy_3.rect.midbottom[0], enemy_3.rect.midbottom[1]])
                            self.enemy_3_bullets.add(enemy_3_bullet)
                        for bullet in self.enemy_3_bullets:
                            bullet.position[1] += 2
                            bullet.rect.midtop = bullet.position
                            if bullet.rect.midtop[1] > 900:
                                self.enemy_3_bullets.remove_internal(bullet)
                            bullet.draw(self.screen)
                if self.judge_11:
                    if pygame.time.get_ticks() % 1500 == 0:
                        enemy_3 = Enemy([self.rect.centerx+50, self.rect.centery])
                        self.enemys.add(enemy_3)
                        self.judge_11 = False'''




if __name__=='__main__':  # 测试程序

    pygame.init()  # 游戏初始化
    screen_image = pygame.display.set_mode((600, 900))  # 初始化屏幕
    screen_rect = screen_image.get_rect()  # 得到屏幕的rect
    pygame.display.set_caption('flight')  # 设置标题
    bg_color1 = (0, 128, 128)  # 初始化颜色
    bg_color2 = (60, 60, 60)
    bg_color3 = (255, 0, 0)
    moving_left = False  # 初始化我方飞机移动方向判定变量
    moving_right = False
    moving_up=False
    moving_down=False
    self_bullets = pygame.sprite.Group()  # 创建我方子弹精灵组
    enemy_bullets = pygame.sprite.Group()  # 创建敌方飞机子弹精灵组
    enemies=pygame.sprite.Group()  # 创建敌方飞机精灵组
    flight_1=flight([200,650])  # 创建我方飞机对象
    while True:
        for event in pygame.event.get():  # 与外界交互
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:  # 若按下上下左右键分别将判断我方飞机上下左右移动的变量改为true
                if event.key == pygame.K_LEFT:
                    moving_left = True
                if event.key == pygame.K_RIGHT:
                    moving_right = True
                if event.key == pygame.K_UP:
                    moving_up=True
                if event.key == pygame.K_DOWN:
                    moving_down=True
                if event.key == pygame.K_SPACE and flight_1.blood>0:  # 若按下空格键、飞机血量大于0并且屏幕中子弹数量小于2则产生子弹
                    if len(self_bullets) < 2:
                        # 生成精灵
                        new_bullet = pygame.sprite.Sprite()
                        # 生成精灵形状
                        new_bullet.rect = pygame.Rect(0, 0, 4, 15)
                        # 绑定位置  精灵中间底部 = 图片顶部
                        new_bullet.rect.midbottom = flight_1.rect.midtop
                        # 精灵放入 盒中
                        self_bullets.add(new_bullet)
            elif event.type == pygame.KEYUP:  # 若放开上下左右键分别将判断我方飞机上下左右移动的变量改为false
                if event.key == pygame.K_LEFT:
                    moving_left = False
                if event.key == pygame.K_RIGHT:
                    moving_right = False
                if event.key == pygame.K_UP:
                    moving_up=False
                if event.key == pygame.K_DOWN:
                    moving_down=False
        if moving_left and flight_1.rect.left:  # 若判断我方飞机上下左右移动的变量为true且飞机在屏幕范围内，则让飞机上下左右移动
            flight_1.position[0] -= 1
            flight_1.rect.center=flight_1.position  # 更新飞机的rect
        if moving_right and flight_1.rect.right < screen_rect.right:
            flight_1.position[0] += 1
            flight_1.rect.center=flight_1.position
        if moving_up and flight_1.rect.top:
            flight_1.position[1]-=1
            flight_1.rect.center = flight_1.position
        if moving_down and flight_1.rect.bottom<screen_rect.bottom:
            flight_1.position[1]+=1
            flight_1.rect.center = flight_1.position
        screen_image.fill(bg_color1)  # 打印背景
        if flight_1.blood>0:  # 如果飞机血量大于0，则打印飞机
            flight_1.draw(screen_image)
            flight_1.draw_shield(screen_image)
        if len(enemies)<5:  # 若敌机数量小于五，则打印敌机
            new_enemy=enemy([random.randint(100,500),random.randint(100,400)])
            enemies.add(new_enemy)
        for bullet in self_bullets:  # 遍历我方子弹组中所有子弹
            pygame.draw.rect(screen_image, bg_color2, bullet.rect)  # 画出子弹
            bullet.rect.y -= 1  # 将子弹向上移动
            if bullet.rect.top <= 0:
                self_bullets.remove(bullet)  # 若子弹处屏幕则将子弹移出精灵组
        for enemy_1 in enemies:  # 遍历敌机组中的所有敌机
            enemy_1.draw(screen_image)  # 画出敌机
            if pygame.sprite.collide_rect(flight_1, enemy_1):  # 如果敌方飞机碰到我方飞机，则让我方飞机扣血
                flight_1.blood-=20
            for bullet in self_bullets:
                if pygame.sprite.collide_rect(bullet,enemy_1):  # 如果我方飞机子弹碰到敌方飞机，则让敌方飞机消失
                    enemies.remove(enemy_1)
                    self_bullets.remove(bullet)
            if enemy_1.rect.left<screen_rect.left:  # 如果敌方飞机出界，则改变其速度使其飞回
                enemy_1.speed_x=0.1
            if enemy_1.rect.right>screen_rect.right:
                enemy_1.speed_x=-0.1
            if enemy_1.rect.top<screen_rect.top:
                enemy_1.speed_y=0.1
            if enemy_1.rect.bottom>screen_rect.bottom:
                enemy_1.speed_y=-0.1
            if pygame.time.get_ticks()%500==0:  # 敌机每0.5秒随机改变一次速度
                enemy_1.speed_x = random.randint(-1,1)/10
                enemy_1.speed_y = random.randint(-1,1)/10
            enemy_1.position[0]+=enemy_1.speed_x  # 更新敌机的位置和rect
            enemy_1.position[1]+=enemy_1.speed_y
            enemy_1.rect.center=enemy_1.position
            if pygame.time.get_ticks() % 2000 == 0:  # 敌机每2秒发一次子弹
                # 生成精灵
                new_bullet = pygame.sprite.Sprite()
                # 生成精灵形状
                new_bullet.rect = pygame.Rect(0, 0, 4, 15)
                # 绑定位置  精灵中间底部 = 图片顶部
                new_bullet.rect.midtop =enemy_1.rect.midbottom
                # 精灵放入 盒中
                enemy_bullets.add(new_bullet)
        for enemy_bullet in enemy_bullets:  # 遍历敌机子弹组中的所有子弹
            pygame.draw.rect(screen_image, bg_color2, enemy_bullet.rect)  # 画出敌机子弹
            if pygame.time.get_ticks() % 4 == 0:  # 敌机子弹移动速度为4毫秒移动1像素
                enemy_bullet.rect.y += 1
            if enemy_bullet.rect.bottom >= screen_rect.bottom:  # 若子弹出界，则让该子弹移出子弹组
                enemy_bullets.remove(enemy_bullet)
            if pygame.sprite.collide_rect(enemy_bullet, flight_1):  # 若敌方飞机子弹碰到我方飞机，则让我方飞机扣血并让子弹消失
                flight_1.blood -= 20
                enemy_bullets.remove(enemy_bullet)
        flight_1.draw_blood(screen_image, [50, 600])
        pygame.display.flip()



