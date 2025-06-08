from flask import Flask, render_template,Blueprint
from .db import setup_connection, close_connection
main = Blueprint('main', __name__)


@main.route("/")
def index():
    return render_template("index.html")

@main.route("/stockholm")
def stockholm():
    conn, cursor = setup_connection()
    cursor.execute("SELECT station, date, celsius, quality FROM stockholm ORDER BY date DESC LIMIT 10")
    rows = cursor.fetchall()

    close_connection(conn,cursor)

    return render_template("stockholm.html", data=rows)
