#! python3

#v1

# Try a dictionary

deck = {"A": 1,
        "2": 2,
        "3": 3, 
        "4": 4, 
        "5": 5, 
        "6": 6, 
        "7": 7, 
        "8": 8, 
        "9": 9, 
        "10": 10, 
        "J": 10, 
        "Q": 10, 
        "K": 10}


def get_player_hand():
    player_hand = []
    for i in range(3):
        get_card = input("Please enter in 3 cards to be added to your hand: (A,1,2,3,4,5,6,7,8,9,10,J,Q,K)"
        player_hand.append(get_card)
    return player_hand

def get_hand_worth(player_hand):
    total_hand = player_hand[0] + player_hand[1] + player_hand[2]
    return total_hand


print(get_hand_worth(get_player_hand()))