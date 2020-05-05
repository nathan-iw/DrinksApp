

class Person:
    def __init__(self, first_name, last_name, age, fav_hd_id, fav_sd_id, fav_ad_id, id=None):  # fav_hd/ fav_sd/ fav_ad
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.fav_hd_id = fav_hd_id
        self.fav_sd_id = fav_sd_id
        self.fav_ad_id = fav_ad_id

    def get_info(self):
        return f"#{self.id} {self.first_name} {self.last_name}   -   {self.age} years old"

def add_person(db, person, first_name, last_name, age):
    try:
        new_id = db.save_person(first_name, last_name, age)
        new_person = Person(first_name, last_name, int(age), None, None, None, int(new_id))
        person.append(new_person)
        print("Person added successfully")
        return new_person

    except Exception as err:
        print(err)


def identify_item_in_list(search_id, search_list):
    try:
        for i in range(len(search_list)):
            if search_list[i].id == int(search_id):
                return i
    except Exception as error:
        print(error)




