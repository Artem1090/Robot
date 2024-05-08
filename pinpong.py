def pinpong():
    # balans1 = int(input('Баланс первого игрока?'))
    # balans2 = int(input('Баланс второго игрока?'))
    # stavcka1 = int(input('Ставка первого игрока?'))
    # stavcka2 = int(input('Ставка второго игрока?'))
    # if balans1 - stavcka1 >= 0:
    #     balans1 -= stavcka1
    # if balans2 - stavcka2 >= 0:
    #     balans2 -= stavcka2
    # bank = stavcka1 + stavcka2
    
    from pygame import sprite, image, transform, display, time, K_w, K_s, K_a, K_d, K_LSHIFT, Surface, mixer, event, QUIT, key, font, K_UP, K_DOWN, KEYDOWN, K_SPACE
    score1 = int(0)
    score2 = int(0)
    class GameSprite(sprite.Sprite):
        def __init__(self, player_image, player_x, player_y, player_speed):
            super().__init__()
            self.image = transform.scale(image.load(player_image), (65, 65))
            self.speed = player_speed
            self.speedX = player_speed
            self.speedY = player_speed
            self.rect = self.image.get_rect()
            self.rect.x = player_x
            self.rect.y = player_y
        def reset(self):
            window.blit(self.image, (self.rect.x, self.rect.y))
    clock = time.Clock()
    window = display.set_mode((700, 500))
    display.set_caption('Пинпонг')


    class Player(GameSprite):
        def update(self):
            key_pessed = key.get_pressed()   
            if key_pessed[K_w]:
                self.rect.y -= self.speed
            if key_pessed[K_s]:
                self.rect.y += self.speed
    class Player2(GameSprite):
        def update(self):
            key_pessed = key.get_pressed()   
            if key_pessed[K_UP]:
                self.rect.y -= self.speed
            if key_pessed[K_DOWN]:
                self.rect.y += self.speed
            





    class Enenemy(GameSprite):
        def update(self):
            nonlocal score1
            nonlocal score2
            if self.rect.y >= 450 or self.rect.y <= 0:
                self.speedY *= -1



            self.rect.x += self.speedX
            self.rect.y += self.speedY

            if sprite.collide_rect(gold, cyborg):
                self.speedX *= -1
            if sprite.collide_rect(gold, hero):
                self.speedX *= -1


            
            if self.rect.x >= 650:
                self.rect.x = 330
                self.rect.y = 220
                score1 += 1
            if self.rect.x <= 0:
                self.rect.x = 330
                self.rect.y = 220
                score2 += 1

    









    background = transform.scale(image.load('biliard.jpg'), (700, 500))



    hero = Player('shaurma.jpg', 50, 200, 5)
    cyborg = Player2('palka.webp', 580, 200, 5)
    gold = Enenemy('sharik.jpg', 330, 200, 3)






    font.init()
    font2 = font.Font(None, 80)
    lose = font2.render('Поражение', True, (180, 0, 0))

    finish = False
    game = True
    gamestart = False
    gold.reset()
    while game:
        if finish != True:
            window.blit(background, (0, 0))
            text = font2.render(str(score1) + ':' + str(score2), 1, (255, 255, 255))
            window.blit(text,(10, 20))
            cyborg.update()
            hero.update()
            hero.reset()
            cyborg.reset()
            
            if gamestart == True:
                gold.update()
                gold.reset()
       
        
        for e in event.get():
            if e.type == QUIT:
                game = False
            if e.type == KEYDOWN:
                if e.key == K_SPACE:
                    gamestart = True

        # if score1 == 10  or score2 == 10:
        #     finish = True
        #     window.blit(lose, (200, 200))
        # if score1 == 10:
        #     balans1 += bank
        #     bank = 0
        # if score2 == 10:
        #     balans2 += bank
        #     bank = 0
        display.update() 
        clock.tick(60)
    return
