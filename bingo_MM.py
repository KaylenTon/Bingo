import pandas as pd
import random

# Bingo Card Arrangement
# ------------------------------------
# 00  01  02  03  04        B
# 05  06  07  08  09        I
# 10  11  12  13  14        N
# 15  16  17  18  19        G
# 20  21  22  23  24        O

winning_patterns = [

    # horizontal
    [0,1,2,3,4],           # B 
    [5,6,7,8,9],           # I 
    [10,11,12,13,14],      # N 
    [15,16,17,18,19],      # G 
    [20,21,22,23,24],      # O 

    # diagonal
    [0, 6, 12, 18, 24],    # \
    [4, 8, 12, 16, 20],    #  / 

    # vertical
    [0, 5, 10, 15, 20],    # B
    [1, 6, 11, 16, 21],    # I
    [2, 7, 12, 17, 22],    # N
    [3, 8, 13, 18, 23],    # G
    [4, 9, 14, 19, 24]     # O

]

false_statements = list(range(1,100, 2))
truth_statements = list(range(2,100, 2))

def create_winning_stack():

    winning_stack = []

    while len(winning_stack) < winning_cards:

        select_random_pattern = random.choice(winning_patterns)
        print(select_random_pattern)

        card = ["Blank"] * 25
        
        card[12] = "FREE"

        if card not in winning_stack:
            winning_stack.append(card)

        return winning_stack

def create_losing_stack():
    losing_stack = []

    while len(losing_stack) < losing_cards:

        card = ["Blank"] * 25
        
        card[12] = "FREE"

        if card not in losing_stack:
            losing_stack.append(card)

    return losing_stack

# main function
def create_set(total_winning_cards = 1):
    total_cards = total_winning_cards * 20 # there is a winner for every twenty cards
    losing_cards = total_cards - total_winning_cards
    return(losing_cards, total_winning_cards)