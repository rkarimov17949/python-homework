class Dessert:
    def __init__(self, title, taste, cost):
        self.title = title
        self.taste = taste
        self.cost = cost

    def show(self):
        print(f"{self.title} | Dad: {self.taste} | {self.cost} AZN")


class Bakery:
    def __init__(self):
        self.menu = []

    def add_item(self, dessert):
        self.menu.append(dessert)

    def remove_unwanted_taste(self, unwanted):
        result = []
        for item in self.menu:
            if item.taste != unwanted:
                result.append(item)
        return result


class Client:
    def __init__(self, fullname, cash):
        self.fullname = fullname
        self.cash = cash
        self.debt = 0

    def has_money(self, amount):
        return self.cash >= amount

    def use_credit(self, amount):
        self.debt += amount
        print(f"Credit is opened: {amount} AZN")


class Register:
    def checkout(self, client, dessert):
        print("\n Booking:")
        dessert.show()
        print(f"💵 Available money: {client.cash} AZN")

        if client.has_money(dessert.cost):
            client.cash -= dessert.cost
            print("Successful")
        else:
            missing = dessert.cost - client.cash
            client.cash = 0
            client.use_credit(missing)
            print("No money, only cash credit")
