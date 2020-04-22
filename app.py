import src.menu as menu
import src.print_data as print_data
import src.ETL.Person as p
import src.ETL.persistence as persist
import src.round.Round as r
import os


def clear_screen():
    os.system("clear")


def create_round(list):
    brewer_id = input("Whose round is it? ")
    if brewer_id == "":
        root()
    brewer_id = int(brewer_id)
    select_id = p.identify_person(brewer_id, list)
    new_round = r.Round(list[select_id])
    print(f"What you having {list[select_id].first_name}?")
    new_round.add_drinker(list[select_id])
    list.remove(list[select_id])
    while True:
        print_data.print_table("Possible Drinkers",list)
        person_id = input("Who else is in the round? ")
        if person_id == "":
            print(new_round.orders)
            root()
        person_id = int(person_id)
        select_id = p.identify_person(person_id, list)
        print(f"What you having {list[select_id].first_name}?")
        new_round.add_drinker(list[select_id])
        list.remove(list[select_id])
        print(new_round.orders)

def unique(drink_list):
    # intilize a null list
    unique_list = []

    # traverse for all elements
    for i in drink_list:
        # check if exists in unique_list or not
        if i.drink_name not in unique_list:
            unique_list.append(i.drink_name)
    return unique_list

# load data
person = []
hot_drink = []
soft_drink = []
alc_drink = []
orders = {}


def root():
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
            print_data.print_table("Hot Drinks", unique(hot_drink))  # test
            print_data.print_table("Soft Drinks", unique(soft_drink))  # test
            print_data.print_table("Alcoholic Drinks", unique(alc_drink))  # test
            menu.return_to_menu()
        elif selection.lower() == "v":
            print(orders)
            menu.return_to_menu()
        elif selection.lower() == "r":
            clear_screen()
            round_options = person
            print_data.print_table("Possible Drinkers", round_options)
            create_round(round_options) # test - challenge
            menu.return_to_menu()
        elif selection.lower() == "e":
            if input("Do you want to save your drink additions? [Y/N] ").lower == "y":
                # save drinks(hot)
                persist.save(hot_drink,"hot_drink")
                # save drinks(soft)
                persist.save(soft_drink,"soft_drink")
                # save drinks(alc)
                persist.save(alc_drink,"alc_drink")
                # save round

                exit()
            else:
                exit()

if __name__ == "__main__":
    # load people
    person = persist.load_all("person")
    # load drinks(hot)
    hot_drink = persist.load_all("hot_drink")
    # load drinks(soft)
    soft_drink = persist.load_all("soft_drink")
    # load drinks(alc)
    alc_drink = persist.load_all("alc_drink")
    # load round
    root()
