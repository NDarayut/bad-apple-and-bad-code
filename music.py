import pygame

#Playing the music
def music():
    pygame.init()
    pygame.mixer.init()
    sound = pygame.mixer.Sound("BadappleAud.mp3")
    sound.set_volume(0.2)
    sound.play()
    while pygame.mixer.get_busy():
        pygame.time.delay(100)
#pygame is the only option I found work best, you can use playsound too, however you can's adjust the volume