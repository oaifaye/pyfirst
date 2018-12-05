import pymysql

db = pymysql.connect("10.0.251.50","root","1234qwer","cms_ju",charset='utf8' )
cursor = db.cursor(pymysql.cursors.DictCursor)
cursor.execute("select * from tj_news_clob order by news_id desc limit %s,%s",(0,10))
rows = cursor.fetchall()
for row in rows:
    print(row['news_id'])
db.close()   