import pymysql

def get_allprod():
    con = pymysql.connect(user='root', passwd='', host='127.0.0.1', db='marketplace', charset='utf8')
    cur = con.cursor(pymysql.cursors.DictCursor)
    cur.execute("SELECT * FROM prod_list;")
    prod_list = cur.fetchall()
    return prod_list

def get_prod(prodid):
    con = pymysql.connect(user='root', passwd='', host='127.0.0.1', db='marketplace', charset='utf8')
    cur = con.cursor(pymysql.cursors.DictCursor)
    cur.execute("SELECT * FROM prod_list WHERE prod_code = '"+str(prodid)+"';")
    prod_list = cur.fetchall()
    return prod_list

def upload(prod_name, prod_image, prod_price,code,prod_tag):
    con = pymysql.connect(user='root', passwd='', host='127.0.0.1', db='marketplace', charset='utf8')
    cur = con.cursor(pymysql.cursors.DictCursor)
    cur.execute("INSERT INTO prod_list(prod_status, prod_image, prod_name, prod_price, prod_code, prod_category, prod_authed, prod_tag) VALUES('0','"+prod_image+"','"+prod_name+"','"+prod_price+"','"+code+"','0','0','"+prod_tag+"');")
    con.commit()
    con.close()
    return "ok"

def upload(prod_name, prod_image, prod_price,code,prod_tag):
    con = pymysql.connect(user='root', passwd='', host='127.0.0.1', db='marketplace', charset='utf8')
    cur = con.cursor(pymysql.cursors.DictCursor)
    cur.execute("INSERT INTO prod_list(prod_status, prod_image, prod_name, prod_price, prod_code, prod_category, prod_authed, prod_tag) VALUES('0','"+prod_image+"','"+prod_name+"','"+prod_price+"','"+code+"','0','0','"+prod_tag+"');")
    con.commit()
    con.close()
    return "ok"

