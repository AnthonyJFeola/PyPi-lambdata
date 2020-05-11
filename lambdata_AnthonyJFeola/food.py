class Food:
    def __init__(self, size, color, price, kind):
        self.size = size
        self.color = color
        self.price = price
        self.kind = kind

    def eat(self):
        print(f"EATING THE {self.size.upper()} {self.color.upper()} {self.kind.upper()}!")

if __name__ == "__main__":

    food = Food(size="Large", color="Yellow", price="3.99", kind='Fries')
    print(food.size, food.color, food.price, food.kind)
    food.eat()
    food2 = Food(size="Small", color="Red", price="7.99", kind='Burger')
    print(food2.size, food2.color, food2.price, food2.kind)
    food2.eat()
