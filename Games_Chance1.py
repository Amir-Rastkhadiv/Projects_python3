# --The Zen of Python: "Beautiful is better than ugly"-------PEP8------

# Games of Chance

# Written by Amir Rastkhadivmasouleh

'''Following suites contains the random module, several functions
   like randint, if statements and print to stimulate 4 games
   namely Coin flipping, Cho-han, Card game and Roulette.Also,
   Python 3 programming language has been applied for writing
   functions,syntaxes control flow etc. However, there are limits
   for applying some modules and functions in our code because of
   the IDE and REPL was assigned for this project. For example, it
   cannot accept inputs for interacting with the user orrendering
   some modules outputs like Datetime.
'''

# Initial assumptions

'''It is assumed every game player has £100.00 in the account
   before playing games. The player can bet a different amount of
   money on each game.(This code is for learning purposes, so
   everything will be guessed by the coder for testing the suit
   and output each time, however, the result will be printed in the
   output with an imaginary game player because there is no option
   to interact with the user at this version.
'''

# Project Objectives:

'''So, the game player must be informed about the statement
   to find out what has happened on each attempt.
   The statement prints the name of the games, how many times
   the user has played each game, how much money the player bet
   on each game and how much money the player won or lost and
   finally how much money has been left. Predefined date and
   time in random has been assigned to each statement to give
   nicer appearance to this code outputs due to the IDE
   limitation for rendering the DateTime module.So, those date
   times will not be real local times in your operating system.
'''

# ----------------------------- Step 1: ---------------------------
#General modules, parameters and vaues of the code 
import random
top_up_money = 0.00  # The amount of money the player adds 
money = 100.00       # Represent the current amount of money
bet = random.randint(1, 200)
game_name = ["Coin flipping", "Cho-han", "Card game", "Roulette"]
game_select = random.choice(game_name)


# Coin flipping varible and parameters. 
tossing_coin = ["Head", "Tail"]
guess_player_coin = random.choice(tossing_coin)


# Cho-han general varible and parameters. 
guess_player_dice = random.randint(2,12) # Sum of two dices


# Card game gemneral varible and parameters. 
player_card_1 = random.randint(1,10)


# Roulette game gemneral varible and parameters.
guess_1 = random.randint(1,38)
color = ['Red', 'Black']
guess_2 = [random.choice(color)]
guess = [str(guess_1)] + [str(guess_2)] + ['0','00']

player_guess = random.choice(guess)
robot_guess = random.choice(guess)

# Final suite for running code.
continue_add_money = ["Yes", "No"]
player_decision_continue = random.choice(continue_add_money)


# ----------------------------- Step 2: ---------------------------
def display_greeting_games():
    #Greeting statement 
    print("-------------Welcome to Games of Chance!-----------")

    
# ----------------------------- Step 3: ---------------------------
def present_game_number() -> int :
    # Generate list of 4 availble games for user.
    print("There are 4 games as below:")
    for number in range(1, 5):
        print(number, ")", game_name[(number-1)])
    return number


# ------------------------------Step 4: ----------------------------
def show_current_balance(money):
    # current money in the account
    print("The cuurrent amount of money in your account is:" ,
          "£" + str(money)
         )
    return money


# ------------------------------Step 5: ----------------------------
def give_date_time():
    #Generating immaginary random date and times at the beginning.
    
    a_month = random.randint(1, 12)
    b_day = random.randint(1, 28)
    c_hour = random.randint(0, 23)
    d_minute = random.randint(0, 23)
    e_seconds = random.randint(0, 60)
    
    print ("Current date and time:")
    
    print("2020-" + str(a_month) + "-" + str(b_day), str(c_hour)
          + ":" + str(d_minute) + ":" + str(e_seconds))
    
    print("-----------------------------------------------------")
    print("        ", "Getting Started Games.Have fun!", "      ")
    print("-----------------------------------------------------")

    
# ---------------------------- Step 6: ----------------------------
"""
  ------------------------                 --------------------
                         Games's functions   
 ------------------------                 -----------------------
 
""" 

