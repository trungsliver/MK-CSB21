# Bài 1: Sử dụng OOP để mô phỏng bộ bài tú lơ khơ (52 lá)
# Yêu cầu:
    # - 2 class: Card (lá bài) và Deck (bộ bài)
    # - Class Card có các thuộc tính: rank (hạng bài), suit (chất bài): 2 of Hearts, Ace of Spades, v.v.
    # - Class Deck có thuộc tính: cards (danh sách các lá bài)
    # - Class Deck có các phương thức: shuffle (xáo bài), deal (chia bài), display (hiển thị)

class Card:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def __str__(self):
        return f"{self.rank} of {self.suit}"
    
    def display_info(self):
        print(f"Card: {self.rank} of {self.suit}")

class Deck:
    suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
    ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']

    def __init__(self):
        self.cards = []
        # Thêm từng lá bài vào bộ bài
            # Duyệt từng chất bài
        for suit in self.suits:
            # Duyệt từng hạng bài
            for rank in self.ranks:
                self.cards.append(Card(rank, suit))

    def display(self):
        for card in self.cards:
            print(card)
            # card.display_info()

    def deal_a_card(self):
        if len(self.cards) == 0:
            return None
        return self.cards.pop()
    
    def shuffle(self):
        import random
        random.shuffle(self.cards)

deck1 = Deck()
deck1.display()
deck1.shuffle()
print("After shuffling:")
deck1.display()
for i in range(53):
    print(f"Dealt card {i+1}:", deck1.deal_a_card())

# Bài 2: Cho mảng số nguyên numbers gồm n phần tử. 
# Yêu cầu: Hãy tìm tất cả các phần tử xuất hiện nhiều hơn 1 lần.

def find_duplicates(numbers, frequency=2):
    # dictionary lưu số lần xuất hiện của từng phần tử
    count_dict = {}
    # Đếm số lần xuất hiện của từng phần tử
    for num in numbers:     # O(n)
        if num in count_dict:
            count_dict[num] += 1
        else:
            count_dict[num] = 1
    # danh sách lưu các phần tử xuất hiện nhiều hơn 1 lần
    duplicates = []
    for key, value in count_dict.items():   # O(n)
        if value >= frequency:
            duplicates.append(key)
    return duplicates

num1 = [1, 2, 2, 3, 3]
print(find_duplicates(num1))   # Output: [2, 3]
num2 = [4, 5, 6, 7]
print(find_duplicates(num2))   # Output: []
num3 = [1, 1, 1, 1, 1]
print(find_duplicates(num3))   # Output: [1]

