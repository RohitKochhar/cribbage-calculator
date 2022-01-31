from CardDeck import Deck, Card
import itertools

class CribbageHand():
    def __init__(self):
        o_Deck = Deck()
        o_Deck.shuffle()
        self.a_Cards = o_Deck.drawCards(5)
        self.setHandRanks()
        self.setCombinations()
        self.setFifteens()
        self.setPairs()
        
    def __str__(self):
        s_Out = ""
        for o_Card in self.a_Cards:
            s_Out += (str(o_Card) + ", ") 
        return s_Out

    def setHandRanks(self):
        self.a_Ranks = []
        for o_Card in self.a_Cards:
            if o_Card.getRank() > 10:
                i_Rank = 10
            else:
                i_Rank = o_Card.getRank() + 1
            self.a_Ranks.append(i_Rank)

    def setCombinations(self):
        self.a_Combinations = []
        for i in range(0, len(self.a_Ranks) + 1):
            for t_Permutation in itertools.combinations(self.a_Ranks, i):
                self.a_Combinations.append(sorted(list(t_Permutation)))
    
    def setFifteens(self):
        self.a_Fifteens = []
        for a_Combo in self.a_Combinations:
            if sum(a_Combo) == 15:
                self.a_Fifteens.append(a_Combo)
    
    def setPairs(self):
        self.a_Pairs = []
        a_Seen = []
        a_RankLiterals = []
        for o_Card in self.a_Cards:
            a_RankLiterals.append(o_Card.getRankLiteral())
        print(a_RankLiterals)


if __name__ == "__main__":
    print("Starting simulations...")
    o_CribbageHand = CribbageHand()
    print(o_CribbageHand)
    print(o_CribbageHand.a_Fifteens)