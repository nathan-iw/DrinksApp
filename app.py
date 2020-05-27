import src.tools.menu as menu
import src.tools.print_data as print_data
import src.ETL.Person as p
from src.ETL.persistence import Database
import src.ETL.extract as e
import src.ETL.transform as t
import src.ETL.search_table as f
import src.round.Round as Round
import src.drinks.Drink as Drink
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
    while True:
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


def clearScreen():
    os.system("clear")


class App():
    def __init__(self, db):
        self.db = db

    def createRound(self, list):
        brewer_id = input("Enter the ID of the brewer: ") # NOT RECOGNISED?
        if brewer_id == "":
            self.returnToMenu()
        try:
            brewer_id = int(brewer_id)
            select_id = p.identify_item_in_list(brewer_id, list)
        except:
            print("ID not found. Round aborted.")
            time.sleep(2)
            self.root()
        new_round = Round.Round(self.db, list[select_id], drink)
        print(f"What you having {list[select_id].first_name}?")
        brewer = list[select_id]
        new_round.add_drinker(brewer)
        list.remove(brewer)
        while True:
            clearScreen()
            print_data.print_table("Possible Drinkers", list)
            person_id = input("Enter the ID of the next person in the round: \nReturn to close round.")
            if person_id == "":
                clearScreen()
                print_data.print_dictionary("Round", new_round.orders)
                db.save_round(brewer, new_round.orders)
                menu.return_to_menu()
                clearScreen()
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

    def returnToMenu(self):
            print("Returning to main menu")
            time.sleep(1)
            self.root()

    def unique(self, drink_list, drink_type):
        # intialize a null list
        unique_list = []
        # traverse for all elements
        for drinks in drink_list:
            # check if exists in unique_list or not
            if drinks.drinkType == drink_type and drinks.drink_name not in unique_list:
                unique_list.append(f"{drinks.drink_name}")
        return unique_list

    def getInput(self, text):
        return input(text)

    def drinkType(self):
        drink_type = self.getInput("""
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
            self.drinkType()

    def root(self):

        while True:

            clearScreen()
            print(welcome())
            selection = menu.main_menu()
            if selection.lower() == "p":
                clearScreen()
                selection = menu.people_menu()
                if selection.lower() == "v":
                    clearScreen()
                    print_data.print_table("people", person)  # test
                elif selection.lower() == "s":
                    clearScreen()
                    print_data.print_table("people", person)
                    search_term = getNonBlankInput("Enter search term: \nor [Q]uit: ","Enter a valid name: ")
                    if search_term == "q":
                        self.returnToMenu()
                    else:
                        results = f.search_person(search_term,person)
                        print_data.print_table("results",results)
                elif selection.lower() == "a":
                    clearScreen()
                    first_name = getNonBlankInput("Enter first name  \nor [Q]uit: ", "Enter a valid name: ")
                    if first_name == "q":
                        self.returnToMenu()
                    else:
                        last_name = getNonBlankInput("Enter last name \nor [Q]uit: ", "Enter a valid name: ")
                        if last_name == "q":
                            self.returnToMenu()
                        else:
                            age = getValidIntegerInput("Enter age \nor [Q]uit: ", "Enter a valid age: ")
                            if age == "q":
                                self.returnToMenu()
                            p.add_person(db, person, first_name, last_name, age)
                elif selection.lower() == "d":
                    clearScreen()
                    print_data.print_table("people", person)
                    del_id = getValidIntegerInput("Which ID do you wish to delete?  \nor [Q]uit: ","Enter a valid ID from the list: ")
                    if del_id == "q":
                        self.returnToMenu()
                    else:
                        try:
                            index = p.identify_item_in_list(del_id, person)
                            person.pop(index)
                            db.delete_person(del_id)  # fix
                        except:
                            print("ID not found in the database.")
                            self.returnToMenu()
                elif selection.lower() =="e":
                    clearScreen()
                    self.root()
                else:
                    print("Invalid selection returning to main menu")
                menu.return_to_menu()  # test
                clearScreen()
            elif selection.lower() == "d":
                clearScreen()
                selection = menu.drinks_menu()
                if selection.lower() == "v":
                    clearScreen()
                    # load drink menus
                    # print drink menus
                    print_data.print_table("Hot Drinks", self.unique(drink, "Hot"))  # test
                    print_data.print_table("Soft Drinks", self.unique(drink, "Soft"))  # test
                    print_data.print_table("Alcoholic Drinks", self.unique(drink, "Alcoholic"))  # test
                elif selection.lower() == "a":
                    clearScreen()
                    drink_type = self.drinkType()
                    print_data.print_table(f"{drink_type} Drinks", self.unique(drink, drink_type))
                    Drink.make_drink(db, drink, drink_type)
                elif selection.lower() == "d":
                    clearScreen()
                    drink_type = self.drinkType()
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
                    clearScreen()
                    self.root()
                else:
                    print("Invalid selection returning to main menu")
                menu.return_to_menu()  # test
                clearScreen()

            elif selection.lower() == "r":
                clearScreen()
                selection = menu.rounds_menu()
                if selection.lower() == "v":
                    orders = db.load_all("round")
                    print_data.print_dictionary("Latest Round", orders)
                elif selection.lower() == "s":
                    clearScreen()
                    selection = menu.round_search_menu()
                    if selection == "1":
                        print_data.print_table("people", person)
                        person_id = getValidIntegerInput("Enter person ID \nor [Q]uit: ", "Enter a valid ID from the list: ")
                        if person_id == "q":
                            self.returnToMenu()
                        else:
                            clearScreen()
                            select_id = p.identify_item_in_list(int(person_id), person)
                            person_object = person[select_id]
                            search_results = Database.search_rounds(db,f"{person_object.first_name} {person_object.last_name}",None)
                            print_data.print_dictionary("Search Results", search_results)
                    elif selection == "2":
                        date = getValidDateInput("Enter search date (YYYY-MM-DD) \nor [Q]uit: ", "Invalid date entry.\nEnter search date (YYYY-MM-DD): ")
                        if date == "q":
                            self.returnToMenu()
                        else:
                            search_results = Database.search_rounds(db,None,date)
                            print_data.print_dictionary("Search Results", search_results)
                    # elif selection == 3:
                    #     print("Under construction")
                    else:
                        print("Invalid selection returning to main menu")
                elif selection.lower() == "c":
                    clearScreen()
                    round_options = person
                    print_data.print_table("Possible Drinkers", round_options)
                    self.createRound(round_options)
                    menu.return_to_menu()
                elif selection.lower() =="e":
                    clearScreen()
                    self.root()
                else:
                    print("Invalid selection returning to main menu")
                menu.return_to_menu()  # test
                clearScreen()

            elif selection.lower() == "e":
                db.update_favourites()
                clearScreen()
                print(bye_mate())
                time.sleep(1)
                clearScreen()
                exit()
            else:
                print("Invalid selection. Have another go...")
                self.returnToMenu()


if __name__ == "__main__":
    clearScreen()
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
