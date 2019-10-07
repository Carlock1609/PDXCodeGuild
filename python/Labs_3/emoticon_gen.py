#! python3

import random

counter = 0

while counter < 6:
    nose_list = ["-", "=", "D"]
    eyes_list = ["O", ":", ";"]
    mouths_list = ["P", "C", "<"]


    nose = random.choice(nose_list)
    eyes = random.choice(eyes_list)
    mouths = random.choice(mouths_list)

    random_face = print(f"{eyes}{nose}{mouths}")
    counter += 1
