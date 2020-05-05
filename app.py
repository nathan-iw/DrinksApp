import src.tools.menu as menu
import src.tools.print_data as print_data
import src.ETL.Person as p
from src.ETL.persistence import Database
import src.ETL.extract as e
import src.ETL.transform as t
import src.ETL.search_table as f
import src.round.Round as r
import src.drinks.Drink as d
import os
import time
import datetime

# load data
person = []
drink = []
orders = {}

def subliminal():
    heybuddy = """
                          ___________
                         |     /\    |   
                         |    /  \   |   
                         |   /,--.\  |   
                         |  /< () >\ |   
                         | /__`--'__\|  
                         |___________| 
                               ||
                        (\__/) || 
                        (•ㅅ•) || 
                        / 　 づ
    """
    return heybuddy

def welcome():
    heybuddy = """
                         ___________
                        | YOU       |
                        | LOOK LIKE |
                        | YOU COULD |
                        | USE A     |
                        | DRINK     |
                        |___________| 
                               ||
                        (\__/) || 
                        (•ㅅ•) || 
                        / 　 づ
    """
    return heybuddy

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

def getNonBlankInput(message, error_message):

    x = input(message)
    while len(x.strip()) == 0:
        x = input(error_message)

    return x

def getValidIntegerInput(message, error_message):

    msg = message
    while(True):
        try:
            x = getNonBlankInput(msg, error_message)
            if x == "q" or "Q":
                return x.lower()
            else:
                int(x)
            break
        except ValueError:
            msg = error_message
    return x


def getValidDateInput(message, error_message):

    msg = message
    while(True):
        try:
            x = (input(msg))
            if x == "q" or "Q":
                return x.lower()
            else:
                year, month, day = map(int, x.split('-'))
                date1 = datetime.date(year, month, day)
                if date1 > datetime.date.today():
                    future_message = "Date is in the future.\nEnter search date (YYYY-MM-DD): "
                    x = getValidDateInput(future_message,error_message)
            break
        except ValueError:
            msg = f"{error_message}"
    return x

def clear_screen():
    os.system("clear")

