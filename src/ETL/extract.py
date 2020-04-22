### EXTRACT ###

import csv 

def csv_load(file):
    person_list = []
    try:
        with open(file,"r") as csv_file:
            rows = csv.reader(csv_file, quoting=csv.QUOTE_ALL, skipinitialspace=True)
            for row in rows:
                person_list.append(row)
        return person_list
    except Exception as error:
        print(f" error {error}")


if __name__== "__main__":
    run=input("Do you really want to run this big file? Y/N: ")
    if run.lower() == "y":
        csv_load("customer.csv")
    else:
        exit()


