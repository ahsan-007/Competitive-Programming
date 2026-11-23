# https://leetcode.com/problems/product-of-the-last-k-numbers/description/?envType=daily-question&envId=2026-11-23

class ProductOfNumbers:
    def __init__(self):
        self.prefix_product = [1]
        self.size = 0

    def add(self, num: int):
        if num == 0:
            self.prefix_product = [1]
            self.size = 0
        else:
            self.prefix_product.append(self.prefix_product[self.size] * num)
            self.size += 1

    def getProduct(self, k: int) -> int:
        if k > self.size:
            return 0
        return (
            self.prefix_product[self.size] // self.prefix_product[self.size - k]
        )

productOfNumbers = ProductOfNumbers()
productOfNumbers.add(3)
productOfNumbers.add(0)
productOfNumbers.add(2)
productOfNumbers.add(5)
productOfNumbers.add(4)
print(productOfNumbers.getProduct(2))
print(productOfNumbers.getProduct(3))
productOfNumbers.getProduct(4)
productOfNumbers.add(8)
print(productOfNumbers.getProduct(2))
