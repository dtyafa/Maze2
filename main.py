import pygame
import data
from maze import *

pygame.init()
window = pygame.display.set_mode((setting_win["Width"], setting_win["Height"]))
pygame.display.set_caption("maze")


def run():
    bg = pygame.image.load("sprites\\bg.png")
    key_png = pygame.image.load("sprites\\Key.png")
    game = True
    clock = pygame.time.Clock()
    hero = Hero(45, 10, 60, 120, hero_list, 4, 1)
    enemy = Enemy(170, 100, 94, 102, robot_list, 4, "x")
    key = Key(175, 420, 69, 30, key_png)
    hero.loadLVL()

    while game:
        pygame.draw.rect(window, (255, 255, 0), (100, 100, 100, 100))
        window.blit(bg, (0, 0))

        hero.move()
        window.blit(hero.IMAGE, (hero.x, hero.y))
        if hero.LVL == 1:
            enemy.move(170, 0, 906, 180)
        elif hero.LVL == 2:
            enemy.move(0, 102, 180, 898)
        window.blit(enemy.IMAGE, (enemy.x, enemy.y))
        if key != 0:
            window.blit(key.IMAGE, (key.x, key.y))
        for EXIT in data.exit_list:
            pygame.draw.rect(window, EXIT.COLOR, EXIT)
            if EXIT.colliderect(hero):
                hero = Hero(45, 10, 60, 136, hero_list, 4, hero.LVL + 1)
                hero.deletewalls(4)
                enemy = Enemy(850, 100, 94, 102, robot_list, 4, "y")
                key = Key(900, 100, 69, 30, key_png)
                hero.lose()
                enemy.lose()
        for wall in data.wall_list:
            pygame.draw.rect(window, wall.COLOR, wall)
        for door in data.door_list:
            pygame.draw.rect(window, door.COLOR, door)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w or event.key == pygame.K_UP:
                    hero.MOVE["UP"] = True
                if event.key == pygame.K_s or event.key == pygame.K_DOWN:
                    hero.MOVE["DOWN"] = True
                if event.key == pygame.K_a or event.key == pygame.K_LEFT:
                    hero.MOVE["LEFT"] = True
                if event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                    hero.MOVE["RIGHT"] = True
                if event.key == pygame.K_g:
                    hero.GODMODE = True
                    print("GODMODE true")
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_w or event.key == pygame.K_UP:
                    hero.MOVE["UP"] = False
                if event.key == pygame.K_s or event.key == pygame.K_DOWN:
                    hero.MOVE["DOWN"] = False
                if event.key == pygame.K_a or event.key == pygame.K_LEFT:
                    hero.MOVE["LEFT"] = False
                if event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                    hero.MOVE["RIGHT"] = False
                if event.key == pygame.K_g:
                    hero.GODMODE = False
                    print("GODMODE false")

        if hero.colliderect(enemy) and hero.GODMODE == False:
            hero.lose()
            enemy.lose()
            if hero.LVL == 1:
                key = Key(175, 420, 69, 30, key_png)
            elif hero.LVL == 1:
                key = Key(900, 100, 69, 30, key_png)
        if key != 0 and hero.colliderect(key):
            hero.HAVE_KEY = True
            key = 0

        clock.tick(80)
        pygame.display.flip()


run()
