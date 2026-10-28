
import mysql.connector
import datetime


class Blooddonarmanager:

    def __init__(self):
        self.connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Angel@1234",
            database="blood_db_b3"
        )
        self.cursor = self.connection.cursor()
        print("Connection successfully!")


    def post(self, **kwargs):
        try:
            query = """
                INSERT INTO donor
                (donor_name, blood_group, phone, city, last_donation)
                VALUES (%s, %s, %s, %s, %s)
            """

            values = list(kwargs.values())

            self.cursor.execute(query, values)
            self.connection.commit()

            print("Donor added successfully!")

        except Exception as e:
            print(e)

    def get(self):
        try:
            query = "SELECT * FROM donor"

            self.cursor.execute(query)
            records = self.cursor.fetchall()

            for record in records:
                print(record)

        except Exception as e:
            print(e)


    def get_object(self, id):
        try:
            query = "SELECT * FROM donor WHERE id=%s"

            self.cursor.execute(query, (id,))
            record = self.cursor.fetchone()

            return record

        except Exception as e:
            print(e)
            return None

    # PUT: Update donor details
    def put(self, id=None, **kwargs):
        try:
            record = self.get_object(id)

            if record is not None:

                allowed_fields = {
                    "don_name",
                    "blood_group",
                    "phone",
                    "city",
                    "last_donation"
                }

                if not kwargs:
                    print("No details provided!")
                    return

                if not set(kwargs).issubset(allowed_fields):
                    print("Invalid field name!")
                    return

                placeholder = ""

                for key in kwargs.keys():
                    placeholder += key + "=%s,"

                placeholder = placeholder.rstrip(",")

                query = f"UPDATE donor SET {placeholder} WHERE id=%s"

                values = list(kwargs.values())
                values.append(id)

                self.cursor.execute(query, values)
                self.connection.commit()

                print("Donor details updated successfully!")

            else:
                print("Donor not found!")

        except Exception as e:
            print(e)


    def delete(self, id):
        try:
            record = self.get_object(id)

            if record is not None:
                query = "DELETE FROM donor WHERE id=%s"

                self.cursor.execute(query, (id,))
                self.connection.commit()

                print("Donor deleted successfully!")

            else:
                print("Donor not found!")

        except Exception as e:
            print(e)


    def close(self):
        self.cursor.close()
        self.connection.close()


donor_instance = Blooddonarmanager()



donor_instance.post(
     donor_name="Suraj",
     blood_group="O+",
     phone="98767432",
     city="Kochi",
     last_donation=datetime.datetime.today()
 )



donor_instance.get()



print(donor_instance.get_object(1))


donor_instance.put(id=1, city="Kollam", blood_group="A+")



donor_instance.delete(1)


donor_instance.close()
