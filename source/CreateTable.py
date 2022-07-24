import sqlite3
db = sqlite3.connect("Burger.db")
cr=db.cursor()
cr.execute('create table regis_table(UNAME text,UADD text,UMOBILE text,UEMAIL text,UPWD text,UCPWD text)')
cr.execute('create table cart(ITEM text,PRICE integer)')
cr.execute('create table cartB(ITEM text,PRICE integer)')
db.commit()
db.close()
print('table created')