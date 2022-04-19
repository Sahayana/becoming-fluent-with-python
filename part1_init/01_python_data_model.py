import collections


Card = collections.namedtuple('Card', ['rank', 'suit']) # 클래스명: Card, 라벨: rank, suit
# namedtuple은 클래스처럼 객체를 생성할 수 있으며 튜플처럼 immutable 타입이고 마치 딕셔너리처럼 값에 대한 label을 부여할 수 있다.
# 결국 튜플처럼 immutable하기 때문에 클래스와 달리 값을 수정할 수 없다. 그리고 튜플처럼 정수 값을 통해서 인덱싱할 수 있다.
# https://wikidocs.net/126315

my_card = Card('5', 'clubs')
my_card2 = Card('A', 'spades')
my_card3 = Card('2', 'clubs')

class FrenchDeck:

    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()

    def __init__(self) -> None:
        self._cards = [Card(rank=rank, suit=suit) for suit in self.suits for rank in self.ranks]

    def __len__(self):
        return len(self._cards)
    
    def __getitem__(self, position):
        return self._cards[position]


deck = FrenchDeck()

# print(deck._cards)  # __init__
# print(len(deck))    # __len__
# print(deck[2])  # __getitem__


def sorted_cards(card):
    suit_values = dict(spades=3, hearts=2, diamonds=1, clubs=0)
    rank_value = FrenchDeck.ranks.index(card.rank)
    return rank_value * len(suit_values) + suit_values[card.suit]

print(sorted_cards(my_card))
print(sorted_cards(my_card2))
print(sorted_cards(my_card3))

# 카드 순위
for card in sorted(deck, key=sorted_cards):
    print(card)


# 특별 메서드의 호출 방법 ex) __len__
# 객체 card의 __len__ 특별 메서드는 len(card)로 호출하며 이는 곳 card.__len__ 메서드를 호출하는 구조 