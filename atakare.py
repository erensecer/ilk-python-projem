import pygame
pygame.init()

ekran = pygame.display.set_mode((800, 800))
kare = pygame.Rect(100, 50, 50, 50)
kare1 = pygame.Rect(20, 50, 50, 50)

calisiyor = True
while calisiyor:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            calisiyor = False

    tuslar = pygame.key.get_pressed()
    if tuslar[pygame.K_LEFT]:
        kare.x -= 1
    if tuslar[pygame.K_RIGHT]:
        kare.x += 1
    if tuslar[pygame.K_DOWN]:
        kare.y += 1
    if tuslar[pygame.K_UP]:
        kare.y -= 1


        


    ekran.fill((0, 0, 0))
    pygame.draw.rect(ekran, (255, 0, 0), kare)
    pygame.display.flip()



pygame.quit()
