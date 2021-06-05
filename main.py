import pygame
import random
import math
import time
from pygame import mixer

# initializeing the pygame

pygame.init()
nomoon = 1
# create the screen
screen = pygame.display.set_mode((1000, 750))
background = pygame.image.load('data/images/space-galaxy-background.jpg')
mixer.music.load('data/sounds/Space Invaders Extreme Title Theme Animatic (2008, Taito).mp3')
mixer.music.play(-1)
pygame.display.set_caption("Space Invaders")
icon = pygame.image.load('data/images/spaceship1.png')
playerimg = pygame.image.load('data/images/spaceship.png')
pygame.display.set_icon(icon)

bulletimg = pygame.image.load('data/images/bullet.png')

# player coordinates
playerx = 370
playery = 683
# monster coordinates

monsterx = []
monstery = []
mincrease = [0.5, 0.5, 0.5, 0.5, 0.5, 0.5]
numbers = 6
for i in range(numbers):
    monsterx.append(random.randint(0, 1000))
    monstery.append(random.randint(12, 600))

# bullet coordinates
bulletx = 0
bullety = 670
bullet_change = 1.3
# bullet state
bullet_state = "ready"
monsterimg1 = pygame.image.load(f'data/monsters/images ({random.randint(1, 104)}).png')

monsterimg2 = pygame.image.load(f'data/monsters/images ({random.randint(1, 104)}).png')
monsterimg3 = pygame.image.load(f'data/monsters/images ({random.randint(1, 104)}).png')
monsterimg4 = pygame.image.load(f'data/monsters/images ({random.randint(1, 104)}).png')
monsterimg5 = pygame.image.load(f'data/monsters/images ({random.randint(1, 104)}).png')
monsterimg6 = pygame.image.load(f'data/monsters/images ({random.randint(1, 104)}).png')

orix = 0


# fire function
def fire(x, y):
    global bullet_state

    bullet_state = "fire"
    screen.blit(bulletimg, (x + 5, y + 10))
    screen.blit(bulletimg, (x + 41, y + 10))


def player(x, y):
    screen.blit(playerimg, (x, y))


soundon = 0

running = True


def iscollision(x, y, p, z):
    distance = math.sqrt(math.pow(abs(x - y), 2) + math.pow(abs(p - z), 2))
    if distance < 50:
        return True
    else:
        return False


def monster1(x, y):
    screen.blit(monsterimg1, (x, y))


def monster2(x, y):
    screen.blit(monsterimg2, (x, y))


def monster3(x, y):
    screen.blit(monsterimg3, (x, y))


def monster4(x, y):
    screen.blit(monsterimg4, (x, y))


def monster5(x, y):
    screen.blit(monsterimg5, (x, y))


def monster6(x, y):
    screen.blit(monsterimg6, (x, y))


def monsterx1():
    global monsterimg1
    dodo = random.randint(1, 104)
    monsterimg1 = pygame.image.load(f'data/monsters/images ({dodo}).png')
    if dodo == 2 or dodo == 6 or dodo == 55 or dodo == 57 or dodo == 82 or dodo == 83 or dodo == 84 or dodo == 93 or dodo == 96 or dodo == 87:
        entry = mixer.Sound('data/sounds/ufo_lowpitch.wav')
        entry.play()


def monsterx2():
    global monsterimg2
    dodo = random.randint(1, 104)
    monsterimg2 = pygame.image.load(f'data/monsters/images ({dodo}).png')
    if dodo == 2 or dodo == 6 or dodo == 55 or dodo == 57 or dodo == 82 or dodo == 83 or dodo == 84 or dodo == 93 or dodo == 96 or dodo == 87:
        entry = mixer.Sound('data/sounds/ufo_lowpitch.wav')
        entry.play()


def monsterx3():
    global monsterimg3
    dodo = random.randint(1, 104)
    monsterimg3 = pygame.image.load(f'data/monsters/images ({dodo}).png')
    if dodo == 2 or dodo == 6 or dodo == 55 or dodo == 57 or dodo == 82 or dodo == 83 or dodo == 84 or dodo == 93 or dodo == 96 or dodo == 87:
        entry = mixer.Sound('data/sounds/ufo_lowpitch.wav')
        entry.play()


def monsterx4():
    global monsterimg4
    dodo = random.randint(1, 104)
    monsterimg4 = pygame.image.load(f'data/monsters/images ({dodo}).png')
    if dodo == 2 or dodo == 6 or dodo == 55 or dodo == 57 or dodo == 82 or dodo == 83 or dodo == 84 or dodo == 93 or dodo == 96 or dodo == 87:
        entry = mixer.Sound('data/sounds/ufo_lowpitch.wav')
        entry.play()


def monsterx5():
    global monsterimg5
    dodo = random.randint(1, 104)
    monsterimg5 = pygame.image.load(f'data/monsters/images ({dodo}).png')
    if dodo == 2 or dodo == 6 or dodo == 55 or dodo == 57 or dodo == 82 or dodo == 83 or dodo == 84 or dodo == 93 or dodo == 96 or dodo == 87:
        entry = mixer.Sound('data/sounds/ufo_lowpitch.wav')
        entry.play()


def monsterx6():
    global monsterimg6
    dodo = random.randint(1, 104)
    monsterimg6 = pygame.image.load(f'data/monsters/images ({dodo}).png')
    if dodo == 2 or dodo == 6 or dodo == 55 or dodo == 57 or dodo == 82 or dodo == 83 or dodo == 84 or dodo == 93 or dodo == 96 or dodo == 87:
        entry = mixer.Sound('data/sounds/ufo_lowpitch.wav')
        entry.play()


