import src.ETL.persistence as persist

class AlcDrink:
    def __init__(self, drink_name, specifics, id=None):
        self.id = id
        self.drink_name = drink_name
        self.specifics = specifics

    def get_info(self):
        return f"#{self.id} {self.drink_name} ({self.specifics})"

    def get_name(self):
        return self.drink_name


def make_alc_drink(db, alcoholic_drink_list):
    drink_name = input("What alcoholic drink do you want? ")
    size = input(f"{drink_name}, no problem - large or small? ")
    new_id = db.save_drink("alc_drink",drink_name,size,None)
    new_drink = AlcDrink(drink_name, size, int(new_id))
    alcoholic_drink_list.append(new_drink)
    print("Drink added successfully")
    return new_drink

