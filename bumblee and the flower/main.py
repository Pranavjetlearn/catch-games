import pgzrun

from random import randint

WIDTH = 600
HEIGHT = 500

score = 0
game_over = False

bee = Actor("bee")
bee.pos = 100, 100
flower = Actor("flower")
flower.pos = 200, 200

def draw():
    screen.blit("bg", (0,0))
    flower.draw()
    bee.draw()
    screen.draw.text("Score = " + str(score), color = "blue", topleft = (10, 10))
    
    if game_over:
        screen.fill("green")
        screen.draw.text("Your time is up! Your score is " + str(score), midtop = (WIDTH / 2, 10), fontsize = 40, color = "blue")

def place_flower():
    flower.x = randint(70, (WIDTH - 70)) 
    flower.y = randint(70, (HEIGHT - 70))

def time_up():
    global game_over 
    game_over = True
def update():
    global score
    if keyboard.left:
        bee.x -= 2
    if keyboard.right:
        bee.x += 2
    if keyboard.up:
        bee.y -= 2
    if keyboard.down:
        bee.y += 2 
    if bee.distance_to(flower) < 20:
            score += 1
            screen.draw.text("Score = " + str(score), color = "blue", topleft = (10, 10))
            place_flower()

clock.schedule(time_up, 60.0)

pgzrun.go()