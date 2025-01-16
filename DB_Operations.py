import pymysql
connection = pymysql.connect(host="localhost",user="root",passwd="",database="db_kesehatan")
cursor = connection.cursor()

def add_text(topik, deskripsi):
    try:
        cursor.execute("INSERT INTO content (id, topik, deskripsi) VALUES (DEFAULT, %s, %s)",(topik, deskripsi),)
        connection.commit()
        return 1
    except Exception as e:
        print(f"Error: {e}")
        connection.rollback()  
        return 0

def get_data():
    cursor.execute("SELECT * FROM content")
    rows = cursor.fetchall()
    return rows

def update_text(id, topik, deskripsi):
    query = "UPDATE content SET topik = %s, deskripsi = %s WHERE id = %s"
    values = (topik, deskripsi, id)
    cursor.execute(query, values)
    connection.commit()
    return cursor.rowcount > 0

def delete_text(id):
    query = "DELETE FROM content WHERE id = %s"
    cursor.execute(query, (id,))
    connection.commit()

    return cursor.rowcount > 0 

def get_data_by_id(id):
    query = "SELECT * FROM content WHERE id = %s"
    cursor.execute(query, (id,))
    rows = cursor.fetchall()
    return rows

