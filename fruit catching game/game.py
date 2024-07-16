#Pygame and random imports for the game to function
import pygame
import random
#Importing my other python files to access their functions
import my_login
import data_tool

#Function that runs the game
def show_game(current_user):
  #Creating the pygame window
  pygame.init()
  width = 800
  height = 600
  screen = pygame.display.set_mode((width, height))
  pygame.display.set_caption("Fruit Catcher")
  clock = pygame.time.Clock()

  #Creating the variables for the game
  counter = 0
  score = 0
  player_x = width/2
  users = data_tool.read()
  high_score = int(users[current_user]["score"])

  #Font for texts
  font = pygame.font.Font('freesansbold.ttf', 32)

  #Getting the background image
  background = pygame.image.load("background.png").convert()

  #Creating the fruits
  fruit = pygame.image.load("mango.png").convert_alpha()
  num_fruits = 15
  fruit_x = [0] * num_fruits
  fruit_y = [0] * num_fruits
  for i in range(num_fruits):
    fruit_x[i] = random.randrange(fruit.get_width(), width-fruit.get_width())
    fruit_y[i] = random.randrange(-2900, 0-fruit.get_height())

  #Creating the bombs
  bomb = pygame.image.load("bomb.png").convert_alpha()
  num_bombs = 10
  bomb_speed = 2
  bomb_x = [0]*num_bombs
  bomb_y = [0]*num_bombs
  for i in range(num_bombs):
    bomb_x[i] = random.randrange(bomb.get_width(), width-bomb.get_width())
    bomb_y[i] = random.randrange(-5000, 0-bomb.get_height())

  #Getting the basket images and using the user's basket stats
  wooden_basket = pygame.image.load("woodenbasket.png").convert_alpha()
  bronze_basket = pygame.image.load("bronzebasket.png").convert_alpha()
  silver_basket = pygame.image.load("silverbasket.png").convert_alpha()
  gold_basket = pygame.image.load("goldbasket.png").convert_alpha()
  emerald_basket = pygame.image.load("emeraldbasket.png").convert_alpha()
  diamond_basket = pygame.image.load("diamondbasket.png").convert_alpha()
  baskets = [wooden_basket, bronze_basket, silver_basket, gold_basket, emerald_basket, diamond_basket]
  basket_stats = [[5, 1, 1], [6, 1, 1], [7, 2, 2], [7, 3, 2], [8, 4, 2], [10, 5, 3]]
  basket = baskets[users[current_user]["item"]]
  basket_stat = basket_stats[users[current_user]["item"]]
  lives = basket_stat[0]

  #Loop that runs the game
  running = True
  while running:
    #Speeds up bomb speed every 15 seconds
    counter += 1
    if counter >= 900:
      counter = 0
      bomb_speed += 2

    #Moves player left or right depending on arrow keys if they are within the window
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        if player_x > 0:
            player_x -= 10
    if keys[pygame.K_RIGHT]:
        if player_x + 100 < width:
            player_x += 10
    #Game closes if window closes or escape is pressed
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        running = False
      if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_ESCAPE:
          running = False

    #Creating the texts for score, coins, lives and lost message
    text = font.render("Score: " + str(score), True, "black", "white")
    text_rect = text.get_rect()
    text_rect.center = (100, 50)

    live = font.render("Lives: " + str(lives), True, "black", "white")
    live_rect = live.get_rect()
    live_rect.center = (700, 50)

    lost = font.render("You lost. Press ESC to leave", True, "black", "white")
    lost_rect = lost.get_rect()
    lost_rect.center = (width/2, 300)

    user_coins = users[current_user]["coin"]
    coins = font.render("Coins: " + str(user_coins), True, "black", "white")
    coins_rect = coins.get_rect()
    coins_rect.center = (width/2, 50)

    #Show the background
    screen.blit(background,(0,0))

    #Show the basket at player location
    the_basket = screen.blit(basket, (player_x, 500))

    #If the user isn't at 0 lives, loop through bombs and fruits else the lost message appears
    if lives > 0:
      #Loops through each bombs position and resets it if it reaches bottom of the screen or hits basket
      for i in range(num_bombs):
        current_bomb = screen.blit(bomb, (bomb_x[i], bomb_y[i]))
        bomb_y[i] += bomb_speed
        if bomb_y[i]-bomb.get_width() > screen.get_height():
          bomb_y[i] = random.randrange(-2000-(700*bomb_speed), 0-bomb.get_height())
          bomb_x[i] = random.randrange(bomb.get_width(), width-bomb.get_width())
        if current_bomb.colliderect(the_basket):
          lives -= 1
          bomb_x[i] = random.randrange(-2000-(700*bomb_speed), 0-bomb.get_height())
          bomb_y[i] = random.randrange(bomb.get_width(), width-bomb.get_width())

      #Loops through each fruit position and resets it if it reaches bottom of screen or hits basket
      for i in range(num_fruits):
        current_fruit = screen.blit(fruit, (fruit_x[i], fruit_y[i]))
        fruit_y[i] += 2
        if fruit_y[i]-fruit.get_height() > screen.get_height():
          fruit_y[i] = random.randrange(-2000, 0-fruit.get_height())
          fruit_x[i] = random.randrange(fruit.get_width(), width-fruit.get_width())
        #If the fruit hits, the basket, add score and points depending on current basket's stats
        if current_fruit.colliderect(the_basket):
          score += 1*basket_stat[2]
          users[current_user]["coin"] += 1*basket_stat[1]
          fruit_y[i] = random.randrange(-2000, 0-fruit.get_width())
          fruit_x[i] = random.randrange(fruit.get_width(), width-fruit.get_width())
    else:
      screen.blit(lost, lost_rect)

    #Show the texts for score, lives and coins
    screen.blit(text, text_rect)
    screen.blit(live, live_rect)
    screen.blit(coins, coins_rect)
    pygame.display.flip()
    clock.tick(60)
  pygame.quit()

  #Updating users coins
  data_tool.update_coin(current_user, users[current_user]["coin"])

  #If score is higher than user's high score, update it with new score
  if score > high_score:
    data_tool.update_score(current_user, score)
  to_main_menu()

#Function that opens main menu
def to_main_menu():
  my_login.create_main_menu()