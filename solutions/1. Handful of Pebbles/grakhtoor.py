from random import choices
from collections import namedtuple


Color = namedtuple('Color', ['SCORE', 'INIT', 'TITLE'])

class COLORS(object):
    YELLOW = Color(1, 20, 'yellow')
    ORANGE = Color(2, 20, 'orange')
    BROWN = Color(5, 10, 'brown')
    RED = Color(-10, 2, 'red')


PIBBLES_IN_HANDFUL = 5
HANDFUL_AMOUNT = 3


class Handful(object):
    def __init__(self, yellow, orange, brown, red):
        self.yellow = yellow
        self.orange = orange
        self.brown = brown
        self.red = red

    def get_score(self):
        return \
            self.yellow * COLORS.YELLOW.SCORE + \
            self.orange * COLORS.ORANGE.SCORE + \
            self.brown * COLORS.BROWN.SCORE + \
            self.red * COLORS.RED.SCORE
    
    def __str__(self):
        return "{}: {}, {}: {}, {}: {}, {}: {}".format(
            COLORS.YELLOW.TITLE, self.yellow,
            COLORS.ORANGE.TITLE, self.orange,
            COLORS.BROWN.TITLE, self.brown,
            COLORS.RED.TITLE, self.red,
        )

    def __radd__(self, other):
        return other + self.get_score()


class Bag(object):
    def __init__(self):
        self.yellow = COLORS.YELLOW.INIT
        self.orange = COLORS.ORANGE.INIT
        self.brown = COLORS.BROWN.INIT
        self.red = COLORS.RED.INIT

    def take_handful(self):
        yellow, orange, brown, red = 0, 0, 0, 0

        color_titles = [COLORS.YELLOW.TITLE, COLORS.ORANGE.TITLE, COLORS.BROWN.TITLE, COLORS.RED.TITLE]
        for _ in range(PIBBLES_IN_HANDFUL):
            color = choices(color_titles, [self.yellow, self.orange, self.brown, self.red])[0]
            if color == COLORS.YELLOW.TITLE:
                self.yellow -= 1
                yellow += 1
            elif color == COLORS.ORANGE.TITLE:
                self.orange -= 1
                orange += 1
            elif color == COLORS.BROWN.TITLE:
                self.brown -= 1
                brown += 1
            elif color == COLORS.RED.TITLE:
                self.red -= 1
                red += 1

        return Handful(yellow, orange, brown, red)


class Player(object):
    def __init__(self):
        self.handfuls = []

    def take_handful(self, bag):
        handful = bag.take_handful()
        self.handfuls.append(handful)
    
    def get_score(self):
        return sum(self.handfuls)

    def __lt__(self, other):
        return self.get_score() < other.get_score()

    def __eq__(self, other):
        return self.get_score() == other.get_score()
    
    def __ge__(self, other):
        return self.get_score() > other.get_score()


class Game(object):
    def play(self):
        bag = Bag()
        player1, player2 = Player(), Player()
        for i in range(1, HANDFUL_AMOUNT+1):
            print("Turn #{}".format(i))
            player1.take_handful(bag)
            print("Player1: ", player1.handfuls[-1])
            player2.take_handful(bag)
            print("Player2: ", player2.handfuls[-1])
            print("Player1`s score: {}\nPlayer2`s score: {}".format(player1.get_score(), player2.get_score()))
            print("")
        if player1 > player2:
            print("Player1 won")
        elif player2 > player1:
            print("Player2 won")
        else:
            print("Draw")

if __name__ == "__main__":
    game = Game()
    game.play()
