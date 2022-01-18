from flask import *
import pymysql


app = Flask(__name__)
app.secret_key = "Any String"
correct_memeber_account ="test"
correct_memeber_password ="test"

@app.route("/")
def index():
    return render_template("main.html")

@app.route("/singin" ,methods = ["POST"])
def singin():
    memeber_account = request.form["memeber_account"]
    memeber_code = request.form["memeber_password"]
    print("account:"+memeber_account,"code:"+memeber_code)
    session["memeber_account"] = memeber_account
    session["memeber_code"] = memeber_code
    if memeber_account == '' or memeber_code == '': 
        return redirect("/error")
    elif memeber_account != correct_memeber_account or memeber_code != correct_memeber_password:
        return redirect("/error?message=帳號、或密碼輸入錯誤")
    elif memeber_account == correct_memeber_account and memeber_code == correct_memeber_password: 
        return redirect("/member")
    
    

#success page
@app.route("/member")
def success():
    if 'memeber_account' in session:
        if session["memeber_account"] == correct_memeber_account and session["memeber_code"] ==correct_memeber_password:
            return render_template("login_success.html")
        else:
            return render_template("main.html")
    else:
        return render_template("main.html")

#error page
@app.route("/error")
def error():
    message = request.args.get("message" ,"請輸入帳號、密碼")   
    return render_template("login_error.html" , message = message)

#http://127.0.0.1:5000/member
#請輸入帳號、密碼
#帳號、或密碼輸入錯誤

#signout
@app.route("/signout")
def signout():
    session.clear()
    return redirect("/")



if __name__ == '__main__':
    app.debug = True
    app.run()
