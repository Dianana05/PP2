import psycopg2

def connect_db():
    return psycopg2.connect(
        host="localhost",
        dbname="postgres",
        user="postgres",
        password="12345678"
    )

def get_or_create_user(username):
    conn = connect_db()
    cur = conn.cursor()
    cur.execute("SELECT id FROM users WHERE username = %s", (username,))
    result = cur.fetchone()

    if result:
        user_id = result[0]
        cur.execute("SELECT current_level FROM users WHERE id = %s", (user_id,))
        level = cur.fetchone()[0]
    else:
        cur.execute("INSERT INTO users (username) VALUES (%s) RETURNING id", (username,))
        user_id = cur.fetchone()[0]
        conn.commit()
        level = 1

    cur.close()
    conn.close()
    return user_id, level

def update_user_progress(user_id, score, level):
    conn = connect_db()
    cur = conn.cursor()
    cur.execute("UPDATE users SET current_level = %s WHERE id = %s", (level, user_id))
    cur.execute("INSERT INTO user_score (user_id, score, level) VALUES (%s, %s, %s)",
                (user_id, score, level))
    conn.commit()
    cur.close()
    conn.close()
