'''MICHAEL IS A BOMB FUNCTIONS FILE'''
import pygame
import socket

pygame.init()
screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
screenWidth, screenHeight = pygame.display.get_surface().get_size()
pygame.display.init()

def game_loop():
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			quit()

	screen.fill((255,255,255))
	pygame.display.flip()
