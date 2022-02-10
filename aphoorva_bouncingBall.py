import pygame, sys
pygame.init()

screen = pygame.display.set_mode((200,200))

pygame.display.set_caption("Bouncing ball")

clock = pygame.time.Clock()

red = (200,0,0)
blue = (0,0,200)

bg_img = pygame.image.load('bg.jpg')
bg_img = pygame.transform.scale(bg_img,(200,200)).convert()

while True:
    
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()  
            
    y1 = 15
    y2 = 185
    while y1<185 and y2>15:        
        screen.blit(bg_img,(True,0))
        pygame.draw.circle(screen,red,(50,y1),10)
        pygame.draw.circle(screen,blue,(150,y2),10)
        y1 = y1 + 1            
        y2 = y2 - 1
        pygame.display.update()
        clock.tick(30)
    
    while y1>0 and y2<185:        
        screen.blit(bg_img,(True,0))
        pygame.draw.circle(screen,red,(50,y1),10)
        pygame.draw.circle(screen,blue,(150,y2),10)
        y1 = y1 - 1            
        y2 = y2 + 1
        pygame.display.update()
    
pygame.quit()