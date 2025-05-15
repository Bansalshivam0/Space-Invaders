import pygame
import random
import math

# Initialize the game
pygame.init()

# Create the screen
screen = pygame.display.set_mode((800, 600))

# Background
background = pygame.image.load('background.jpg')

# Set title and icon
pygame.display.set_caption("Space Invaders")
icon = pygame.image.load('game.png').convert_alpha()
icon = pygame.transform.scale(icon, (10, 10))
pygame.display.set_icon(icon)

# Player
playerImg = pygame.image.load('space-invaders.png').convert_alpha()
playerImg = pygame.transform.scale(playerImg, (64, 64))
playerX = 360
playerY = 480
playerX_change = 0

# Enemy
num_of_enemies = 15
enemyImg = pygame.image.load('ufo.png').convert_alpha()
enemyImg = pygame.transform.scale(enemyImg, (64, 64))
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []

for _ in range(num_of_enemies):
    enemyX.append(random.randint(0, 736))
    enemyY.append(random.randint(50, 150))
    enemyX_change.append(0.3)
    enemyY_change.append(20)

# Bullet
bulletImg = pygame.image.load('bullet.png').convert_alpha()
bulletImg = pygame.transform.scale(bulletImg, (64, 64))
bulletX = 0
bulletY = 480
bulletY_change = 5
bullet_state = "ready"  # ready = not visible, fire = moving

# Score
score_value = 0
high_score_value = 0
font = pygame.font.Font('freesansbold.ttf', 32)

# Functions
def show_score(x, y):
    score = font.render("Score : " + str(score_value), True, (255, 255, 255))
    screen.blit(score, (x, y))

def show_high_score(x, y):
    high_score = font.render("High Score : " + str(high_score_value), True, (255, 255, 255))
    screen.blit(high_score, (x, y))

def game_over_text():
    over_text = font.render("GAME OVER", True, (255, 0, 0))
    screen.blit(over_text, (300, 250))

def player(x, y):
    screen.blit(playerImg, (x, y))

def enemy(x, y):
    screen.blit(enemyImg, (x, y))

def fire_bullet(x, y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletImg, (x + 10, y + 16))

def is_collision(enemy_x, enemy_y, bullet_x, bullet_y):
    distance = math.sqrt((enemy_x - bullet_x)**2 + (enemy_y - bullet_y)**2)
    return distance < 27

# Game Loop
running = True
while running:
    screen.fill((85, 85, 85))
    screen.blit(background, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Key events
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -0.3
            if event.key == pygame.K_RIGHT:
                playerX_change = 0.3
            if event.key == pygame.K_SPACE and bullet_state == "ready":
                bulletX = playerX
                bulletY = playerY
                fire_bullet(bulletX, bulletY)

        if event.type == pygame.KEYUP:
            if event.key in (pygame.K_LEFT, pygame.K_RIGHT):
                playerX_change = 0

    # Player movement
    playerX += playerX_change
    playerX = max(0, min(playerX, 736))

    # Enemies
    for i in range(num_of_enemies):
        enemyX[i] += enemyX_change[i]

        if enemyX[i] <= 0:
            enemyX_change[i] = 0.3
            enemyY[i] += enemyY_change[i]
        elif enemyX[i] >= 736:
            enemyX_change[i] = -0.3
            enemyY[i] += enemyY_change[i]

        # Collision detection
        if is_collision(enemyX[i], enemyY[i], bulletX, bulletY):
            bullet_state = "ready"
            bulletY = playerY
            score_value += 1
            high_score_value = max(score_value, high_score_value)
            enemyX[i] = random.randint(0, 736)
            enemyY[i] = random.randint(50, 150)

        # Game over
        if pygame.Rect(playerX, playerY, 64, 64).colliderect(pygame.Rect(enemyX[i], enemyY[i], 64, 64)):
            for j in range(num_of_enemies):
                enemyY[j] = 2000
            game_over_text()
            pygame.display.update()
            pygame.time.wait(2000)
            running = False
            break

        enemy(enemyX[i], enemyY[i])

    # Bullet movement
    if bullet_state == "fire":
        fire_bullet(bulletX, bulletY)
        bulletY -= bulletY_change
        if bulletY < 0:
            bullet_state = "ready"
            bulletY = playerY

    player(playerX, playerY)
    show_score(10, 10)
    show_high_score(500, 10)
    pygame.display.update()

pygame.quit()
