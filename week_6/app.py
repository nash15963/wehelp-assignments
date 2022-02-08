from flask import *
import pymysql

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



if __name__ == '__main__':
    app.debug = True
    app.run()









