import csv


def save_list(filepath, items):
    try:
        with open(filepath, "w") as csvfile:
            for item in items:
                csvfile.write(item + "\n")
    except Exception as error:
        print(error)


def save_dictionary(filepath, dictionary):
    try:
        with open(filepath, "w") as csvfile:
            csv_writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
            for key, value in dictionary.items():
                csv_writer.writerow([key, value])
    except Exception as error:
        print(error)


