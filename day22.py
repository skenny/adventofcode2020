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

def play(player1_cards, player2_cards, recursive_combat_enabled):
    winner, winning_cards = play_game(1, player1_cards, player2_cards, recursive_combat_enabled)
    score = 0
    for i, card in enumerate(reversed(winning_cards)):
        score += (i + 1) * card
    return score

def play_game(game_num, player1_cards, player2_cards, recursive_combat_enabled):
    prev_rounds = {}
    round_num = 0

    print("\n=== Game {} ===\n".format(game_num))

    while len(player1_cards) > 0 and len(player2_cards) > 0:
        round_num += 1

        p1_cards_str = ", ".join(str(c) for c in player1_cards)
        p2_cards_str = ", ".join(str(c) for c in player2_cards)
        for prev_round_num, cards in prev_rounds.items():
            if cards[0] == p1_cards_str and cards[1] == p2_cards_str:
                print("Deck state repeats previous round, instant win for player 1!", prev_round_num)
                # TODO handle player 1 game winner
                break
        prev_rounds[round_num] = (p1_cards_str, p2_cards_str)

        print("-- Round {} (Game {}) --".format(round_num, game_num))
        print("Player 1's deck: {}".format(", ".join(str(c) for c in player1_cards)))
        print("Player 2's deck: {}".format(", ".join(str(c) for c in player2_cards)))

        p1 = player1_cards.pop(0)
        p2 = player2_cards.pop(0)

        print("Player 1 plays: {}".format(p1))
        print("Player 2 plays: {}".format(p2))

        if recursive_combat_enabled and p1 <= len(player1_cards) and p2 <= len(player2_cards):
            print("Playing a sub-game to determine the winner...")
            player1_cards_copy = player1_cards[:p1]
            player2_cards_copy = player2_cards[:p2]
            # TODO play sub game
            # TODO handle sub game winner
        else:
            if p1 > p2:
                print("Player 1 wins round {} of game {}!\n".format(round_num, game_num))
                player1_cards.append(p1)
                player1_cards.append(p2)
            else:
                print("Player 2 wins round {} of game {}!\n".format(round_num, game_num))
                player2_cards.append(p2)
                player2_cards.append(p1)

    print("\n== Post-game results ==")
    print("Player 1's deck: {}".format(", ".join(str(c) for c in player1_cards)))
    print("Player 2's deck: {}".format(", ".join(str(c) for c in player2_cards)))
    print("\n=======================\n")

    if len(player1_cards) > 0:
        return (1, player1_cards)
    return (2, player2_cards)

def run(label, input_file):
    player1_cards, player2_cards = read_input(input_file)
    print("{} 1: {}".format(label, play(player1_cards, player2_cards, False)))

run("test", "day22-input-test")
#run("part", "day22-input")
