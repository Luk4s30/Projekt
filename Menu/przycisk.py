import pygame

#button class
class Przycisk():
	def __init__(self, x, y, image, scale):
		width = image.get_width()
		height = image.get_height()
		self.image = pygame.transform.scale(image, (int(width * scale), int(height * scale)))
		self.rect = self.image.get_rect()
		self.rect.center = (x, y)
		self.clicked = False

	def rysuj(self, surface):
		action = False
		pos = pygame.mouse.get_pos()    #pozycja myszki

		if self.rect.collidepoint(pos): #sprawdzanie czy kursor najeżdża na przycisk
			if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:        #sprawdza czy było kliknięcie
				self.clicked = True
				action = True

		if pygame.mouse.get_pressed()[0] == 0:
			self.clicked = False

		surface.blit(self.image, (self.rect.x, self.rect.y))    #rysuje przycisk

		return action
