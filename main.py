from flask import Flask,render_template
import sqlite3
app = Flask(__name__)
c=sqlite3.connect("tea_store")


c.execute("CREATE TABLE movie(title, year, score)");

c.execute("""
    INSERT INTO movie VALUES
        ('Monty Python and the Holy Grail', 1975, 8.2),
        ('And Now for Something Completely Different', 1971, 7.5)
""")

c.commit()



@app.route('/')
def home ():
    return   render_template("index.html")


app.run(host='0.0.0.0', port=81)


