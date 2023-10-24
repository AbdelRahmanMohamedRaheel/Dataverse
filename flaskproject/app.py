
from flask import Flask, render_template , request , redirect, url_for , flash
from flask_mysqldb import MySQL 


raheel = Flask(__name__)
raheel.secret_key = 'raheelsecretkey'


raheel.config['MYSQL_HOST'] = '127.0.0.1'
raheel.config['MYSQL_USER'] = 'root'
raheel.config['MYSQL_PASSWORD'] = 'password'
raheel.config['MYSQL_DB'] = 'Mydata'


mysql = MySQL(raheel)  
  

@raheel.route("/")
def homepage():
    return render_template('home.html')


@raheel.route("/showusers")
def show_data():
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT * FROM Users")
    data = cursor.fetchall()   
         
    return render_template('htmlfile.html', data=data)






@raheel.route("/adduser" , methods=['POST', 'GET'])
def add_user():
  if request.method == 'POST':
         
         name = request.form['name']
         phone_no = request.form['phone_no']
         password = request.form['password']
         address = request.form['address']

         cursor = mysql.connection.cursor()
         cursor.execute("INSERT INTO Users (name, phone_no, password, address) VALUES (%s, %s, %s, %s)",
                       (name, phone_no, password, address))
         mysql.connection.commit()
         cursor.close()
         
         return redirect(url_for('homepage'))
    

  return render_template('adduser.html')


@raheel.route("/delete", methods=['GET', 'POST'])
def delete_user():
    if request.method == 'POST':
        phone_no = request.form.get('phone_no')  
        cursor = mysql.connection.cursor()
        Phone = cursor.execute("SELECT phone_no FROM Users WHERE phone_no = %s", (phone_no,))
        # print(Phone)
        if Phone > 0:
            cursor.execute("DELETE FROM Users WHERE phone_no = %s", (phone_no,))
            mysql.connection.commit()
            cursor.close()
            flash("User with phone number {} deleted successfully.".format(phone_no), "success")
        else:
             flash("User with phone number {} not found.".format(phone_no), "error")

    return render_template('delete.html')




       
    
if __name__ == "__main__":
    raheel.run(debug=True, port=5000)
