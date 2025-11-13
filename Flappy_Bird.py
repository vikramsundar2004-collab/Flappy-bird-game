import pygame
import random
pygame.init()
count=0
class Bird:

    def __init__(self, x, y, velocity, color):
        self.x = x
        self.y = y
        self.velocity = velocity
        self.color = color
        self.jump_velocity = 7
        self.hitbox=pygame.Rect(self.x-10,self.y-10,20,20)#20 is for the diameter of the bird circle

    def jump(self):
        self.velocity = -self.jump_velocity

    def draw(self, screen):
        pygame.draw.circle(screen, self.color,[self.x,self.y],10)

    def update(self):
        self.y += self.velocity
        self.velocity += .4
        if self.y > 400:
            self.y = 400
        if self.y<0:
            self.y=5
        self.hitbox.y=self.y-10
startingx=800
class Pipe:
    def __init__(self, x,y,length):
        self.x = x
        self.y = y
        self.color = [51, 125, 72]
        self.speed = 5
        self.length=length
        self.hitbox=pygame.Rect(self.x,self.y,50,self.length)

    def move(self):
        self.x -= 1
        if self.x<0:
            self.x=startingx
        self.hitbox.x=self.x
    def draw(self, screen):
        #pygame.draw.rect(screen, self.color, [self.x, self.y-10, 50,self.length ] )
        pygame.draw.rect(screen,self.color, self.hitbox)


WIDTH, HEIGHT = 800,400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
font = pygame.font.SysFont('Arial', 36)
pipes=[]
for i in range(4):
    length = random.randint(75, 300)
    pipes.append(Pipe(800 + i * 200, 0, length))
    pipes.append(Pipe(800 + i * 200, length + 100, 999))
game_over=False
clock=pygame.time.Clock()
bird_1=Bird(100,700,10,('#00ff00'))
while True:
    screen.fill('#87cefa')  # background color
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bird_1.jump()
    bird_1.update()
    bird_1.draw(screen)
    text=font.render(f"Score:{count//50}",True,(255,0,0))
    screen.blit(text,[0,0,100,100])
    for pipe in pipes:
        pipe.draw(screen)
        pipe.move()
        if bird_1.hitbox.colliderect(pipe.hitbox):
            game_over=True
    if game_over==False:
        pygame.display.flip()
    clock.tick(50)

    count+=1