# Game name: Coin flipping
def play_coin_flipping(guess_player_coin, money , bet):
    # if game_select == 'Coin flipping' and money >= bet
    print("Head or Tail?")
    print( " You bet: £" + str(bet), "on", guess_player_coin)
    print(">>>Let's tossing the coin!")
    
    guess_robot= random.choice(tossing_coin)
    #Represents computer guess
    
    if guess_robot == guess_player_coin:
        print("Hooray! It's", guess_robot + ".", "You won.")
        print("You won:" , "£" + str(bet))
        money += bet
        print("You balance is:","£" + str(money))
        print("-----------------------------------------")
        return money, bet
        
    else:
        print("I am afraid! It's", guess_robot+".", "You lost.")
        print("You lost:" , "-"+ "£" + str(bet))
        money = money-bet
        print("You balance is:","£" + str(money))
        print("-----------------------------------------")
        return money, bet

    
# Game name: Cho-han
def play_cho_han(guess_player_dice, money, bet):
    #player must guesses sum of two dices Even or odd.
    # Player guess assigned by random.
    
    print(" Sum of two dices is Odd or Even?")
    print(">>>let's shaking two dices!")
    print( " You bet: £" + str(bet), "on", guess_player_dice)
    
    if guess_player_dice %2 == 0:
        print("Player guess:",guess_player_dice," Your number is Even.")
    else:
        print("Player guess:",guess_player_dice," Your number is Odd.")
        print(">>>let's shaking two dices!")
        
    guess_robot = random.randint(2, 12)
    # Rolling dices for computer and adding their numbers.
          
    if guess_robot %2 == 0 and guess_player_dice %2 == 0:
        print("Hooray! It's", str(guess_robot) + ".",
              "That is Even.", "You won."
             )
        money += bet
        print("You won:" ,"£" + str(bet))
        print("You balance is:", "£" + str(money))
        print("-----------------------------------------")
        return money, bet
        
    elif guess_robot %2 != 0 and guess_player_dice %2 != 0:
        print("Hooray! It's", str(guess_robot) + ".", "That is Odd.",
              "You won."
             )
        money += bet
        print("You won:" ,"£"+ str(bet))
        print("You balance is:","£" + str(money))
        print("-----------------------------------------")
        return money, bet
    
    else:
        print("I am afraid! It's", str(guess_robot) + ".",
              "You lost."
             )
        money = money-bet
        print("You lost:" ,"-" + "£" + str(bet))
        print("You balance is:","£" + str(money))
        print("-----------------------------------------")
        return money, bet

    
# Game name: Card game
def play_card_game(player_card_1, money, bet):
    # Players must pick  cards. Player cards' numberes assigned by random.

    player_card_robot = random.randint(1, 10)
    
    print("Who has maximum","card", "number?")
    print(">>>let's picking cards!")
    
    print("Player card:", str(player_card_1))
    print( " You bet: £" + str(bet), "on this card number.")
    
    if int(player_card_1) > int(player_card_robot):
        print("My card is", str(player_card_robot) + ".", "You won.")
        money += bet
        print("You won:" , "£" + str(bet))
        print("You balance is:" , "£" + str(money))
        print("-----------------------------------------")
        return money, bet
        
        
    elif int(player_card_1) == int(player_card_robot): 
        print("The game is tie.", "My card is", str(player_card_1)
              + "."
              )
        money += 0
        
        print("You balance is:","£" + str(money))
        print("-----------------------------------------")
        return money, bet
        
    else:
        print("I am afraid! My card is", str(player_card_robot)
              + ".", "You lost"
             )
        money = money - bet
        
        print("You lost:" , "-" + "£" + str(bet))
        print("You balance is:", "£" + str(money))
        print("-----------------------------------------")
        return money, bet

