import pygame
pygame.init()
screen=pygame.display.set_mode((500,500))
pygame.display.set_caption("Game")
bg=pygame.transform.scale(pygame.image.load("bg.jpg"),(500,500))
done=False
while not done:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            
    screen.blit(bg,(0,0))
    pygame.display.flip()
