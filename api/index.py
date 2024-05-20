from flask import Flask , render_template , request , jsonify ,redirect, send_file



chatroom =  []

app = Flask(__name__)
# CORS(app)

@app.route("/",methods=['GET','POST'])
def login():
    if request.method == "POST":
        uname = request.form.get("username")

        return redirect(f"/chat?user={uname}")

    return render_template("login.html")

@app.get("/chat")
def chat():

    uname = request.args.get("user")

    return render_template("chatroom.html")

@app.route("/signup",methods=['GET','POST'])
def signUp():

    return redirect("/login")

@app.route("/error")
def error_page():
    error404 = request.args.get("msg")
    return render_template("error.html",error=error404)

