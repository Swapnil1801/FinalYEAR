
from flask import Flask,render_template,request, url_for, redirect,flash,Markup

import mysql.connector
import DiamondTest as t
import pymysql
from werkzeug.utils import secure_filename
import jsonify

app = Flask(__name__,template_folder='templates')


conn = pymysql.connect(host='localhost', port=3308, user='root', passwd='root', db='diamond')
cur = conn.cursor()

@app.route('/')
def home():
    return render_template('home1.html')


@app.route('/CallUser',methods=['GET','POST'])
def CallUser():
    return render_template('User_Login.html')



@app.route('/CallAdmin',methods=['GET','POST'])
def CallAdmin():
    return render_template('Admin_Login.html')



@app.route('/UserHome',methods=['GET','POST'])
def UserHome():
    UserEmail = request.form['email']
    UserPwd = request.form['pwd']

    sql = "select * from user where Email ='" + UserEmail + "' And Password ='" + UserPwd+ "'"

    cur.execute(sql)

    if cur.rowcount > 0:
        return render_template('CheckDiamondQuality.html')
    else:
        return render_template('User_Login.html')








@app.route('/upload', methods = ['GET', 'POST'])
def upload():
    if request.method == 'POST':
     f = request.files['file']
     f.save(secure_filename(f.filename))
     name = f.filename
     print(name)

     t.classify(name)

     sql = "select * from DiamondDetails where ImageName = %s"
     adr = (name,)

     cur.execute(sql, adr)

     data=cur.fetchall()
     print(data)

     return render_template('result1.html',data=data)



if __name__ == '__main__':
    app.run(debug=True)