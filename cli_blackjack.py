
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


print(logo)
print("""          [Welcome to CLI Black Jack!]\n""")

player_cards = []
dealer_cards = []



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
        list.remove(11)
        list.append(1)
        return sum(list)
    else:
        return sum(list)
    
def compare_cards(player_score,dealer_score):
    if player_score == dealer_score:
        print(f"You have a score of '{player_score}', the dealer has a score of '{dealer_score}'  It's a draw!")
    elif player_score > dealer_score:
        print(f"You have a score of '{player_score}', the dealer has a score of '{dealer_score}'  You Win this round!")
    elif player_score < dealer_score:
        print(f"You have a score of '{player_score}', the dealer has a score of '{dealer_score}'  The Dealer wins this round!")



def the_game():

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
            hit_me = input("Would out like another card? Enter 'y' for yes and 'n' for no: ")
            if hit_me.lower() == 'y':
                player_cards.append(deal_card())
            else:
                game_over = True

    while dealer_total_score < 17 and dealer_total_score != 0:
            dealer_cards.append(deal_card())
            dealer_total_score = total_score(dealer_cards)
    
    # elif total_score(player_cards) > 21:
    #     print("""You have gone bust! \n       :( """)
    #     exit()



    # player_stick = 0

    # while player_stick == 0:
    #     hit_me = input(f"The total of your cards is {total_score(player_cards)}   Would you like to be dealt another card?!: ")
    #     if hit_me.lower() == "y":
    #         player_cards.append(deal_card())
    #         if total_score(player_cards) > 21:
    #             print("""You have gone bust! \n       :( """)
    #             exit()
    #     else:
    #         player_stick = 1


    # dealer_stick = 0

    # while dealer_stick == 0:
    #     if total_score(dealer_cards) < 17:
    #         dealer_cards.append(deal_card())
    #     else:
    #         dealer_stick = 1


    compare_cards(total_score(player_cards),total_score(dealer_cards))
    

    #play again choice
    # play_again = input("Would you like to play another game?")
    # if play_again.lower() == "y":
    #     player_cards = []
    #     dealer_cards = []
    #     the_game()
        


the_game()

