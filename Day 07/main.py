from collections import Counter

CARD_TO_VALUE = {"T": "10", "J": "1", "Q": "12", "K": "13", "A": "14"}


def rate(cards):
    counter = Counter(cards)
    if 1 in counter:
        n = counter.pop(1)
        max_card = max(counter, key=lambda card: counter[card]) if len(counter) > 0 else "A"
        counter[max_card] += n
    distinct = sorted(counter.values())
    if distinct == [5]:
        return 7, cards
    elif distinct == [1, 4]:
        return 6, cards
    elif distinct == [2, 3]:
        return 5, cards
    elif distinct == [1, 1, 3]:
        return 4, cards
    elif distinct == [1, 2, 2]:
        return 3, cards
    elif distinct == [1, 1, 1, 2]:
        return 2, cards
    elif distinct == [1, 1, 1, 1, 1]:
        return 1, cards


hands = []
with open("input.txt") as file:
    for line in file.read().splitlines():
        hand, bid = line.split(" ")
        hand = [int(num) for num in [CARD_TO_VALUE.get(card, card) for card in hand]]
        hands.append((hand, bid))
hands = sorted(hands, key=lambda cards: rate(cards[0]))
winnings = 0
for i in range(len(hands)):
    winnings += (i + 1) * int(hands[i][1])
print(winnings)
