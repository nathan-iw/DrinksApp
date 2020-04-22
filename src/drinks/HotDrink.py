import src.ETL.persistence as persist

class HotDrink:
    def __init__(self, drink_name, milk, sugar, id=None):
        self.id = id
        self.drink_name = drink_name
        self.milk = milk
        self.sugar = sugar

    def with_milk(self):
        if self.milk == 1:
            return "Milk, "
        else:
            return ""

    def get_info(self):
        return f"#{self.id} {self.drink_name} ({self.with_milk()}{self.sugar} sugars)"

    def get_name(self):
        return self.drink_name

def make_hot_drink(hot_drink_list):
    drink_name = input("What hot drink can I get you? ")
    milk = plus("Milk")
    sugar = input("One lump or two? ")
    new_id = persist.save_drink("hot_drink",drink_name,milk,sugar)
    new_drink = HotDrink(drink_name, milk, sugar, int(new_id))
    hot_drink_list.append(new_drink)
    return new_drink


def plus(feature):
    feature = input(f"{feature}? [Y/N] ")
    if feature.lower() == "y":
        return True
    else:
        return False