def labirint():    
    from pygame import sprite, image, transform, display, time, K_w, K_s, K_a, K_d, K_LSHIFT, Surface, mixer, event, QUIT, key, font 


    class GameSprite(sprite.Sprite):
        def __init__(self, player_image, player_x, player_y, player_speed):
            super().__init__()
            self.image = transform.scale(image.load(player_image), (65, 65))
            self.speed = player_speed
            self.rect = self.image.get_rect()
            self.rect.x = player_x
            self.rect.y = player_y
        def reset(self):
            window.blit(self.image, (self.rect.x, self.rect.y))
    clock = time.Clock()
    window = display.set_mode((700, 500))
    display.set_caption('Лабиринт ')


    class Player(GameSprite):
        def update(self):
            key_pessed = key.get_pressed()   
            if key_pessed[K_w]:
                self.rect.y -= self.speed
            if key_pessed[K_s]:
                self.rect.y += self.speed
            if key_pessed[K_a]:
                self.rect.x -= self.speed
            if key_pessed[K_d]:
                self.rect.x += self.speed
            if key_pessed[K_LSHIFT] and key_pessed[K_d]:
                self.rect.x += 5
            if key_pessed[K_LSHIFT] and key_pessed[K_w]:
                self.rect.y -= 5
            if key_pessed[K_LSHIFT] and key_pessed [K_s]:
                self.rect.y += 5
            if key_pessed[K_LSHIFT] and key_pessed [K_a]:
                self.rect.x -= 5




    class Enenemy(GameSprite):
        direction = "left"
        def update(self):
                if self.rect.x <=470:
                    self.direction = "right"
                if self.rect.x >= 650:
                    self.direction = 'left'
                if self.direction == 'left':
                    self.rect.x -= self.speed
                if self.direction == 'right':
                    self.rect.x += self.speed
    class Wall (sprite.Sprite):
        def __init__(self,  r, g, b, x, y, w, h):
            super().__init__()
            self.red = r
            self.green = g
            self.blue = b
            self.width = w
            self.height = h
            self.image = Surface((self.width, self.height))
            self.image.fill((r, g, b))
            self.rect = self.image.get_rect()
            self.rect.x = x
            self.rect.y = y
        def draw_wall(self):
            window.blit(self.image,(self.rect.x, self.rect.y))









    background = transform.scale(image.load('щд.webp'), (700, 500))



    hero = Player('эдгар.png', 50, 50, 5)
    cyborg = Enenemy('mma.png', 300, 250, 3)
    gold = GameSprite('diz.png', 600, 400, 0)
    w1 = Wall(129, 54, 4, 150, -150, 10, 510)
    w2 = Wall(129, 54, 4, 200, 0, 400, 10)
    w3 = Wall(129, 54, 4, 150, 485, 350, 10)
    w4 = Wall(129, 54, 4, 300, 150, 10, 340)
    w5 = Wall(129, 54, 4, 520, 150, 10, 340)
    w6 = Wall(129, 54, 4, 400, -150, 10, 450)
    w7 = Wall(129, 54, 4, 650, 150, 350, 10)


    


    font.init()
    font = font.Font(None, 80)
    win = font.render('Ура победа', True, (250, 0, 0))
    lose = font.render('лузер ахахахаххахахах', True, (180, 0, 0))

    finish = False
    game = True
    while game:
        if finish != True:
            window.blit(background, (0, 0))
            cyborg.update()
            hero.update()
            hero.reset()
            cyborg.reset()
            gold.reset()
            w1.draw_wall()
            w2.draw_wall()
            w3.draw_wall()
            w4.draw_wall()
            w5.draw_wall()
            w6.draw_wall()
            w7.draw_wall()
            if sprite.collide_rect(hero, gold):
                finish = True
                window.blit(win, (200, 200))
            if sprite.collide_rect(hero, cyborg):
                finish = True
                window.blit(lose, (200, 200))
            if sprite.collide_rect(hero, w1) or sprite.collide_rect(hero, w2) or sprite.collide_rect(hero, w3) or sprite.collide_rect(hero, w4) or sprite.collide_rect(hero, w5) or sprite.collide_rect(hero, w6) or sprite.collide_rect(hero, w7):
                finish = True
                window.blit(lose, (200, 200))
        
        
        
        
        
        
        
        
        for e in event.get():
            if e. type == QUIT:
                game = False

        display.update() 
        clock.tick(60)
