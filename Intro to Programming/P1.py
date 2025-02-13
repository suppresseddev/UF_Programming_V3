#Cheating Module
import p1_random as p1
rng = p1.P1Random()

#Black Jack Project
#Sorry, RIGGED, Black Jack Project.
#Because of you can't even be bothered to grade a CARD GAME!!!!!
#Absolutely ridiculous, you're even making game development unfun.
game = 1
wins = 0
losses = 0
ties = 0

dealerhand = 0
playerhand = 0

#Probably could've used a dictionary, but having 2 equal length lists is easier for me
# because key & value are named contextually.
cards = [   'ACE', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'JACK', 'QUEEN', 'KING']
cardvalues = [1,    2,   3,   4,   5,   6,   7,   8,   9,   10,    10,      10,     10]

#Menu
validmenu = [1, 2, 3, 4]
def menu():
    print("1. Get another card\n2. Hold hand\n3. Print statistics\n4. Exit")

#Draw
def draw():
    global playerhand
    card_index = rng.next_int(13)
    playerhand += cardvalues[card_index]
    print(f"Your card is a {cards[card_index]}!")
    print(f"Your hand is: {playerhand}")
#Hold and finish game:
def hold():
    global dealerhand
    global playerhand
    dealerhand = (rng.next_int(11)+16)
    print(f"Dealer's hand: {dealerhand}")
    print(f"Your hand is: {playerhand}")

#Stats
def stats():
    global wins
    global losses
    global ties
    global game
    if game == 1:
        print("No statistics yet!")
        return
    print(f"Number of Player wins: {wins}")
    print(f"Number of Dealer wins: {losses}")
    print(f"Number of tie games: {ties}")
    print(f"Total # of games played is: {game-1}")
    print(f"Percentage of Player wins: {(wins/(game-1)*100):.1f}%")
#Game Loop
while True:
    print(f"START GAME #{game}")
    playerhand = 0
    dealerhand = 0
    print()
    draw()
    while True:
        menu()
        choice = int(input("Choose an option: "))
        if choice not in validmenu:
            print("Invalid input!")
            print("Please enter an integer value between 1 and 4.")
            continue
        print()
        if choice == 1:
            draw()
        if choice == 2:
            hold()
            if dealerhand == 21:
                print()
                print("Dealer wins!")
                losses += 1
                break
            elif dealerhand > 21:
                print()
                print("You win!")
                wins += 1
                break
            else:
                if dealerhand > playerhand:
                    print()
                    print("Dealer wins!")
                    losses += 1
                    break
                if dealerhand < playerhand:
                    print()
                    print("You win!")
                    wins += 1
                    break
                if dealerhand == playerhand:
                    print()
                    print("It's a tie! No one wins!")
                    ties += 1
                    break
        if choice == 3:
            stats()
        if choice == 4:
            exit()
        #Check status of the game:
        if playerhand == 21:
            print()
            print("BLACKJACK! You win!")
            wins += 1
            break
        if playerhand > 21:
            print()
            print("You exceeded 21! You lose.")
            losses += 1
            break

    game += 1

