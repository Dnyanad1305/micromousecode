import pygame
import sys
import time
import rotateImage as rotator
path = ''
pygame.init()
while path != 'x':
    path = input('Enter your path or stop it by typing x:- ')


a = float(input('Enter the Distance the bot wants to travel (in cm):- '))
b = int(input("Enter the Step Angle of the robot's first stepper motor:- "))
b1 = b
b2 = b
c = float(input('Enter the Diameter of the first wheel of the bot (in cm) :- '))
y = int(input("Enter the Step Angle of the robot's second stepper motor:- "))
y1 = y
y2 = y
z = float(input('Enter the Diameter of the second wheel of the bot (in cm) :- '))

# finding the circumference
pi = 3.14
circum = pi * c

# finding the length of the steps
step_len = (circum * b) / 360

# finding the number of steps
step_num = a / step_len


circum2 = pi * z

# finding the length of the steps
step_len2 = (circum * y) / 360

# finding the number of steps
step_num2 = a / step_len2

menu = pygame.image.load('MENU.png')
wheel1 = pygame.image.load('WHEEL.png')
wheel2 = pygame.image.load('WHEEL.png')
grid = pygame.image.load('grid.png')
bot = pygame.image.load('bot.png')
angle = 0
win = pygame.display.set_mode((1000, 700))

pygame.display.set_caption('Step Simulator')
pygame.display.update()
run = True
while run:
    win.blit(menu, (0,0))
    win.blit(grid, (700,0))
    #win.blit(bot, (700, 0))
    rotator.blitRotate(win, bot, (700, 2), 180)
    font = pygame.font.SysFont('SHOWCARD GOTHIC', 45)
    sa1 = font.render(str(b), True, (0, 0, 0))
    win.blit(sa1, (550, 200))
    sa2 = font.render(str(y), True, (0, 0, 0))
    win.blit(sa2, (550, 465))
    sn1 = font.render(str(int(step_num)), True, (0, 0, 0))
    win.blit(sn1, (580, 270))
    sn2 = font.render(str(int(step_num2)), True, (0, 0, 0))
    win.blit(sn2, (580, 535))
    wd1 = font.render(str(int(c)), True, (0, 0, 0))
    win.blit(wd1, (670, 310))
    wd2 = font.render(str(int(z)), True, (0, 0, 0))
    win.blit(wd2, (675, 580))

    if step_num >= 0:
        rotator.blitRotate(win, wheel1, (0,100), b1)
        step_num = step_num - 1
        time.sleep(1)
    if step_num2 >= 0:
        rotator.blitRotate(win, wheel2, (0,380), y1)
        step_num2 = step_num2 - 1
        time.sleep(1)

    b1 = b1 - b2
    y1 = y1 - y2

    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()