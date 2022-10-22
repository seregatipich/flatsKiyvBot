import sqlite3


def connect(adv_list):
    try:
        conn = sqlite3.connect('posts.db')
        cur = conn.cursor()
        cur.execute("CREATE TABLE if not exists Posts (id INTEGER PRIMARY KEY UNIQUE, price INTEGER, district TEXT, floor INTEGER, floor_count INTEGER, area INTEGER, living_area INTEGER, kitchen_area INTEGER, wall_type TEXT, room_count INTEGER, description TEXT)")
        cur.execute(
            "INSERT INTO Posts VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", adv_list)
        conn.commit()
        cur.close()
    except sqlite3.IntegrityError as error:
        return 'recurring post'

# connect()


def select():
    try:
        conn = sqlite3.connect('posts.db')
        cur = conn.cursor()
        cur.execute(f"SELECT * FROM Posts")
        for result in cur:
            print(result)
        conn.commit()
        cur.close()
    except sqlite3.IntegrityError as error:
        return str(error)

# select()


def drop():
    conn = sqlite3.connect('posts.db')
    cur = conn.cursor()
    cur.execute("DROP TABLE Posts")
    conn.commit()
    cur.close()


# drop()
