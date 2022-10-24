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


def get_post_info(id_adv):
    message = {}
    conn = sqlite3.connect('posts.db')
    cur = conn.cursor()
    cur.execute(f"SELECT * FROM Posts WHERE id={id_adv}")
    for result in cur:
        message = {
            'id': f'{result[0]}',
            'price': f'{result[1]}',
            'district': f'{result[2]}',
            'floor': f'{result[3]}',
            'floor_count': f'{result[4]}',
            'area': f'{result[5]}',
            'living_area': f'{result[6]}',
            'kitchen_area': f'{result[7]}',
            'wall_type': f'{result[8]}',
            'room_count': f'{result[9]}',
            'description': f'{result[10]}'
        }
    conn.commit()
    conn.close()
    return message
