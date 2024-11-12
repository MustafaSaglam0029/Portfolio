import random


def create_deck(): #creating a deck
    suits=["Spades", "Clubs", "Diamonds", "Hearts", "Spades"]
    ranks=["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
    cards={"A":(1,11),"K":10,"Q":10,"J":10,"2":2,"3":3,"4":4,"5":5,"6":6,"7":7,"8":8,"9":9,"10":10}
    deck=[(f"{rank} of {suit}",cards[rank]) for suit in suits for rank in ranks]
    random.shuffle(deck)
    return deck

#initial cards for player and dealer
def initial_cards(shuffled_deck):
    player_hand=[shuffled_deck.pop(),shuffled_deck.pop()]
    dealer_hand=[shuffled_deck.pop(),shuffled_deck.pop()]
    return player_hand,dealer_hand

#total of hands
def calculate_score(hand):
    total=0
    aces=0
    for card,value in hand:
        if isinstance(value,tuple):
            aces+=1
            total += 11
        else:
            total += value
    while total>21 and aces>0:
        total -= 10
        aces -= 1
    return total

def player_turn(shuffled_deck,player_hand):
    while True:
        player_total=calculate_score(player_hand)
        print(f"Your current hand is {player_hand} and total is  {player_total}")

        if player_total>21:
            print(f"You lost!,Your total score {player_total} is over 21")
            return player_hand,player_total,"bust"

        decision=input("Would you like to hit or stand?(h/s)").lower()

        if decision=="s":
            return player_hand,player_total,"s"
        elif decision=="h":
            new_card=shuffled_deck.pop()
            player_hand.append(new_card)
            print(f"You drew {new_card}")
            player_total=calculate_score(player_hand)
        else:
            print("Invalid input, please type 's' or 'h'?")


def dealer_turn(shuffled_deck,dealer_hand):
    while calculate_score(dealer_hand)<17:
        new_card=shuffled_deck.pop()
        dealer_hand.append(new_card)
        print(f"Dealer drew {new_card}")

    dealer_total=calculate_score(dealer_hand)
    print(f"Dealer hand is {dealer_hand} and total is  {dealer_total}")
    return dealer_hand,dealer_total

def play_game():
    player_money=int(input("How much money would you like to play:"))
    dealer_money=10000
    round_number=1

    while player_money>0:
        answer=input("Would you like to play? (y/n)").lower()
        if answer=="y":
            print(f"\n Starting round {round_number}")
        elif answer=="n":
            print(f"You have {player_money} Euros")
            break
        else:
            print("Invalid input, please type 'y' or 'n'")
            continue

        bet_amount=int(input("How much money would you like to bet:"))
        if bet_amount>player_money or bet_amount<0:
            print("Invalid input, please enter a valid amount.")
            continue

        deck=create_deck()
        player_hand,dealer_hand=initial_cards(deck)

        print(f"Dealer visible card is {dealer_hand[0]}")
        player_hand, player_total, player_status=player_turn(deck,player_hand)

        if player_status=="bust":
            dealer_money+=bet_amount
            player_money-=bet_amount
            print(f"Your current money {player_money} Euros and dealer money is {dealer_money}")
            round_number+=1
            continue
        print(f"Dealer's hidden card was : {dealer_hand[1]} ")
        dealer_hand,dealer_total=dealer_turn(deck,dealer_hand)
        print(f"Dealer total is {dealer_total} and player total is {player_total}")
        if player_total>dealer_total or dealer_total>21 or player_total==21:
            print("You win!")
            dealer_money-=bet_amount*2
            player_money+=bet_amount*2
        elif player_total<dealer_total:
            print("You lost!")
            dealer_money+=bet_amount
            player_money-=bet_amount
        else:
            print("It is a tie")
        print(f"Your current money {player_money} Euros and dealer money is {dealer_money} Euros")
        round_number+=1
    if player_money==0:
        print(f"Game over. You ran out of money")
    print(f"Thank you for playing ")

if __name__=="__main__":
    play_game()













