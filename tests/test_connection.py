from utils.dbconnection import get_connection

def test_db_connection():
    conn=get_connection()
    cursor=conn.cursor()
    cursor.execute("select empno,count(*) from employee group by empno having count(*)=1")
    result=cursor.fetchall()
    assert result !=1 ,'no duplicated found'
