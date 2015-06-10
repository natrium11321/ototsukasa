import pygame

class Speaker:
	
	def __init__(self):
		pygame.init()
		pygame.mixer.quit()
		pygame.mixer.init()
		self.sound = {}
		self.sound["test"] = pygame.mixer.Sound("/usr/share/sounds/alsa/Front_Center.wav")
	
	def speak(self, name):
		self.sound[name].play()
