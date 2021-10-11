from engine import *

game = Game()
game.create_screen((1280,680))     
game.onQuit = pygame.quit   
# Creating Sprite Definition
sprite = game.image_sprite("./assets/ssl.png",50,50)
# Shrinking Sprite
sprite.shrink(3)

# Create Background Definition
bg = game.background_image("./assets/bg.jpg")

ypos = 550
bulletImage = pygame.image.load("./assets/bullet.png")
bulletImage = pygame.transform.scale(bulletImage,(32,32))
bulletY = 545
bullet_state = "ready"

def fire_bullet(x):
    global bullet_state
    bullet_state = "fire"
    game.screen.blit(bulletImage,(x,bulletY))
while True:
    bulletX = sprite.get_XPosition()+62
    # Setting Background Color
    game.set_bgcolor((0,250,255))
    # Drawing Background Image
    bg.draw()
    if bulletY <=0:
        bulletY = 545
        bullet_state = "ready"
    if bullet_state == "fire":
        fire_bullet(bulletX)
        bulletY-=10
        
    # Drawing Sprite
    sprite.draw()     
    sprite.setPosToCursorPos(True,550,True) 
    if game.key_pressed(pygame.K_SPACE):
        bullet_state = "fire"
    # Setting Sprite Position to Cursor Position
    
    
    game.run()