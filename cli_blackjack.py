
import random
import os


#ASCII ART GENERATED AT: https://patorjk.com/software/taag/

logo = """

       _        _    _              _                 _   
      | | o    | |  | |            | |  o            | |  
  __  | |      | |  | |  __,   __  | |     __,   __  | |  
 /    |/  |    |/ \_|/  /  |  /    |/_) | /  |  /    |/_) 
 \___/|__/|_/   \_/ |__/\_/|_/\___/| \_/|/\_/|_/\___/| \_/
                                       /|                 
                                       \|                 


"""

#FUNCTION THAT WILL DEAL CARDS 
#x4 10 cards in list = 10 suited, jack, queen, king
def deal_card():
    card_deck = [1,2,3,4,5,6,7,8,9,10,10,10,10,11]
    return random.choice(card_deck)


#TOTALS CARDS IN HAND
def total_score(list):
    #if statement to check for blackjack
    if sum(list) == 21 and len(list) == 2:
        return 0
    elif sum(list) > 21 and 11 in list:
        print("\nYou are now using you Ace (11) as a '1'")
        list.remove(11)
        list.append(1)
        return sum(list)
    else:
        return sum(list)
    
def compare_cards(player_score,dealer_score):
    if player_score == dealer_score:
        return f"\nIt was a draw!"
    elif dealer_score == 0:
        return f"\nYou lost, Dealer has blackjack!"
    elif player_score == 0:
        return f"\nYou where dealt Blackjack! Congrats you win!"
    elif player_score > 21:
        return f"\nYou went bust :("
    elif dealer_score > 21:
        return f"\nYou win! The dealer went bust!"
    elif player_score > dealer_score:
        return f"\nYou win! Good lad yourself!"
    else:
        return f"\nDealer has won...no good. You lose!"



def the_game():

    print(logo)
    print("""          [Welcome to CLI Black Jack!]\n""")

    player_cards = []
    dealer_cards = []


    game_over = False

    #DEAL THE PLAYER A CARDS
    for i in range(2):
        player_cards.append(deal_card())
        dealer_cards.append(deal_card())
    

    player_total_score = total_score(player_cards)
    dealer_total_score = total_score(dealer_cards)

    while game_over == False:

        print(f"\nYour cards are: {player_cards}, Your current total score is: {sum(player_cards)}")
        print(f"The dealers first card is {dealer_cards[0]}")

        if player_total_score == 0 or dealer_total_score == 0 or player_total_score > 21:
            game_over = True
        else:
            hit_me = input("Would you like another card? Enter 'y' for yes and 'n' for no: ")
            if hit_me.lower() == 'y':
                player_cards.append(deal_card())
                player_total_score = total_score(player_cards)
            else:
                game_over = True

    while dealer_total_score < 17 and dealer_total_score != 0:
            dealer_cards.append(deal_card())
            dealer_total_score = total_score(dealer_cards)
    
    print("\n-------------------------------------")
    print(f"\nYour hand was {player_cards}. Your total score was: {sum(player_cards)} ")
    print(f"\nThe Dealers hand was {dealer_cards}. Your total score was: {sum(dealer_cards)} ")

    print(compare_cards(player_total_score, dealer_total_score))
    print("\n-------------------------------------")


        
print("""\n               [Welcome to CLI Black Jack!]""")
while input("\nWould you like to play a game of Black Jack? Type 'y' to play!: ") == "y":
    os.system('cls') #windows clear screen
    os.system('clear') #linux clear screen
    the_game()

