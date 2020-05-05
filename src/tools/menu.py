def main_menu():
    menu_text = """
Welcome to BrewHaHa©. 
Sit down.
Take a load off.
Let's get you a drink.
                   
                
Select an option from the list:
    [P]eople
    [D]rinks
    [R]ounds
    [E]xit
"""
    print(menu_text)
    return input("Enter selection: ")

def return_to_menu():
    input("Press ENTER to return to main menu")
    return

def people_menu():
    menu_text = """ 
    Select an option from the list:
        [V]iew full people list
        [S]earch people list
        [A]dd a person to the list
        [D]elete a person from the list
        [E]xit
    """
    print(menu_text)
    return input("Enter selection: ")

def drinks_menu():
    menu_text = """                
    Select an option from the list:
        [V]iew full drinks list
        [A]dd a drink
        [D]elete a drink
        [E]xit
    """
    print(menu_text)
    return input("Enter selection: ")

def rounds_menu():
    menu_text = """                
    Select an option from the list:
        [V]iew latest round
        [S]earch rounds
        [C]reate Round
        [E]xit
    """
    print(menu_text)
    return input("Enter selection: ")

def round_search_menu():
    menu_text = """                
    Select an option from the list:
        [1] Search rounds by person
        [2] Search rounds by date
        [3] Search rounds by person and date [UNDER CONSTRUCTION]
        [E]xit
    """
    print(menu_text)
    return input("Enter selection: ")