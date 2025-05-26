from lib.db.connection import get_connection

def setup_database():
    conn = get_connection()
    cursor = conn.cursor()


    with open('lib/db/schema.sql', 'r') as f:
        schema = f.read()


    cursor.executescript(schema)
    conn.commit()
    print("table created :)")

if __name__ == '__main__':
    setup_database()