import pygame
import pygame.camera

pygame.camera.init()
camlist = pygame.camera.list_cameras()
print(camlist)
