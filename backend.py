import sqlite3


def connect():
    con = sqlite3.connect("books.db")
    cur = con.cursor()
    cur.execute(
        "CREATE TABLE IF NOT EXISTS book(id INTEGER PRIMARY KEY AUTOINCREMENT, title TEXT, author TEXT,year INTEGER, isbn INTEGER)")
    con.commit()
    con.close()


def insert(title, author, year, isbn):
    con = sqlite3.connect("books.db")
    cur = con.cursor()
    cur.execute("INSERT INTO book VALUES (NULL,?,?,?,?)", (title, author, year, isbn))
    con.commit()
    con.close()


def view():
    con = sqlite3.connect("books.db")
    cur = con.cursor()
    cur.execute("SELECT * FROM book")
    rows = cur.fetchall()
    cur.close()
    return rows


def search(title="", author="", year="", isbn=""):
    con = sqlite3.connect("books.db")
    cur = con.cursor()
    cur.execute("SELECT * FROM book WHERE title=? or author=? or year=? or isbn=?", (title, author, year, isbn))
    rows = cur.fetchall()
    cur.close()
    return rows


def delete(id):
    con = sqlite3.connect("books.db")
    cur = con.cursor()
    cur.execute("DELETE FROM book WHERE id=?", (id,))
    con.commit()
    con.close()


def update(id, title, author, year, isbn):
    con = sqlite3.connect("books.db")
    cur = con.cursor()
    cur.execute("UPDATE book SET title=?, author=?, year=?, isbn=? WHERE id=?", (title, author, year, isbn, id))
    con.commit()
    con.close()


connect()
insert(title="The Glass Castle", author="Jeannette Walls", year=2005, isbn=54654165)
insert(title="Great Fire", author="James Williams", year=2001, isbn=21858763)
insert(title="Fallen Star", author="Nancy Young", year=1995, isbn=78987456)
update(3, title="Fallen Sun", author="Gilbert Clark", year=2000, isbn=78987456)
print(view())
print(search(author="Gilbert Clark"))
