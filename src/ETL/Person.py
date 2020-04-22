import src.ETL.persistence as persist

class Person:
    def __init__(self, first_name, last_name, age, id=None):  # fav_hd/ fav_sd/ fav_ad
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.fav_hd_id = None
        self.fav_sd_id = None
        self.fav_ad_id = None

    def get_info(self):
        return f"#{self.id} {self.first_name} {self.last_name}   -   {self.age}"


def add_person(person):
    first_name = input("First name: ")
    last_name = input("Last name: ")
    age = int(input("Age: "))
    try:
        new_id = persist.save_person(first_name,last_name,age)
        new_person = Person(first_name, last_name, int(age), int(new_id))
        person.append(new_person)
        return new_person

    except Exception:
        print("Duplicate entry in table")


def identify_person(search_id, person_list):
    try:
        for i in range(len(person_list)):
            if person_list[i].id == search_id:
                return i
    except Exception as error:
        print(error)





