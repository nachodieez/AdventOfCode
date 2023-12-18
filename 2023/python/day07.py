from collections import defaultdict

data = open("../data/day07.in").read().strip().split("\n")

cards = ["A", "K", "Q", "J", "T", "9", "8", "7", "6", "5", "4", "3", "2"]
cards_strengths = dict(zip(cards, reversed(list(range(len(cards))))))
types = ["Five of a kind", "Four of a kind", "Full house", "Three of a kind",
         "Two pair", "One pair", "High card"]
hands = [(5,), (4, 1), (3, 2), (3, 1, 1), (2, 2, 1), (2, 1, 1, 1), (1, 1, 1, 1, 1)]
handstypes = dict(zip(hands, types))
hands_strengths = dict(zip(types, reversed(list(range(len(types))))))

def total_winnings() -> int:
    hands = []
    for line in data:
        hand, bid = line.split(" ")
        hands.append((Hand(hand), bid))
    hands.sort(key = lambda x: x[0])

    total_winnings = 0
    for rank in range(1, len(hands) + 1):
        total_winnings += rank * int(hands[rank - 1][1])
    return total_winnings

class Hand:
    def __init__(self, cards):
        self.cards = cards
        self.type = self._get_hand_type(self.cards)

    def _get_hand_type(self, cards) -> list[tuple]:
        d = defaultdict(int)
        for card in cards:
            d[card] += 1
        hand = tuple(sorted(d.values(), reverse = True))
        return handstypes[hand]
    

    def __eq__(self, other) -> bool:
        return set(self.cards) == set(other.cards)

    def __lt__(self, other) -> bool:
        if hands_strengths[self.type] < hands_strengths[other.type]:
            return True
        elif hands_strengths[self.type] == hands_strengths[other.type]:
            for i in range(len(self.cards)):
                if cards_strengths[self.cards[i]] < cards_strengths[other.cards[i]]:
                    return True
                elif cards_strengths[self.cards[i]] > cards_strengths[other.cards[i]]:
                    return False
            return False
        else:
            return False
    
    def __str__(self) -> str:
        return self.cards
    
    def __repr__(self) -> str:
        return f"Hand({self.cards})"


print("Sol 1:", total_winnings())

# special joker case
cards = ["A", "K", "Q", "T", "9", "8", "7", "6", "5", "4", "3", "2", "J"]
cards_strengths = dict(zip(cards, reversed(list(range(len(cards))))))
class Hand:
    def __init__(self, cards):
        self.cards = cards
        self.type = self._get_hand_type(self.cards)

    def _get_hand_type(self, cards) -> list[tuple]:
        d = defaultdict(int)
        for card in cards:
            d[card] += 1
        if "J" in d: # this way, the new 
            nj = d["J"]
            if nj != 5: # all jokers case
                del d["J"]
                d[max(d, key=d.get)] += nj  
        hand = tuple(sorted(d.values(), reverse = True))
        return handstypes[hand]

    def __eq__(self, other) -> bool:
        return set(self.cards) == set(other.cards)

    def __lt__(self, other) -> bool:
        if hands_strengths[self.type] < hands_strengths[other.type]:
            return True
        elif hands_strengths[self.type] == hands_strengths[other.type]:
            for i in range(len(self.cards)):
                if cards_strengths[self.cards[i]] < cards_strengths[other.cards[i]]:
                    return True
                elif cards_strengths[self.cards[i]] > cards_strengths[other.cards[i]]:
                    return False
            return False
        else:
            return False
    
    def __str__(self) -> str:
        return self.cards
    
    def __repr__(self) -> str:
        return f"Hand({self.cards})"

print("Sol 2:", total_winnings())