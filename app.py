from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)

@app.route('/')  
def index():
    conn = sqlite3.connect('cv_database.db')
    c = conn.cursor()
    c.execute("SELECT * FROM cv_data")  
    cv_data = c.fetchall()  # Use fetchall() to get all rows
    conn.close()

    return render_template('index.html', cv_data=cv_data)

@app.route('/cv')
def cv():
    conn = sqlite3.connect('cv_database.db')
    c = conn.cursor()
    c.execute("SELECT * FROM cv_data")  
    cv_data = c.fetchall()
    conn.close()

    return render_template('cv2.html', cv_data=cv_data)

if __name__ == '__main__':
    app.run(debug=True)
