from flask import Flask , render_template , request , jsonify ,redirect, send_file

# from mycypher import encrypt
# import time
# import uuid 
# from flask_cors import CORS



chatroom =  []

app = Flask(__name__)
# CORS(app)

@app.route("/",methods=['GET','POST'])
def login():
    if request.method == "POST":
        uname = request.form.get("username")
        # upasw = request.form.get("password")
        # print(uname,upasw)
        
        
        # pasKey = encrypt(upasw)
        # userCred = db.search(users.username == uname)
        # print(userCred[0])
        # if len(userCred)!=0:
            # print('ACCOUNT EXIST')
            # if userCred[0].get("password") ==  pasKey:
                # print("PASSWORD CORRECT")
                # return redirect(f"/chat?auth-key={pasKey}&token={int(time.time())}&user={uname}")
        return redirect(f"/chat?user={uname}")

            # else: return  redirect(f"/error?msg=password wrong, try again")
        # else: return redirect(f"/error?msg=account not exist, please signup or check username")
    return render_template("login.html")

@app.get("/chat")
def chat():
    # key = request.args.get("auth-key")
    uname = request.args.get("user")
    # token = int(request.args.get("token")) + 150
    # print("AUTH KEY", key,"TOKEN", token)
    # Auth_Token = int(time.time())
    # if token >= Auth_Token :
    #     print("TOKEN ACCEPTED")
    #     return render_template("chatroom.html")
    # else: 
    #     print("TOKEN EXPIRED")
    #     return redirect(f"/error?msg=token expired, login again")
    return render_template("chatroom.html")

@app.route("/signup",methods=['GET','POST'])
def signUp():
    # if request.method == "POST":
    #     uname = request.form.get("username")
    #     upasw = request.form.get("password")
    #     uemail = request.form.get("email")
    #     upass = encrypt(upasw)

    #     print(uname,upass)
    #     if len(db.search(tinydb.where('username') == uname)) == 0:
    #         db.insert({'username': uname,"email":uemail, 'password': upass})
    #         return redirect("/")
    #     else:
    #         return redirect(f"/error?msg=you already have a account with username {uname}")
        

    # return render_template("signup.html")
    return redirect("/login")

@app.route("/error")
def error_page():
    error404 = request.args.get("msg")
    return render_template("error.html",error=error404)

# @app.get("/api/room-updates")
# def room_updates():
#     msg_id = request.args.get("id")
#     try :
#         latestmsg =jsonify({"messages":[chatroom[-1]]}) 
#     except:
#         latestmsg =jsonify({"messages":[]}) 
#     if msg_id == "new-client-200":

#         return latestmsg
#     else:
#         for i,k in enumerate(chatroom):
#             if k['id'] == msg_id:             
#                 data = chatroom.copy()
#                 data = data[i+1:]
#                 print(data)
#                 return jsonify({"messages":data})
#         return latestmsg

# @app.post("/api/send-msg")
# def send_msg():
#     reply = request.get_json()
#     id = uuid.uuid4()
#     data = {"user":reply['user'], "msg":reply['msg'],"id":str(id.int)}
#     if len(chatroom)> 70:
#         try: 
#             chatroom.remove(chatroom[0])
#         except:
#             pass
#     chatroom.append(data)
    

#     return jsonify({"status":200})

# @app.get("/api/admin/download")
# def download_data():
#     return send_file("./db/db.json",as_attachment=True)

if __name__== "__main__":
    app.run(debug=True, host="0.0.0.0")