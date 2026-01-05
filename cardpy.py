from dataclasses import dataclass
import random

@dataclass
class Suit:
    symbol: int
    name: str
    rank: int

    #def __repr__(self):
    #    return f"Suit({hex(self.symbol)}, '{self.name}', {self.rank})"


spades      = Suit('\u2664', "Spades", 0)
hearts      = Suit('\u2661', "Hearts", 1)
diamonds    = Suit('\u2662', "Diamonds", 2)
clubs       = Suit('\u2667', "Clubs", 3)

suits = [spades, hearts, diamonds, clubs]
facecards = list("AKQJ")
numbercards = [str(i) for i in range(10, 1, -1)]
ranks = facecards + numbercards

@dataclass
class Card:
    rank: str
    suit: Suit

    def __str__(self):
        return f"{self.suit.symbol} {self.rank}"


class Deck:
    def __init__(self):
        self.cards = []
        self.played = 0
        for suit in suits:
            for rank in ranks:
                self.cards.append(Card(rank, suit))

    def shuffle(self):
        """ https://en.wikipedia.org/wiki/Fisher%E2%80%93Yates_shuffle """
        for i in range(len(self.cards) - 1, 0, -1):
            j = random.randint(0, i)
            self.cards[i], self.cards[j] = self.cards[j], self.cards[i]
        self.played = 0 # Shuffling resets deck: no concept of shuffling remaining cards yet.

    def list(self):
        for i in range(len(self.cards)):
            print(self.cards[i], end=',')

    def deal(self, count=1):
        cards = self.cards[self.played : self.played + count ]
        self.played += count
        self.played = min(self.played, len(self.cards))
        return cards

    def left(self):
        return len(self.cards) - self.played

    def has_been_played(self, card):
        return self.cards[0:self.played].__contains__(card)


# Tests
if __name__ == '__main__':

    print("--- card and deck tests ---")
    ace = Card('A', spades)
    print("ace: ", ace)
    ace = Card('A', spades)
    print("ace: ", ace)
    deck = Deck()
    print(f"deck: {deck}\n")
    
    print("Before shuffling:")
    deck.list()
    print("\n\n")
    
    deck.shuffle()
    print("After shuffling:")
    deck.list()
    print("\n\n")
    
    print("--- deck.has_been_played(card) tests ---")
    first_card = deck.deal()[0]
    last_card = deck.cards[-1]
    print("Deal 'first_card':", first_card);
    print("Set 'last_card' (peaked at bottom): ", last_card);
    
    print("deck.has_been_played(first_card): ", deck.has_been_played(first_card), "\n")
    print("deck.has_been_played(last_card): ", deck.has_been_played(last_card), "\n\n")
    print("Deal a card:", deck.deal()[0])
    print("Deal a hand:", [str(c) for c in deck.deal(5)])
    
    print("deck.left(): ", deck.left(), "\n\n")
    
    print("Test of limit: deck.deal(50)")
    print('cards50 = deck.deal(50)')
    cards50 = deck.deal(50)
    print("len(cards50): ", len(cards50)) # 45
    
    
    print("deck.left(): ", deck.left(), "\n\n")
        
