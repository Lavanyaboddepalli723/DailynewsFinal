from flask import Flask, render_template,request,redirect,url_for
import requests
import sqlite3


app = Flask(__name__)
app.secret_key = 'secret123'

@app.route('/')
def home():
    return render_template('mainpage.html')

@app.route('/home')
def index():
    url = "https://newsapi.org/v2/top-headlines?country=in&category=general&apiKey=7e1737d3191d4fe894fc579df01b7bde"
    r= requests.get(url).json()
    case = {
        'articles': r['articles']
    }
    return render_template('index.html',cases = case)
@app.route('/sports')
def sports():
    url = "https://newsapi.org/v2/top-headlines?country=in&category=sports&apiKey=7e1737d3191d4fe894fc579df01b7bde"
    r= requests.get(url).json()
    case = {
        'articles': r['articles']
    }
    return render_template('sports.html',cases = case)

@app.route('/business')
def business():
    url = "https://newsapi.org/v2/top-headlines?country=in&category=business&apiKey=7e1737d3191d4fe894fc579df01b7bde"
    r= requests.get(url).json()
    case = {
        'articles': r['articles']
    }
    return render_template('business.html',cases = case)

@app.route('/technology')
def technology():
    url = "https://newsapi.org/v2/top-headlines?country=in&category=technology&apiKey=7e1737d3191d4fe894fc579df01b7bde"
    r= requests.get(url).json()
    case = {
        'articles': r['articles']
    }
    return render_template('tech.html',cases = case)

@app.route('/science')
def science():
    url = "https://newsapi.org/v2/top-headlines?country=in&category=science&apiKey=7e1737d3191d4fe894fc579df01b7bde"
    r= requests.get(url).json()
    case = {
        'articles': r['articles']
    }
    return render_template('science.html',cases = case)

@app.route('/health')
def health():
    url = "https://newsapi.org/v2/top-headlines?country=in&category=health&apiKey=7e1737d3191d4fe894fc579df01b7bde"
    r= requests.get(url).json()
    case = {
        'articles': r['articles']
    }
    return render_template('health.html',cases = case)

@app.route('/login',methods=['GET','POST'])
def login():
    t = 0
    if request.method == 'POST':
        username = request.form.get("username")
        password = request.form.get("password")
        conn = sqlite3.connect("users.db")
        c = conn.cursor()
        query = "SELECT * FROM readers where username=?"
        c.execute(query,(username,))
        tables = c.fetchall()
        conn.commit()
        conn.close()
        if  tables and tables[0][0] and tables[0][2]==password:
            return render_template('user.html')
        else:
            t = 1
    return render_template('login.html',t=t)

@app.route('/signup',methods=['GET','POST'])
def signup():
    t = 0
    if request.method == 'POST':
        username = request.form.get("username")
        password = request.form.get("password")
        conn = sqlite3.connect("users.db")
        c = conn.cursor()
        query = "SELECT * FROM readers where username=?"
        c.execute(query,(username,))
        r = c.fetchall()
        conn.commit()
        conn.close()
        if not r :
            conn = sqlite3.connect("users.db")
            c = conn.cursor()
            query = "INSERT INTO readers (username, password) VALUES(?, ?)"
            c.execute(query,(username,password))
            conn.commit()
            conn.close()
            return redirect(url_for('login'))
        else:
            t = 1 
    return render_template('signup.html',t=t)

def create_user_table():
    conn = sqlite3.connect("users.db")
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS readers
              (id INTEGER PRIMARY KEY AUTOINCREMENT,
              username TEXT,
              password TEXT)''')
    
if __name__ == '__main__':
    create_user_table()
    app.run(debug=True)
