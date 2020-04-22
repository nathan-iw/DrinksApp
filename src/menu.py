def show_menu():
    menu_text = """                
Select an option from the list:
    [G]et all people
    [A]dd a person
    [D]rinks menu
    [R]ound builder
    [V]iew round
    [E]xit
"""
    print(menu_text)
    return input("Enter selection: ")

def return_to_menu():
    input("Press ENTER to return to main menu")
    return