# Roulette
def play_roulette_game(player_guess, robot_guess, money, bet):
    '''players can guess numbers 1 to 38  or red and black colours.  
       Three are especial guess like numbers 0 and 00, even and odd
       numbers with different amount of prizes.player and robot guess
       assigned by random.
    '''
    
    print(" Special numbers are: 0 and 00", "Colours are: Red and"
          , "Black"
         )
    print(" prize : £35 for special numbers and £25 for colours")
    print(" Also, prize for  specific even number is extra £5")
    
    print("Player guess:", str(player_guess))
    print( " You bet: £" + str(bet), "on this attempt.")
    
    print(">>>let's spin the wheel.")
    
    if robot_guess == player_guess and robot_guess == 0:
            
        print("Hooray! It's", str(robot_guess) + ".",
              "You won special"
              + "prize."
             )
        
        money += bet + 35
        
        print("You won:", "£" + str(bet + 35))
        print("You balance is:", "£" +  str(money))
        print("-----------------------------------------")
        return money, bet
        
        
    elif robot_guess == player_guess and robot_guess == 00:

        print("Hooray! It's", str(robot_guess) + "." ,
              "You won special prize.")
        
        money += bet + 35
        
        print("You won:" , "£" + str(bet+35))
        print("You balance is:", "£" + str(money))
        print("-----------------------------------------")
        return money, bet
        
    elif robot_guess == player_guess and (guess_1)%2 == 0:
        print("Hooray! It's", str(robot_guess) + "." ,
              "You won Even number prize."
              )

        money += bet + 5
        
        print("You won:" , "£" + str(bet + 5))
        print("You balance is:", "£" + str(money))
        return money, bet
        
    elif robot_guess == player_guess:
        
        if robot_guess == str("Black") or robot_guess == str("Red"):
            
            print("Hooray! It's", str(robot_guess) + ".",
                  "You won colour prize."
                 )
        
            money += bet + 15
        
            print("You won:" ,"£" + str(bet+15))
            print("You balance is:","£" + str(money))
            print("-----------------------------------------")
            return money, bet
    
    elif robot_guess == player_guess:
        
        print("Hooray! It's", str(robot_guess) + ".",
              "You won."
             )

        money += bet
        
        print("You won:" , "£" + str(bet))
        print("You balance is:", "£"  + str(money))
        print("-----------------------------------------")
        return money, bet
        
    else:
        print("I am afraid! It's", str(robot_guess) + ".",
              "You lost"
              )
        money = money - bet
        
        print("You lost:" , "-" + "£"+ str(bet))
        print("You balance is: ", "£" + str(money))
        print("-----------------------------------------")
        return money, bet

# ------------------------------Step 7: ----------------------------

def random_game_function(money, bet):
    game_playing = game_select 
    if game_playing == game_name[0]:
        play_coin_flipping(guess_player_coin, money , bet)
        return money, bet
    
    elif game_playing == game_name[1]:
        play_cho_han(guess_player_dice, money, bet)
        return money, bet
    
    elif game_playing == game_name[2]:
        play_card_game(player_card_1, money, bet)
        return money, bet
    
    else:
        play_roulette_game(player_guess, robot_guess, money, bet)
        return money, bet

    
# ------------------------------Step 8: ----------------------------

def check_bet_random(money, bet):
# Give options by checking the availble money and the bet amount. 
    games_attempt=0
    
    while money >= 0:

        games_attempt += 1
        
        game_playing = game_select
        
        if money >= bet:
            print("------------------------------------------------")
            print("             You are playing: " + game_playing   )
            print("------------------------------------------------")
            (money, bet) = random_game_function(money, bet)
            return money, bet 
            
        elif money < bet:
            print("------------------------------------------------")
            print("             You are playing: " + game_playing   )
            print("------------------------------------------------")
            print(" You cannot bet more than the money in your account.")
            print(" Your current  blanace is :" + "£", str(money))
            print(" You need to increase your credit", "£" + str(bet-money))
            print(" Are you going to continue ?")
            
            if player_decision_continue == continue_add_money[0]:
                print(continue_add_money[0])
                print("You added " + "£", str(bet-money), "into your account.")
                money = bet
                print("Your balance is: " + "£", str(money))
                
                (money, bet) = random_game_function(money, bet)
                return money, bet
            else:
                print(continue_add_money[1])
                print("Thank you for visiting us. See you soon.")
                return money, bet
        else:
            print("------------------------------------------------")
            print("             You are playing: " + game_playing   )
            print("------------------------------------------------")
            
            print(" You do not have money in your account")
            print(" your blance is : ", str(money- money))
            print(" Are you going to continue ?")
        
            if player_decision_continue == continue_add_money[0]:
            
                print(continue_add_money[0])
                top_up = random.randint(bet, bet+100)
                top_up_money += top_up
            
                print("You added " + "£", str(top_up), "into your account")
                money += top_up_money
                
                
                (money, bet) = random_game_function(money, bet)
                return money, bet
        
            else:
                print(continue_add_money[1])
                print("Thank you for visiting us. See you soon.")
                return money, bet
        
        

            
# ------------------------------Step 9: ----------------------------
#............................Runinning code...................


games_attempt = 0
for games in range (0, 10):
    games_attempt += 1
    display_greeting_games()
    present_game_number()
    show_current_balance(money)
    give_date_time()
    print( "Attempt:" + str(games_attempt))
    game_select = random.choice(game_name)
    check_bet_random(money, bet)
    game_select = random.choice(game_name)
    
    

       


    
    
    
            
        
    
    
           
    









