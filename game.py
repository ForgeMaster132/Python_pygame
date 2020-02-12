import pygame
import random

pygame.init()
window = pygame.display.set_mode((750,500))
# Importing image files
# ============================================================================
# Importing end-screen image files ==============================
lose_screen = pygame.image.load("lose_screen.jpg")
lose_screen = pygame.transform.scale(lose_screen,(750,500))

win_screen = pygame.image.load("win_screen.png")
win_screen = pygame.transform.scale(win_screen,(750,500))

# Importing fruit image files ===================================
fruit_orange = pygame.image.load("fruit_orange.png")
fruit_orange = pygame.transform.scale(fruit_orange,(50,50))

fruit_apple = pygame.image.load("fruit_apple.png")
fruit_apple = pygame.transform.scale(fruit_apple,(50,50))

fruit_banana = pygame.image.load("fruit_banana.png")
fruit_banana = pygame.transform.scale(fruit_banana,(50,50))

# Importing enemy image files ===================================
enemy_red = pygame.image.load("ghost_red.png")
enemy_red = pygame.transform.scale(enemy_red,(50,50))

enemy_orange = pygame.image.load("ghost_orange.png")
enemy_orange = pygame.transform.scale(enemy_orange,(50,50))

enemy_blue = pygame.image.load("ghost_blue.png")
enemy_blue = pygame.transform.scale(enemy_blue,(50,50))

enemy_green = pygame.image.load("ghost_green.png")
enemy_green = pygame.transform.scale(enemy_green,(50,50))

enemy_purple = pygame.image.load("ghost_purple.png")
enemy_purple = pygame.transform.scale(enemy_purple,(50,50))

# Importing player files ========================================
player_right = pygame.image.load("player_right.png")
player_right = pygame.transform.scale(player_right,(50, 50))

player_left = pygame.image.load("player_left.png")
player_left = pygame.transform.scale(player_left,(50,50))

player_up = pygame.image.load("player_up.png")
player_up = pygame.transform.scale(player_up,(50,50))

player_down = pygame.image.load("player_down.png")
player_down = pygame.transform.scale(player_down,(50,50))
# ============================================================================

# Sizes
width = 50
height = 50

# Player variables
player_x = 375 - width
player_y = 250 - height
player = player_right
speed = 5

# Fruit Variables ============================================================
fruits_collected = 0

banana_taken = False
fruit_banana_x = random.randint(50,250)
fruit_banana_y = random.randint(50,250)

apple_taken = False
fruit_apple_x = random.randint(300,600)
fruit_apple_y = random.randint(250,450)

orange_taken = False
fruit_orange_x = random.randint(50,700)
fruit_orange_y = random.randint(50,450)

# Enemy variables ============================================================
enemy_red_x = 750
enemy_red_y = random.randint(250,450)
enemy_red_speed = random.randint(8,14)

enemy_orange_x = random.randint(250,450)
enemy_orange_y = 500
enemy_orange_speed = random.randint(2,8)

enemy_green_x = random.randint(50,200)
enemy_green_y = 0
enemy_green_speed = random.randint(6,12)

enemy_purple_x = random.randint(500,700)
enemy_purple_y = 500
enemy_purple_speed = random.randint(4,9)

enemy_blue_x = 0
enemy_blue_y = random.randint(50,200)
enemy_blue_speed = random.randint(3,6)
# ============================================================================

# Game state Variables
run = True
success = None
background_color = (0,0,0)

# Game window Title
pygame.display.set_caption("Best Game!")

