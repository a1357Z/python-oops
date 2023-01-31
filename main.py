import csv


class Item:
    # class attribute: attribute that belongs to class & can be accessed by every instance
    pay_rate = 0.8  # pay rate after 20% discount
    instances = []
    instanceMap = {}

    def __init__(self, name: str, price: float, quantity: int = 0):
        # Run validation on data
        # Can u be very useful for design by contract and assertive programming!
        assert type(name == str), f"{name} should be a string!"
        assert price >= 0, f"Price: {price} should be > 0"

        # Assign to self object
        # These are instance attributes
        self.name = name
        self.price = price
        self.quantity = quantity

        # update the instances list and instanceMap
        Item.instances.append(self)
        Item.instanceMap[name] = price

    def calculate_price(self):
        return self.price * self.quantity

    def apply_discount(self):
        return self.calculate_price() * self.pay_rate
        # always use self.pay_rate instead of Item.pay_rate for overriding issues

    def __repr__(self):
        return f"Item('{self.name}', {self.price}, {self.quantity})"

    # We will use this to create instances from csv file.
    # So this will be a class method.
    @classmethod
    def instantiate_from_csv(cls):
        with open("items.csv", "r") as f:
            reader = csv.DictReader(f)
            items = list(reader)

        for item in items:
            print(f"creating item: {item}")
            Item(item.get("name"), float(item.get("price")), int(item.get("quantity")))

    # create static method
    # static methods don't get the object as first parameter by default
    @staticmethod
    def is_integer(num):
        # we will count
        if isinstance(num, float):
            # return true for numbers like 10.00, 345.0 etc
            return num.is_integer()
        elif isinstance(num, int):
            return True
        else:
            return False


def printType(element):
    print(f"data type of: {element} = {type(element)}")


"""
session 1: code

item1 = Item("phone", 500, 5)

# get the class types of data structures
printType(item1)
printType(item1.name)
printType(item1.price)

print(f"pay rate from class: {Item.pay_rate}")
print(f"pay rate from instance: {item1.pay_rate}")  # looks for the attribute at instance then at the class level

# get all the attributes
print(f"All class level attributes: {Item.__dict__}")
print(f"All instance attributes: {item1.__dict__}")

# get discount
print(f"Original price: {item1.calculate_price()}")
print(f"Discounted price using class attribute: {item1.apply_discount()}")

item2 = Item("laptop", 1000, 2)
item2.pay_rate = 0.7  # add the pay_rate attribute to the instance
print(f"Original price: {item2.calculate_price()}")
print(f"Discounted price using class attribute: {item2.apply_discount()}")

# five items
item_1 = Item("Phone", 100, 1)
item_2 = Item("Laptop", 1000, 3)
item_3 = Item("Cable", 10, 5)
item_4 = Item("Mouse", 50, 5)
item_5 = Item("Keyboard", 75, 5)

"""

print(f"Count of Item instances: {len(Item.instances)}")
print(f"Map of Item instances: {Item.instanceMap}")

# printing all the instances

print("Pretty print Item instances:")
for instance in Item.instances:
    print(instance)

# printing all the instance names
print("Instance names so far: ")
for instance in Item.instances:
    print(instance.name)

# print all
print(f"print all: {Item.instances}")

# create items from csv
Item.instantiate_from_csv()
print(f"print all: {Item.instances}")

# static methods
print(Item.is_integer(7.0))  # true
print(Item.is_integer(7.8))  # false
