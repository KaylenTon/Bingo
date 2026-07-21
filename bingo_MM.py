# Bingo Card Arrangement
# ------------------------------------
# 00  01  02  03  04        B
# 05  06  07  08  09        I
# 10  11  12  13  14        N
# 15  16  17  18  19        G
# 20  21  22  23  24        O

winning_patterns = [

    # vertical
    [0,1,2,3,4],                # B 
    [5,6,7,8,9],                # I 
    [10,11,12,13,14],      # N 
    [15,16,17,18,19],      # G 
    [20,21,22,23,24],      # O 

    # diagonal
    [0, 6, 12, 18, 24],      # \
    [4, 8, 12, 16, 20],      #  / 

    # horizontal
    [0, 5, 10, 15, 20],      # B
    [1, 6, 11, 16, 21],      # I
    [2, 7, 12, 17, 22],      # N
    [3, 8, 13, 18, 23],      # G
    [4, 9, 14, 19, 24]       # O

]

false_statements = list(range(1,50, 2))
truth_statements = list(range(2,50, 2))

def create_set(winning_cards = 1):
    total_cards = winning_cards * 20
    losing_cards = total_cards - winning_cards
    return(losing_cards, winning_cards)

print(create_set(5))
print(winning_patterns[1])