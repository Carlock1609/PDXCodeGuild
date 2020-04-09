#  version 2:
import random
 
cards_dict  =  { "K" : 10 , "Q" : 10 , "J" : 10 , "10" : 10 , "9" : 9 , "8" : 8 , "7" : 7 , "6" : 6, "5" : 5 , "4" : 4 , "3" : 3 , "2" : 2 , "A" : 11}
 
# print(cards_dict.values())
 
# print (cards_dict['K'])
 
print("Whats your first card?")
 
card_1 = 'A'
 
# print(type(card_1))
 
print("Whats your second card?")
 
card_2 = 'A'
 
print(card_2)
 
print("Whats your third card?")
 
card_3 = '8'
 
print(card_3)
user_sum = cards_dict[card_1] + cards_dict[card_2] + cards_dict[card_3]

print(type(user_sum))
print(user_sum)

if user_sum > 21:
    cards_dict['A'] = 1

print("Total in hand: ")
print(cards_dict.get(card_1) + cards_dict.get(card_2) + cards_dict.get(card_3))
# if card_1 or card_2  or card_3 ==  "A"  and cards_dict.get(card_1) + cards_dict.get(card_2) + cards_dict.get(card_3) < 10:
#     cards_dict.update({"A":11})
# print(f'A: ')
# print(cards_dict["A"])
 
if cards_dict.get(card_1) + cards_dict.get(card_2) + cards_dict.get(card_3) == 21:
                print("Blackjack")
if cards_dict.get(card_1) + cards_dict.get(card_2) + cards_dict.get(card_3) < 17:
                print( "Hit" )
 
if 21 > cards_dict.get(card_1) + cards_dict.get(card_2) + cards_dict.get(card_3) >= 17:
                print("Stay")
if cards_dict.get(card_1) + cards_dict.get(card_2) + cards_dict.get(card_3) > 21:
                print("Broken")
