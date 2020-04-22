import pymysql
from src.db import db_login as login
from src.drinks import HotDrink as h, SoftDrink as s, AlcDrink as a
from src.ETL import Person as p

class Database():

    def get_connection(self):  # function to get the connection string using: pymysql.connect(host, username, password, database)
        db_connection = pymysql.connect(
            login.db_host,  # host address
            login.user_name,  # user name
            login.password,  # pw
            login.database  # db
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


    def save_person(self, first,last,age):
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