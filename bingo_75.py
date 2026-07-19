import pandas as pd
import random

def create_bingo_card(count = 1):
    stack = []

    while len(stack) < count:
        B = random.sample(range(1, 16), 5)
        I = random.sample(range(16, 31), 5)
        N = random.sample(range(31, 46), 5)
        G = random.sample(range(46, 61), 5)
        O = random.sample(range(61, 76), 5)

        card = []
        
        card.extend(B)
        card.extend(I)
        card.extend(N)
        card.extend(G)
        card.extend(O)
        card[12] = "FREE"

        if card not in stack:
            stack.append(card)

    return stack

cards = create_bingo_card(5)
stack = pd.DataFrame(cards)
print(stack.duplicated().sum())

columns = [
    "B1","B2","B3","B4","B5",
    "I1","I2","I3","I4","I5",
    "N1","N2","N3","N4","N5",
    "G1","G2","G3","G4","G5",
    "O1","O2","O3","O4","O5"
]

stack.columns = columns
stack.to_csv("bingo_card_values.csv", index=False)