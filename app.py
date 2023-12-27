import sqlite3
from flask import Flask, render_template


app = Flask(__name__)

@app.route('/')  
def index():
    """
    Route for the home page.

    Retrieves CV data from the SQLite database and renders the 'index.html' template.

    Returns:
        str: Rendered HTML content for the home page.
    """
    conn = sqlite3.connect('cv_database.db')
    c = conn.cursor()
    c.execute("SELECT * FROM cv_data")  
    cv_data = c.fetchall()  # Use fetchall() to get all rows
    conn.close()

    return render_template('index.html', cv_data=cv_data)

@app.route('/cv')
def cv():
    """
    Route for the CV page.

    Retrieves CV data from the SQLite database and renders the 'cv2.html' template.

    Returns:
        str: Rendered HTML content for the CV page.
    """
    conn = sqlite3.connect('cv_database.db')
    c = conn.cursor()
    c.execute("SELECT * FROM cv_data")  
    cv_data = c.fetchall()
    conn.close()

    return render_template('cv2.html', cv_data=cv_data)

if __name__ == '__main__':
    app.run(debug=True)

