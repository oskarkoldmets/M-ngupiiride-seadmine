import pygame
pygame.init()

#värvid
red = [255, 0, 0]
lBlue = [153, 204, 255]
 
#ekraani seaded
screenX = 640
screenY = 480
screen=pygame.display.set_mode([screenX,screenY])
pygame.display.set_caption("Klaviatuuriga juhtimine")
screen.fill(lBlue)
clock = pygame.time.Clock()

#koordinaadid ja kiirus
posX, posY = screenX/2, screenY/2
speedX, speedY = 0, 0
directionX, directionY = 0, 0


gameover = False
while not gameover:
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameover = True

        #klahvivajutus
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                directionX = "move_right"
            elif event.key == pygame.K_LEFT:
                directionX = "move_left"
            elif event.key == pygame.K_UP:
                directionY = "move_up"
            elif event.key == pygame.K_DOWN:
                directionY = "move_down"

        #klahvivajutuse vabastamine
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT or event.key == pygame.K_LEFT:
                directionX = 0
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                directionY = 0

    #mängu piirjoonte tuvastamine
    if directionX == "move_left":
        if posX > 0:
            posX -= 3
    elif directionX == "move_right":
        if posX + 30 < screenX:
            posX += 3
    if directionY == "move_up":
        if posY > 0:
            posY -= 3
    elif directionY == "move_down":
        if posY + 30 < screenY:
            posY += 3

    ruut = pygame.draw.rect(screen, red, [posX, posY, 30, 30])
    pygame.display.flip()
    screen.fill(lBlue)
pygame.quit()