import pymysql

def register(id, pw, phone, code, status):
    con = pymysql.connect(user='root', passwd='', host='127.0.0.1', db='marketplace', charset='utf8')
    cur = con.cursor(pymysql.cursors.DictCursor)
    cur.execute("INSERT INTO user_list(id, password, phone, code, authed) VALUES('"+id+"', '"+pw+"', '"+phone+"', '"+code+"', '"+status+"');")
    con.commit()
    con.close()
   
    return "ok"

def login(id, pw):
    con = pymysql.connect(user='root', passwd='', host='127.0.0.1', db='marketplace', charset='utf8')
    cur = con.cursor(pymysql.cursors.DictCursor)
    cur.execute("SELECT * FROM user_list WHERE id='"+str(id)+"';")
    rows = cur.fetchone()
    con.close()
    if rows != None:
        if rows["password"] == pw:
            return True 
        else:
            return False 
    else:
        return False