# Example file showing a circle moving on screen
import pygame
import time
# pygame setup
pygame.init()
screen = pygame.display.set_mode((1260, 710))
clock = pygame.time.Clock()
running = True
dt = 0

player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)
x = 20
y = 500
i=1
j=1
while running:
    screen.fill((0, 0, 0))
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    # screen.image.

    image = pygame.image.load("./GraPython/mapy/nature_1/origbig.png")
    image2 = pygame.image.load("./GraPython/avatars/Samuraj/Samurai_Commander/Idle/commanderidle{}.png".format(i))
    time.sleep(0.05)
    i+=1
    if i == 5:
        i=1
    

    

    screen.blit(image2,(x,y), (10, 10, 100, 150))
    screen.blit(image, (0, 0))
    # screen.blit(image2,(x,y), (10, 10, 100, 150))
    # if keys[pygame.K_UP]:
    #     y-=20
    def gravity():
        global y
        if y != 500:
            screen.fill((0, 0, 0))
            screen.blit(image2,(x,y), (10, 10, 100, 150))
            time.sleep(0.1)
            y=500

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
       y -= 20
       gravity()
    #    time.sleep(0.5)
        
    #    y +=10
    #    y=500
    # if keys[pygame.K_s]:
    #     player_pos.y += 300 * dt
    if keys[pygame.K_a]:
        image2 = pygame.image.load("./GraPython/avatars/Samuraj/Samurai_Commander/Walk/commanderwalk{}.png".format(j))
        j-=1
        
        if j < 1:
            j=9
        
        x -= 10
        
    if keys[pygame.K_d]:
        
        image2 = pygame.image.load("./GraPython/avatars/Samuraj/Samurai_Commander/Walk/commanderwalk{}.png".format(j))
        j+=1
        
        if j > 9:
            j=1
        
        x += 10
    
    # screen.blit(image2,(x,y), (10, 10, 100, 150))
    gravity()
    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60) / 1000

pygame.quit()