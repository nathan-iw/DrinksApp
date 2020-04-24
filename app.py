import src.tools.menu as menu
import src.tools.print_data as print_data
import src.ETL.Person as p
from src.ETL.persistence import Database
import src.ETL.extract as e
import src.ETL.transform as t
import src.ETL.search_table as f
import src.round.Round as r
import src.drinks.AlcDrink as a
import src.drinks.HotDrink as h
import src.drinks.SoftDrink as s
import os

# load data
person = []
hot_drink = []
soft_drink = []
alc_drink = []
orders = {}

def bye_mate():
    ciao = """
$$$$$$$$$$$$$$$$$$$$$$$$$
$$$$$$$$$$$$$$$$$$$$$$$$$
$$$$$'`$adiosamigo$'`$$$$
$$$$$$  $$$$$$$$$$$  $$$$
$$$$$$$  '$/ `/ `$' .$$$$
$$$$$$$$. i  i  /! .$$$$$
$$$$$$$$$.--'--'   $$$$$$
$$^^$$$$$'        J$$$$$$
$$$   ~""   `.   .$$$$$$$
$$$$$e,      ;  .$$$$$$$$
$$$$$$$$$$$.'   $$$$$$$$$
$$$$$$$$$$$$.    $$$$$$$$
$$$$$$$$$$$$$    $$$$$$$$"""
    return ciao

def clear_screen():
    os.system("clear")

