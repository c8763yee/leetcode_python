class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        location = defaultdict(list)
        for i, card in enumerate(cards):
            location[card].append(i)
        
        minimum = -1
        for card, card_index in location.items():
            print(card_index)
            if len(card_index) == 1:
                continue
                
            for i in range(len(card_index)-1):
                minimum = min(minimum if minimum != -1 else float('inf'), card_index[i+1]-card_index[i]+1)
                
        return minimum