# TODO list
# Make art for the little cross thingies
# get classes for the pole, the ball, and the holes
# get a score working
# get a timer working

import pygame
from button import Button

pygame.init()

pygame.font.init()

scene = "game"

font = pygame.font.SysFont("Arial", 32)
title_font = pygame.font.SysFont("Arial", 128)


def text(words, font, x, y, color=pygame.Color(0, 0, 0)):
  text = font.render(words, True, color)

  textRect = text.get_rect()  
  
  textRect.center = (x, y) 
  screen.blit(text, textRect)


pool_stick_image = pygame.image.load("./poolStick.png")
ball_image = pygame.image.load("./ball.png")
red_ball_image = pygame.image.load("./redBall.png")

screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
display_info = pygame.display.Info()
size = width, height = display_info.current_w, display_info.current_h


play_button = Button(screen, font, "Play")


while True:
  screen.fill(pygame.Color(255, 255, 255))
  if scene == "home":

    screen.blit(pool_stick_image, (0, 0))

    text("Ball", title_font, 300, 100)
    text("Billiards", title_font, 500, 200)

    play_button.render()
  elif scene == "game":
    screen.fill(pygame.Color(100, 200, 100))
    

  pygame.display.update()