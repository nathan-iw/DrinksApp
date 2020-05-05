import src.drinks.Drink as d
from src.ETL.persistence import Database
import src.tools.print_data as print_data
import src.ETL.Person as p

db = Database()


def unique(drink_list, drink_type):
    # intialize a null list
    unique_list = []
    # traverse for all elements
    for i in drink_list:
        # check if exists in unique_list or not
        if i.drink_type == drink_type and i.drink_name not in unique_list:
            unique_list.append(f"{i.drink_name}")
    return unique_list

class Round:
    """Class to create a round of drinks, which is created with the name of the round brewer"""
    def __init__(self, db, brewer, drink):
        self.db = db
        self.brewer = brewer
        self.orders = {}  # Dictionary to store key: value pairs of person_name: HotDrink/SoftDrink/AlcoholicDrink
        self.drink = drink

    def add_drinker(self, person):
        """Method to add drinkers (and their drinks) to the round and a drink for the brewer"""
        self.orders[person] = self.choose_drink(person)

    def get_input(self, text):
        return input(text)

    def getNonBlankInput(self, message, error_message):

        x = input(message)
        while len(x.strip()) == 0:
            x = input(error_message)

        return x

    def get_drink_type(self):
        drink_type = self.getNonBlankInput("""
        Select drink type:
            [H]ot drinks
            [S]oft drinks
            [A]lcoholic drinks
                Selection: ""","Enter a valid selection: ")
        drink_type = drink_type.lower()
        if drink_type == "h":
            return "Hot"
        elif drink_type == "s":
            return "Soft"
        elif drink_type == "a":
            return "Alcoholic"
        else:
            print("Come again")
            self.get_drink_type()

    def same_again(self, fav, type):
        if fav is not None:
            list_index = p.identify_item_in_list(fav, self.drink)
            usual_drink = self.drink[list_index]
            usual = self.getNonBlankInput(f"Same again? {usual_drink.drink_name} ({usual_drink.details}), right? Y/N: ", "Enter a valid response: ")
            if usual.lower() == "y":
                list_index = p.identify_item_in_list(fav, self.drink)
                choice = self.drink[list_index]
            else:
                print_data.print_table(f"{type} Drinks", unique(self.drink, type))
                choice = d.make_drink(self.db, self.drink, type)
        else:
            print_data.print_table(f"{type} Drinks", unique(self.drink, type))
            choice = d.make_drink(db, self.drink, type)  # Add each additional name and drink to the order​
        return choice

    def choose_drink(self, person):
        drink_type = self.get_drink_type()
        if drink_type == "Hot":
            return self.same_again(person.fav_hd_id, drink_type)
        elif drink_type == "Soft":
            return self.same_again(person.fav_sd_id, drink_type)
        elif drink_type == "Alcoholic":
            return self.same_again(person.fav_ad_id, drink_type)


