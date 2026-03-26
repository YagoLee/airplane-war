import pygame


class adjutant():
    def __init__(self, position):
        self.image = pygame.image.load('image/NPC/adjutant.png')
        self.rect = self.image.get_rect()
        self.rect.center = position
        self.position = position
        self.f = pygame.font.Font('C:/Windows/Fonts/simhei.ttf', 15)
        self.text_1 = self.f.render('指挥官，这里是帝国前线第二十五训练区，我是你的副官，', True, (0, 0, 0), (0, 128, 128))
        self.text_1_ = self.f.render('我的名字叫戴夫', True, (0, 0, 0), (0, 128, 128))
        self.text_1_rect = self.text_1.get_rect()
        self.text_1_rect.topleft = [10, 750]
        self.text_1_rect_ = self.text_1_.get_rect()
        self.text_1_rect_.topleft = [10, 775]
        self.text_2 = self.f.render('现在是你的第一次实弹演习，请注意开火', True, (0, 0, 0), (0, 128, 128))
        self.text_2_rect = self.text_2.get_rect()
        self.text_2_rect.topleft = [10, 750]
        self.text_3 = self.f.render('这是战场上的第一种敌人，它的移速偏慢，射速较慢，', True, (0, 0, 0), (0, 128, 128))
        self.text_3_rect = self.text_3.get_rect()
        self.text_3_rect.topleft = [10, 750]
        self.text_3_ = self.f.render('但是是在战场上非常多的部队，根据最高统帅部发布的公告', True, (0, 0, 0), (0, 128, 128))
        self.text_3_rect_ = self.text_3_.get_rect()
        self.text_3_rect_.topleft = [10, 775]
        self.text_3__ = self.f.render('来看我们的x-02型实验战机在移速和火力密度方面', True, (0, 0, 0), (0, 128, 128))
        self.text_3_rect__ = self.text_3__.get_rect()
        self.text_3_rect__.topleft = [10, 800]
        self.text_3___ = self.f.render('都对其有代差。', True, (0, 0, 0), (0, 128, 128))
        self.text_3_rect___ = self.text_3___.get_rect()
        self.text_3_rect___.topleft = [10, 825]
        self.text_4 = self.f.render('你可以在商店中购买道具，道具数量在下面显示。', True, (0, 0, 0), (0, 128, 128))
        self.text_4_rect = self.text_4.get_rect()
        self.text_4_rect.topleft = [10, 750]
        self.text_4_1 = self.f.render('你可以通过按键盘上的“1”来使你的飞机最大血量增加', True, (0, 0, 0), (0, 128, 128))
        self.text_4_rect_1 = self.text_4_1.get_rect()
        self.text_4_rect_1.topleft = [10, 775]
        self.text_4_2 = self.f.render('通过按键盘上的“2”来使你的飞机血量增加', True, (0, 0, 0), (0, 128, 128))
        self.text_4_rect_2 = self.text_4_2.get_rect()
        self.text_4_rect_2.topleft = [10, 800]
        self.text_4_3 = self.f.render('通过按键盘上的“3”来使你的飞机进入无敌状态', True, (0, 0, 0), (0, 128, 128))
        self.text_4_rect_3 = self.text_4_3.get_rect()
        self.text_4_rect_3.topleft = [10, 825]
        self.text_4_4 = self.f.render('通过按键盘上的“4”来使你的飞机发出炸弹', True, (0, 0, 0), (0, 128, 128))
        self.text_4_rect_4 = self.text_4_4.get_rect()
        self.text_4_rect_4.topleft = [10, 850]
        self.text_4_5 = self.f.render('通过按键盘上的“5”来使你的飞机发出穿甲弹', True, (0, 0, 0), (0, 128, 128))
        self.text_4_rect_5 = self.text_4_5.get_rect()
        self.text_4_rect_5.topleft = [10, 875]
        self.text_5 = self.f.render('敌方突袭，紧急支援', True, (0, 0, 0), (0, 128, 128))
        self.text_5_rect = self.text_5.get_rect()
        self.text_5_rect.topleft = [10, 750]
        self.text_6 = self.f.render('敌方突袭训练营，注意这不是演习，指挥官现在是你紧急上场的时候了', True, (0, 0, 0), (0, 128, 128))
        self.text_6_rect = self.text_6.get_rect()
        self.text_6_rect.topleft = [10, 750]
        self.text_7 = self.f.render('他们的指挥机就在附近，让我们去干掉他', True, (0, 0, 0), (0, 128, 128))
        self.text_7_rect = self.text_7.get_rect()
        self.text_7_rect.topleft = [10, 750]
        self.text_8 = self.f.render('指挥官，你是一个新兵王牌飞行员，可以上战场了。', True, (0, 0, 0), (0, 128, 128))
        self.text_8_rect = self.text_8.get_rect()
        self.text_8_rect.topleft = [10, 750]
        self.text_9_1 = self.f.render('指挥官，最高统帅部根据你的优秀战绩决定把你编入第二飞行教导队', True, (0, 0, 0), (0, 128, 128))
        self.text_9_rect_1= self.text_9_1.get_rect()
        self.text_9_rect_1.topleft = [10, 750]
        self.text_9_2 = self.f.render('这一次是要去支援前线部队，取得制空权，第5集团军的陆军陷入苦战，', True, (0, 0, 0), (0, 128, 128))
        self.text_9_rect_2 = self.text_9_2.get_rect()
        self.text_9_rect_2.topleft = [10, 775]
        self.text_9_3 = self.f.render('我们需要取得空中优势，以便支援我们的陆军兄弟', True, (0, 0, 0), (0, 128, 128))
        self.text_9_rect_3 = self.text_9_3.get_rect()
        self.text_9_rect_3.topleft = [10, 800]
        self.text_10 = self.f.render('敌方的大部分飞机都被击毁了，敌方王牌飞机应该要来了', True, (0, 0, 0), (0, 128, 128))
        self.text_10_rect = self.text_10.get_rect()
        self.text_10_rect.topleft = [10, 750]
        self.text_11 = self.f.render('祝贺你指挥官，你的表现真的太优异了，最高统帅部对这次胜利的消息非常喜悦', True, (0, 0, 0), (0, 128, 128))
        self.text_11_rect = self.text_11.get_rect()
        self.text_11_rect.topleft = [10, 750]
        self.text_12 = self.f.render('这次最高统帅部决定让指挥官你作为队长带领第三飞行教导队突击敌方实验机场', True, (0, 0, 0), (0, 128, 128))
        self.text_12_rect = self.text_12.get_rect()
        self.text_12_rect.topleft = [10, 750]
        self.text_13 = self.f.render('敌人把实验飞机升空了，指挥官，这将是一场硬仗。', True, (0, 0, 0), (0, 128, 128))
        self.text_13_rect = self.text_13.get_rect()
        self.text_13_rect.topleft = [10, 750]
        self.text_14 = self.f.render('很好指挥官，我相信你的勋章已经在等着你回去了', True, (0, 0, 0), (0, 128, 128))
        self.text_14_rect = self.text_14.get_rect()
        self.text_14_rect.topleft = [10, 750]


    def draw(self, surface):
        surface.blit(self.image, self.rect)

    def draw_text_1(self, surface):
        surface.blit(self.text_1, self.text_1_rect)
        surface.blit(self.text_1_, self.text_1_rect_)

    def draw_text_2(self, surface):
        surface.blit(self.text_2, self.text_2_rect)

    def draw_text_3(self, surface):
        surface.blit(self.text_3, self.text_3_rect)
        surface.blit(self.text_3_, self.text_3_rect_)
        surface.blit(self.text_3__, self.text_3_rect__)
        surface.blit(self.text_3___, self.text_3_rect___)

    def draw_text_4(self, surface):
        surface.blit(self.text_4, self.text_4_rect)
        surface.blit(self.text_4_1, self.text_4_rect_1)
        surface.blit(self.text_4_2, self.text_4_rect_2)
        surface.blit(self.text_4_3, self.text_4_rect_3)
        surface.blit(self.text_4_4, self.text_4_rect_4)
        surface.blit(self.text_4_5, self.text_4_rect_5)

    def draw_text_5(self, surface):
        surface.blit(self.text_5, self.text_5_rect)

    def draw_text_6(self, surface):
        surface.blit(self.text_6, self.text_6_rect)

    def draw_text_7(self, surface):
        surface.blit(self.text_7, self.text_7_rect)

    def draw_text_8(self, surface):
        surface.blit(self.text_8, self.text_8_rect)

    def draw_text_9(self, surface):
        surface.blit(self.text_9_1, self.text_9_rect_1)
        surface.blit(self.text_9_2, self.text_9_rect_2)
        surface.blit(self.text_9_3, self.text_9_rect_3)

    def draw_text_10(self, surface):
        surface.blit(self.text_10, self.text_10_rect)

    def draw_text_11(self, surface):
        surface.blit(self.text_11, self.text_11_rect)

    def draw_text_12(self, surface):
        surface.blit(self.text_12, self.text_12_rect)

    def draw_text_13(self, surface):
        surface.blit(self.text_13, self.text_13_rect)

    def draw_text_14(self, surface):
        surface.blit(self.text_14, self.text_14_rect)