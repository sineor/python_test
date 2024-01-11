import pygame
import sys

pygame.init()

white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)

# razmer okna
width, heght = 800, 600

# sozdaniye okna
screen = pygame.display.set_mode((width, heght))
pygame.display.set_caption('Jylan')

# nachalniye koordinaty zmeiki
snake_post = [100, 50]
snake_body = [[100, 50], [90, 50], [80, 50]]

# napravleniya dvijeniya
direction = 'RIGHT'
change_to = direction
speed = 15

# Osnovnoi sikl igry
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                change_to = 'UP'
            elif event.key == pygame.K_DOWN:
                change_to = 'DOUN'
            elif event.key == pygame.K_LEFT:
                change_to = 'LEFT'
            elif event.key == pygame.RIGHT:
                change_to = 'RIGHT'

            # IZMENENIYE NAPRAVLENIYE DVIJENIYE
            if change_to == 'UP' and not direction == 'DOWN':
                direction == 'UP'
            if change_to == 'DOWN' and not direction == 'UP':
                direction == 'DOWN'
            if change_to == 'LEFT' and not direction == 'RIGHT':
                direction == 'LEFT'
            if change_to == 'RIGHT' and not direction == 'LEFT':
                direction == 'RIGHT'

                # dvij. zmeiki
            if direction == 'UP':
                snake_post[1] -= 10
            if direction == 'DOWN':
                snake_post[1] += 10
            if direction == 'LEFT':
                snake_post[0] -= 10
            if direction == 'RIGHT':
                snake_post[0] += 10

            # otrisovka zmeyki
            screen.fill(black)
            for pos in snake_body:
                pygame.draw.rect(screen, white, pygame.Rect(pos[0], pos[1], 10, 10))

            # obnovlenie ekrana
            pygame.display.flip()

            # zaderjka dlya kontrolya skorosti
            pygame.time.Clock().tick(speed)
