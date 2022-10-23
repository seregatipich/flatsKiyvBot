import sqlite3


def uniqueness_test(adv_list):
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