def gameover():
    gameover = pygame.font.Font('freesansbold.ttf', 64)

    over = gameover.render("Gameover :( ", True, (200, 200, 200))

    screen.blit(over, (300, 400))
    over1 = mixer.Sound('data/sounds/mixkit-arcade-retro-game-over-213.wav')
    global soundon
    if (soundon == 0):
        soundon = 3
        over1.play()


myfuncs = [monster1, monster2, monster3, monster4, monster5, monster6]
myfuncsx = [monsterx1, monsterx2, monsterx3, monsterx4, monsterx5, monsterx6]

tpo = 5
kp = 0.3
increase = 0
font = pygame.font.Font('freesansbold.ttf', 28)
textx = 10
texty = 10

score = 0
pk = 0

global oldscore
oldscore = 0


def show(x, y):
    global score
    global oldscore
    scorep = font.render("Score :" + str(score), True, (200, 200, 200))
    screen.blit(scorep, (x, y))
    if (score > oldscore):
        oldscore = score
    scoreh = font.render("High Score :" + str(oldscore), True, (200, 200, 200))
    screen.blit(scoreh, (800, 5))
    global pk
    if (pk < 800):
        qp = font.render("Press Spacebar to Shoot", True, (200, 200, 200))
        screen.blit(qp, (350, 10))
    elif (pk < 1800 and pk > 900):
        wp = font.render("Use Arrow Keys to pan across the screen", True, (200, 200, 200))
        screen.blit(wp, (250, 35))
    elif (pk < 3800 and pk > 1900):
        font1 = pygame.font.Font('freesansbold.ttf', 18)
        wp = font1.render("Shoot descending swarms of invaders before they reach the bottom", True, (200, 200, 200))
        screen.blit(wp, (175, 20))


f = open("data/scorefile.txt", "r")
oldscore = (f.read())
oldscore = int(oldscore)
print(oldscore)
f.close()
shouldwrite = False
while running:
    pk += 1
    screen.fill((16, 16, 16))
    screen.blit(background, (0, 0))
    for i in range(numbers):

        if (monstery[i] >= 670):

            f = open("data/scorefile.txt", "r")
            oldscore = (f.read())
            oldscore = int(oldscore)
            print(oldscore)
            f.close()

            if (score > oldscore):
                f = open("data/scorefile.txt", "w")
                f.write(f"{score}")
                f.close()

            for j in range(6):
                monstery[j] = 4000
            gameover()

        # if (abs(bulletx - monsterx[i]) < 15 and abs(bullety - monstery[i]) < 15):
        #     monsterx[i] = random.randint(0, 800)
        #     monstery[i] += 20
        randop = random.randint(0, 500)
        if (randop == 1):
            mincrease[i] *= -1
        if (monsterx[i] >= 950):
            monsterx[i] = 950
            monstery[i] += 10
            mincrease[i] *= -1
        if (monsterx[i] <= 5):
            monsterx[i] = 5
            monstery[i] += 10
            mincrease[i] *= -1
        # k = random.randint(0, 1000)
        #
        # if (k == 1):
        #     mincrease *= -1
        monsterx[i] += mincrease[i]
        myfuncs[i](monsterx[i], monstery[i])
        collision = iscollision(monsterx[i], orix, monstery[i], bullety)

        if collision:
            if randop < 10:
                invaderkilled = mixer.Sound('data/sounds/mixkit-arcade-video-game-explosion-2810.wav')
                invaderkilled.play()
            else:

                invaderkilled = mixer.Sound('data/sounds/invaderkilled.wav')
            invaderkilled.play()
            if bullet_change < 3.9:
                bullet_change += 0.1
            if (mincrease[i] < 0 and abs(mincrease[i]) < 1.5):
                mincrease[i] -= 0.3
            if (mincrease[i] >= 0 and abs(mincrease[i]) < 1.5):
                mincrease[i] += 0.3
            tpo += 0.7
            ip0 = (i + 1) % 6
            ip1 = (i + 2) % 6
            ip2 = (i + 3) % 6
            ip3 = (i + 4) % 6
            ip4 = (i + 5) % 6

            monstery[ip0] += tpo
            monstery[ip1] += tpo
            monstery[ip2] += tpo
            monstery[ip3] += tpo
            monstery[ip4] += tpo

            if kp < 2.5:
                kp += 0.1
            myfuncsx[i]()

            monsterx[i] = random.randint(0, 1000)
            monstery[i] = random.randint(50, 350)
            bullety = 670
            bullet_state = "ready"
            score = score + 1

    playerx += increase

    if (playerx >= 930):
        playerx = 930
    if (playerx <= 5):
        playerx = 5

    if bullety <= 0:
        bullety = 670
        bullet_state = "ready"
    if bullet_state is "fire":
        fire(orix, bullety)
        bullety -= bullet_change

    player(playerx, playery)
    show(textx, texty)
    pygame.display.update()
    # running conditions
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            f = open("data/scorefile.txt", "r")
            oldscore = (f.read())
            oldscore = int(oldscore)
            print(oldscore)
            f.close()
            if (score > oldscore):
                f = open("data/scorefile.txt", "w")
                f.write(f"{score}")
                f.close()
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                increase = -kp
            if event.key == pygame.K_RIGHT:
                increase = kp
            if event.key == pygame.K_SPACE:
                if bullet_state is "ready":
                    bullet_sound = mixer.Sound('data/sounds/shoot.wav')
                    bullet_sound.play()
                    orix = playerx
                    fire(playerx, bullety)
                    bullety -= bullet_change

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                increase = 0
