# SEV Advanced - Introduction to Game Development

# start your game code here!
import pgzrun # import game library!
import random

# set up screen
WIDTH = 1000
HEIGHT = 600
SCOREBOX_HEIGHT = 50

score = 0

# Speeds
junk_speed = 5
SAT_SPEED = 4
deb_speed = 5
healing_speed = 3


BACKGROUNG_IMG = "space_background"
PLAYER_IMG = 'player_ship'
JUNK_IMG = "my_space_junk"
SAT_IMG = 'my_game_satellite'
DEBRIS_IMG = 'broken_satellite'
HEAL_IMG = 'heal_satellite'


player = Actor(PLAYER_IMG)
player.midright = (WIDTH-15, HEIGHT/2)

junk = Actor(JUNK_IMG)
junk.pos = (0, HEIGHT/2)

# INITIALIZE JUNKS
junks = []
for i in range(5):
    junk = Actor(JUNK_IMG)
    x_pos = random.randint(-500, -50)
    y_pos = random.randint(60, HEIGHT - junk.height)
    junk.topleft = (x_pos, y_pos)
    junk.junk_speed = random.randint(2, 10)
    junks.append(junk)

#intialize satellite sprites
sat = Actor(SAT_IMG) # sat = satellite
x_sat = random.randint(-500, -50)
y_sat = random.randint(60, HEIGHT - sat.height)
sat.topright = (x_sat, y_sat)

#intialize satellite sprites
debris = Actor(DEBRIS_IMG)
x_debris = random.randint(-500, -50)
y_debris = random.randint(60, HEIGHT - debris.height)
debris.topright = (x_debris, y_debris)

#
healing = Actor(HEAL_IMG)
x_healing = random.randint(-500, -50)
y_healing = random.randint(60, HEIGHT - healing.height)
healing.topright = (x_healing, y_healing)

# main game loop
def update():
    updatePlayer()
    updateJunk()
    junk.angle -= 1
    updateSatellite()
    updateDebris()
    updateHealing()

def draw():
    screen.clear()
    screen.blit(BACKGROUNG_IMG, (0,0))
    player.draw()
    for junk in junks:
        junk.draw()
    sat.draw()
    debris.draw()
    healing.draw()

    # draw text on screen
    show_score = "Score: " + str(score)
    screen.draw.text(show_score, fontsize=35, topleft=(850,15), color="black")

def updatePlayer():
    # detect player input
    if (keyboard.UP == 1):
        #player.y = + (-5)
        player.y += -5

    elif keyboard.DOWN == 1:
        #player.y = + 5
        player.y += 5
    if player.top < SCOREBOX_HEIGHT:
        player.top = SCOREBOX_HEIGHT
    if player.bottom > HEIGHT:
        player.bottom = HEIGHT

def updateJunk():
    global score, junk_speed
    for junk in junks:
        junk.x += junk.junk_speed
    
        collision = player.colliderect(junk)

        if junk.left > WIDTH or collision == 1:
            x_pos = random.randint(-500, -50) # strating junk off screen
            y_pos = random.randint(60, HEIGHT - junk.height)
            junk.topleft = (x_pos, y_pos)
        
        if collision == 1:
            print("collision")
            score += 1
            sounds.collect_pep.play()

def updateSatellite():
    global score
    sat.x += SAT_SPEED # moving 3 pixels every loop

    collision = player.colliderect(sat)

    if sat.left > WIDTH or collision ==1:
        x_sat = random.randint(-500, -50)
        y_sat = random.randint(60, HEIGHT - sat.height)
        sat.topright = (x_sat, y_sat)

    if collision == 1:
        score += -10
        sounds.explosion.play()

def updateDebris():
    global score
    debris.x += deb_speed

    collision = player.colliderect(debris)

    if debris.left > WIDTH or collision ==1:
        x_debris = random.randint(-500, -50)
        y_debris = random.randint(60, HEIGHT - debris.height)
        debris.topright = (x_debris, y_debris)

    if collision == 1:
        score += -10
        sounds.explosion.play()

def updateHealing():
    global score
    healing.x += healing_speed

    collision = player.colliderect(healing)

    if healing.left > WIDTH or collision ==1:
        x_healing = random.randint(-500, -50)
        y_healing = random.randint(60, HEIGHT - healing.height)
        healing.topright = (x_healing, y_healing)

    if collision == 1:
        score += +10
        sounds.collect_pep.play()

        
  

pgzrun.go()

