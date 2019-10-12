#! python3

#v1

# Need to figure out how to convert JQK to 10's

def get_player_hand():
    player_hand = []
    for i in range(3):
        get_card = int(input("Please enter in 3 cards to be added to your hand: (A,1,2,3,4,5,6,7,8,9,10,J,Q,K)"))
        player_hand.append(get_card)
    return player_hand

def convert_face_cards(player_hand):
    for i in player_hand:
        if i == "J" or i == "Q" or i == "K":
            i = 10
    return i

def get_hand_worth(player_hand):
    total_hand = player_hand[0] + player_hand[1] + player_hand[2]
    return total_hand


print(get_hand_worth(get_player_hand()))