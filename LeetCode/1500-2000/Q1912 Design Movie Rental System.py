from collections import defaultdict
from typing import List

from sortedcontainers import SortedList


class MovieRentingSystem:

    def __init__(self, n: int, entries: List[List[int]]):
        self.rented = SortedList()
        self.movies = defaultdict(SortedList)
        self.prices = {}
        for shop, movie, price in entries:
            self.movies[movie].add((price, shop))
            self.prices[(shop, movie)] = price

    def search(self, movie: int) -> List[int]:
        return [shop for price, shop in self.movies[movie][:5]]

    def rent(self, shop: int, movie: int) -> None:
        price = self.prices[(shop, movie)]
        self.movies[movie].remove((price, shop))
        self.rented.add((price, shop, movie))

    def drop(self, shop: int, movie: int) -> None:
        price = self.prices[(shop, movie)]
        self.movies[movie].add((price, shop))
        self.rented.remove((price, shop, movie))

    def report(self) -> List[List[int]]:
        return [[shop, movie] for _, shop, movie in self.rented[:5]]
