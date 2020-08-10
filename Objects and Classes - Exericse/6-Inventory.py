class Inventory:
    def __init__(self, capacity):
        self.__capacity = int(capacity)
        self.items = []

    def add_item(self, item):
        if self.__capacity > len(self.items):
            self.items.append(item)
        else:
            return f'not enough room in the inventory'

    def get_capacity(self):
        return len(self.items)

    def __repr__(self):
        left_capacity = self.__capacity - len(self.items)
        result = f"Items: {', '.join(self.items)}.\nCapacity left: {left_capacity}"
        return result

inventory = Inventory(2)
inventory.add_item("potion")
inventory.add_item("sword")
inventory.add_item("bottle")
print(inventory.get_capacity())
print(inventory)