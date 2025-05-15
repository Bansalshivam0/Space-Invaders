# import pygame
# import random
#
# # Initialization of the game
# pygame.init()
#
# # Create the screen
# screen = pygame.display.set_mode((800, 600))
#
# # Background
# background = pygame.image.load('background.jpg')
#
# # Set window title and icon
# pygame.display.set_caption("Space Invaders")
# icon = pygame.image.load('game.png').convert_alpha()
# icon = pygame.transform.scale(icon, (10, 10)).convert_alpha()
# pygame.display.set_icon(icon)
#
# # Load and resize the player image
# playerImg = pygame.image.load('space-invaders.png').convert_alpha()
# playerImg = pygame.transform.scale(playerImg, (64, 64))  # Resize to 64x64 pixels
# playerX = 360
# playerY = 480
# playerX_change = 0  # Initialize movement variable
#
# # Enemy
# enemyImg = pygame.image.load('alien.png').convert_alpha()
# enemyImg = pygame.transform.scale(enemyImg, (64, 64))  # Resize to 64x64 pixels
# enemyX = random.randint(0, 736)  # Random starting x-coordinate
# enemyY = random.randint(50, 150)
# enemyX_change = 0.3  # Initialize movement variable
# enemyY_change = 20
#
# # Bullet
# # "ready" - You can't see the bullet on the screen
# # "fire"  - Bullet is currently moving
# bulletImg = pygame.image.load('bullet.png').convert_alpha()
# bulletImg = pygame.transform.scale(bulletImg, (64, 64))  # Correctly scale the bullet image
# bulletX = 0
# bulletY = 480
# bulletY_change = 10
# bullet_State = "ready"
#
# def player(x, y):
#     screen.blit(playerImg, (x, y))
#
# def enemy(x, y):
#     screen.blit(enemyImg, (x, y))
#
# def fire_bullet(x, y):
#     global bullet_State
#     bullet_State = "fire"
#     # Adjust bullet position for better alignment with the player
#     screen.blit(bulletImg, (x + 10, y + 16))
#
# # Game Loop
# running = True
# while running:
#     # Fill the screen with a color and draw the background image
#     screen.fill((85, 85, 85))
#     screen.blit(background, (0, 0))
#
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False
#
#         # Keydown events
#         if event.type == pygame.KEYDOWN:
#             if event.key == pygame.K_LEFT:
#                 playerX_change = -0.3
#             if event.key == pygame.K_RIGHT:
#                 playerX_change = 0.3
#             if event.key == pygame.K_SPACE:
#                 if bullet_State == "ready":
#                     bulletX = playerX  # Set bullet starting x-coordinate at player's position
#                     bulletY = playerY  # Set bullet starting y-coordinate at player's position
#                     fire_bullet(bulletX, bulletY)
#
#         # Keyup events
#         if event.type == pygame.KEYUP:
#             if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
#                 playerX_change = 0  # Stop movement when key is released
#
#     # Update player position and keep within boundaries
#     playerX += playerX_change
#     if playerX <= 0:
#         playerX = 0
#     elif playerX >= 736:  # 800 - 64 (player width)
#         playerX = 736
#
#     # Update enemy position
#     enemyX += enemyX_change
#     if enemyX <= 0:
#         enemyX_change = 0.3
#         enemyY += enemyY_change
#     elif enemyX >= 736:  # 800 - 64 (enemy width)
#         enemyX_change = -0.3
#         enemyY += enemyY_change
#
#     # Bullet movement
#     if bullet_State == "fire":
#         fire_bullet(bulletX, bulletY)
#         bulletY -= bulletY_change
#     # Reset bullet when it goes off the screen
#     if bulletY < 0:
#         bullet_State = "ready"
#         bulletY = playerY
#
#     player(playerX, playerY)
#     enemy(enemyX, enemyY)
#     pygame.display.update()
#
# pygame.quit()


# import pygame
# import random
# import math
#
# # Initialization of the game
# pygame.init()