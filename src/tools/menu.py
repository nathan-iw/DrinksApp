def main_menu():
    menu_text = """                
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
    def people_menu():
        menu_text = """                
        Select an option from the list:
            [V]iew last round
            [S]earch rounds - Under development
            [C]reate Round
            [E]xit
        """
        print(menu_text)
        return input("Enter selection: ")
