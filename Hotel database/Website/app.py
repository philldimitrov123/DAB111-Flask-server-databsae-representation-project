from flask import Flask, render_template
from pathlib import Path
import sqlite3

app = Flask(__name__)

base_path = Path.cwd()
foldername = "database_folder"
dbname = "hotelDB.db"
file_path = base_path / foldername / dbname

print(file_path)

@app.route("/")  # default page
def index():
    return render_template("Homepage.html")

@app.route("/about")  # about page
def about():
    return render_template("About.html")

@app.route("/data")  # data page
def data():
    con = sqlite3.connect(file_path)  # database connection
    cursor = con.cursor()
    result = cursor.execute("SELECT * FROM hotel_table LIMIT 10").fetchall()
    con.close()
    return render_template("Data.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)


