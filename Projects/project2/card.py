import stdio
import stdrandom

# Ranks and suits set
RANKS = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']
SUITS = ['Clubs', 'Diamonds', 'Hearts', 'Spades']

# Deck
deck = []
for rank in RANKS:
    for suit in SUITS:
        card = rank + ' of ' + suit
        deck += [card]

# Deck shuffle
n = len(deck)
for i in range(n):
    r = stdrandom.uniformInt(i, n)
    temp = deck[r]
    deck[r] = deck[i]
    deck[i] = temp

# Drawing of random card from the deck and output to std
rank = stdrandom.uniformInt(0, len(RANKS))
suit = stdrandom.uniformInt(0, len(SUITS))
stdio.writeln(RANKS[rank] + ' of ' + SUITS[suit])
