# SEV Advanced - Introduction to Game Development

# start your game code here!
import pgzrun # import game library!
import random

# set up screen
WIDTH = 1000
HEIGHT = 600
SCOREBOX_HEIGHT = 50

score = 0
SCORE_END = -20 # end the game when the score becomes <= -20

# Speeds
junk_speed = 5
SAT_SPEED = 3
deb_speed = 5
laser_speed = -10


BACKGROUNG_IMG = "space_background"
PLAYER_IMG = 'player_ship'
JUNK_IMG = "my_space_junk"
SAT_IMG = 'my_game_satellite'
DEBRIS_IMG = 'broken_satellite'
LASER_IMG = 'laser_red'


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

# INITIALIZA LAsERS
lasers = []

sounds.spacelife.play(-1)

# main game loop
def update():
    if score > SCORE_END: # negative value -20
        updatePlayer()
        updateJunk()
        updateSatellite()
        updateDebris()
        updateLasers()
    if score <= SCORE_END:
        sounds.spacelife.stop()

def draw():
    screen.clear()
    screen.blit(BACKGROUNG_IMG, (0,0))
    player.draw()
    for junk in junks:
        junk.draw()
    sat.draw()
    debris.draw()
    for laser in lasers:
        laser.draw()

    # draw text on screen
    show_score = "Score: " + str(score)
    screen.draw.text(show_score, fontsize=35, topleft=(850,15), color="black")

    # show GAME OVER
    show_game_over = "GAME OVER"
    if score <= SCORE_END:
        BACKGROUNG_IMG = (0, 0, 0)
        screen.draw.text(show_game_over, fontsize=60, center=(WIDTH/2, HEIGHT/2), color="red", ocolor='white', owidth=0.5)
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
    # fire lasers
    if keyboard.space == 1:
        laser = Actor(LASER_IMG)
        laser.midright = (player.midleft)
        fireLasers(laser) # firing lasers

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
        score += -5
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
        score += -5
        sounds.explosion.play()

def updateLasers():
    global score
    for laser in lasers:
        laser.x += laser_speed

        collision_sat = sat.colliderect(laser)
        collision_debris = debris.colliderect(laser)

        if laser.right < 0 or collision_sat == 1 or collision_debris == 1:
            lasers.remove(laser)
        # reposition our sprites
        if collision_sat == 1:
            x_sat = random.randint(-500, -50)
            y_sat = random.randint(60, HEIGHT - sat.height)
            sat.topright = (x_sat, y_sat)
            score += -5

        if collision_debris == 1:
            x_debris = random.randint(-500, -50)
            y_debris = random.randint(60, HEIGHT - debris.height)
            debris.topright = (x_debris, y_debris)
            score += 5

# activating lasers (template code)____________________________________________________________________________________________
player.laserActive = 1  # add laserActive status to the player

def makeLaserActive():  # when called, this function will make lasers active again
    global player
    player.laserActive = 1

def fireLasers(laser):
    if player.laserActive == 1:  # active status is used to prevent continuous shoot when holding space key
        player.laserActive = 0
        clock.schedule(makeLaserActive, 0.2)  # schedule an event (function, time afterwhich event will occur)
        sounds.laserfire02.play()  # play sound effect
        lasers.append(laser)  # add laser to lasers list     
  

pgzrun.go()

