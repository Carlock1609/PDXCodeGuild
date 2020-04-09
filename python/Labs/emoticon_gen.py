#! python3

import random

def display_face(eyes,nose,mouths):
    random_face = print(f"{eyes}{nose}{mouths}")
    return random_face

def main():
    counter = 0

    while counter < 6:
        nose_list = ["-", "=", "~"]
        eyes_list = ["O", ":", ";"]
        mouths_list = ["P", "C", "<"]
        nose = random.choice(nose_list)
        eyes = random.choice(eyes_list)
        mouths = random.choice(mouths_list)

        display_face(eyes,nose,mouths)
        counter += 1
main()
