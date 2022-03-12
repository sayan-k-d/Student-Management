import mysql.connector
class Student:
    def findall(self):
        con= mysql.connector.connect(
    host='localhost',
    database='testclient',
    user='root',
    password=''
    )
        cursor=con.cursor()
        cursor.execute("select * from details")
        data=cursor.fetchall()
        return data
    def findone(self,id):
        con= mysql.connector.connect(
    host='localhost',
    database='testclient',
    user='root',
    password=''
    )
        cursor=con.cursor()
        cursor.execute("select * from details where id="+id)
        data=cursor.fetchone()
        return data
    def addone(self,nm,ph,em,ps):
        con= mysql.connector.connect(
    host='localhost',
    database='testclient',
    user='root',
    password=''
    )
        cursor=con.cursor()
        cursor.execute("insert into details (name,phone,email,pass1)values('%s','%s','%s','%s')"%(nm,ph,em,ps))
        rows = cursor.rowcount
        con.commit()
        con.close()
        return rows
    def updateuser(self,nm,ph,em,ps,id):
        con= mysql.connector.connect(
    host='localhost',
    database='testclient',
    user='root',
    password=''
    )
        cursor=con.cursor()
        cursor.execute("update details set name='%s',phone='%s',email='%s',pass1='%s' where id='%d'"%(nm,ph,em,ps,id))
        rows=cursor.rowcount
        con.commit()
        con.close()
        return rows
        
    def deluser(self,id):
        con= mysql.connector.connect(
    host='localhost',
    database='testclient',
    user='root',
    password=''
    )
        cursor=con.cursor()
        cursor.execute("delete from details where id="+str(id))
        rows=cursor.rowcount
        if rows!=0:
            con.commit()
            con.close()
        return rows
