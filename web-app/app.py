from flask import Flask, render_template, request, redirect, session


import pandas as pd
import os

# FLASK INITIALISATION
PROJECT_ROOT = os.path.dirname(os.path.realpath(__file__))
filename = pd.Timestamp.today().strftime('%Y-%m-%d') + '_laws.csv'
DATABASE = os.path.join(PROJECT_ROOT, 'data', filename)

df = pd.read_csv(DATABASE)

app = Flask(__name__)




# ROUTING
@app.route("/")
def index():
    return render_template("index.html", 
                           summary=df['summary'].tolist(), 
                           title=df['Pavadinimas'].tolist(),
                           author=df['Pateikė'].tolist(),
                           date=df['Data'].tolist(),
                           number=df['Numeris'].tolist())

if __name__ == "__main__":
    app.run(port=3000, debug=True)