# Game State =================================================================
while run:
    pygame.time.delay(50)
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
    if success == None:

        keys = pygame.key.get_pressed()

        # Player controls and movement =======================================
        if keys[pygame.K_LEFT]:
            if player_x - speed > 0:
                player = player_left
                window.blit(player,(player_x, player_y, width, height))
                player_x -= speed
        elif keys[pygame.K_RIGHT]:
            if player_x + speed < 700:
                player = player_right
                window.blit(player,(player_x, player_y, width, height))
                player_x += speed
        elif keys[pygame.K_UP]:
            if player_y - speed > 0:
                player = player_up
                window.blit(player,(player_x, player_y, width, height))
                player_y -= speed
        elif keys[pygame.K_DOWN]:
            if player_y + speed < 450:
                player = player_down
                window.blit(player,(player_x, player_y, width, height))
                player_y += speed
        # ====================================================================
        
        # Enemy movements ====================================================
        if enemy_red_x + 10 > -50:
            enemy_red_x -= enemy_red_speed
        else:
            enemy_red_y = random.randint(0,450)
            enemy_red_x = 750
        
        if enemy_orange_y + 10 > -50:
            enemy_orange_y -= enemy_orange_speed
        else:
            enemy_orange_x = random.randint(0,700)
            enemy_orange_y = 500
        
        if enemy_purple_y + 10 < 500:
            enemy_purple_y += enemy_purple_speed
        else:
            enemy_purple_x = random.randint(0,700)
            enemy_purple_y = 0
        
        if enemy_green_y + 10 < 500:
            enemy_green_y += enemy_green_speed
        else:
            enemy_green_x = random.randint(0,700)
            enemy_green_y = 0
        
        if enemy_blue_x + 10 < 750:
            enemy_blue_x += enemy_blue_speed
        else:
            enemy_blue_y = random.randint(0,450)
            enemy_blue_x = 0
        # ====================================================================
        
        # Enemy collision ====================================================
        if (player_x + 35 > enemy_red_x and player_x < enemy_red_x + 40) and \
            (player_y + 35 > enemy_red_y and player_y - 10 < enemy_red_y + 30):
            pygame.time.delay(50)
            success = False
        
        if (player_x + 35 > enemy_orange_x and player_x < enemy_orange_x + 40) and \
            (player_y + 35 > enemy_orange_y and player_y - 10 < enemy_orange_y + 30):
            pygame.time.delay(50)
            success = False

        if (player_x + 35 > enemy_purple_x and player_x < enemy_purple_x + 40) and \
            (player_y + 35 > enemy_purple_y and player_y - 10 < enemy_purple_y + 30):
            pygame.time.delay(50)
            success = False
        
        if (player_x + 35 > enemy_blue_x and player_x < enemy_blue_x + 40) and \
            (player_y + 35 > enemy_blue_y and player_y - 10 < enemy_blue_y + 30):
            pygame.time.delay(50)
            success = False
        
        if (player_x + 35 > enemy_green_x and player_x < enemy_green_x + 40) and \
            (player_y + 35 > enemy_green_y and player_y - 10 < enemy_green_y + 30):
            pygame.time.delay(50)
            success = False
        # ====================================================================
        
        #Fruit collision =====================================================
        if apple_taken == False:
            if (player_x + 40 > fruit_apple_x and player_x - 10 < fruit_apple_x + 40) and \
                (player_y + 40 > fruit_apple_y and player_y - 10 < fruit_apple_y + 40):
                apple_taken = True
                fruits_collected += 1
                if fruits_collected == 3:
                    pygame.time.delay(50)
                    success = True
        if banana_taken == False:
            if (player_x + 40 > fruit_banana_x and player_x - 10 < fruit_banana_x + 40) and \
                (player_y + 40 > fruit_banana_y and player_y - 10 < fruit_banana_y + 40):
                banana_taken = True
                fruits_collected += 1
                if fruits_collected == 3:
                    pygame.time.delay(50)
                    success = True
        if orange_taken == False:
            if (player_x + 40 > fruit_orange_x and player_x - 10 < fruit_orange_x + 40) and \
                (player_y + 40 > fruit_orange_y and player_y - 10 < fruit_orange_y + 40):
                orange_taken = True
                fruits_collected += 1
                if fruits_collected == 3:
                    pygame.time.delay(50)
                    success = True
        # ====================================================================

        # Displays
        # ====================================================================
        window.fill((background_color))
        window.blit(player,(player_x, player_y, width, height))

        # Enemies ===============================================
        window.blit(enemy_orange,(enemy_orange_x, enemy_orange_y, width, height))
        window.blit(enemy_red,(enemy_red_x, enemy_red_y, width, height))
        window.blit(enemy_blue,(enemy_blue_x, enemy_blue_y, width, height))
        window.blit(enemy_green,(enemy_green_x, enemy_green_y, width, height))
        window.blit(enemy_purple,(enemy_purple_x, enemy_purple_y, width, height))
        
        # Fruit =================================================
        if banana_taken == False:
            window.blit(fruit_banana,(fruit_banana_x, fruit_banana_y))
        
        if apple_taken == False:
            window.blit(fruit_apple,(fruit_apple_x,fruit_apple_y))
        
        if orange_taken == False:
            window.blit(fruit_orange,(fruit_orange_x,fruit_orange_y))
        
        if success == None:
            pygame.display.update()
        # ====================================================================

        # Ending the game ====================================================
        if success == True:
            window.blit(win_screen,(0, 0, 750, 500))
            pygame.display.update()
            pygame.time.delay(3000)
            pygame.quit()
            exit(0)
        if success == False:
            window.blit(lose_screen,(0, 0, 750, 500))
            pygame.display.update()
            pygame.time.delay(3000)
            pygame.quit()
            exit(0)
        # ====================================================================