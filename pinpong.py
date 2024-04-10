
from pygame import sprite, image, transform, display, time, K_w, K_s, K_a, K_d, K_LSHIFT, Surface, mixer, event, QUIT, key, font, K_UP, K_DOWN 


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
        if key_pessed[K_UP]:
            self.rect.y -= self.speed
        if key_pessed[K_DOWN]:
            self.rect.y += self.speed
class Player2(GameSprite):
    def update(self):
        key_pessed = key.get_pressed()   
        if key_pessed[K_w]:
            self.rect.y -= self.speed
        if key_pessed[K_s]:
            self.rect.y += self.speed
        





class Enenemy(GameSprite):
    def update(self):
        self.rect.x += self.speed
        self.rect.y += self.speed
        if sprite.collide_rect(gold, cyborg):
            self.speed *= -1
        if sprite.collide_rect(gold, hero):
            self.speed *= -1










background = transform.scale(image.load('biliard.jpg'), (700, 500))



hero = Player('shaurma.jpg', 50, 200, 5)
cyborg = Player2('palka.webp', 580, 200, 5)
gold = Enenemy('sharik.jpg', 330, 200, 3)






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
        gold.update()
        hero.reset()
        cyborg.reset()
        gold.reset()
    
    
    
    
    
    
    
    
    for e in event.get():
        if e. type == QUIT:
            game = False

    display.update() 
    clock.tick(60)