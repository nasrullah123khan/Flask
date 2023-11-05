from flask import Flask, render_template,request,jsonify

app = Flask(__name__) 

@app.route("/")
def home():
    name  = "Nasir",
    age = 23
    data = {'name':name, 'age':age}

    return jsonify(data)
app.run(debug=True)