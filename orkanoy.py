from pygame import *
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
display.set_caption('Арканоид ')


background = transform.scale(image.load('shd.webp'), (700, 500))




finish = False
game = True
while game:
    if finish != True:
        window.blit(background, (0, 0))
    for e in event.get():
        if e.type == QUIT:
            game = False

    display.update() 
    clock.tick(60)

























