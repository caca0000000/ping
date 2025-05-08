from pygame import *

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed, size_x, size_y):
       sprite.Sprite.__init__(self)

       self.image = transform.scale(image.load(player_image), (size_x, size_y))
       self.speed = player_speed

       self.rect = self.image.get_rect()
       self.rect.x = player_x
       self.rect.y = player_y
 #метод, отрисовывающий героя на окне
    def reset(self):
       window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update_R(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < win_width - 80:
            self.rect.y += self.speed
    def update_l(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < win_width - 80:
            self.rect.y += self.speed
    

back = (200, 255, 255)
win_width = 700
win_height = 500
window = display.set_mode((win_width, win_height))
display.set_caption('pigpog')
window.fill(back)

racket1 = Player('rocket1.png', 0, 200, 4, 50, 150)
racket2 = Player('rocket2.png', 650, 200, 4, 50, 150)
ball = GameSprite('ball.png', 350, 200, 4, 50, 50)

font.init()
font = font.Font(None, 35)
lose1 = font.render('Правый игрок - ЛОХ!', True, (255, 147, 0))
lose2 = font.render('left player - ЛОХ!', True, (255, 147, 0))

game = True 
finish = False
clock = time.Clock()
FPS = 60
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    if finish != True:
        window.fill(back)
        racket1.update_l()
        racket2.update_R()

        racket1.reset()
        racket2.reset()
        ball.reset()
    display.update()
    clock.tick(FPS)
     