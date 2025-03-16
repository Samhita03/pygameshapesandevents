import pygame
WIDTH= 600
HEIGHT=600
TITLE="Shapes and events"
screen=pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption(TITLE)

class Circle():
    def __init__(self,c,r,x,y):
        self.color=c
        self.radius=r
        self.x=x
        self.y=y
    def draw(self):
        pygame.draw.circle(screen,self.color,(self.x,self.y),self.radius,0)
circle= Circle("blue",90,300,300)


        
 
   
run=True
screen.fill("black")
while run==True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            run=False
        if event.type==pygame.MOUSEBUTTONDOWN:
            circle.draw()
        if event.type==pygame.MOUSEBUTTONUP:
            screen.fill("black")
        if event.type==pygame.MOUSEMOTION:
            pos=pygame.mouse.get_pos()
            circle2= Circle("blue",10,pos[0],pos[1])
            circle2.draw()
    pygame.display.update()