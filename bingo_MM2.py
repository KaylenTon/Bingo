import pandas as pd
import random

# Bingo Card Arrangement
# -----------------------------
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

bingo_columns = [
    "B1","B2","B3","B4","B5",
    "I1","I2","I3","I4","I5",
    "N1","N2","N3","N4","N5",
    "G1","G2","G3","G4","G5",
    "O1","O2","O3","O4","O5"
]

# VALIDATION FUNCTION
def count_winning_patterns(card):

    count = 0

    for pattern in winning_patterns:
        if all(card[index] in truth_statements or card[index] == "FREE"
               for index in pattern):
            count += 1

    return count

# CARD GENERATOR FUNCTIONS
def create_winning_stack(total_winning_cards):

    cards = []

    while len(cards) < total_winning_cards:

        select_random_pattern = random.choice(winning_patterns)
        print(f"\nSelected Winning Pattern {len(cards) + 1}: {select_random_pattern}")

        card = ["Blank"] * 25

        # Fill with true statements for the winning pattern
        pattern_truths = random.sample(truth_statements, len(select_random_pattern))
        for index, value in zip(select_random_pattern, pattern_truths):
            card[index] = value

        # Fill with false statements for the rest of the card
        remaining_indexes = [index for index in range(25) if index not in select_random_pattern]
        remaining_falses = random.sample(false_statements, len(remaining_indexes))
        for index, value in zip(remaining_indexes, remaining_falses):
            card[index] = value

        # Set the center space to "FREE" (Overwrite the value at index 12)
        card[12] = "FREE"

        remaining_indexes = [
            i for i in range(25)
            if i not in select_random_pattern
            and i != 12
        ]

        extra_truth_count = random.randint(3,6)
        extra_truth_indexes = random.sample(
            remaining_indexes,
            extra_truth_count
        )
        print(f"Extra Truth Count: {extra_truth_count}, Extra Truth Indexes: {extra_truth_indexes}")
        for index, value in zip(extra_truth_indexes, random.sample(truth_statements, extra_truth_count)):
            card[index] = value

        # Preventing duplicate winning cards
        if card not in cards:
            cards.append(card)

    winning_stack = pd.DataFrame(cards, columns=bingo_columns)
    winning_stack.index += 1
    print(f"\n Winning Stack: \n{winning_stack}")

    return winning_stack
def create_losing_stack(total_losing_cards):

    cards = []

    while len(cards) < total_losing_cards:

        card = ["Blank"] * 25

        available_indexes = [
            i for i in range(25)
            if i != 12
        ]

        random_T_count = random.randint(5,10)

        losing_card_truth_index = random.sample(
            available_indexes,
            random_T_count
        )

        for index,value in zip(losing_card_truth_index, random.sample(truth_statements, random_T_count)):
            card[index] = value

        remaining_indexes = [index for index in range(25) if index not in losing_card_truth_index]
        remaining_falses = random.sample(false_statements, len(remaining_indexes))
        for index, value in zip(remaining_indexes, remaining_falses):
            card[index] = value
        
        # Set the center space to "FREE" (Overwrite the value at index 12)
        card[12] = "FREE"

        if card not in cards and card not in cards and count_winning_patterns(card) == 0:
            cards.append(card)

    losing_stack = pd.DataFrame(cards, columns=bingo_columns)
    losing_stack.index += 1
    print(f"\n Losing Stack: \n{losing_stack}")

    return losing_stack

# MAIN FUNCTION (CREATES SET)
def create_set(total_winning_cards = 1, total_losing_cards = 10):

    total_cards = total_winning_cards + total_losing_cards
    winning_stack = create_winning_stack(total_winning_cards)
    losing_stack = create_losing_stack(total_losing_cards)

    all_cards = pd.concat(
        [winning_stack, losing_stack],
        ignore_index=True
    )

    all_cards.insert(
        0,
        "card_id",
        range(1, len(all_cards) + 1)
    )

    print(all_cards)
    return(all_cards)

create_set(2, 2)