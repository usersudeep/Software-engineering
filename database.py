import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="venki",
    database="railway_system"
)
c = mydb.cursor()


def create_table():
    c.execute('CREATE TABLE IF NOT EXISTS TRAIN(Train_No TEXT, Name TEXT, Train_Type TEXT, Source TEXT, Destination TEXT, Availability TEXT)')


def add_data(Train_No, Name, Train_Type, Source, Destination, Availability):
    c.execute('INSERT INTO TRAIN(Train_No, Name, Train_Type, Source, Destination, Availability) VALUES (%s,%s,%s,%s,%s,%s)',
              (Train_No, Name, Train_Type, Source, Destination, Availability))
    mydb.commit()


def view_all_data():
    c.execute('SELECT * FROM TRAIN')
    data = c.fetchall()
    return data


def view_only_train_number():
    c.execute('SELECT Train_No FROM TRAIN')
    data = c.fetchall()
    return data


def edit_dealer_data(new_availability, Train_No):
    c.execute("UPDATE TRAIN SET Availability=%s where Train_No = %s", (new_availability, Train_No))
    mydb.commit()
    data = c.fetchall()
    return data


def delete_data(Train_No):
    c.execute('DELETE FROM TRAIN WHERE Train_No="{}"'.format(Train_No))
    mydb.commit()