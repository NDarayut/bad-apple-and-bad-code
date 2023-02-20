import pygame
def music():
    pygame.init()
    pygame.mixer.init()
    sound = pygame.mixer.Sound("BadappleAud.mp3")
    sound.set_volume(0.2)
    sound.play()
    while pygame.mixer.get_busy():
        pygame.time.delay(100)
