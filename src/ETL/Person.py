from src.ETL.persistence import Database

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


def add_person(db, person, first_name, last_name, age):
    try:
        new_id = db.save_person(first_name, last_name, age)
        new_person = Person(first_name, last_name, int(age), int(new_id))
        person.append(new_person)
        print("Person added successfully")
        return new_person

    except Exception as err:
        print(err)


def identify_item_in_list(search_id, search_list):
    try:
        for i in range(len(search_list)):
            if search_list[i].id == search_id:
                return i
    except Exception as error:
        print(error)




