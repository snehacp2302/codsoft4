import random

def get_computer_choice():
    return random.choice(["rock", "paper", "scissors"])

def determine_winner(player, computer):
    if player == computer:
        return "tie"
    wins_against = {"rock": "scissors", "paper": "rock", "scissors": "paper"}
    return "player" if wins_against[player] == computer else "computer"

def display_result(player, computer, result):
    icons = {"rock": "🪨", "paper": "📄", "scissors": "✂️"}
    print(f"\n  You:      {icons[player]} {player.capitalize()}")
    print(f"  Computer: {icons[computer]} {computer.capitalize()}")
    if result == "tie":
        print("  → It's a tie!")
    elif result == "player":
        print("  → You win! 🎉")
    else:
        print("  → Computer wins! 🤖")

def play():
    print("=" * 35)
    print("    ✂️  ROCK  PAPER  SCISSORS  🪨")
    print("=" * 35)

    scores = {"player": 0, "computer": 0, "ties": 0}

    while True:
        print("\nEnter your choice:")
        print("  [r] Rock  |  [p] Paper  |  [s] Scissors  |  [q] Quit")
        user_input = input("  > ").strip().lower()

        choice_map = {"r": "rock", "p": "paper", "s": "scissors", "rock": "rock", "paper": "paper", "scissors": "scissors"}

        if user_input == "q":
            print("\n--- Final Score ---")
            print(f"  You: {scores['player']}  |  Computer: {scores['computer']}  |  Ties: {scores['ties']}")
            if scores["player"] > scores["computer"]:
                print("  🏆 You won the series! Well played!")
            elif scores["computer"] > scores["player"]:
                print("  🤖 Computer won the series. Better luck next time!")
            else:
                print("  🤝 The series ended in a draw!")
            print("\nThanks for playing! Goodbye 👋")
            break

        if user_input not in choice_map:
            print("  ⚠️  Invalid choice. Please enter r, p, s, or q.")
            continue

        player_choice = choice_map[user_input]
        computer_choice = get_computer_choice()
        result = determine_winner(player_choice, computer_choice)

        display_result(player_choice, computer_choice, result)

        if result == "player":
            scores["player"] += 1
        elif result == "computer":
            scores["computer"] += 1
        else:
            scores["ties"] += 1

        print(f"  Score → You: {scores['player']}  Computer: {scores['computer']}  Ties: {scores['ties']}")

if __name__ == "__main__":
    play()
