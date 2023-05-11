# Example file showing a circle moving on screen
import pygame
import threading
import time
import random
from enemy import Enemy

# pygame setup

pygame.init()
screen = pygame.display.set_mode((1260, 710))
clock = pygame.time.Clock()
running = True
dt = 0
healthBarFrame = pygame.image.load("./GraPython/details/healthbar.png")
healthBarCopy = healthBarFrame.copy()
player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)
x = 200
y = 500
enemy_x = 700
enemy_y = 525
ei = 1
ej = 1
i = 1
j = 1
b = 1
a = 1
eattack = 1
w = 1
health = 220
enemy_health = 220
# def Attack():
# def PlayerHurt():
enemyHealthBar = pygame.transform.flip(healthBarCopy, True, False)

while running:
    isBlocking = False
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    # screen.image.

    # enemy_x-=1
    image = pygame.image.load("./GraPython/mapy/nature_1/origbig.png")
    image2 = pygame.image.load(
        "./GraPython/avatars/Samuraj/Samurai_Commander/Idle/commanderidle{}.png".format(
            i
        )
    )
    enemyImg = pygame.image.load(
        "./GraPython/avatars/Samuraj/Samurai/Idle/samuraiidle{}.png".format(ei)
    )
    
    healthBarFrame = pygame.image.load("./GraPython/details/healthbar.png")

    time.sleep(0.06)

    screen.blit(image, (0, 0))

    # pygame.draw.circle(screen, (0,0,255), (enemy_x, enemy_y), 15, 1)

    screen.blit(healthBarFrame, (0, 0))
    screen.blit(enemyHealthBar, (891, 0))

    def gravity():
        global y
        if y != 500:
            time.sleep(0.1)
            y = 500

    # KEY PRESSED CAPTURE

    keys = pygame.key.get_pressed()
    if keys[pygame.K_x]:
        health -= 20

    if health <= 0:
        print("GAME OVER")

    # BOT

    if x > enemy_x and x - 70 != enemy_x:
        enemy_x += 10
        enemyImg = pygame.image.load(
            "./GraPython/avatars/Samuraj/Samurai/Walk/samuraiWalk{}.png".format(ej)
        )
        if ej > 10:
            ej = 1
        else:
            ej += 1
        screen.blit(enemyImg, (enemy_x, enemy_y), (0, 0, 120, 150))
        # print([x, enemy_x])
    elif x < enemy_x and x + 70 != enemy_x:
        enemyImg = pygame.image.load(
    "./GraPython/avatars/Samuraj/Samurai/Walk/samuraiWalk{}.png".format(ej)
        )
        
        if ej >= 10:
            ej = 1
        else:
            ej += 1

        enemy_x -= 10
        # print("test1")

    ei += 1
    if ei > 6:
        ei = 1

    #   HEALTH
    pygame.draw.rect(screen, (85, 43, 25), pygame.Rect(905.5, 33, 221, 20))
    pygame.draw.rect(screen, (207, 41, 41), pygame.Rect(905.5, 33, enemy_health, 20))

    #   ATTACK FUNCTION
    def EnemyAttack():
        global enemyImg, eattack
       
        enemyImg = pygame.image.load("./GraPython/avatars/Samuraj/Samurai/Attack/samuraiattack{}.png".format(eattack))
        
        if eattack >= 13:
            eattack = 1
        else:
            eattack += 1
        if isBlocking == False:
            global health
        
            if x + 70 == enemy_x:
                health -= random.randint(1, 15)

    # PLAYER
    #   HEALTH
    pygame.draw.rect(screen, (85, 43, 25), pygame.Rect(135.5, 33, 221, 20))
    pygame.draw.rect(screen, (207, 41, 41), pygame.Rect(135.5, 33, health, 20))

    #   ATTACK
    def PlayerAttack():
        if isBlocking == False:
            global enemy_health
            if x + 70 == enemy_x:
                enemy_health -= random.randint(1, 15)
                print(enemy_health)

    i += 1
    if i == 5:
        i = 1
    if keys[pygame.K_a]:
        image2 = pygame.image.load(
            "./GraPython/avatars/Samuraj/Samurai_Commander/Walk/commanderwalk{}.png".format(
                j
            )
        )
        j -= 1

        if j < 1:
            j = 9

        x -= 10

    if keys[pygame.K_d]:
        if enemy_x == x + 70:
            enemy_x += 10
            enemyImg = pygame.image.load(
                "./GraPython/avatars/Samuraj/Samurai/Walk/samuraiWalk{}.png".format(ej)
            )
            
            ej -= 1

            if ej < 1:
                ej = 9

        image2 = pygame.image.load(
            "./GraPython/avatars/Samuraj/Samurai_Commander/Walk/commanderwalk{}.png".format(
                j
            )
        )
        j += 1

        if j > 9:
            j = 1
        x += 10
    if keys[pygame.K_SPACE]:
        if not (keys[pygame.K_s]):
            PlayerAttack()
        image2 = pygame.image.load(
            "./GraPython/avatars/Samuraj/Samurai_Commander/Attack/commanderattack{}.png".format(
                a
            )
        )
        a += 1
        if a > 14:
            a = 1
    else:
        a = 1
    if keys[pygame.K_s]:
        isBlocking = True
        image2 = pygame.image.load(
            "./GraPython/avatars/Samuraj/Samurai_Commander/Protect/protect{}.png".format(
                b
            )
        )
        b += 1
        if b > 2:
            b = 2
    else:
        b = 1

    if keys[pygame.K_w]:
        image2 = pygame.image.load(
            "./GraPython/avatars/Samuraj/Samurai_Commander/Jump/commanderjump{}.png".format(
                w
            )
        )
        w += 1
        if w >= 3:
            y -= 20

        if w > 7 or y < 470:
            w = 7
            y = 500
            w = 1

    else:
        w = 1
        y = 500
    if x+70 == enemy_x:
        EnemyAttack()
    screen.blit(image2, (x, y), (0, 0, 100, 150))
    enemyImg = pygame.transform.flip(enemyImg, True, False)
    screen.blit(enemyImg, (enemy_x, enemy_y), (0, 0, 120, 150))
    pygame.display.flip()
    dt = clock.tick(60) / 1000

pygame.quit()
