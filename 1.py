from flask import Flask,request,render_template
import re
app=Flask(__name__)
a=""
b=""
c=""
d=""
e=""
f=""
g=""
h=""
i=""
j=""
k=""
l=""
m=""
n=""
@app.route("/")
def A():
	return render_template("1.html")
@app.route("/register",methods=["POST"])
def B():
    global a
    a=request.form.get("a")
    r2=""
    with open("1","r",encoding="utf-8") as r:
        for r1 in r:
            r2+=r1
        if a in r2:
            return "这个域名已经注册过了"
    with open("1","a",encoding="utf-8") as f:
        f.write(f"{a}\n")
    return """
    <h1>域名已注册完成!!!</h1>
    <p>域名是:"""+a+"""</p>
    <a href="/static/add.htm">请点击此链接去往添加记录页面</a><br>
    <code>这个域名太棒啦!!!</code>
    <script>
	localStorage.setItem("a",\""""+a+"""\");
    </script>
    """
@app.route("/add/go",methods=["POST"])
def C():
    global b,c,d
    b=request.form.get("b")
    c=request.form.get("c")
    d=request.form.get("d")
    with open(f"D:\\a\\{b}","w",encoding="utf-8") as f:
        f.write(f"{c}\n{d}")
    return """记录已修改✅✅✅"""
@app.route("/visit/start/go",methods=["GET"])
def D():
    global e
    e5=""
    e=request.args.get("e")
    e1=e.replace("https://","",1).split("/")[0]
    e1_2=e.replace("https://","",1).split("/")[1]
    with open(f"D:\\a\\{e1}","r",encoding="utf-8") as r:
        e2=r.read()
        e3=e2.split("\n")[0]
        e4=e2.split("\n")[1]
        if e3=="CNAME" or e3=="A":
            e5=f"https://{e4}/{e1_2}"
        elif e3=="HTML":
            e5=f"/HTML/show?code={e4}"
        else:
            e5="/type"
    return render_template("2.html",e5=e5)
@app.route("/HTML/show",methods=["GET"])
def E():
    f=request.args.get("code")
    return render_template("3.html",f=f)
@app.route("/type")
def F():
    return """
    <h1>填入的解析类型不存在</h1>
    """
@app.route("/fetch",methods=["GET"])
def G():
    global g
    g=request.args.get("fetch")
    g5=""
    g1=g.replace("https://","",1).split("/")[0]
    g1_2=g.replace("https://","",1).split("/")[1]
    with open(f"D:\\a\\{g1}","r",encoding="utf-8") as r:
        g2=r.read()
        g3=g2.split("\n")[0]
        g4=g2.split("\n")[1]
        if g3=="CNAME" or g3=="A":
            g5=f"https://{g4}/{g1_2}"
        elif g3=="HTML":
            g5=f"https://xushi-1009.cc/HTML/show?code={e4}"
        else:
            g5="/type"
    return render_template("4.html",g5=g5)
@app.route("/1.com/r",methods=["POST"])
def H():
    global h,i
    h=request.form.get("email")
    i=request.form.get("password")
    with open(f"D:\\b\\{i}","w",encoding="utf-8") as f:
        f.write(f"{h}")
    return render_template("5.html")
@app.route("/1.com",methods=["GET"])
def I():
    global j,k
    j=request.args.get("email")
    k=request.args.get("message") or "你还没有新消息"
    return f"已发送给{j}:{k}"
@app.route("/2.com",methods=["GET"])
def J():
    global l,m,k
    r1=""
    l=request.args.get("email")
    m=request.args.get("password")
    with open(f"D:\\b\\{m}","r",encoding="utf-8") as r:
        r1=r.read()
    return render_template("6.html",k=k,l=l)
@app.route("/bus",methods=["GET"])
def K():
    global n
    n=request.args.get("url")
    g5=""
    g1=g.replace("https://","",1).split("/")[0]
    g1_2=g.replace("https://","",1).split("/")[1]
    with open(f"D:\\a\\{g1}","r",encoding="utf-8") as r:
        g2=r.read()
        g3=g2.split("\n")[0]
        g4=g2.split("\n")[1]
        if g3=="CNAME" or g3=="A":
            g5=f"https://{g4}/{g1_2}"
        elif g3=="HTML":
            g5=f"https://xushi-1009.cc/HTML/show?code={e4}"
        else:
            g5="/type"
    return render_template("7.html",g5=g5)
app.run(host="localhost",port=2025)