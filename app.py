#!pip install flask-ngrok 
import sqlite3
from flask import Flask,render_template,request,url_for
#from flask_ngrok import run_with_ngrok
app = Flask(__name__)
#run_with_ngrok(app)

@app.route('/')
def home():
  
    return  render_template('home.html')

@app.route('/enternew')
def new_student():
   return render_template('student.html')    

@app.route('/addrec',methods = ['POST', 'GET'])
def addrec():
   if request.method == 'POST':
      #try:
         nm = request.form.get('nm')
         addr = request.form.get('add')
         city = request.form.get('city')
         pin = request.form.get('pin')
         conn=sqlite3.connect("C:\\Users\\ishuk\\Desktop\\sem 6\\lab\\python\\12\\my_db.db")
            
         cur = conn.cursor()
         cur.execute("INSERT INTO students (name,addr,city,pin) VALUES (?,?,?,?)",(nm,addr,city,pin))
         conn.commit()  
         msg = "Student successfully Added"  
         return render_template("result.html",msg = msg)
         conn.close()

@app.route('/list')
def list():
   
   
    conn=sqlite3.connect("C:\\Users\\ishuk\\Desktop\\sem 6\\lab\\python\\12\\my_db.db")
  
    conn.row_factory = sqlite3.Row  
    cur = conn.cursor()  
    cur.execute("select * from students")  
    rows = cur.fetchall()  
    return render_template("list.html",rows = rows)  

@app.route('/del_student')
def del_student():
    conn=sqlite3.connect("C:\\Users\\ishuk\\Desktop\\sem 6\\lab\\python\\12\\my_db.db")
  
      
    cur = conn.cursor()  
    cur.execute("delete from students")
    conn.commit()    
    return render_template("list.html") 

    



if __name__ == '__main__':
   app.run() 