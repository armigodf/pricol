import copy


class Item:
    def __init__(self, name, price, amount, rarity) -> None:
        self.name = name
        self.price = price
        self.amount = amount
        self.rarity = rarity
        if amount > 0:
            pass
        else:
            print(name + " out of stock")

    def decrease_amount(self, value=1):
        if self.amount - value >= 0:
            self.amount -= value
        else:
            raise ValueError("Такого количества нет в наличии")

    def increase_amount(self, value):
        if value < 0:
            raise ValueError("Значение не может быть отрицательным")
        self.amount += value

    def set_amount(self, amount=1):
        if amount < 0:
            raise ValueError("Количество не может быть отрицательным")
        self.amount = amount


class Shop:
    def __init__(self, *items: Item) -> None:
        self.stock = list(items)

    def list_items(self):
        items = ""
        for item in self.stock:
            items += f"{item.name}: {item.price}, {item.amount}, {item.rarity}\n"
        return items

    def sell(self, name, amount=1):
        for item in self.stock:
            if item.name == name:
                item.decrease_amount(amount)
                break
        else:
            raise ValueError("товара нет в наличие")
        item_copy = copy.deepcopy(item)
        item_copy.set_amount(amount)
        return item_copy

    def buy(self, item: Item, amount=1):
        for stock_item in self.stock:
            if stock_item.name == item.name:
                stock_item.increase_amount(item.amount)
                break
        else:
            self.stock.append(item)
        return item


stone_shop = Shop(
    Item("emerald", "677000" + " За один карат", 748, "epic"),
    Item("diamond", "700000" + " За один карат", 576, "legendary"),
    Item("ruby", "560000" + " За один карат", 936, "rare"),
    Item("sapphire", "6000" + " За один карат", 200, "rare"),
    Item("cobblestone", "25" + " За один кг", 1000, "common"),
    Item("meteor_shard", " 7500100" + " За один осколок", 35, "unique")
)

print("Приветствуем вас в нашем магазине")

print(stone_shop.list_items())

item = stone_shop.sell("emerald", 36)
print(f"вы купили {item.name}: {item.amount}")

item = stone_shop.buy(
    # Item("sapphire", 0, 150, ""),
    # Item("pearl", 78, 177, "legendary"),
    Item("amethyst", "7500" + " За один грамм", 378, "rare")
)
print(f"В магазине появилося новый товар {item.name}: {item.price}, {item.amount}, {item.rarity}")
print(stone_shop.list_items())
