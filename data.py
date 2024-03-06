import pygame

pygame.init()

setting_win = {
    "Width": 1000,
    "Height": 700
}

maps = dict(MAP1=[
    "00010000000000000000",
    "00000000000000000000",
    "00000000000000000000",
    "00000000000000000000",
    "00000000000000000000",
    "0000000000000000000e",
    "00000567805678008d0r",
    "00000000000000000000",
    "00000000000000000000",
    "0002000000000000000t",
    "00003400234002002607",
    "00000000000000000000",
    "00000000000000000000",

], MAP2=[
    "00010000000000001000",
    "00000000000000000000",
    "00000000000000000000",
    "00020000000000002000",
    "00003000000000004000",
    "00000000000000000000",
    "00000000000000000000",
    "000000000000000e0000",
    "60000000000000075000",
    "0000000000000000000",
    "000000000000000t0000",
    "00030000000000004000",
    "00000000000000000000",
    "00000000000000000000",
    "00000000000000000000",
    "00000000000000000000"

])

wall_list = list()
door_list = list()
exit_list = list()

name_image_list = [
    "bullet.png", "bg.png", "Player.png", "Player_left.png", "Player_right.png", "robot.png", "robot_left.png",
    "robot_right.png", "robot_guner.png", "robot_guner_shot.png"]
image_list = list()

for image in name_image_list:
    image_list.append(pygame.image.load("sprites\\" + image))

hero_list = [image_list[2], image_list[3], image_list[4]]

robot_list = [image_list[5], image_list[6], image_list[7]]

guner_list = [image_list[8], image_list[9], image_list[1]]
