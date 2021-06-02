#records to query convertor
import sqlite3
from sqlite3 import Error


conn = sqlite3.connect('bankDB.sqlite')
cur = conn.cursor()
cur.execute("SELECT * FROM customerdetails_retail;")
rows = cur.fetchall()
for row in rows:
    l = "INSERT INTO "+ "customerdetails_retail(customerID, name, FatherName, MotherName, dob, address, Aadhar, PANNumber, branch) "+ "VALUES (\""+str(row[0])+"\", \""+str(row[1])+"\", \""+str(row[2])+"\", \""+str(row[3])+"\", \""+str(row[4])+"\", \""+str(row[5])+"\", \""+str(row[6])+"\", \""+str(row[7])+"\", \""+str(row[8])+"\");"+"\n"
    f = open("recordsSQL2.txt","a")
    f.writelines(l)
