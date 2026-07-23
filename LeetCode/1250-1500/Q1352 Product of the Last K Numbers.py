class ProductOfNumbers:

    def __init__(self):
        self.prefix_products = []

    def add(self, num: int) -> None:
        n = len(self.prefix_products)
        if n == 0:
            self.prefix_products.append(num)
        else:
            prefix = self.prefix_products[n - 1] * num
            if prefix == 0:
                prefix = num
                self.prefix_products = []
            self.prefix_products.append(prefix)

    def getProduct(self, k: int) -> int:
        print(self.prefix_products)
        n = len(self.prefix_products)
        if n < k:
            return 0
        elif n == k:
            return self.prefix_products[-1]
        return self.prefix_products[n - 1] // self.prefix_products[n - k - 1]


# Your ProductOfNumbers object will be instantiated and called as such:
obj = ProductOfNumbers()
obj.add(3)
obj.add(0)
obj.add(2)
obj.add(5)
obj.add(4)
print(obj.getProduct(2))
print(obj.getProduct(3))
print(obj.getProduct(4))
obj.add(8)
print(obj.getProduct(2))
