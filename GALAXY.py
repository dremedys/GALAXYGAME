import pygame
import random
pygame.init()

screen = pygame.display.set_mode((612, 612)) #same as size of bacground
background = pygame.image.load("background.jpg")
fonts = pygame.font.get_fonts()

font = pygame.font.SysFont('Elephant', 30)     
Bullet = pygame.image.load('deal.png')
Player = pygame.image.load("player.png")
Enemy= pygame.image.load("enemy.png")

player_x = 200
player_y = 548
bullet_x = 215
bullet_y = 518
bullet_dx = 5
bullet_dy = 3
enemy_x = random.randint(0, 548)
enemy_y = random.randint(20, 50)
enemy_dx = 2
enemy_dy = 64
player_dx=5
score=0
shot=False  
def over(enemy_y):          #CHECK IF ENEMY IS TOO CLOSE
    if enemy_y > 420:
        return True
    return False
def colission(enemy_x, enemy_y, bulllet_x, bullet_y):
    if bullet_x >= enemy_x and bullet_x <= enemy_x + 50 and bullet_y <=enemy_y + 70 and not over(enemy_y):
        return True
    return False


Mainloop=True
while Mainloop:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            Mainloop = False

    pressed = pygame.key.get_pressed() 

    if pressed[pygame.K_LEFT] and player_x > 0: 
        player_x -= player_dx
        bullet_x -= bullet_dx

    if pressed[pygame.K_RIGHT] and player_x <736: 
        player_x+=player_dx
        bullet_x+=bullet_dx
        
    enemy_x += enemy_dx

    if enemy_x < 0 or enemy_x > 548: #враг передвигается вниз при столкновении со стеной
        enemy_dx = -enemy_dx
        enemy_y += enemy_dy

    if bullet_x == player_x + 15 and bullet_y == 518:
        player_current = player_x

    if pressed[pygame.K_SPACE]:
        shot = True
    if shot == True:
        bullet_y -= bullet_dy
        bullet_x = player_current + 15

    if bullet_y<5:
        shot=False
        bullet_x = player_x + 15
        bullet_y = 518

    
    if colission(enemy_x, enemy_y, bullet_x, bullet_y):
        enemy_y+=10
        shot=False
        bullet_y = 518
        bullet_x = player_x + 15
        score += 1
    result = font.render('SCORE:' + str(score), True, (255, 255, 255))    
    if over(enemy_y)==True:
            player_dx=0
            bullet_dx=0
            bullet_dy=0
            enemy_dx=0
            enemy_dy=0
    
    screen.blit(background, (0, 0))
    screen.blit(Enemy, (enemy_x,enemy_y))
    screen.blit(Player, (player_x,player_y))
    screen.blit(Bullet, (bullet_x,bullet_y))
    screen.blit(result, (400,20))

    pygame.display.update()
