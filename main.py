import pygame
import random

#initialize pygame
pygame.init()

#constants
WIDTH, HEIGHT = 600, 600
PLAYER_WIDTH, PLAYER_HEIGHT = 50, 50
DEBRIS_WIDTH, DEBRIS_HEIGHT = 40, 40
PLAYER_SPEED = 5
DEBRIS_SPEED = 4
FPS = 60

#Load Images
background = pygame.image.load("ayu.jpg")
player_img = pygame.image.load("player.png")
debris_img = pygame.image.load("debris.png")

#images
player_img = pygame.transform.scale(player_img, (PLAYER_WIDTH, PLAYER_HEIGHT))
debris_img = pygame.transform.scale(debris_img, (DEBRIS_WIDTH, DEBRIS_HEIGHT))

#screen setup
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Chocolate Debris Dodge")

#score setup
score = 0
font = pygame.font.Font(None, 36)

#player setup
player = pygame.Rect(WIDTH//2, HEIGHT - 50, PLAYER_WIDTH, PLAYER_HEIGHT)

#debris setup
debris = []

def spawn_debris():
    x = random.randint(0, WIDTH - DEBRIS_WIDTH)
    debris.append(pygame.Rect(x, 0, DEBRIS_WIDTH, DEBRIS_HEIGHT))

#Start Menu Function
def start_menu():
    menu_running = True
    font_large = pygame.font.Font(None, 50)
    start_text = font_large.render("Click to Start", True, (255, 255, 255))
    
    text_width, text_height = start_text.get_size()
    text_x, text_y = WIDTH // 2 - text_width // 2, HEIGHT // 2 - text_height // 2

    while menu_running:
        screen.blit(background, (0, 0))

        #black rectangle behind text
        pygame.draw.rect(screen, (0, 0, 0), (text_x - 10, text_y - 5, text_width + 20, text_height +10))

        #text on top
        screen.blit(start_text, (text_x, text_y))

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                menu_running =False


start_menu()

#Game Loop
clock = pygame.time.Clock()
running = True
spawn_timer = 0
while running:
    screen.blit(background, (0, 0))


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    #movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player.x > 0:
        player.x -= PLAYER_SPEED
    if keys[pygame.K_RIGHT] and player.x < WIDTH - PLAYER_WIDTH:
        player.x += PLAYER_SPEED

    #spawn debris
    spawn_timer += 1
    if spawn_timer > 30: 
        spawn_debris()
        spawn_timer = 0

    #Move debris
    for d in debris:
        d.y += DEBRIS_SPEED
    
    #Collision Check
    for d in debris:
        if player.colliderect(d):
            print(f"Game Over! Final Score: {score}")
            running = False

    #increase score
    score +=1


    screen.blit(player_img, (player.x, player.y))
    for d in debris:
        screen.blit(debris_img, (d.x, d.y))

    #Display score
    score_text = font.render(f"Score: {score}", True, (255, 255, 255))
    screen.blit(score_text, (10, 10))

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
