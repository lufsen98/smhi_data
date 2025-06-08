import  mysql.connector
from datetime import datetime
def setup_connection():
    cnx = mysql.connector.connect(
            host="localhost",
            user="root",
            password="rootpassword",
            database="temperature",
            port=1338
            )
    cursor = cnx.cursor()
    return cnx, cursor

def create_table(cursor):
    cursor.execute("DROP TABLE IF EXISTS stockholm")
    cursor.execute("""CREATE TABLE stockholm(
                       id INT AUTO_INCREMENT PRIMARY KEY,
                       station VARCHAR(100),
                       date VARCHAR(100),
                       celsius VARCHAR(100),
                       quality VARCHAR(10)
                       )""")
def insert_data(data, cnx, cursor):
    time_stamp_ms = data["value"][0]["date"]
    time_stamp_s = time_stamp_ms / 1000
    dt = datetime.fromtimestamp(time_stamp_s)
    formatted_dt = dt.strftime("%Y-%m-%d %H:%M:%S")
    
    cursor.execute("INSERT INTO stockholm(station,date,celsius,quality)VALUES(%s,%s,%s,%s)",

                   (
                       data["station"]["name"],
                       formatted_dt,
                       data["value"][0]["value"],
                       data["value"][0]["quality"]
                   )
                   )
    cnx.commit()

def store_data_in_mysql(data,conn,cursor):
    insert_data(data,conn,cursor)




def close_connection(conn,cursor):
    cursor.close()
    conn.close()





