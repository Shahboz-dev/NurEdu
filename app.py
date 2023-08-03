from flask import Flask,render_template , request
import sqlite3 as sql

app = Flask(__name__)


@app.route('/')

def home():
    return render_template('index.html')

@app.route('/register')

def register():
    return render_template('register.html')

@app.route('/addrec', methods = ['POST','GET'])
def addrec():
    if request.method == 'POST':
        try:
            name = request.form['name']
            number = request.form['number']

            with sql.connect("database.db") as con:
                cur = con.cursor()
                cur.execute("INSERT INTO students (name,phoneNumber) VALUES (? , ?) ", (name,number))
                msg = 'Record added'
        except:
            con.rollback()
            msg = 'Error in INSERT operation'

        finally:
            return render_template('result.html', msg=msg)
            con.close()

if __name__=='__main__':
    app.run(debug=True)