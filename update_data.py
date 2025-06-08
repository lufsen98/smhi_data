from app.api import get_data
import app.db as db
def main():
   #smhi json api
   bromma_url = "https://opendata-download-metobs.smhi.se/api/version/1.0/parameter/1/station/97200/period/latest-hour/data.json"
   arlanda_url = "https://opendata-download-metobs.smhi.se/api/version/1.0/parameter/1/station/97400/period/latest-hour/data.json"
   bromma_data = get_data(bromma_url)
   arlanda_data = get_data(arlanda_url)
   conn, cursor =db.setup_connection()
   db.create_table(cursor)
   db.store_data_in_mysql(bromma_data,conn,cursor)
   db.store_data_in_mysql(arlanda_data,conn,cursor)
   db.close_connection(conn, cursor)
   


   


if __name__ == "__main__":
    main()

