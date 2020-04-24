import src.ETL.persistence as persist


class SoftDrink:
    def __init__(self, drink_name, glass, ice, id=None):
        self.id = id
        self.drink_name = drink_name
        self.glass = glass
        self.ice = ice

    def serving(self):
        if self.glass == 0:
            return ""
        else:
            if self.ice == 1:
                return "(Glass and ice)"
            else:
                return "(Glass, no ice)"

    def get_info(self):
        return f"#{self.id} {self.drink_name} {self.serving()} "

    def get_name(self):
        return self.drink_name


def make_soft_drink(db, soft_drink_list):
    drink_name = input("What soft drink can I get you? ")
    glass = plus("Glass")
    if glass:
        ice = plus("Ice")
    else:
        ice = False
    new_id = db.save_drink("soft_drink",drink_name,glass,ice)
    new_drink = SoftDrink(drink_name, glass, ice, int(new_id))
    soft_drink_list.append(new_drink)
    print("Drink added successfully")
    return new_drink


def plus(feature):
    feature = input(f"{feature}? [Y/N] ")
    if feature.lower() == "y":
        return True
    else:
        return False