class App():
    def __init__(self, db):
        self.db = db

    def create_round(self, list):
        brewer_id = input("Whose round is it? ")
        if brewer_id == "":
            self.root()
        brewer_id = int(brewer_id)
        select_id = p.identify_item_in_list(brewer_id, list)
        new_round = r.Round(self.db, list[select_id], hot_drink, soft_drink, alc_drink)
        print(f"What you having {list[select_id].first_name}?")
        new_round.add_drinker(list[select_id])
        list.remove(list[select_id])
        while True:
            print_data.print_table("Possible Drinkers", list)
            person_id = input("Who else is in the round? ")
            if person_id == "":
                print(new_round.orders)
                self.root()
            person_id = int(person_id)
            select_id = p.identify_item_in_list(person_id, list)
            print(f"What you having {list[select_id].first_name}?")
            new_round.add_drinker(list[select_id])
            list.remove(list[select_id])
            print(new_round.orders)

    def unique(self, drink_list):
        # intialize a null list
        unique_list = []

        # traverse for all elements
        for i in drink_list:
            # check if exists in unique_list or not
            if i.drink_name not in unique_list:
                unique_list.append(i.drink_name)
        return unique_list

    def drink_type(self):
        drink_type = input("""
        Select drink type:
            [H] Hot drinks
            [S] Soft drinks
            [A] Alcoholic drinks
                Selection: """).lower()
        return drink_type

    def save_csv_customers(self, db, csv_file):
        dirty_people = e.csv_load(csv_file)
        clean_people = t.process_people(dirty_people)
        db.save_to_db(clean_people)

    def choose_drink(self, chooser):
        choice = None
        drink_type = input("""Select drink type:
                    [H] Hot drinks
                    [S] Soft drinks
                    [A] Alcoholic drinks

                    Selection: """).lower()
        if drink_type == "h":
            if chooser.fav_hd_id is not None:
                usual = input(f"Same again? Y/N: ")
                if usual.lower() == "y":
                    choice = chooser.fav_hd_id
                else:
                    chooser.fav_hd_id = None
            else:
                choice = h.make_hot_drink(db, hot_drink)  # Add each additional name and drink to the order​
                chooser.fav_hd_id = choice.id
                db.update(chooser.id, "fav_hd_id", chooser.fav_hd_id)
            return choice
        elif drink_type == "s":
            if chooser.fav_sd_id is not None:
                usual = input(f"Same again? Y/N: ")
                if usual.lower() == "y":
                    choice = chooser.fav_sd_id
                else:
                    chooser.fav_sd_id = None
            else:
                choice = s.make_soft_drink(db, soft_drink)  # Add each additional name and drink to the order​
                chooser.fav_sd_id = choice.id
                db.update(chooser.id, "fav_sd_id", chooser.fav_sd_id)
            return choice
        elif drink_type == "a":
            if chooser.fav_ad_id is not None:
                usual = input(f"Same again? Y/N: ")
                if usual.lower() == "y":
                    choice = chooser.fav_ad_id
                else:
                    chooser.fav_ad_id = None
            else:
                choice = a.make_alc_drink(db, alc_drink)  # Add each additional name and drink to the order​
                chooser.fav_ad_id = choice.id
                db.update(chooser.id, "fav_ad_id", chooser.fav_ad_id)
            return choice

    def root(self):
        while True:

            selection = menu.main_menu()
            if selection.lower() == "p":
                clear_screen()
                selection = menu.people_menu()
                try:
                    if selection.lower() == "v":
                        clear_screen()
                        print_data.print_table("people", person)  # test
                    elif selection.lower() == "s":
                        clear_screen()
                        search_term = input("Enter search term: ")
                        results = f.search_person(search_term,person)
                        print_data.print_table("results",results)
                    elif selection.lower() == "a":
                        clear_screen()
                        first_name = input("First name: ")
                        last_name = input("Last name: ")
                        age = int(input("Age: "))
                        p.add_person(db, person, first_name, last_name, age)
                    elif selection.lower() == "d":
                        clear_screen()
                        print_data.print_table("people", person)
                        del_id = input("Which ID do you wish to delete? ")
                        index = p.identify_item_in_list(del_id, person)
                        person.remove(index)
                        db.delete_person(del_id)  # fix
                    elif selection.lower() =="e":
                        clear_screen()
                        self.root()
                except ValueError:
                        print("Come again?")
                menu.return_to_menu()  # test
                clear_screen()

            elif selection.lower() == "d":
                clear_screen()
                selection = menu.drinks_menu()
                try:
                    if selection.lower() == "v":
                        clear_screen()
                        # load drink menus
                        # print drink menus
                        print_data.print_table("Hot Drinks", self.unique(hot_drink))  # test
                        print_data.print_table("Soft Drinks", self.unique(soft_drink))  # test
                        print_data.print_table("Alcoholic Drinks", self.unique(alc_drink))  # test
                    elif selection.lower() == "a":
                        drink_type = self.drink_type()
                        if drink_type.lower() == "h":
                            h.make_hot_drink(db,hot_drink)
                        elif drink_type.lower() == "s":
                            s.make_soft_drink(db,soft_drink)
                        elif drink_type.lower() == "a":
                            a.make_alc_drink(db,alc_drink)
                    elif selection.lower() == "d":
                        drink_list = self.drink_type().lower()
                        if drink_list == "h":
                            print_data.print_table("Hot Drinks", self.unique(hot_drink))
                            del_drink = input("Which drink do you wish to delete? ")
                            for drink in hot_drink:
                                if drink.drink_name == del_drink:
                                    hot_drink.remove(drink)
                            db.delete_drink("hot_drink", del_drink)
                        elif drink_list == "s":
                            print_data.print_table("Soft Drinks", self.unique(soft_drink))
                            del_drink = input("Which drink do you wish to delete? ")
                            for drink in soft_drink:
                                if drink.drink_name == del_drink:
                                    soft_drink.remove(drink)
                            db.delete_drink("soft_drink", del_drink)
                        elif drink_list == "a":
                            print_data.print_table("Alcoholic Drinks", self.unique(alc_drink))
                            del_drink = input("Which drink do you wish to delete? ")
                            for drink in alc_drink:
                                if drink.drink_name == del_drink:
                                    alc_drink.remove(drink)
                            db.delete_drink("alc_drink", del_drink)
                    elif selection.lower() =="e":
                        clear_screen()
                        self.root()
                except ValueError:
                        print("Come again?")
                menu.return_to_menu()  # test
                clear_screen()

            elif selection.lower() == "r":
                clear_screen()
                selection = menu.rounds_menu()
                try:
                    if selection.lower() == "v":

                    elif selection.lower() == "s":
                        print("Under construction")
                    elif selection.lower() == "c":
                        clear_screen()
                        round_options = person
                        print_data.print_table("Possible Drinkers", round_options)
                        self.create_round(round_options)

                        menu.return_to_menu()

                    elif selection.lower() =="e":
                        clear_screen()
                        self.root()
                except ValueError:
                        print("Come again?")
                menu.return_to_menu()  # test
                clear_screen()

            elif selection.lower() == "e":
                print(bye_mate())
                exit()


if __name__ == "__main__":
    db = Database()
    app = App(db)
    # load people
    person = db.load_all("person")
    # load drinks(hot)
    hot_drink = db.load_all("hot_drink")
    # load drinks(soft)
    soft_drink = db.load_all("soft_drink")
    # load drinks(alc)
    alc_drink = db.load_all("alc_drink")
    # load round
    app.root()
