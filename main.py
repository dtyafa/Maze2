import pygame
from data import *
from maze import *

pygame.init()
window = pygame.display.set_mode((setting_win["Width"], setting_win["Height"]))
pygame.display.set_caption("maze")

def run():
    bg = pygame.image.load("sprites\\bg.png")
    key_png = pygame.image.load("sprites\\Key.png")
    game = True
    clock = pygame.time.Clock()
    
    hero = Hero(45, 10, 60, 136, hero_list, 5)
    enemy = Enemy(255, 0, 94, 102, robot_list, 2)
    #enemy2 = Enemy(0, 0, 94, 102, robot_list, 3)

    

    while game:
        pygame.draw.rect(window, (255, 255, 0), (100, 100, 100, 100))
        window.blit(bg, (0, 0))

        hero.move()
        window.blit(hero.IMAGE, (hero.x, hero.y))
        if key != True:
            a = window.blit(key_png, (175,340))
        enemy.move(255, 0, 255, 180, "y")
        window.blit(enemy.IMAGE, (enemy.x, enemy.y))
        #enemy2.move()
        #window.blit(enemy2.IMAGE, (enemy2.x, enemy2.y))
        for wall in wall_list:
            pygame.draw.rect(window, wall.COLOR, wall)
        for door in door_list:
            pygame.draw.rect(window, door.COLOR, door)


        

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    hero.MOVE["UP"] = True
                if event.key == pygame.K_s:
                    hero.MOVE["DOWN"] = True
                if event.key == pygame.K_a:
                    hero.MOVE["LEFT"] = True
                if event.key == pygame.K_d:
                    hero.MOVE["RIGHT"] = True
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_w:
                    hero.MOVE["UP"] = False
                if event.key == pygame.K_s:
                    hero.MOVE["DOWN"] = False
                if event.key == pygame.K_a:
                    hero.MOVE["LEFT"] = False
                if event.key == pygame.K_d:
                    hero.MOVE["RIGHT"] = False

        if hero.colliderect(enemy):
            hero.lose()
        #    enemy2.lose()
            enemy.lose()
        if hero.colliderect(a):
            key_up()
            

        clock.tick(80)
        pygame.display.flip()

run()
