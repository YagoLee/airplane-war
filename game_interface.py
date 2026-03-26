import sys
import pygame
import store_system


class button():  # button类管理所有的按钮交互

    def __init__(self, x, y, image, text='', centre=True):  # 构造函数：导入按钮的背景图片和按钮上的文字
        pygame.font.init()
        self.text = text
        self.text = pygame.font.SysFont("simhei", 40).render(text, 1,(255,255,255))  # 储存文字
        self.image=pygame.image.load(image)  # 储存图片
        if centre:  # 规定按钮图片和文字的坐标（坐标表示图片和文字的中间）
            self.x = int(x - self.image.get_width() / 2)
            self.y = int(y - self.image.get_height() / 2)
            self.x_text = int(x - self.text.get_width() / 2)
            self.y_text = int(y - self.text.get_height() / 2)
        else:  # 规定按钮图片和文字的坐标（坐标表示图片和文字的左上角）
            self.x = x
            self.y = y
        self.width = int(self.image.get_width())  # 储存图片和文字的宽度和高度
        self.height = int(self.image.get_height())
        self.width_text=int(self.text.get_width())
        self.height_text = int(self.text.get_height())

    def draw(self, surface):  # draw函数负责将按钮画在屏幕上
        surface.blit(self.image,(self.x,self.y))
        surface.blit(self.text, (self.x_text, self.y_text))

    def is_over(self):  # is_over函数负责判断鼠标是否在按钮上方
        pos = pygame.mouse.get_pos()
        if pos[0] > self.x and pos[0] < self.x + self.width:
            if pos[1] > self.y and pos[1] < self.y + self.height:
                return True
        return False

    def is_pressed(self):  # is_press函数负责判断鼠标是否按下
        mouse = pygame.mouse.get_pressed()
        if mouse[0]:
            if mouse[0]:
                return True
        return False


