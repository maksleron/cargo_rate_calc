from flask import Flask
from datetime import datetime
import json

app = Flask(__name__)

@app.route('/cargo_type=<cargo_type>')
def get_sum(cargo_type):
    current_date = datetime.today().strftime('%Y-%m-%d')
    print("Дата: " + current_date)
    print("Тип груза: " + cargo_type)
    return "<p>Accepted!</p>"