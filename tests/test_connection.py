from utils.dbconnection import get_connection

def test_db_connection():
    conn=get_connection()
    cursor=conn.cursor()
    cursor.execute("select * from employee")
    result=cursor.fetchall()
    for i in result:
        print(i[5])
