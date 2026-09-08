from csv import excel
from enum import nonmember
from logging import exception

import mysql.connector
from mysql import connector
import datetime
class Blooddonarmanager:
    def __init__(self):
        self.connection=connector.connect(
            host="localhost",
            user="root",
            password="Angel@1234",
            database="blood_db_b3"
        )

        print("connection successfullly----")
    def post(self,**kwargs):
        try:
            self.cursor=self.connection.cursor()
            query="insert into donor(name,blood_group,phone,city,last_donation)values(%s,%s,%s,%s,%s)"
            values =[v for v in kwargs.values()]
            self.cursor.execute(query,values)
            self.connection.commit()
            print("donar added successfully----")
        except Exception as e:
            print(e)
donor_instance=Blooddonarmanager()
donor_instance.post(name="suraj",blood_group="0+",phone="9876432",city="kochi",last_donation=datetime.datetime.today())
donor_instance.post(name="anu",blood_group="A+",phone="9834563845",city="kallor",last_donation=datetime.datetime.today())
donor_instance.post(name="priya",blood_group="AB-",phone="23567456",city="pala",last_donation=datetime.datetime.today())
def put(self,id=None,**kwargs):
    try:
        record=self.get_object(id=id)
        if record !=None:
            self.cursor=self.connection.cursor()
            placeholder=""
            for k in kwargs.keys():
                placeholder +="%s,"
            placeholder=placeholder.rstrip("'")
            query=f"update donar set {placeholder}where id=1"
            values=[v for v in kwargs.values()]
            values.append(id)
            self.cursor.execute (query,values)
            self.connection.commoit()
            print("donar details updated successfully-----!")
        else:
            print("donar not found------!")

    except exception as e:

         print(e)
         