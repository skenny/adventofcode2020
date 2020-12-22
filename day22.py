def read_input(file):
    player1_cards = []
    player2_cards = []
    working_array = None
    with open(file, "r") as fin:
        for l in fin.readlines():
            l = l.strip()
            if l == "Player 1:":
                working_array = player1_cards
            elif l == "Player 2:":
                working_array = player2_cards
            elif l.isdigit():
                working_array.append(int(l))
    return (player1_cards, player2_cards)

def play(player1_cards, player2_cards):
    while len(player1_cards) > 0 and len(player2_cards) > 0:
        p1 = player1_cards.pop(0)
        p2 = player2_cards.pop(0)
        if p1 > p2:
            player1_cards.append(p1)
            player1_cards.append(p2)
        else:
            player2_cards.append(p2)
            player2_cards.append(p1)
    
    winning_cards = player1_cards if len(player1_cards) > 0 else player2_cards
    score = 0
    for i, card in enumerate(reversed(winning_cards)):
        score += (i + 1) * card
    return score

def run(label, input_file):
    player1_cards, player2_cards = read_input(input_file)
    print("{} 1: {}".format(label, play(player1_cards, player2_cards)))

run("test", "day22-input-test")
run("part", "day22-input")