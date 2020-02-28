import csv
import io
import json

import flask
import pandas as pd
import requests
from flask import Flask, Response, jsonify

app = Flask(__name__)

@app.route('/csv')

def write_to_csv():
    response = requests.get("https://services.cars45.ng/index.php?route=api/product&apikey=eSjItOjFfvzaDuCFG4N0WfrbmMekdk8y")
    cars_data = response.json()
    df = pd.DataFrame(cars_data)
    df_tr = df.transpose()
    df_tr['img_base_url'] = 'https://buy.cars45.com/image/'
    df_tr['image'] = df_tr['img_base_url'].map(str) + df_tr['image'].map(str)
    df_csv = df_tr.to_csv
    si = io.StringIO()
    df_csv = df_tr.to_csv()
    return Response(
        df_csv,
        mimetype="text/csv",
        headers={"Content-disposition":
                 "attachment; filename=cars_data.csv"})    
app.run()
