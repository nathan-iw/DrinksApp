import pymysql
from os import environ
from datetime import datetime
from src.drinks import Drink as d
from src.ETL import Person as p

class Database():

    def get_connection(self):  # function to get the connection string using: pymysql.connect(host, username, password, database)
        db_connection = pymysql.connect(
            environ.get("DB_HOST"),  # host
            environ.get("DB_USER"),  # username
            environ.get("DB_PW"),  # password
            environ.get("DB_NAME")  # database
        )
        return db_connection


    def save_to_db(self, people):
        connection = self.get_connection()
        cursor = connection.cursor()
        for person_tuple in people:
            cursor.execute(
            """INSERT INTO person (first_name, last_name, age) 
                    VALUES (%s, %s, %s)""", person_tuple)
        connection.commit()
        cursor.close()
        connection.close()

    def save_round(self, brewer, dictionary):
        connection = self.get_connection()
        cursor = connection.cursor()
        date=datetime.today().strftime('%Y-%m-%d')
        try:
            for key, value in dictionary.items():
                round_tuple = (f"{brewer.first_name} {brewer.last_name}", f"{key.first_name} {key.last_name}",
                               f"{value.drink_name} {value.details}", value.price, date, value.id,
                               value.drinkType)
                cursor.execute(
                """INSERT INTO round (brewer, drinker, drink, price, date, drink_id, drink_type) 
                VALUES (%s, %s, %s, %s, %s, %s, %s)""", round_tuple)
        except Exception as err:
            print(err)
        connection.commit()
        cursor.close()
        connection.close()

    def load_all(self, table):  # function to run a select query like `SELECT * FROM players`
        connection = self.get_connection()
        cursor = connection.cursor()
        table_list = []
        if table == "person":
            cursor.execute(f"SELECT * FROM {table} ORDER BY last_name")
        elif table == "drink":
            cursor.execute(f"SELECT * FROM {table} ORDER BY drink_name")
        elif table == "round":
            table_list = {}
            cursor.execute("SELECT brewer, date FROM round ORDER BY date DESC LIMIT 1")
            row = cursor.fetchone()
            date = row[1]
            brewer = row[0]
            cursor.execute(f"SELECT * FROM round WHERE date='{date}' AND brewer='{brewer}' ORDER BY date")
        while True:
            row = cursor.fetchone()
            if row == None:
                break
            elif table == "person":
                item = p.Person(row[1], row[2], row[3], row[4], row[5], row[6], row[0])
                table_list.append(item)
            elif table == "drink":
                item = d.Drink(row[1], row[2], row[3], row[4], row[0])
                table_list.append(item)
            elif table == "round":
                table_list[row[1]]=row[2]
        cursor.close()
        connection.close()
        return table_list

    def search_rounds(self,person_name, date):
        connection = self.get_connection()
        cursor = connection.cursor()
        table_list = {}
        if person_name is not None and date is None:
            cursor.execute(f"SELECT * FROM round where brewer='{person_name}' AND date = (SELECT MAX(date) FROM round WHERE brewer='{person_name}')")
        elif person_name is None and date is not None:
            cursor.execute(f"SELECT * FROM round where date='{date}' ORDER BY date DESC")
        elif person_name is not None and date is not None:
            cursor.execute(f"SELECT * FROM round where brewer='{person_name}' AND date='{date}' ORDER BY date DESC")
        row = cursor.fetchone()
        print(f"Brewer: {row[0]}")
        print(f"Date: {row[4]}")
        while True:
            row = cursor.fetchone()
            if row == None:
                break
            else:
                table_list[row[1]] = row[2]
        cursor.close()
        connection.close()
        return table_list

    def load_distinct(self, table):  # function to run a select query like `SELECT * FROM players`
        connection = self.get_connection()
        cursor = connection.cursor()
        cursor.execute(f"SELECT DISTINCT drink_name FROM {table}")
        table = []
        while True:
            row = cursor.fetchone()
            if row == None:
                break
            # person = Player(row[1], row[2], row[3], row[4], row[5], row[0])  # row 0 last because it's a default
            item = row[0]
            table.append(item)

        cursor.close()
        connection.close()
        return table

    def save_person(self, first, last, age):
        connection = self.get_connection()
        cursor = connection.cursor()
        args = (first, last, age)
        cursor.execute(f"INSERT INTO person (first_name, last_name, age) VALUES (%s, %s, %s)",
                       args)  # %s prevents SQL injection!
        cursor.execute("SELECT MAX(id) FROM person")
        new_id = cursor.fetchall()[0][0]
        # except:
        connection.commit()
        cursor.close()
        connection.close()
        return new_id

    def delete_person(self, id):
        connection = self.get_connection()
        cursor = connection.cursor()
        arg = id
        try:
            cursor.execute(f"DELETE FROM person WHERE id=%s",arg)  # %s prevents SQL injection!
            connection.commit()
            cursor.close()
            connection.close()
            print("Person deleted successfully")
        except Exception as err:
            print(err)

    def delete_drink(self, drink_type, drink):
        connection = self.get_connection()
        cursor = connection.cursor()
        table = drink_type
        arg = drink
        try:
            cursor.execute(f"DELETE FROM {table} WHERE drink_name=%s", arg)  # %s prevents SQL injection!
            connection.commit()
            cursor.close()
            connection.close()
            print("Drink deleted successfully")
        except Exception as err:
            print(err)

    # UPDATE person SET fav_drink_id = 1 WHERE id=2
    def save_drink(self, table, type, name, details, price):
        connection = self.get_connection()
        cursor = connection.cursor()
        if details == "-":
            args = (type, name, details, price, f"{name}")
        else:
            args = (type, name, details, price, f"{name} {details}")
        cursor.execute(f"INSERT INTO {table} (drink_type, drink_name, details, price, drink_order) VALUES (%s, %s, %s, %s, %s)", args)
        #     # %s prevents SQL injection!
        # if table == "alc_drink":
        #     args = (name,ft1)
        #     cursor.execute(f"INSERT INTO {table} (drink_name, specifics) VALUES (%s, %s)",args)
        #     # %s prevents SQL injection!
        # elif table == "hot_drink":
        #     args = (name, ft1, ft2)
        #     cursor.execute(f"INSERT INTO {table} (drink_name, milk, sugar) VALUES (%s, %s, %s)",
        #                    args)  # %s prevents SQL injection!
        # else:
        #     args = (name, ft1, ft2)
        #     cursor.execute(f"INSERT INTO {table} (drink_name, glass, ice) VALUES (%s, %s, %s)",
        #                    args)  # %s prevents SQL injection!
        cursor.execute(f"SELECT MAX(id) FROM {table}")
        new_id = cursor.fetchall()[0][0]
        # except:
        connection.commit()
        cursor.close()
        connection.close()
        return new_id

    def update(self,id,field,arg):
        connection = self.get_connection()
        cursor = connection.cursor()
        cursor.execute(f"UPDATE person SET {field} = %s WHERE id={id}", arg)
        connection.commit()
        cursor.close()
        connection.close()

    def update_favourites(self):
        connection = self.get_connection()
        with connection.cursor() as cursor:
            cursor.execute("""UPDATE person p INNER JOIN (select drinker, drink_id, drink, drink_type, count(*) FROM round WHERE drink_type='Hot' GROUP BY drinker, drink HAVING count(*)>3 ORDER BY drinker, count(*) DESC) AS d ON p.full_name = d.drinker SET p.fav_hd_id = d.drink_id""")
            cursor.execute("""UPDATE person p INNER JOIN (select drinker, drink_id, drink, drink_type, count(*) FROM round WHERE drink_type='Soft' GROUP BY drinker, drink HAVING count(*)>3 ORDER BY drinker, count(*) DESC) AS d ON p.full_name = d.drinker SET p.fav_sd_id = d.drink_id""")
            cursor.execute("""UPDATE person p INNER JOIN (select drinker, drink_id, drink, drink_type, count(*) FROM round WHERE drink_type='Alcoholic' GROUP BY drinker, drink HAVING count(*)>3 ORDER BY drinker, count(*) DESC) AS d ON p.full_name = d.drinker SET p.fav_ad_id = d.drink_id""")
            connection.commit()
            cursor.close()
            connection.close()