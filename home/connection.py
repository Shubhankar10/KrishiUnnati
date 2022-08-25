import mysql.connector

def sql_connection():
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="4844",
        database="krishi"
    )
    print("Connection Successful")
    return mydb

def tables():
    con=sql_connection()
    mycursor = con.cursor()
    mycursor.execute("CREATE TABLE farmer_profile (email varchar(50) NOT NULL,name varchar(100) DEFAULT NULL,phonenumber int DEFAULT NULL,town varchar(200) DEFAULT NULL,district varchar(100) DEFAULT NULL,state varchar(100) DEFAULT NULL,country varchar(100) DEFAULT NULL,pincode int DEFAULT NULL,aadhar int DEFAULT NULL,PRIMARY KEY (email)")
    mycursor.execute("CREATE TABLE if not exist farmer_land(email varchar(100) DEFAULT NULL,landarea float DEFAULT NULL,adress varchar(200) DEFAULT NULL,income int DEFAULT NULL,cropname varchar(200) DEFAULT NULL,grownfrom date DEFAULT NULL,grownuntill date DEFAULT NULL,KEY email (email),CONSTRAINT farmer_land_ibfk_1 FOREIGN KEY (email) REFERENCES farmer_profile (email)")
    tables = mycursor.fetchall()
    return tables
