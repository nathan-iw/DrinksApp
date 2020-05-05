import sys


# function to print title in capital letters
def print_header(title):
    print(f"| {title.upper()}")
    # print(f"| {title.upper()}{line_adjustment(title)}")


# prints table outline
def print_outline():
    print(f"+{'=' * 20}+")


# prints table header structure
def print_table_header(title):
    print_outline()
    print_header(title)
    print_outline()


# Adjusts formatting to accommodate longest word in data (does not work for added names/drinks)
def line_adjustment(word):
    adjustment = " "* (30 - len(word)) + "|"
    return adjustment


# prints rows in a table of objects
def print_rows(rows):
    if rows == []:
        print("| Move along. Nothing to see here. ")
    else:
        for row in rows:
            try:
                print(f"| {row.get_info()}")
            except AttributeError:
                print(f"| {row}")
            except:
                print("Unexpected error: ", sys.exc_info()[0])
                raise



# prints outline, header and rows. Building the table
def print_table(header, rows):
    print_table_header(header)
    print_rows(rows)
    print_outline()

def print_dictionary(header, dictionary):
    print_table_header(header)
    for key, value in dictionary.items():
        try:
            print(f"| {key.first_name} {key.last_name} -  {value.drink_name} {value.details}")
        except:
            print(f" {key} -  {value}")
    print_outline()
