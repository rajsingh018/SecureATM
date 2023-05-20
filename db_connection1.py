import mysql.connector as m

def mysql_connect():

    db_connection = m.connect(host="localhost",user="root",passwd="diviyadav",database="account")

    return db_connection

mysql_connect()
