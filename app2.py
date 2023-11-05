from flask import Flask, request, render_template

app = Flask(__name__)

data = []

@app.route("/", methods=["GET","POST"])
def home2():
    if request.method=='POST':
        name = request.form['name']
        email = request.form['email']
        roll = request.form['roll']
        course = request.form['course']
        record1 = {
            'name':name,
            'email':email,
            'roll':roll,
            'course':course
        }
        data.append(record1)
         
    return render_template("home2.html")
    

@app.route("/about", methods=["GET","POST"])
def about():
    return render_template("about.html", data=data)

    
if __name__=="__main__":
    app.run(debug=True)