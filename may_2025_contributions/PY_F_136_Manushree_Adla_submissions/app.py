from flask import Flask, render_template, request, redirect
import csv, os
import pandas as pd
import matplotlib.pyplot as plt
from io import BytesIO
import base64
from datetime import datetime

app = Flask(__name__)
FILENAME = 'expenses.csv'

# Create CSV with headers if not exists
if not os.path.exists(FILENAME):
    with open(FILENAME, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Date', 'Amount', 'Category', 'Description'])

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/add', methods=['POST'])
def add():
    data = [request.form['date'], request.form['amount'], request.form['category'], request.form['description']]
    with open(FILENAME, 'a', newline='') as file:
        csv.writer(file).writerow(data)
    return redirect('/')

@app.route('/summary')
def summary():
    df = pd.read_csv(FILENAME)
    df['Amount'] = pd.to_numeric(df['Amount'], errors='coerce')
    df.dropna(subset=['Amount'], inplace=True)
    income = df[df['Amount'] > 0]['Amount'].sum()
    expense = df[df['Amount'] < 0]['Amount'].sum()
    balance = income + expense
    return f"""
        <h2>📊 Expense Summary</h2>
        <p><strong>Income:</strong> ₹{income}</p>
        <p><strong>Expenses:</strong> ₹{abs(expense)}</p>
        <p><strong>Balance:</strong> ₹{balance}</p>
        <a href='/'>← Back</a>
    """

@app.route('/monthly-report')
def monthly_report():
    df = pd.read_csv(FILENAME)
    df['Date'] = pd.to_datetime(df['Date'], errors='coerce')
    df['Amount'] = pd.to_numeric(df['Amount'], errors='coerce')
    df.dropna(subset=['Date', 'Amount'], inplace=True)

    now = datetime.now()
    month_df = df[(df['Date'].dt.month == now.month) & (df['Date'].dt.year == now.year)]

    if month_df.empty:
        return "<h3>No expense data for this month.</h3><a href='/'>← Back</a>"

    grouped = month_df.groupby('Category')['Amount'].sum()
    plt.figure(figsize=(6,6))
    plt.pie(grouped, labels=grouped.index, autopct='%1.1f%%')
    plt.title("Monthly Expenses by Category")

    img = BytesIO()
    plt.savefig(img, format='png')
    img.seek(0)
    chart_url = base64.b64encode(img.getvalue()).decode()
    plt.close()

    return f"""
        <h2>📅 Monthly Report</h2>
        <img src='data:image/png;base64,{chart_url}'/>
        <br><a href='/'>← Back</a>
    """

if __name__ == '__main__':
    app.run(debug=True)
