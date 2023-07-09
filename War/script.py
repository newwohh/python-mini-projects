import random


suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven',
         'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7, 'Eight': 8,
          'Nine': 9, 'Ten': 10, 'Jack': 11, 'Queen': 12, 'King': 13, 'Ace': 14}


class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]

    def __str__(self):
        return self.rank + " of " + self.suit


two_hearts = Card("Heart", "Two")


class Deck:

    def __init__(self):

        self.all_cards = []

        for suit in suits:
            for rank in ranks:
                created_card = Card(suit, rank)
                self.all_cards.append(created_card)

    def shuffle_deck(self):
        random.shuffle(self.all_cards)

    def deal_one(self):
        return self.all_cards.pop()


new_deck = Deck()

first_card = new_deck.all_cards[0]

new_deck.shuffle_deck()

my_card = new_deck.deal_one()


class Player:

    def __init__(self, name):
        self.name = name
        self.allcards = []

    def remove_card(self):
        return self.allcards.pop(0)

    def add_card(self, new_card):
        if type(new_card) == type([]):
            self.allcards.extend(new_card)
        else:
            self.allcards.append(new_card)

    def __str__(self) -> str:
        return f'Player {self.name} has {len(self.allcards) } cards'


player_one = Player("One")
player_two = Player("Two")

new_deck = Deck()
new_deck.shuffle_deck()

for x in range(26):
    player_one.add_card(new_deck.deal_one())
    player_two.add_card(new_deck.deal_one())

game_on = True

round_num = 0

while game_on:
    round_num += 1
    print(f'Round {round_num}')

    if len(player_one.allcards) == 0:
        print('Player one, out of cards! Player two wins')
        game_on = False
        break

    if len(player_two.allcards) == 0:
        print('Player two, out of cards! Player one wins')
        game_on = False
        break

    player_one_cards = []
    player_one_cards.append(player_one.remove_card())

    player_two_cards = []
    player_two_cards.append(player_two.remove_card())

    at_war = True

    while at_war:
        if player_one_cards[-1].value > player_two_cards[-1].value:

            player_one.add_card(player_one_cards)
            player_one.add_card(player_two_cards)

            at_war = False

        elif player_one_cards[-1].value < player_two_cards[-1].value:

            player_two.add_card(player_one_cards)
            player_two.add_card(player_two_cards)

            at_war = False

        else:
            print("War")

            if len(player_one.allcards) < 5:
                print("Player one unable to declare war")
                print("Player two wins")
                game_on = False
                break

            if len(player_two.allcards) < 5:
                print("Player two unable to declare war")
                print("Player one wins")
                game_on = False
                break

            else:
                for num in range(5):
                    player_one_cards.append(player_one.remove_card())
                    player_two_cards.append(player_two.remove_card())
