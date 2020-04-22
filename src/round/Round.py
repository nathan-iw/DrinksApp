import src.drinks.AlcDrink as a
import src.drinks.HotDrink as h
import src.drinks.SoftDrink as s
from app import hot_drink, soft_drink, alc_drink
import src.ETL.persistence as persist


class Round:
    """Class to create a round of drinks, which is created with the name of the round brewer"""

    def __init__(self, brewer):
        self.brewer = brewer
        self.orders = {}  # Dictionary to store key: value pairs of person_name: HotDrink/SoftDrink/AlcoholicDrink

    def add_drinker(self, person):
        """Method to add drinkers (and their drinks) to the round and a drink for the brewer"""
        self.orders[person] = choose_drink(person)



def choose_drink(person):
    choice = None
    drink_type = input("""Select drink type:
                [H] Hot drinks
                [S] Soft drinks
                [A] Alcoholic drinks

                Selection: """).lower()
    if drink_type == "h":
        if person.fav_hd_id is not None:
            usual = input(f"Same again? Y/N: ")
            if usual.lower() == "y":
                choice = person.fav_hd_id
            else:
                person.fav_hd_id = None
        else:
            choice = h.make_hot_drink(hot_drink)  # Add each additional name and drink to the order​
            person.fav_hd_id = choice.id
            persist.update(person.id,"fav_hd_id",person.fav_hd_id)
        return choice
    elif drink_type == "s":
        if person.fav_sd_id is not None:
            usual = input(f"Same again? Y/N: ")
            if usual.lower() == "y":
                choice = person.fav_sd_id
            else:
                person.fav_sd_id = None
        else:
            choice = s.make_soft_drink(soft_drink)  # Add each additional name and drink to the order​
            person.fav_sd_id = choice.id
            persist.update(person.id, "fav_sd_id", person.fav_sd_id)
        return choice
    elif drink_type == "a":
        if person.fav_ad_id is not None:
            usual = input(f"Same again? Y/N: ")
            if usual.lower() == "y":
                choice = person.fav_ad_id
            else:
                person.fav_ad_id = None
        else:
            choice = a.make_alc_drink(alc_drink)  # Add each additional name and drink to the order​
            person.fav_ad_id = choice.id
            persist.update(person.id, "fav_ad_id", person.fav_ad_id)
        return choice