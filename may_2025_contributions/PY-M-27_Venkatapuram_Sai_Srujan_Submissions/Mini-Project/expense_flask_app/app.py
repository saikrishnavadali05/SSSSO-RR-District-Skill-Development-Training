from flask import Flask, render_template, request, redirect, send_file
import pandas as pd
import os
from datetime import datetime
import matplotlib.pyplot as plt
from io import BytesIO

app = Flask(__name__)

CSV_FILE = r"C:\Users\saisr\OneDrive\Desktop\SSSSO-RR-District-Skill-Development-Training\may_2025_contributions/PY-M-27_Venkatapuram_Sai_Srujan_Submissions/Mini-Project/expense_flask_app/exxpenses_app.csv"
HEADERS = ['Date', 'Type', 'Category', 'Amount', 'Description']


def load_data():
    if not os.path.exists(CSV_FILE) or os.stat(CSV_FILE).st_size == 0:
        df = pd.DataFrame(columns=HEADERS)
        df.to_csv(CSV_FILE, index=False)
        return df

    try:
        df = pd.read_csv(CSV_FILE, header=0, names=HEADERS, on_bad_lines='skip')
        df['Date'] = pd.to_datetime(df['Date'], errors='coerce')
        df['Amount'] = pd.to_numeric(df['Amount'], errors='coerce').fillna(0.0)
        df = df.dropna(subset=['Type', 'Category'])
        df = df[df['Type'].str.upper() != 'SUMMARY']
        return df
    except Exception as e:
        print(f"Error loading data: {e}")
        return pd.DataFrame(columns=HEADERS)


def save_data(df):
    df.to_csv(CSV_FILE, index=False)


@app.route('/')
def index():
    df = load_data()
    income = df[df['Type'] == 'income']['Amount'].sum()
    expense = df[df['Type'] == 'expense']['Amount'].sum()
    net = income - expense
    return render_template("index.html", data=df.to_dict(orient='records'), income=income, expense=expense, net=net)


@app.route('/add', methods=['GET', 'POST'])
def add_transaction():
    if request.method == 'POST':
        df = load_data()
        date = request.form.get('date') or datetime.today().strftime('%Y-%m-%d')
        ttype = request.form['type']
        category = request.form['category']
        try:
            amount = float(request.form['amount'])
        except ValueError:
            amount = 0.0
        description = request.form.get('description', '')

        new_row = pd.DataFrame([[date, ttype, category, amount, description]], columns=HEADERS)
        df = pd.concat([df, new_row], ignore_index=True)
        save_data(df)
        return redirect('/')

    return render_template("add.html")


@app.route('/report')
def monthly_report():
    df = load_data()
    if df.empty:
        return "No data available."

    df['Month'] = df['Date'].dt.to_period('M')
    summary = df.groupby('Month').agg(
        Income=('Amount', lambda x: x[df.loc[x.index, 'Type'] == 'income'].sum()),
        Expenses=('Amount', lambda x: x[df.loc[x.index, 'Type'] == 'expense'].sum())
    ).reset_index()
    summary['Net'] = summary['Income'] - summary['Expenses']
    return render_template("report.html", summary=summary.to_dict(orient='records'))


@app.route('/plot/trends')
def plot_trends():
    df = load_data()
    if df.empty:
        return "No data to plot."

    df['Month'] = df['Date'].dt.to_period('M')
    trend = df.groupby('Month').agg(
        Income=('Amount', lambda x: x[df.loc[x.index, 'Type'] == 'income'].sum()),
        Expenses=('Amount', lambda x: x[df.loc[x.index, 'Type'] == 'expense'].sum())
    ).reset_index()
    trend['Net'] = trend['Income'] - trend['Expenses']
    trend['Month'] = trend['Month'].dt.to_timestamp()

    plt.figure(figsize=(8, 5))
    plt.plot(trend['Month'], trend['Income'], label='Income', marker='o')
    plt.plot(trend['Month'], trend['Expenses'], label='Expenses', marker='o')
    plt.plot(trend['Month'], trend['Net'], label='Net', linestyle='--')
    plt.legend()
    plt.title("Monthly Financial Trends")
    plt.xlabel("Month")
    plt.ylabel("Amount")
    plt.grid(True)
    plt.tight_layout()

    img = BytesIO()
    plt.savefig(img, format='png')
    img.seek(0)
    return send_file(img, mimetype='image/png')


if __name__ == "__main__":
    app.run(debug=True)
