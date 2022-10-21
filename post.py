import sqlite3


def connect():
    conn = sqlite3.connect('posts.db')
    cur = conn.cursor()
    cur.execute("CREATE TABLE if not exists Posts (id INTEGER PRIMARY KEY AUTOINCREMENT, price INTEGER, district TEXT, floor INTEGER, floor_count INTEGER, area INTEGER, living_area INTEGER, kitchen_are INTEGER, wall_type TEXT, room_count INTEGER)")
    wall_type = "-"
    price = 12
    district = "-"
    floor = 1
    floor_count = 2
    total_square_meters = 3
    living_square_meters = 4
    kitchen_square_meters = 5
    wall_type = "-"
    rooms_count = 1
    description = 2

    adv_list = [
        price,
        district,
        floor,
        floor_count,
        total_square_meters,
        living_square_meters,
        kitchen_square_meters,
        wall_type,
        rooms_count,
        description
    ]
    cur.execute(
        "INSERT INTO Posts VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", adv_list)
    conn.commit()
    cur.close()

# connect()


def select():
    conn = sqlite3.connect('posts.db')
    cur = conn.cursor()
    cur.execute("SELECT id FROM Posts")
    for result in cur:
        print(result)
    conn.commit()
    cur.close()


# select()


def drop():
    conn = sqlite3.connect('posts.db')
    cur = conn.cursor()
    cur.execute("DROP TABLE Posts")
    conn.commit()
    cur.close()


# drop()
