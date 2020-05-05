import src.ETL.Person as p



class Drink:
    def __init__(self, drink_type, drink_name, details, price, id=None):
        self.id = id
        self.drink_type = drink_type
        self.drink_name = drink_name
        self.details = details
        self.price = price

    def get_info(self):
        return f"#{self.id} {self.drink_name} {self.details}"

    def get_name(self):
        return self.drink_name

def contains(list, name_filter, details_filter):
    for drink_object in list:
        if name_filter(drink_object) and details_filter(drink_object):
            return drink_object
    return False


def make_drink(db, drink_list, drink_type):
    drink_name = input(f"What {drink_type} drink do you want? ")
    if drink_name == "":
        print("Invalid selection returning to main menu")
    else:
        if drink_type == "Hot":
            details = milk_sugar()
        else:
            details = size()
        drink_check = contains(drink_list,lambda x: x.drink_name == drink_name.capitalize(),lambda x: x.details ==details)
        if not drink_check:
            price = input(f"What is the price of a {drink_name}? ")
            new_id = db.save_drink("drink", drink_type, drink_name.capitalize(), details, price)
            chosen_drink = Drink(drink_type, drink_name, details, price, int(new_id))
            print("Drink added successfully")
        else:
            chosen_drink = drink_check
        drink_list.append(chosen_drink)
        return chosen_drink


def milk_sugar():
    details = int(input("""
    [1] Extra milk
    [2] Sugar
    [3] N/A

    Selection: """))
    if details == 1:
        return "extra milk"
    elif details == 2:
        return "with sugar"
    else:
        return "-"


def size():
    details = int(input("""
        [1] Large
        [2] Small

        Selection: """))
    if details == 1:
        return "large"
    else:
        return "small"
