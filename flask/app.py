from flask import Flask, render_template,request

app = Flask(__name__) 

data = {}

@app.route("/")
def home():
    name  = input("User please tell me your name")
    data['name'] = name

    return render_template("home.html", data = {'name':name})

@app.route("/add" ,methods=['GET','POST'])
def about():
    if request.method=="POST":
        num1 = int(request.form['num1'])
        num2 = int(request.form['num2'])
        result = num1 + num2 


        return render_template("About.html", result = {"result":result})

    else:
        return render_template('about.html',result = {"result":"result"})


if __name__ == "__main__":

    app.run(debug=True)