class interface():  # interface类负责储存所有的游戏界面以及界面上的按钮

    def __init__(self,surface):  # 构造函数：导入并储存屏幕
        self.surface=surface
        self.button_pause = button(550, 50, 'image/game/pause.png')  # 导入并打印按钮

    def main_interface(self):  # main_interface函数负责将游戏主界面打印到屏幕上
        self.main_bg = pygame.image.load('image/main/main_bg.png')  # 导入并打印背景
        self.surface.blit(self.main_bg, (0, 0))
        self.main_title = pygame.image.load('image/main/title.png')  # 导入并打印标题
        self.surface.blit(self.main_title, (150, 100))
        pygame.font.init()
        self.button_start=button(300,475,'image/main/box.png',"开始游戏")  # 导入并打印按钮
        self.button_start.draw(self.surface)
        self.button_store = button(300, 575, 'image/main/box.png', "商店")
        self.button_store.draw(self.surface)
        self.button_exit = button(300, 675, 'image/main/box.png', "退出游戏")
        self.button_exit.draw(self.surface)

    def game_interface(self):  # game_interface函数负责将游戏界面打印到屏幕上
        self.game_bg=pygame.image.load('image/game/game_bg.png')  # 导入并打印背景
        self.surface.blit(self.game_bg, (0, 0))

    def game_interface_button(self):
        self.button_pause.draw(self.surface)
        blood = pygame.image.load('image/store/blood.png')
        blood = pygame.transform.scale(blood, [75, 75])
        self.surface.blit(blood, (0, 800))
        fix = pygame.image.load('image/store/fix.png')
        fix = pygame.transform.scale(fix, [75, 75])
        self.surface.blit(fix, (120, 800))
        shield = pygame.image.load('image/store/shield.png')
        shield = pygame.transform.scale(shield, [75, 75])
        self.surface.blit(shield, (240, 800))
        bomb_1 = pygame.image.load('image/store/bomb_1.png')
        bomb_1 = pygame.transform.scale(bomb_1, [75, 75])
        self.surface.blit(bomb_1, (360, 800))
        bomb_2 = pygame.image.load('image/store/bomb_2.png')
        bomb_2 = pygame.transform.scale(bomb_2, [75, 75])
        self.surface.blit(bomb_2, (480, 800))
        money = pygame.image.load('image/store/money.png')
        money = pygame.transform.scale(money,[75,75])
        self.surface.blit(money, (15, 15))

    def pause_interface(self):  # pause_interface函数负责将暂停界面打印到屏幕上
        self.pause_bg=pygame.image.load('image/pause/pause_bg.png')  # 导入并打印背景
        self.surface.blit(self.pause_bg,(0,0))
        self.pause_title = pygame.image.load('image/pause/title.png')  # 导入并打印标题
        self.surface.blit(self.pause_title,(125,150))
        self.button_pause_home = button(100,600,'image/pause/home.png')  # 导入并打印按钮
        self.button_pause_game = button(500,600,'image/pause/game.png')
        self.button_pause_home.draw(self.surface)
        self.button_pause_game.draw(self.surface)

    def store_interface(self):  # store_interface函数负责将商店界面打印到屏幕上
        self.store_bg=pygame.image.load('image/store/bg.png')
        self.surface.blit(self.store_bg,(0,0))
        self.store_title = pygame.image.load('image/store/title.png')
        self.surface.blit(self.store_title,(200,0))
        self.button_store_blood = button(100,500,'image/store/blood.png')
        self.button_store_bomb_1 = button(200,700,'image/store/bomb_1.png')
        self.button_store_bomb_2 = button(400,700,'image/store/bomb_2.png')
        self.button_store_fix = button(300,500,'image/store/fix.png')
        self.button_store_shield = button(500,500,'image/store/shield.png')
        self.button_store_home = button(500,820,'image/store/home.png')
        self.button_store_blood.draw(self.surface)
        self.button_store_bomb_1.draw(self.surface)
        self.button_store_bomb_2.draw(self.surface)
        self.button_store_fix.draw(self.surface)
        self.button_store_shield.draw(self.surface)
        self.button_store_home.draw(self.surface)
        blood=pygame.image.load('image/store/blood.png')
        blood=pygame.transform.scale(blood,[75,75])
        self.surface.blit(blood, (20, 285))
        fix = pygame.image.load('image/store/fix.png')
        fix = pygame.transform.scale(fix, [75, 75])
        self.surface.blit(fix, (140, 285))
        shield = pygame.image.load('image/store/shield.png')
        shield = pygame.transform.scale(shield, [75, 75])
        self.surface.blit(shield, (260, 285))
        bomb_1 = pygame.image.load('image/store/bomb_1.png')
        bomb_1 = pygame.transform.scale(bomb_1, [75, 75])
        self.surface.blit(bomb_1, (380, 285))
        bomb_2 = pygame.image.load('image/store/bomb_2.png')
        bomb_2 = pygame.transform.scale(bomb_2, [75, 75])
        self.surface.blit(bomb_2, (500, 285))
        money = pygame.image.load('image/store/money.png')
        self.surface.blit(money,(25,50))
        self.f = pygame.font.Font('C:/Windows/Fonts/simhei.ttf', 50)
        text_blood = self.f.render('20', True, (0, 0, 0), (255, 255, 255))
        textRect = text_blood.get_rect()
        textRect.topleft = (80, 600)
        self.surface.blit(text_blood, textRect)
        text_fix = self.f.render('10', True, (0, 0, 0), (255, 255, 255))
        textRect = text_fix.get_rect()
        textRect.topleft = (280, 600)
        self.surface.blit(text_fix, textRect)
        text_shield = self.f.render('30', True, (0, 0, 0), (255, 255, 255))
        textRect = text_shield.get_rect()
        textRect.topleft = (480, 600)
        self.surface.blit(text_shield, textRect)
        text_bomb_1 = self.f.render('15', True, (0, 0, 0), (255, 255, 255))
        textRect = text_bomb_1.get_rect()
        textRect.topleft = (175, 800)
        self.surface.blit(text_bomb_1, textRect)
        text_bomb_2 = self.f.render('10', True, (0, 0, 0), (255, 255, 255))
        textRect = text_bomb_2.get_rect()
        textRect.topleft = (380, 800)
        self.surface.blit(text_bomb_2, textRect)



    def gameover_interface(self):
        self.gameover_bg = pygame.image.load('image/pause/gameover.png')
        self.surface.blit(self.gameover_bg,(0,0))
        self.gameover_home = button(300,800,'image/pause/home.png')
        self.gameover_home.draw(self.surface)

    def win_game_interface(self):
        self.win_game_bg = pygame.image.load('image/pause/pause_bg.png')
        self.surface.blit(self.win_game_bg, (0, 0))
        self.win_game_title = pygame.image.load('image/game/win.png')  # 导入并打印标题
        self.surface.blit(self.win_game_title, (15, 150))
        self.win_game_home = button(300, 600, 'image/pause/home.png')
        self.win_game_home.draw(self.surface)

    pass


if __name__=="__main__":  # 测试程序
    screen=pygame.display.set_mode((600,900))
    pygame.display.set_caption("game interface")
    interface = interface(screen)
    while True:
        for event in pygame.event.get():
            interface.win_game_interface()
            # interface.game_interface_button()
            if event.type==pygame.QUIT:
                pygame.quit()
                sys.exit()
        pygame.display.flip()