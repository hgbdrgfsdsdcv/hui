from pygame import *
from random import randint
clock = time.Clock()
FPS = 60

lifes = 3
lost = 0
count = 0
font.init()
font1 = font.SysFont("Arial",36)
font2 = font.SysFont("Arial",72)

game = True
finish = False

heigth = 700
width = 500

window = display.set_mode((heigth,width))
display.set_caption("шутер")

mixer.init()
mixer.music.load("bs.mp3")
mixer.music.play()
kick = mixer.Sound("vis.ogg")

background = transform.scale(image.load("sd.jpg"),(heigth,width))

class GameSprite(sprite.Sprite):
    def __init__(self,player_image, player_x, player_y, player_speed,height,width):
        super().__init__()
        self.height = height
        self.width = width
        self.image = transform.scale(image.load(player_image),(self.height,self.width))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_a] and self.rect.x > 0:
            self.rect.x -= self.speed
        if keys_pressed[K_d] and self.rect.x < heigth - 65:
            self.rect.x += self.speed
        display.update()
    def fire(self):
        pula = Pulya("bullet.png", player.rect.x + 13,400,5,25,50)
        puli.add(pula)
        kick.play()
        if pula.rect.y < 0:
                pula.kill()

class Enemy(GameSprite):
    def update(self):
        if self.rect.y < 500:
            self.rect.y += self.speed
        else:
            global lost
            lost += 1
            self.rect.y = 0
            self.rect.x = randint(50,650)
    def res(self):
        self.kill()
        monster = Enemy("ufo.png",randint(50,650),0,1,100,50)
        monsters.add(monster)


class Pulya(GameSprite):
    def update(self):
        self.rect.y -= self.speed

class asteroid(GameSprite):
    def update(self):
        if self.rect.y < 500:
            self.rect.y += self.speed
        else:
            self.rect.y = 0
            self.rect.x = randint(50,650)

    def res(self):
        self.kill()
        global lifes
        lifes -= 1
        asteroid0 = asteroid("asteroid.png",randint(50,650),0,2,50,50)
        asteroids.add(asteroid0)

player = Player("rocket.png", 345,390,5,50,100)
monster1 = Enemy("ufo.png", 100, 0,2,100,50)
monster2 = Enemy("ufo.png", 200, 0,2,100,50)
monster3 = Enemy("ufo.png", 300, 0,2,100,50)
monster4 = Enemy("ufo.png", 400, 0,2,100,50)
monster5 = Enemy("ufo.png", 500, 0,2,100,50)
monsters = sprite.Group()
monsters.add(monster1)
monsters.add(monster2)
monsters.add(monster3)
monsters.add(monster4)
monsters.add(monster5)
puli = sprite.Group()
asteroid1 = asteroid('asteroid.png', 100,0,2,50,50)
asteroid2 = asteroid('asteroid.png', 200,0,2,50,50)
asteroid3 = asteroid('asteroid.png', 300,0,2,50,50)
asteroids = sprite.Group()
asteroids.add(asteroid1)
asteroids.add(asteroid2)
asteroids.add(asteroid3)
players = sprite.Group()
players.add(player)

while game:

    text_lose = font1.render("Пропущено: " + str(lost), 1,(255,255,255))
    text = font1.render("Счёт: " + str(count),1,(255,255,255))
    win = font2.render("YOU WIN!!!",1,(0,255,0))
    lose = font2.render("YOU LOSE!",1,(255,0,0))
    life = font1.render("Жизни: " + str(lifes), 1,(255,255,255))

    for e in event.get():
        if e.type == QUIT:
            game = False
        elif e.type == MOUSEBUTTONDOWN:
                    if self.Button1.pressed(pygame.mouse.get_pos()):
                        print("Give me a command!")


    if finish != True:
        window.blit(background,(0,0))
        window.blit(text_lose, (20,80))
        window.blit(text, (20,50))
        window.blit(life,(500,50))
        players.draw(window)
        monsters.draw(window)
        puli.draw(window)
        asteroids.draw(window)

        keys_pressed = key.get_pressed()
        if keys_pressed[K_SPACE]:
            player.fire()

        sprites_list = sprite.groupcollide(monsters, puli, True, True)
        for s in sprites_list:
            s.res()

        if len(sprites_list) == 1:
            count += 1

        if count >= 10:
            window.blit(win,(100,250))
            finish = True
        if lost >= 3:
            window.blit(lose,(200,250))
            finish = True

        asteroids_list = sprite.groupcollide(asteroids, players, False, False)
        for a in asteroids_list:
            a.res()

        if lifes == 0:
            window.blit(lose,(200,250))
            finish = True


    players.update()
    monsters.update()
    puli.update()
    asteroids.update()

    display.update()
    clock.tick(FPS)