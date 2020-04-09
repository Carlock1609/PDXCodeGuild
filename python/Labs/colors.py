from colorama import Fore, Back, Style
import random, time

backgroundColors = [Back.YELLOW, Back.GREEN, Back.RED, Back.BLUE]
colors = [Fore.RED, Fore.YELLOW, Fore.BLUE, Fore.GREEN]

string = 'helllolololoolosdaldsadsahkjhwdkwa'


for i in string:
    print(i, random.choice(colors), random.choice(backgroundColors))