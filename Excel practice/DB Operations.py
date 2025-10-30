# Insert, Update, Delete

insert_query="insert into student values(5, 'xyz', 250)"
update_query="update student set sname='Smith' where sno=1;"
delete_query="delete from student where sno=2"

import mysql.connector

try:
    con=mysql.connector.connect(host="localhost",port=3307,user="root",passwd="123@123Dc",database="mydb")
    curs=con.cursor()  # create cursor
    # curs.execute(insert_query)  # exceute insert query
    # curs.execute(update_query) # execute update query
    curs.execute(delete_query)
    con.commit()
    con.close()

except:
    print("Connection unsuccessfull.....")

print("Finished......")