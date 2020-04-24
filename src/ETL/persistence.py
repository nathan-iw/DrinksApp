import pymysql
from os import environ
from src.drinks import HotDrink as h, SoftDrink as s, AlcDrink as a
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


    def load_all(self, table):  # function to run a select query like `SELECT * FROM players`
        connection = self.get_connection()
        cursor = connection.cursor()
        cursor.execute(f"SELECT * FROM {table}")
        table_list = []
        while True:
            row = cursor.fetchone()
            if row == None:
                break
            # person = Player(row[1], row[2], row[3], row[4], row[5], row[0])  # row 0 last because it's a default
            if table == "person":
                item = p.Person(row[1], row[2], row[3], row[0])
            elif table == "hot_drink":
                item = h.HotDrink(row[1], row[2], row[3], row[0])
            elif table == "soft_drink":
                item = s.SoftDrink(row[1], row[2], row[3], row[0])
            elif table == "alc_drink":
                item = a.AlcDrink(row[1], row[2], row[0])

            table_list.append(item)

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
    def save_drink(self, table, name, ft1, ft2):
        connection = self.get_connection()
        cursor = connection.cursor()

        if table == "alc_drink":
            args = (name,ft1)
            cursor.execute(f"INSERT INTO {table} (drink_name, specifics) VALUES (%s, %s)",args)
            # %s prevents SQL injection!
        elif table == "hot_drink":
            args = (name, ft1, ft2)
            cursor.execute(f"INSERT INTO {table} (drink_name, milk, sugar) VALUES (%s, %s, %s)",
                           args)  # %s prevents SQL injection!
        else:
            args = (name, ft1, ft2)
            cursor.execute(f"INSERT INTO {table} (drink_name, glass, ice) VALUES (%s, %s, %s)",
                           args)  # %s prevents SQL injection!
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