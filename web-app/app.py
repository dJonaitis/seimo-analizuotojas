from flask import Flask, render_template, request

import pandas as pd


#FLASK APP
app = Flask(__name__)

today = pd.Timestamp.today().strftime('%Y-%m-%d')
today_laws = pd.read_csv(f'{today}_laws.csv')

# ROUTING
@app.route("/")
def index():
    return render_template("landing.html")





if __name__ == "__main__":
    app.run(port=3000, debug=True)