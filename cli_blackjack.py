
from faulthandler import cancel_dump_traceback_later
from os import remove
import random


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
    if list == [11,10] or list == [10,11]:
        return 0
    elif sum(list) > 21 and 11 in list:
        list.remove(11)
        list.append(1)
        return(sum(list))
    else:
        return sum(list)
    


#DEAL THE PLAYER A CARDS
deal_player_one = player_cards.append(deal_card())
deal_player_two = player_cards.append(deal_card())
deal_player_two = player_cards.append(deal_card())

#DEAL THE DEALER CARDS
deal_dealer_one = dealer_cards.append(deal_card())
deal_dealer_two = dealer_cards.append(deal_card())

# print(player_cards)
if total_score(player_cards) == 0:
    print(f"You got Black Jack Well Done!")
    exit()
elif total_score(player_cards) > 21:
    print("""You have gone bust! \n       :( """)


