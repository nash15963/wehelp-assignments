from flask import *
import pymysql

app = Flask(__name__)
app.secret_key = "Any String"

db_settings = {
    "host": "127.0.0.1",
    "port": 3306,
    "user": "root",
    "password": "DB_code",
    "db": "website",
    "charset": "utf8"
}
db = pymysql.connect(**db_settings)
# cursor = db.cursor()
# cursor.execute("SELECT VERSION()")
# version = cursor.fetchone()
# print ("Database version : %s " % version)


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
        db = pymysql.connect(**db_settings)
        cursor = db.cursor()
        cursor.execute("SELECT COUNT(*) FROM member WHERE username = %s ;",(username))
        repeat = cursor.fetchone()
        print(repeat[0])
        if int(repeat[0]) > 0 :
            return render_template("login_error.html" , Sys_message = "此帳號已被註冊")
        else :
            cursor.execute("INSERT INTO member (name, username, password) VALUES (%s,%s,%s)",(name, username, code))
            db.commit()
            print("Done")
            return redirect('/')
        

#signin
@app.route("/signin" ,methods = ["POST"])
def signin():
    memeber_username = request.form["memeber_username"]
    member_password = request.form["member_password"]
    print("memeber_username:"+memeber_username,"memeber_code:"+member_password)
    db = pymysql.connect(**db_settings)
    cursor = db.cursor()
    user = cursor.execute("SELECT name ,username ,password FROM member WHERE username = %s and password = %s;",
    (memeber_username,member_password))
    repeat = cursor.fetchone()
    if user == True :
        name = repeat[0]
        session["username"] = memeber_username
        session["name"] = name
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


db.close()
if __name__ == '__main__':
    app.debug = True
    app.run()



