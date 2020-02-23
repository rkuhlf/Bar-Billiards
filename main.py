import pygame

pygame.init();

pygame.font.init();

screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
display_info = pygame.display.Info()
size = width, height = display_info.current_w, display_info.current_h

while True:
  screen.fill(pygame.Color(255, 255, 255))

  pygame.display.update()