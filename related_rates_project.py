import pygame
pygame.init()
import math

# variable presets
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
blue = (0, 0, 255)
green = (0, 255, 0)
base_distance = 0
height_distance = 152
red_rect = pygame.Rect(585, 335, 30, 30)
reset_rect = pygame.Rect(20, 220, 760, 260)
text_font = pygame.font.SysFont("microsofthimalaya", 40)

# introduction and given values
print()
print("The following program tells how fast a ladder is sliding down a house when given some parameters")
input()
ladder_length = float(input("How long is the ladder?(no units) "))
base_rate = float(input("Assuming that the base of the ladder is moving at a constant rate, what is it?(no units) "))
base_length = float(input("At what distance is the base of the ladder from the house?(no units) "))
print()

# checking for errors in the user's values
if base_length >= ladder_length or base_length <= 0 or 30 * base_length <= ladder_length:
    print("retry and input an appropriate value")
    input()

# equation and derivative
print("With these values you can form the equation x^2 + y^2 = " + str(ladder_length) + "^2")
print("When you differentiate and simplify this equation you get x(dx/dt) + y(dy/dt) = 0")
print()

# solving for values and pluggin in
height_length = math.sqrt(math.pow(ladder_length, 2) - math.pow(base_length, 2))
print("When you plug " + str(ladder_length) + " and " + str(base_length) + " into Pythagorean's Theorem, you would solve it and get " + str(height_length))
print("You would then plug all of your known values into the differentiated equation and get (" + str(base_length) + ")(" + str(base_rate) + ") + (" + str(height_length) + ")(dy/dt) = 0")

# solving problem
moment_height_rate = (-(base_length * base_rate))/(height_length)
print("When you solve for (dy/dt), you get " + str(round(moment_height_rate, 3)) + " length unit/time unit")
print()

# explaining window
print("The following window shows 2 pictures of the scenario and 1 picture depicting the movment")
print("The velocity is shown on the left of the movement picture and to the right a red square appears when the moment in time in the picture equals the momemnt in time of the problem")

# ratio for picture
base_to_hypotenuse = (base_length / ladder_length)
height_to_hypotenuse = (height_length / ladder_length)

# initializing screen
screen = pygame.display.set_mode((800, 500))
screen.fill((white))

# screen and borders
pygame.draw.line(screen, black, (0, 200), (800, 200), 5)
pygame.draw.line(screen, black, (400, 0), (400, 200), 5)
pygame.draw.line(screen, black, (0, 0), (800, 0), 20)
pygame.draw.line(screen, black, (800, 0), (800, 500), 20)
pygame.draw.line(screen, black, (800, 500), (0, 500), 20)
pygame.draw.line(screen, black, (0, 500), (0, 0), 20)

# top left picture
img = text_font.render("Before", True, black)
screen.blit(img, (215, 25))
pygame.draw.line(screen, black, (77.5, 0), (140, 62.5), 5)
pygame.draw.line(screen, black, (140, 60), (0, 60), 5)
pygame.draw.line(screen, black, (125, 60), (125, 180), 5)
pygame.draw.line(screen, black, (0, 180), (800, 180), 5)

# top right picture
img = text_font.render("After", True, black)
screen.blit(img, (215 + 400, 25))
pygame.draw.line(screen, black, (77.5 + 400, 0), (140 + 400, 62.5), 5)
pygame.draw.line(screen, black, (140 + 400, 60), (0 + 400, 60), 5)
pygame.draw.line(screen, black, (125 + 400, 60), (125 + 400, 180), 5)

# top left triangle(before)
if (height_length / base_length) < 2:
    pygame.draw.line(screen, red, (125, 180), (125 + 47, 180), 5)
    pygame.draw.line(screen, blue, (125, 180 - 94), (125, 180), 5)
    pygame.draw.line(screen, green, (125, 180 - 94), (125 + 47, 180), 5)
else:
    pygame.draw.line(screen, red, (125, 180), (125 + 15, 180), 5)
    pygame.draw.line(screen, blue, (125, 180 - 103), (125, 180), 5)
    pygame.draw.line(screen, green, (125, 180 - 103), (125 + 15, 180), 5)

# top right triangle(after)
pygame.draw.line(screen, red, (125 + 400, 180), (125 + 400 + (105 * base_to_hypotenuse), 180), 5)
pygame.draw.line(screen, blue, (125 + 400, 180 - (105 * height_to_hypotenuse)), (125 + 400, 180), 5)
pygame.draw.line(screen, green, (125 + 400, 180 - (105 * height_to_hypotenuse)), (125 + 400 + (105 * base_to_hypotenuse), 180), 5)

# main loop
running = True
while running: 

    # quiting program
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            running = False

    # rectangle for resetting frame to white
    pygame.draw.rect(screen, white, reset_rect)
    
    # calculating new (dy/dt) and changing height & length
    height_rate = (-(base_distance * (base_rate)))/(height_distance) * (1/60)
    base_distance += base_rate * (1/60)
    height_distance += height_rate

    # displaying (dy/dt)
    img = text_font.render("Velocity: " + str(round((height_rate * 60), 3)), True, black)
    screen.blit(img, (40, 330))

    # resetting the base and height values if base or height are too extreme
    if base_distance >= 154 or height_distance <= 0:
        base_distance = 0
        height_distance = 152

    # rectange for showing when the moment in the picture equals the moment in the scenario
    if (height_rate * 60 + 0.25) > moment_height_rate and (height_rate * 60 - 0.25) < moment_height_rate:
        pygame.draw.rect(screen, red, red_rect)

    # middle picture
    pygame.draw.line(screen, black, (225, 200), (315, 285), 5)
    pygame.draw.line(screen, black, (315, 285), (225, 285), 5)
    pygame.draw.line(screen, black, (285, 285), (285, 460), 5)
    pygame.draw.line(screen, black, (285, 460), (515, 460), 5)

    # middle triangle
    pygame.draw.line(screen, red, (285, 460), (285 + 20 + base_distance, 460), 5)
    pygame.draw.line(screen, blue, (285, 460), (285, 460 - height_distance), 5)
    pygame.draw.line(screen, green, (285, 460 - height_distance), (285 + 20 + base_distance, 460), 5)

    pygame.display.flip() 