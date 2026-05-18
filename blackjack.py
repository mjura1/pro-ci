import random
# Card values
cards = {
    '2': 2, '3': 3, '4': 4, '5': 5, '6': 6,
    '7': 7, '8': 8, '9': 9, '10': 10,
    'J': 10, 'Q': 10, 'K': 10, 'A': 11
}


def deal_card():
    return random.choice(list(cards.keys()))


def calculate_hand(hand: list[str]):
    if len(hand) < 2:
        raise ValueError("Not enough cards!")

    value = sum(cards[card] for card in hand)

    # Adjust for Aces
    aces = hand.count('A')
    while value > 21 and aces:
        value -= 10
        aces -= 1
    return value


def show_hand(player_hand, dealer_hand, hide_dealer=True):
    print(f"\nYour hand: {player_hand} (value: {calculate_hand(player_hand)})")
    if hide_dealer:
        print(f"Dealer's hand: [{dealer_hand[0]}, ?]")
    else:
        print(f"Dealer's hand: {dealer_hand} (value: {calculate_hand(dealer_hand)})")

def determine_winner(player_hand, dealer_hand):
    player_score = calculate_hand(player_hand)
    dealer_score = calculate_hand(dealer_hand)

    if player_score > 21:
        print("Player busts! You lose!")
        return "dealer"
    if dealer_score > 21:
        print("Dealer busts! You win!")
        return "player"
    if dealer_score > player_score:
        print("Dealer wins!")
        return "dealer"
    elif dealer_score < player_score:
        print("Player wins!")
        return "player"
    else:
        return "tie"

def blackjack():
    print("Welcome to Blackjack!\n")

    player_hand = [deal_card(), deal_card()]
    dealer_hand = [deal_card(), deal_card()]

    game_over = False

    while not game_over:
        show_hand(player_hand, dealer_hand)

        if calculate_hand(player_hand) == 21:
            print("Blackjack! You win!")
            return
        elif calculate_hand(player_hand) > 21:
            print("You busted! Dealer wins.")
            return

        choice = input("Type 'h' to hit or 's' to stand: ").lower()

        if choice == 'h':
            player_hand.append(deal_card())
        elif choice == 's':
            game_over = True
        else:
            print("Invalid input!")

    # Dealer's turn
    while calculate_hand(dealer_hand) < 17:
        dealer_hand.append(deal_card())

    show_hand(player_hand, dealer_hand, hide_dealer=False)

    # Determine winner
    determine_winner(player_hand, dealer_hand)


# Run the game
if __name__ == "__main__":
    while True:
        blackjack()
        again = input("\nPlay again? (y/n): ").lower()
        if again != 'y':
            print("Thanks for playing!")
            break