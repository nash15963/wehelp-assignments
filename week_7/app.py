from base64 import encode
from distutils.command.upload import upload
from tarfile import ENCODING
from flask import *
import pymysql
import json

app = Flask(__name__)
app.secret_key = "Any String"

connection  = pymysql.connect(host='127.0.0.1',
                              user='root',
                              password='不要壞壞',
                              database='website',
                              charset='utf8',
                              cursorclass=pymysql.cursors.DictCursor)

#main page
@app.route("/")
def index():
    return render_template("main.html")

#signup
@app.route("/signup" ,methods = ["POST"])
def signup():
    name =request.form['name']
    username = request.form['username']
    code = request.form['password']
    print("memeber_name :"+name,"account :"+username,"code:"+code)
    if name == '' or username == '' or code == '' :
        print("Null data")
        return render_template("login_error.html" ,Sys_message ='仍有欄位未填寫')
    else:
        cursor = connection.cursor()
        sql = "SELECT COUNT(*) FROM member WHERE username = %s"
        cursor.execute(sql, (username))
        result = cursor.fetchone()
        print("RESULT",result)
        if result['COUNT(*)'] > 0:
            return render_template("login_error.html" , Sys_message = "此帳號已被註冊")
        else :
            sql = "INSERT INTO member (name, username, password) VALUES (%s,%s,%s)"
            cursor.execute(sql, (name, username, code))
            connection.commit()
            print("Done")
            return redirect('/')

      

#signin
@app.route("/signin" ,methods = ["POST"])
def signin():
    memeber_username = request.form["memeber_username"]
    member_password = request.form["member_password"]
    print("memeber_username:"+memeber_username,"memeber_code:"+member_password)
    cursor = connection.cursor()
    sql = "SELECT name ,username ,password FROM member WHERE username = %s and password = %s;"
    user = cursor.execute(sql, (memeber_username,member_password))
    result = cursor.fetchone()
    print("user" ,user)
    if result['username'] == memeber_username :
                    session['username'] = result['username']
                    session["name"] = result['name']
                    return redirect("/member")
    else :
        return redirect("/error?Sys_message=帳號、或密碼輸入錯誤")



#success page
@app.route("/member")
def success():
    if "username" in session :
        name = session['name']
        return render_template("login_success.html" ,name=name)
    else:
        return render_template("main.html")


#error page
@app.route("/error")
def error():
    message = request.args.get("Sys_message" ,"不要壞壞")   
    return render_template("login_error.html" , Sys_message = message)


#signout
@app.route("/signout")
def signout():
    session.clear()
    return redirect("/")


#api 查詢姓名
@app.route("/api/members")
def api():
    username = request.args.get("username",'')
    print("username:"+username)
    cursor = connection.cursor()
    sql = "SELECT id ,name ,username FROM member WHERE username = %s "
    cursor.execute(sql, (username))
    result = cursor.fetchone()
    # print("RESULT:",result)
    result_JSON = json.dumps({"data":result},ensure_ascii=False)
    print("RESULT : ",result_JSON)
    return result_JSON

  
#api 修改姓名
@app.route("/api/member" ,methods = ["POST"])
def api_modify():
    new_name_dict = request.get_json()
    new_name = new_name_dict['name']
    name = session['name']
    username = session['username']
    if new_name == name or new_name == '' :
        data = {'error': True}
        print(data)
        return data
    else :
        data = {'ok': True}
        print('data :',data)
        cursor = connection.cursor()
        sql = 'UPDATE `website`.`member` SET `name` = %s WHERE (`username` = %s);'
        cursor.execute(sql, (new_name,username))
        connection.commit()
        session['name'] = new_name
        print(data)
        return data

#預設帳號: strong
#預設密碼: 123
  

if __name__ == '__main__':
    app.debug = True
    app.run()




# http://127.0.0.1:5000/error?Sys_message=123
# http://127.0.0.1:5000/api/members?username=strong
# http://127.0.0.1:5000/api/members?username=100 (get api)
# http://127.0.0.1:5000/api/member (post api)




