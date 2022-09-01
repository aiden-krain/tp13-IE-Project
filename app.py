from flask import Flask, render_template, url_for, request, jsonify
import pandas as pd
import json
# import openpyxl
# import mysql.connector
import sqlite3

app = Flask(__name__)
app.config['MYSQL_HOST'] = 'tp13mysqlserver.mysql.database.azure.com'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'flask'


# sqlite3.connect()

@app.route('/')
def home():
    return render_template('home.html')


@app.route('/recommendation', methods=["POST", "GET"])
def get_recommendation():
    return render_template('recommendation.html')


suburbs = ['Albert Park-Middle Park-West St Kilda', 'Armadale', 'Carlton North', 'Carlton-Parkville', 'CBD-St Kilda Rd'
    , 'Collingwood-Abbotsford', 'Docklands', 'East Melbourne', 'East St Kilda', 'Elwood', 'Fitzroy',
           'Fitzroy North-Clifton Hill', 'Flemington-Kensington', 'North Melbourne-West Melbourne',
           'Port Melbourne', 'Prahran-Windsor', 'Richmond-Burnley', 'South Melbourne', 'South Yarra', 'Southbank',
           'St Kilda', 'Toorak']
median_rent = pd.read_excel("Final_file.xlsx")


# suburb_req=10
@app.route('/accommodation', methods=["POST", "GET"])
def get_accommodation():
    while True:
        if request.method == "GET":
            # search = request.args.get('autocomplete')
            # app.logger.debug(search)
            return render_template('accommodation.html', suburbs=suburbs)
        if request.method == "POST":
            suburb_req = request.form['suburb']
            median_value = median_rent[median_rent['Suburb'] == suburb_req]
            median_value = median_value[median_value['Quarter'] == "Sep"]
            median_value = median_value[median_value['Property type'] == "Suburbs - All properties"]
            median_value = median_value[median_value['Year'] == 2021]
            if len(median_value) == 1:
                suburb_req =  median_value.iloc[0]['Median']
            if len(median_value) != 1:
                suburb_req = "Suburb not found"
            return render_template('accommodation.html', suburb_req=suburb_req)

    # return render_template('accommodation.html')


if __name__ == '__main__':
    app.run(debug=True)
