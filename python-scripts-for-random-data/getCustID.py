import sqlite3

c = sqlite3.connect("bankDB.sqlite")
cur = c.cursor()
cur.execute("SELECT customerID FROM customerdetails_retail;")
rows = cur.fetchall()
l = len(rows)
for i  in range(0, l):
    
    f = open("custID.txt","a")
    line = rows[i][0].strip()
    l = ["\"", line, "\", "]
    f.writelines(l)

''' #alterhnative way of above block
for row in rows:
    print(row[0])

'''
