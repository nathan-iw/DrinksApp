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

