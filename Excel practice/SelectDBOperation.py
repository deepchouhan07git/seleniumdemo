import mysql.connector

try:
    con=mysql.connector.connect(host="localhost",port=3306,user="root",passwd="123@123Dc",database="hr")
    curs=con.cursor()  # create cursor
    curs.execute("select * from orders")

    for row in curs:
        print(row[0],row[1],row[2])

    con.close()

except:
    print("Connection unsuccessfull.....")

print("Finished......")