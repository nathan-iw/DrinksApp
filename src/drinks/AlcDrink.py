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


def make_alc_drink(alcoholic_drink_list):
    drink_name = input("What alcoholic drink do you want? ")
    specifics = input(f"{drink_name}, no problem - anything special? ")
    new_id = persist.save_drink("alc_drink",drink_name,specifics,None)
    new_drink = AlcDrink(drink_name, specifics, int(new_id))
    alcoholic_drink_list.append(new_drink)
    return new_drink
