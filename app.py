from flask import Flask, request, jsonify, render_template
from numpy import ceil
import pandas as pd
from flask_cors import CORS
import math

app = Flask(__name__)
CORS(app)
df = pd.read_csv('dataset.csv')

def data(cus_id):
    cur_df = df.loc[df['Coustomer ID'] == cus_id].reset_index()
    name = cur_df['Name'].to_numpy()[0]
    rating = cur_df['Rating'].to_numpy()[0]
    total_orders = cur_df['Total Orders'].to_numpy()[0]
    ret_orders = cur_df['Orders Returned'].to_numpy()[0]
    total_amount = cur_df['Total Amount'].to_numpy()[0]
    ret_amount = cur_df['Returned Amount'].to_numpy()[0]
    difference = cur_df['Difference in Days'].to_numpy()[0]

    credit = math.trunc(((1-(ret_orders/total_orders)) + (1-(ret_amount/total_amount)) + (1-(rating/5)) + (1-(difference/7)))*25)

    if ret_orders == 0:
        credit = 95
    return {
        "name": name,
        "credit": credit,
        "total": total_orders,
        "ret": ret_orders
    }

@app.route('/calculator', methods = ['POST', 'GET'])
def calci():
    if request.method == "POST":
        s1 = int(request.form['username'])
        res = data(s1)        
        return render_template('calculator.html', data = res)
    return render_template('calculator.html', data = {
        "name": None,
        "credit": 0,
    })

@app.route('/login')
def login():    
    return render_template('login.html')

@app.route('/')
def dashboard():
    return render_template('dashboard.html')

@app.route('/aboutus')
def dashboar():
    return render_template('aboutus.html')

@app.route('/contactus')
def dashboa():
    return render_template('contactus.html')


if __name__ == '__main__':
    app.run(debug=True)