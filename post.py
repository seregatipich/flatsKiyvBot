import sqlite3


def connect(adv_list):
    conn = sqlite3.connect('posts.db')
    cur = conn.cursor()
    cur.execute("CREATE TABLE if not exists Posts (id INTEGER PRIMARY KEY AUTOINCREMENT, price INTEGER, district TEXT, floor INTEGER, floor_count INTEGER, area INTEGER, living_area INTEGER, kitchen_are INTEGER, wall_type TEXT, room_count INTEGER, description TEXT)")
    cur.execute(
        "INSERT INTO Posts (price, district, floor, floor_count, area, living_area, kitchen_are, wall_type, room_count, description) VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", adv_list)
    conn.commit()
    cur.close()

# connect()


def select(id):
    conn = sqlite3.connect('posts.db')
    cur = conn.cursor()
    cur.execute(f"SELECT * FROM Posts WHERE id = ({id})")
    for result in cur:
        print(result)
    conn.commit()
    cur.close()


def last_id():
    conn = sqlite3.connect('posts.db')
    cur = conn.cursor()
    cur.execute(f"SELECT * FROM Posts WHERE id = ({id})")
    for result in cur:
        print(result)
    conn.commit()
    cur.close()


def drop():
    conn = sqlite3.connect('posts.db')
    cur = conn.cursor()
    cur.execute("DROP TABLE Posts")
    conn.commit()
    cur.close()


# drop()
