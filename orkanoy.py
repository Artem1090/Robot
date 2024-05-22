from pygame import *

clock = time.Clock()
dx = 3
dy = 3
window = display.set_mode((700, 500))
display.set_caption('Арканоид ')
plaform_x = 200
plaform_y = 330
move_right = False
move_left = False
game_over = False
red = (255, 0, 0)
class Area():
    def __init__(self, x = 0, y = 0, width = 10, height = 10, color = None):
        self.rect = Rect(x, y, width, height)
        self.fill_color = red
        if color:
            self.fill_color = color
    def color(self, new_color):
        self.fill_color = new_color
    def fill(self):
        draw.rect(window, self.fill_color, self.fill_color, self.rect)
    def colliderect(self, rect):
        return self.rect.colliderect(rect)
class Label(Area):
    def set_text(self, text, fsize=12, text_color=(0, 0, 0)):
        self.image = font.SysFont('verdana', fsize).render(text, True, text_color)
    def draw(self, shift_x=0, shift_y=0):
        self.fill()
        window.blit(self. image, (self.rect.x + shift_x, self.rect.y + shift_y))
class Picter(Area):
    def __init__(self, filename, x=0, y=0, width=10, height=10, ):
        Area.__init__(self, x=x, y=y, width=width, height=height, color=None)
        self.image = image.load(filename)
    def draw(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
ball = Picter('sharik.jpg', 160, 200, 50, 50)
plaform = Picter('T.jpg', plaform_x, plaform_y, 100, 30)
start_x = 5
start_y = 5
count = 9


monsters = []
for a in range(3):
    y = start_y + (55 * a)
    x = start_x + (27.5 * a)
    for i in range (count):
        d = Picter('mma.png',x, y, 50, 50)
        monsters.append(d)
        x = x + 55
    count = count -  1
while not game_over:
    ball.fill()
    plaform.fill()

    for event in event.get():
        if event.type == QUIT:
            game_over = True
        if eval.type == KEYDOWN:
            if event.key == K_d:
                move_right = True
            if event.key == K_a:
                move_left = True
        elif event. key == K_w:
            if event.key == K_d:
                move_right = False
            if event.key == K_a:
                move_left = False
        if move_right:
            plaform.rect.x += 3
        if move_left:
            plaform.rect.x -=3
        ball.rect.x += dx
        ball.rect.y += dy
        if ball.rect.y < 0:
            dy *= -1
        if ball.rect.x > 450 or ball.rect.x < 0:
            dx *= -1
        if ball.rect.y > 350:
            time_text = Label(150,150,50,50,red)
            time_text.set_text('You LOSE', 60, (255, 0, 0))
            time_text.draw(10, 10)
            game_over = True
        if len(monsters) == 0:
            time_text = Label(150,150,50,50,back)
            time_text.set_text('YOU WIN',60, (0,200,0))
            time_text.draw(10, 10)
            game_over = True
        if ball.rect.colliderect(plaform.rect):
            dy *= -1
        for m in monsters:
            m.draw()
            #если монстра коснулся мяч, удаляем монстра из списка и меняем направления движения мяча
            if m.rect.colliderect(ball.rect):
                monsters.remove(m)
                m.fill()
                dy *= -1
        plaform.draw()
        ball.draw()
        display.update()
        clock.tick(40)










