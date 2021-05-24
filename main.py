#! /usr/bin/env python
import sys
import os
import pygame
import pygame_menu
import random

def resource_path(relative_path):
    try:
    # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

WIDTH = 760
HEIGHT = 480  # высота
FPS = 60

# Задаем цвета
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("DUNGEON FROG")
clock = pygame.time.Clock()
bullets = []
########################################################################################
def resource_path(relative_path):                                                      #
    try:                                                                               #
    # PyInstaller creates a temp folder and stores path in _MEIPASS                    #
        base_path = sys._MEIPASS                                                       #
    except Exception:                                                                  #
        base_path = os.path.abspath("main.py")                                         #      #Штука для компиляции
                                                                                       ############№№№№№№№№№№№№№№№№№
    return os.path.join(base_path, relative_path)                                      #
########################################################################################


#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$#$
  #Счетчик                                                                             #$
def start_the_game():                                                                  #$
    def draw_shield_bar(surf, x, y, pct):                                              #$
        if pct < 0:                                                                    #$
            pct = 0                                                                    #$
        BAR_LENGTH = 100                                                               #$
        BAR_HEIGHT = 10                                                                #$
        fill = (pct / 100) * BAR_LENGTH                                                #$
        outline_rect = pygame.Rect(x, y, BAR_LENGTH, BAR_HEIGHT)                       #$       #Счетчик
        fill_rect = pygame.Rect(x, y, fill, BAR_HEIGHT)                                #$##################
        pygame.draw.rect(surf, GREEN, fill_rect)                                       #$
        pygame.draw.rect(surf, WHITE, outline_rect, 2)                                 #$
#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

    def newmob():
        m = Mob()
        all_sprites.add(m)
        mobs.add(m)



    font_name = pygame.font.match_font('Verdana')

    calEnem2 = 3
    def draw_text (surf, text, size, x, y):
        font = pygame.font.Font(font_name, size)
        text_surface = font.render(text, True, WHITE)
        text_rect = text_surface.get_rect()
        text_rect.midtop = (x, y)
        surf.blit(text_surface, text_rect)                                      #<Классы>
#######################################################################################################################
    #######################################################################################
    # Снаряд (Язык лягухи) ############################################
    class Bullet(pygame.sprite.Sprite):
        def __init__(self, x, y):
            pygame.sprite.Sprite.__init__(self)
            self.image = pygame.Surface((10, 20))
            self.image.fill(WHITE)
            self.rect = self.image.get_rect()
            self.rect.bottom = y
            self.rect.centerx = x
            self.speedy = -10

        def update(self):
            self.rect.y += self.speedy
            # убить, если он заходит за верхнюю часть экрана
            if self.rect.bottom < 0:
                self.kill()


    # враг
    class Mob(pygame.sprite.Sprite):
        def __init__(self):
            pygame.sprite.Sprite.__init__(self)
            self.image = pygame.Surface((30, 40))
            self.image.fill(RED)
            self.rect = self.image.get_rect()
            self.rect.x = random.randrange(WIDTH - self.rect.width)
            self.rect.y = random.randrange(-100, -40)
            self.speedy = random.randrange(1, 8)
            self.speedx = random.randrange(-3, 3)


        def update(self):
            self.rect.x += self.speedx
            self.rect.y += self.speedy
            if self.rect.top > HEIGHT + 10 or self.rect.left < -25 or self.rect.right > WIDTH + 20:
                self.rect.x = random.randrange(WIDTH - self.rect.width)
                self.rect.y = random.randrange(-100, -40)
                self.speedy = random.randrange(1, 8)
    #персонаж
    class Player(pygame.sprite.Sprite):
        def __init__(self):
            self.speedx = 0
            self.shield = 100
            pygame.sprite.Sprite.__init__(self)
            self.image = pygame.Surface((50, 80))
            self.image.fill(GREEN)
            self.rect = self.image.get_rect()
            self.rect.x = self.rect.centerx = WIDTH / 2
            self.rect.y =self.rect.bottom = HEIGHT - 10


        # характеристики персонажа
        def shoot(self):
            bullet = Bullet(self.rect.centerx, self.rect.top)
            all_sprites.add(bullet)
            bullets.add(bullet)
        def update(self):
            speed = 10
            jump=10
            down =1
            #обработка нажатия на клавиш (ЛЕВО, ПРАВО, ПРЫЖОК при ходьбе)
            keys = pygame.key.get_pressed()
        #ходьба
            if keys[pygame.K_a] and self.rect.x >6:
                self.rect.x -= speed
                self.rect.y -= jump

                if self.rect.y <= 320:
                    jump_2 = 1
                    while self.rect.y != 380:
                        self.rect.y += jump_2

            if keys[pygame.K_d] and self.rect.x < 700:
                self.rect.x += speed
                self.rect.y -= jump

                if self.rect.y <= 320:
                    jump_2 = 1
                    while self.rect.y != 380:                                   #</Классы>
                        self.rect.y += jump_2                      ####################################################
                                #############################################################################
    ###################################################################################################

    # Создаем игру и окно

    all_sprites = pygame.sprite.Group()
    mobs = pygame.sprite.Group()
    bullets = pygame.sprite.Group()
    player = Player()
    all_sprites.add(player)

####################
               ####################################

    for i in range(8):             ##################################
        newmob()
    score = 0                             ##################################
               ####################################
#####################
    # Цикл игры
    running = True
    while running:
        # Держим цикл на правильной скорости
        clock.tick(FPS)
        # Ввод процесса (события)
        for event in pygame.event.get():
            # проверка для закрытия окна
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    player.shoot()

        # Обновление
        all_sprites.update()

        hits = pygame.sprite.groupcollide(mobs, bullets, True, True)
        for hit in hits:
            score += 50
            m = Mob()
            all_sprites.add(m)
            mobs.add(m)


        # Проверка, не ударил ли моб игрока
        hits = pygame.sprite.spritecollide(player, mobs, False)
        if hits:
            player.shield -= 2
            if player.shield <= 0:
                running = False

        # Рендеринг
        screen.fill(BLACK)
        all_sprites.draw(screen)
        draw_text(screen, str(score), 18, WIDTH / 2, 10)
        draw_shield_bar(screen, 5, 5, player.shield)
        all_sprites.draw(screen)
        # После отрисовки всего, переворачиваем экран
        pygame.display.flip()


    pygame.quit()

menu = pygame_menu.Menu(400, 660, 'Данжн Лягуха',
                       theme=pygame_menu.themes.THEME_ORANGE)

menu.add_button('Играть', start_the_game)
menu.add_button('Выйти', pygame_menu.events.EXIT)

menu.mainloop(screen)