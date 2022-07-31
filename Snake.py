import pygame
pygame.init()
window = pygame.display.set_mode((400,300))
pygame.display.set_caption("Snake game")

white = ((255,255,255))
black = ((0,0,0))
red =((255,0,0))
game_over = False

x1 = 300
y1 = 300

new_x = 0
new_y = 0
clock = pygame.time.Clock()

while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: #This allows the user to exit the window 
            game_over =True
        if event.type == pygame.KEYDOWN: #This allows the event of using the keyboard to move up,down,left and right
            if event.type == pygame.K_LEFT:
                new_x = -10
                new_y = 0
            elif event.type == pygame.K_RIGHT:
                new_x = 10
                new_y = 0
            elif event.type == pygame.K_UP:
                new_y = -10
                new_x = 0
            elif event.type == pygame.K_DOWN:
                new_y = 10
                new_x = 10 
    x1 += new_x
    y1 += new_y
    window.fill(white)
    pygame.draw.rect(window,black,[x1,y1,10,10])
    pygame.display.update()
    clock.tick(10)


pygame.quit()
quit()