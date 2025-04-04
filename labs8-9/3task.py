import pygame
pygame.display.set_caption("Current mode: Brush. Current color: Blue." + "; r=red; g=green; b=blue; l=brush; c=circle; p=rectangle; e=eraser; s=square; t=right triange; h=equilateral triangle; o=rhombus ")
data = [] # save to all elements(objects)
elements = 0 # amount object
def main(): # main function
    pygame.init()
    screen = pygame.display.set_mode((1280, 720))
    clock = pygame.time.Clock()
    
    radius = 15
    mode = 'Blue'
    drawmode = 'Brush' # starter tool
    oldmode = 'Brush'
    oldcmode = 'Blue'
    while True: # main loop
        
        pressed = pygame.key.get_pressed()
        
        alt_held = pressed[pygame.K_LALT] or pressed[pygame.K_RALT]
        ctrl_held = pressed[pygame.K_LCTRL] or pressed[pygame.K_RCTRL]

        for event in pygame.event.get():
            
            # determin if X was clicked, or Ctrl+W or Alt+F4 used
            if event.type == pygame.QUIT:
                return
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w and ctrl_held:
                    return
                if event.key == pygame.K_F4 and alt_held:
                    return
                if event.key == pygame.K_ESCAPE:
                    return
            
                # determine if letter was pressed
                if event.key == pygame.K_r:
                    mode = 'Red'
                elif event.key == pygame.K_g:
                    mode = 'Green'
                elif event.key == pygame.K_b:
                    mode = 'Blue'
                #checking shapes
                if event.key == pygame.K_l:
                    drawmode = 'Brush'
                elif event.key == pygame.K_c:
                    drawmode = 'Circle'
                elif event.key == pygame.K_p:
                    drawmode = 'Rectangle'
                elif event.key == pygame.K_e:
                    drawmode = 'Eraser'
                elif event.key == pygame.K_s:
                    drawmode = 'Square'
                elif event.key == pygame.K_t:
                    drawmode = 'Right Triangle'
                elif event.key == pygame.K_h:
                    drawmode = 'Equilateral Triangle'
                elif event.key == pygame.K_o:
                    drawmode = 'Rhombus'
                if oldmode != drawmode:
                    oldmode = drawmode # exchange curreent draw_mode
                    pygame.display.set_caption("Current mode: "+drawmode+" Current color: "+mode + "; r=red; g=green; b=blue; l=brush; c=circle; p=rectangle; e=eraser; s=square; t=right triange; h=equilateral triangle; o=rhombus ")  #update paint status
                if oldcmode != mode:
                    oldcmode = mode # exchange current mode
                    pygame.display.set_caption("Current mode: "+drawmode+" Current color: "+mode + "; r=red; g=green; b=blue; l=brush; c=circle; p=rectangle; e=eraser; s=square; t=right triange; h=equilateral triangle; o=rhombus ") #update paint status
            screen.fill((0, 0, 0))    
            if event.type == pygame.MOUSEBUTTONDOWN: # if mouse clicked
                if event.button == 1: #check if clicked, add to draw
                    drawadd(event.pos, radius, mode, drawmode)
                if event.button == 4: #check mousewhell, increase or decrease the radius
                    radius = min(200, radius + 1)
                elif event.button == 5:
                    radius = max(1, radius - 1)
                
        draw(screen)
        pygame.display.flip() # обновлять screen
        
        clock.tick(60)

def drawadd(start, width, color_mode, draw_mode): # add new object for draw
    global data, elements
    if color_mode == 'Blue': # color mode
        color = (0, 0, 255)
    elif color_mode == 'Red':
        color = (255, 0, 0)
    elif color_mode == 'Green':
        color = (0, 255, 0)
    clist = [] # creating data list for our drawing
    clist.append(start[0]) # x-coordinate
    clist.append(start[1]) # y - coordinate
    clist.append(width) # object size
    clist.append(color)
    clist.append(draw_mode) # object type
    data.append(clist) # appending this list to gen data
    elements += 1

def draw(screen): # draw function
    global data, elements 
    if elements != 0: # checking if elements exist
        for element in data:
            if element[4] == 'Brush': # checking every possible shape
                pygame.draw.circle(screen, element[3], (element[0], element[1]), element[2])
            elif element[4] == 'Circle':
                pygame.draw.circle(screen, element[3], (element[0], element[1]), element[2], 1)
            elif element[4] == 'Rectangle':
                pygame.draw.rect(screen, element[3], pygame.Rect(element[0], element[1], element[2], element[2] / 2), 1)
            elif element[4] == 'Eraser':
                pygame.draw.circle(screen, (0,0,0), (element[0], element[1]), element[2])
            elif element[4] == 'Square':
                pygame.draw.rect(screen, element[3], pygame.Rect(element[0], element[1], element[2], element[2]), 1)
            elif element[4] == 'Right Triangle':
                pygame.draw.polygon(screen, element[3], ((element[0], element[1]), (element[0] + element[2], element[1]), (element[0], element[1] - element[2])), 1)
            elif element[4] == 'Equilateral Triangle':
                pygame.draw.polygon(screen, element[3], ((element[0], element[1]), (element[0] - (element[2] / 2), element[1] + element[2]), (element[0] + (element[2] / 2), element[1] + element[2])), 1)
            elif element[4] == 'Rhombus':
                pygame.draw.polygon(screen, element[3], ((element[0], element[1]), (element[0] - (element[2] / 2), element[1] + element[2]), (element[0], element[1] + (element[2] * 2)), (element[0] + (element[2] / 2), element[1] + element[2])), 1)
main()