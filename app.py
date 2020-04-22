import src.menu as menu
import src.print_data as print_data
import src.ETL.Person as p
from src.ETL.persistence import Database
import src.ETL.extract as e
import src.ETL.transform as t
import src.round.Round as r
import os

# load data
person = []
hot_drink = []
soft_drink = []
alc_drink = []
orders = {}

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
        select_id = p.identify_person(brewer_id, list)
        new_round = r.Round(list[select_id], hot_drink, soft_drink, alc_drink)
        print(f"What you having {list[select_id].first_name}?")
        new_round.add_drinker(list[select_id])
        list.remove(list[select_id])
        while True:
            print_data.print_table("Possible Drinkers",list)
            person_id = input("Who else is in the round? ")
            if person_id == "":
                print(new_round.orders)
                self.root()
            person_id = int(person_id)
            select_id = p.identify_person(person_id, list)
            print(f"What you having {list[select_id].first_name}?")
            new_round.add_drinker(list[select_id])
            list.remove(list[select_id])
            print(new_round.orders)

    def unique(self, drink_list):
        # intilize a null list
        unique_list = []

        # traverse for all elements
        for i in drink_list:
            # check if exists in unique_list or not
            if i.drink_name not in unique_list:
                unique_list.append(i.drink_name)
        return unique_list

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
                choice = h.make_hot_drink(hot_drink)  # Add each additional name and drink to the order​
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
                choice = s.make_soft_drink(soft_drink)  # Add each additional name and drink to the order​
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
                choice = a.make_alc_drink(alc_drink)  # Add each additional name and drink to the order​
                chooser.fav_ad_id = choice.id
                db.update(chooser.id, "fav_ad_id", chooser.fav_ad_id)
            return choice

    def root(self):
        while True:

            selection = menu.show_menu()
            if selection.lower() == "g":
                clear_screen()
                print_data.print_table("people", person)  # test
                menu.return_to_menu()  # test
            elif selection.lower() == "a":
                print_data.print_table("people", person)  # test
                p.add_person(person)
            elif selection.lower() == "d":
                # load drink menus
                #print drink menus
                print_data.print_table("Hot Drinks", self.unique(hot_drink))  # test
                print_data.print_table("Soft Drinks", self.unique(soft_drink))  # test
                print_data.print_table("Alcoholic Drinks", self.unique(alc_drink))  # test
                menu.return_to_menu()
            elif selection.lower() == "v":
                print(orders)
                menu.return_to_menu()
            elif selection.lower() == "r":
                clear_screen()
                round_options = person
                print_data.print_table("Possible Drinkers", round_options)
                self.create_round(round_options) # test - challenge
                menu.return_to_menu()
            elif selection.lower() == "e":
                if input("Do you want to save your drink additions? [Y/N] ").lower == "y":
                    # # save drinks(hot)
                    # persist.save(hot_drink,"hot_drink")
                    # # save drinks(soft)
                    # persist.save(soft_drink,"soft_drink")
                    # # save drinks(alc)
                    # persist.save(alc_drink,"alc_drink")
                    # # save round
                    exit()
                else:
                    exit()
            elif selection.lower() == "data":
                self.save_csv_customers("customers.csv")





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
