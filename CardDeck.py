from random import shuffle, randint

class Card:
    _a_Suits    = ["SPADE", "CLUB", "HEART", "DIAMOND"]
    _a_Ranks     = ["ACE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE", "TEN", "JACK", "QUEEN", "KING"]
    def __init__(self, i_ID=randint(0,52)):
        self.i_ID       = i_ID
        self.i_Rank     = i_ID % 13
        self.i_Suit    = int(i_ID / 13)

    def getRank(self):
        return self.i_Rank

    def getSuit(self):
        return self.i_Suit

    def getRankLiteral(self):
        return self._a_Ranks[self.i_Rank]

    def getSuitLiteral(self):
        return self._a_Suits[self.i_Suit]

    def __str__(self):
        return f"Card ID{self.i_ID} -> the {self.getRankLiteral()} of {self.getSuitLiteral()}S"

class Deck:
    def __init__(self):
        self.a_Cards            = []
        self.a_CardsById        = []
        self.a_DrawnCards       = []
        self.a_DrawnCardsById   = []
        for i in range(0, 52):
            self.a_Cards.append(Card(i))
            self.setCardIDArray()

    def setCardIDArray(self):
        self.a_CardsById = []
        for o_Card in self.a_Cards:
            self.a_CardsById.append(o_Card.i_ID)

    def shuffle(self):
        shuffle(self.a_Cards)
        self.setCardIDArray()

    def getCardIDArray(self):
        return self.a_CardsById

    def reset(self):
        self.__init__()

    def drawCard(self):
        o_DrawnCard = self.a_Cards.pop(0)
        self.a_DrawnCards.append(o_DrawnCard)
        self.a_DrawnCardsById.append(o_DrawnCard.i_ID)
        self.setCardIDArray()
        return o_DrawnCard

    def drawCards(self, i_NumCards):
        a_DrawnCards = []
        for i in range(0, i_NumCards):
            a_DrawnCards.append(self.drawCard())
        return a_DrawnCards