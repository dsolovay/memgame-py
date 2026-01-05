import cardpy
import random

print('Welcome!')
while True:
    deck = cardpy.Deck()
    deck.shuffle()

    while True:
        x = input("How many cards should I deal? ")
        try:
            if int(x) >= 0 and int(x) <= deck.left():
                break
        except:
            pass
        print(x, "is invalid")
    
    
    cards = deck.deal(int(x))
    print("These cards have been dealt:")
    for i in range(len(cards)):
        print(cards[i])
    
    
    input("Memorize, then press Enter to clear screen")
    
    print("\033c", end="")
    correct = 0
    guesses = 0
    wrong = []
    # TODO Prompt for number of guesses
    for i in range(5):
        guesses += 1
        # TODO Avoid showing the same card twice
        random_card = deck.cards[random.randint(0, len(deck.cards) -1)]
        answer = input(f"Did the {random_card} appear? ")
        if ((answer.lower() == 'y' and deck.has_been_played(random_card)) or
                (answer.lower() in ('n', '') and (not deck.has_been_played(random_card)))):
                correct += 1
        else:
            wrong.append((random_card.__str__(), answer.lower()))
    print(f"Score: guesses={guesses}, correct={correct}")
    if len(wrong) > 0:
        print("Incorrect guesses:")
        for i in range(len(wrong)):
            print(wrong[i])
    else:
        print("Perfect!")
            

    print("\nOriginal cards:")

    for i in range(len(cards)):
        print(cards[i])
    
    if (input("Play again? ").lower() != 'y'):
        print("Bye!")
        break
    
