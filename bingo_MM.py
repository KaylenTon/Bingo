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

# main function
def create_set(total_winning_cards = 1):
    total_cards = total_winning_cards * 20 # there is a winner for every twenty cards
    total_losing_cards = total_cards - total_winning_cards
    return(total_losing_cards, total_winning_cards)

total_losing_cards, total_winning_cards = create_set(8)
print("\n")
print(f"Winning Cards: {total_winning_cards}, Losing Cards: {total_losing_cards}")

bingo_columns = [
    "B1","B2","B3","B4","B5",
    "I1","I2","I3","I4","I5",
    "N1","N2","N3","N4","N5",
    "G1","G2","G3","G4","G5",
    "O1","O2","O3","O4","O5"
]

def create_winning_stack():

    cards = []

    while len(cards) < total_winning_cards:

        select_random_pattern = random.choice(winning_patterns)
        print(f"\n Selected Winning Pattern {len(cards) + 1}: {select_random_pattern}")

        card = ["Blank"] * 25

        # Fill with true statements for the winning pattern
        for index in select_random_pattern:
            card[index] = random.choice(truth_statements)

        # Fill with false statements for the rest of the card
        for index in range(25):
            if index not in select_random_pattern:
                card[index] = random.choice(false_statements)

        # Set the center space to "FREE" (Overwrite the value at index 12)
        card[12] = "FREE"

        # Preventing duplicate winning cards
        if card not in cards:
            cards.append(card)

    winning_stack = pd.DataFrame(cards, columns=bingo_columns)
    winning_stack.index += 1
    print(f"\n Winning Stack: \n{winning_stack}")

    return winning_stack
    
create_winning_stack()

def create_losing_stack():

    losing_stack = []

    while len(losing_stack) < total_losing_cards:

        card = ["Blank"] * 25
        
        card[12] = "FREE"

        if card not in losing_stack:
            losing_stack.append(card)

    return losing_stack

print("\n")