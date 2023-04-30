import pygame
pygame.init()

setting_win = {
    "Width": 1024,
    "Height": 768
}

name_image_list = [
    "bullet.png", "bg.png", "Player.png", "Player_left.png", "Player_right.png", "robot.png", "robot_left.png", "robot_right.png", "robot_guner.png", "robot_guner_shot.png"
    ]
image_list = list()

for image in name_image_list:
    image_list.append(pygame.image.load("sprites\\" + image))

hero_list = [image_list[3], image_list[4], image_list[5]]

robot_list = [image_list[6], image_list[7], image_list[8]]

guner_list = [image_list[9], image_list[10], image_list[1]]