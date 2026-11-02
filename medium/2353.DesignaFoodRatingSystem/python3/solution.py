from collections import defaultdict
import heapq

class FoodRatings:
    def __init__(self, foods: List[str], cuisines: List[str], ratings: List[int]):
        self.scores = dict(zip(foods, ratings))
        self.food_cuisine = dict(zip(foods, cuisines))  
        self.heaps = defaultdict(list) 
        
        for i, (food, cuisine) in enumerate(zip(foods, cuisines)):
            heapq.heappush(self.heaps[cuisine], (-ratings[i], food))

    def changeRating(self, food: str, newRating: int) -> None:
        cuisine = self.food_cuisine[food]
        self.scores[food] = newRating
        heapq.heappush(self.heaps[cuisine], (-newRating, food))

    def highestRated(self, cuisine: str) -> str:
        while True:
            rating, food = self.heaps[cuisine][0]
            if -rating == self.scores[food]:
                return food
            else:
                heapq.heappop(self.heaps[cuisine])