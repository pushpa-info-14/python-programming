import heapq
from typing import List


class FoodRatings:
    def __init__(self, foods: List[str], cuisines: List[str], ratings: List[int]):
        n = len(foods)
        self.rating_by_food = {}
        self.cuisine_by_food = {}
        self.ratings_by_cuisine = {}
        for cuisine in set(cuisines):
            self.ratings_by_cuisine[cuisine] = []
        for i in range(n):
            self.rating_by_food[foods[i]] = ratings[i]
            self.cuisine_by_food[foods[i]] = cuisines[i]
            heapq.heappush(self.ratings_by_cuisine[cuisines[i]], (-ratings[i], foods[i]))

    def changeRating(self, food: str, newRating: int) -> None:
        self.rating_by_food[food] = newRating
        heapq.heappush(self.ratings_by_cuisine[self.cuisine_by_food[food]], (-newRating, food))

    def highestRated(self, cuisine: str) -> str:
        while -self.ratings_by_cuisine[cuisine][0][0] != self.rating_by_food[self.ratings_by_cuisine[cuisine][0][1]]:
            heapq.heappop(self.ratings_by_cuisine[cuisine])
        return self.ratings_by_cuisine[cuisine][0][1]


obj = FoodRatings(["kimchi", "miso", "sushi", "moussaka", "ramen", "bulgogi"],
                  ["korean", "japanese", "japanese", "greek", "japanese", "korean"], [9, 12, 8, 15, 14, 7])
print(obj.highestRated("korean"))
print(obj.highestRated("japanese"))
obj.changeRating("sushi", 16)
print(obj.highestRated("japanese"))
obj.changeRating("ramen", 16)
print(obj.highestRated("japanese"))