class App():
    def __init__(self, db):
        self.db = db

    def create_round(self, list):
        brewer_id = input("Enter the ID of the brewer: ") # NOT RECOGNISED?
        if brewer_id == "":
            self.return_to_menu()
        try:
            brewer_id = int(brewer_id)
            select_id = p.identify_item_in_list(brewer_id, list)
        except:
            print("ID not found. Round aborted.")
            time.sleep(2)
            self.root()
        new_round = r.Round(self.db, list[select_id], drink)
        print(f"What you having {list[select_id].first_name}?")
        brewer = list[select_id]
        new_round.add_drinker(brewer)
        list.remove(brewer)
        while True:
            clear_screen()
            print_data.print_table("Possible Drinkers", list)
            person_id = input("Enter the ID of the next person in the round: \nReturn to close round.")
            if person_id == "":
                clear_screen()
                print_data.print_dictionary("Round", new_round.orders)
                db.save_round(brewer, new_round.orders)
                menu.return_to_menu()
                clear_screen()
                self.root()
            try:
                person_id = int(person_id)
                select_id = p.identify_item_in_list(person_id, list)
            except:
                print("ID not found. Round aborted.")
                time.sleep(2)
                self.root()
            print(f"What you having {list[select_id].first_name}?")
            new_round.add_drinker(list[select_id])
            list.remove(list[select_id])



    def return_to_menu(self):
            print("Returning to main menu")
            time.sleep(1)
            self.root()

    def unique(self, drink_list, drink_type):
        # intialize a null list
        unique_list = []

        # traverse for all elements
        for i in drink_list:
            # check if exists in unique_list or not
            if i.drink_type == drink_type and i.drink_name not in unique_list:
                unique_list.append(f"{i.drink_name}")
        return unique_list

    def get_input(self, text):
        return input(text)

    def drink_type(self):
        drink_type = self.get_input("""
        Select drink type:
            [H]ot drinks
            [S]oft drinks
            [A]lcoholic drinks
                Selection: """).lower()
        if drink_type == "h":
            return "Hot"
        elif drink_type == "s":
            return "Soft"
        elif drink_type == "a":
            return "Alcoholic"
        else:
            print("Come again")
            self.drink_type()


    #
    # def save_csv_customers(self, db, csv_file):
    #     dirty_people = e.csv_load(csv_file)
    #     clean_people = t.process_people(dirty_people)
    #     db.save_to_db(clean_people)
    #
    # def same_again(self, fav, type):
    #     if fav is not None:
    #         usual = input(f"Same again? Y/N: ")
    #         if usual.lower() == "y":
    #             choice = fav
    #     else:
    #         choice = d.make_drink(db, drink, type)  # Add each additional name and drink to the order​
    #     return choice
    #
    # def choose_drink(self, chooser):
    #     print(chooser)
    #     drink_type = self.drink_type()
    #     print(drink_type)
    #     if drink_type == "Hot":
    #         return self.same_again(chooser.fav_hd_id, drink_type)
    #     elif drink_type == "Soft":
    #         return self.same_again(chooser.fav_sd_id, drink_type)
    #     elif drink_type == "Alcoholic":
    #         return self.same_again(chooser.fav_ad_id, drink_type)

    def root(self):

        while True:

            clear_screen()
            print(welcome())
            selection = menu.main_menu()
            if selection.lower() == "p":
                clear_screen()
                selection = menu.people_menu()
                if selection.lower() == "v":
                    clear_screen()
                    print_data.print_table("people", person)  # test
                elif selection.lower() == "s":
                    clear_screen()
                    print_data.print_table("people", person)
                    search_term = getNonBlankInput("Enter search term: \nor [Q]uit: ","Enter a valid name: ")
                    if search_term == "q":
                        self.return_to_menu()
                    else:
                        results = f.search_person(search_term,person)
                        print_data.print_table("results",results)
                elif selection.lower() == "a":
                    clear_screen()
                    first_name = getNonBlankInput("Enter first name  \nor [Q]uit: ", "Enter a valid name: ")
                    if first_name == "q":
                        self.return_to_menu()
                    else:
                        last_name = getNonBlankInput("Enter last name \nor [Q]uit: ", "Enter a valid name: ")
                        if last_name == "q":
                            self.return_to_menu()
                        else:
                            age = getValidIntegerInput("Enter age \nor [Q]uit: ", "Enter a valid age: ")
                            if age == "q":
                                self.return_to_menu()
                            p.add_person(db, person, first_name, last_name, age)
                elif selection.lower() == "d":
                    clear_screen()
                    print_data.print_table("people", person)
                    del_id = getValidIntegerInput("Which ID do you wish to delete?  \nor [Q]uit: ","Enter a valid ID from the list: ")
                    if del_id == "q":
                        self.return_to_menu()
                    else:
                        try:
                            index = p.identify_item_in_list(del_id, person)
                            person.pop(index)
                            db.delete_person(del_id)  # fix
                        except:
                            print("ID not found in the database.")
                            self.return_to_menu()
                elif selection.lower() =="e":
                    clear_screen()
                    self.root()
                else:
                    print("Invalid selection returning to main menu")
                menu.return_to_menu()  # test
                clear_screen()
            elif selection.lower() == "d":
                clear_screen()
                selection = menu.drinks_menu()
                if selection.lower() == "v":
                    clear_screen()
                    # load drink menus
                    # print drink menus
                    print_data.print_table("Hot Drinks", self.unique(drink, "Hot"))  # test
                    print_data.print_table("Soft Drinks", self.unique(drink, "Soft"))  # test
                    print_data.print_table("Alcoholic Drinks", self.unique(drink, "Alcoholic"))  # test
                elif selection.lower() == "a":
                    clear_screen()
                    drink_type = self.drink_type()
                    print_data.print_table(f"{drink_type} Drinks", self.unique(drink, drink_type))
                    d.make_drink(db, drink, drink_type)
                elif selection.lower() == "d":
                    clear_screen()
                    drink_type = self.drink_type()
                    print_data.print_table(f"{drink_type} Drinks", self.unique(drink, drink_type))
                    del_drink = getNonBlankInput("Which drink do you wish to delete? \nor [Q]uit ", "Enter a valid drink name: ")
                    try:
                        for item in drink:
                            if item.drink_name == del_drink:
                                drink.remove(item)
                        db.delete_drink("drink", del_drink)
                    except:
                        print("Invalid selection returning to main menu")
                elif selection.lower() =="e":
                    clear_screen()
                    self.root()
                else:
                    print("Invalid selection returning to main menu")
                menu.return_to_menu()  # test
                clear_screen()

            elif selection.lower() == "r":
                clear_screen()
                selection = menu.rounds_menu()
                if selection.lower() == "v":
                    orders = db.load_all("round")
                    print_data.print_dictionary("Latest Round", orders)
                elif selection.lower() == "s":
                    clear_screen()
                    selection = menu.round_search_menu()
                    if selection == "1":
                        print_data.print_table("people", person)
                        person_id = getValidIntegerInput("Enter person ID \nor [Q]uit: ", "Enter a valid ID from the list: ")
                        if person_id == "q":
                            self.return_to_menu()
                        else:
                            clear_screen()
                            select_id = p.identify_item_in_list(int(person_id), person)
                            person_object = person[select_id]
                            search_results = Database.search_rounds(db,f"{person_object.first_name} {person_object.last_name}",None)
                            print_data.print_dictionary("Search Results", search_results)
                    elif selection == "2":
                        date = getValidDateInput("Enter search date (YYYY-MM-DD) \nor [Q]uit: ", "Invalid date entry.\nEnter search date (YYYY-MM-DD): ")
                        if date == "q":
                            self.return_to_menu()
                        else:
                            search_results = Database.search_rounds(db,None,date)
                            print_data.print_dictionary("Search Results", search_results)
                    # elif selection == 3:
                    #     print("Under construction")
                    else:
                        print("Invalid selection returning to main menu")
                elif selection.lower() == "c":
                    clear_screen()
                    round_options = person
                    print_data.print_table("Possible Drinkers", round_options)
                    self.create_round(round_options)
                    menu.return_to_menu()
                elif selection.lower() =="e":
                    clear_screen()
                    self.root()
                else:
                    print("Invalid selection returning to main menu")

                menu.return_to_menu()  # test
                clear_screen()

            elif selection.lower() == "e":
                db.update_favourites()
                clear_screen()
                print(bye_mate())
                time.sleep(1)
                clear_screen()
                exit()
            else:
                print("Invalid selection. Have another go...")
                self.return_to_menu()


if __name__ == "__main__":
    clear_screen()
    db = Database()
    app = App(db)
    # load people
    person = db.load_all("person")
    # load drinks(hot)
    drink = db.load_all("drink")
    # load orders
    orders = db.load_all("round")
    # print subliminal message
    print(subliminal())
    time.sleep(0.3)
    # load round
    app.root()
