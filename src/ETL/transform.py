    ## Transform ###
from datetime import date


title_list = ["miss","ms","mrs","mr","dr"]

def name_breaker(name): # Function to reformat names into the order "title","first name", "last name"
    breaking_name = name.strip().lower().replace(".", "") # Strip away unwanted things e.g leading and trailing spaces, \n etc, formats all to lowercase and replaces any "." with ""
    broken_name = breaking_name.split(" ") # Takes breaking_name and splits where there are " " into seperate values
    last_name = broken_name[-1].title() # looks up the final index (-1) and formats it using "title" which recognises irish and double barrelled names.
    if broken_name[0] in title_list: # if the first value in broken_name is a title from the list above in title_list then continue
        title = broken_name[0].capitalize() # defining the first value as "title" and capitalising it
        first_name = broken_name[1].capitalize() # the remainin value is then defined as the "first_name"
    else:
        title = None # if there is no title then None
        first_name = broken_name[0].capitalize() #  the remainin value is then defined as the "first_name"
    return (title, first_name, last_name) # Either way, return the define values: title, first_name, last_name

# Name,DOB,Address,email,billing address,ccn
def process_people(data):
    people_list=[]
    for row in data:
        if len(row) == 0 or row[0] == "Name": # check for empty rows or rows indicating table headers 
            continue # if the above is the case skips that row 
        try:
            age = age_gen(row[1]) # try to generate an age from the DOB 
        except ValueError: # if that fails gives a value error
            continue # then skips that row
        title, first_name, last_name = name_breaker(row[0]) # assigning the values in the tuple
        person_tuple = (first_name, last_name, age) # making a new tuple with the age and masked ccn
        people_list.append(person_tuple) # appending aforementioned tuple to the people_list
    return people_list # returns list


def age_gen(dob): # generate an age from a dob
    days_in_year = 365.2425 # defines how many days are a year including leap years 
    y, m, d = int(dob[:4]), int(dob[5:7]), int(dob[-2:]) # essentially splitting the dob according to the index and defining the y, m, d varibles.
    birth_date = date(y, m, d) # defining the variable "birth_date" in the "date" format using the y, m, d varables from above.
    age = int((date.today() - birth_date).days / days_in_year) # Defining variable age as: todays date subtract the birth_date, format this in number of days and divide by the days in the year. 
    return age # returns age in years

