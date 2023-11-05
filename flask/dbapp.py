from flask import Flask,request,render_template
from flask_mysqldb import MySQL 

app = Flask(__name__)
mysql = MySQL(app)


app.config['MYSQL_HOST']='localhost'
app.config['MYSQL_USER']='root'
app.config['MYSQL_PASSWORD'] = "Nasrullah123%"
app.config['MYSQL_DB']= 'mydb'


@app.route("/" ,methods=['GET',"POST"])
def index():
    if request.method=="POST":
        id = request.form['studentID']
        lname = request.form['LastName']
        fname = request.form['FirstName']
        address = request.form['Address']
        city = request.form['City']
        
        cur = mysql.connection.cursor()
        
        cur.execute("INSERT INTO students (studentID,LastName, FirstName, Address, City) VALUES (%s,%s,%s,%s,%s)",(id,lname,fname,address,city))
        mysql.connection.commit()
        cur.close()
        return 'Successfully updated record in database'
    return render_template("index.html")

@app.route("/students")
def getstudents():
    cur = mysql.connection.cursor()
    users = cur.execute("SELECT * FROM students")
    if users > 0:
        userDetails = cur.fetchall()
    
    return render_template('students.html',students=userDetails)




if __name__ =="__main__":
    app.run(debug=True)
