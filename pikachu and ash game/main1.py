import pgzrun
from random import randint

WIDTH = 1400
HEIGHT = 800

score = 0
game_over = False

charmander = Actor("charmander")
charmander.pos = 200, 200

pickachu = Actor("pickachu")
pickachu.pos = 400, 400

def draw():
    screen.blit("bg", (0,0))
    pickachu.draw()
    charmander.draw()
    screen.draw.text("Score = " + str(score), color = "blue", midtop = (700, 10), fontsize = 40)

if game_over:
        screen.fill("green")
        screen.draw.text("Your time is up! Your score is " + str(score), midtop = (WIDTH / 2, 10), fontsize = 40, color = "blue")

def place_pickachu():
    pickachu.x = randint(70, (WIDTH - 70)) 
    pickachu.y = randint(70, (HEIGHT - 70))

def time_up():
    global game_over 
    game_over = True
def update():
    global score
    if keyboard.left:
       charmander.x -= 2
    if keyboard.right:
       charmander.x += 2
    if keyboard.up:
       charmander.y -= 2
    if keyboard.down:
       charmander.y += 2 
    if charmander.distance_to(pickachu) < 20:
            score += 1
            screen.draw.text("Score = " + str(score), color = "blue", midtop = (700, 10), fontsize = 40)
            place_pickachu()

clock.schedule(time_up, 10.0)

pgzrun.go()
