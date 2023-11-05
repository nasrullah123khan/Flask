from flask import Flask, request, render_template, jsonify

app = Flask(__name__)

data = []

@app.route("/", methods=["GET","POST"])
def home():
    if request.method=='POST':
        name = request.json['name']
        email = request.json['email']
        roll = request.json['roll']
        course = request.json['course']
        record1 = {
            'name':name,
            'email':email,
            'roll':roll,
            'course':course
        }
        data.append(record1)
    return jsonify(data)
    

@app.route("/about", methods=["GET","POST"])
def about():
    return jsonify(data)

# @app.route("/",methods=["Put"])
# def update():
#     if request="POST":



    
if __name__=="__main__":
    app.run(debug=True)