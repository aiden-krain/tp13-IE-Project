from flask import Flask,render_template,url_for,request,jsonify
import pandas as pd
import json
#import openpyxl
import mysql.connector
import sqlite3
app = Flask(__name__)
#ozcobbydb = mysql.connector.connect(
#    host="tp13mysqlserver.mysql.database.azure.com",
#    user="tp13admin",
#    password="Project5120",
#    database="ozcobby"
#)
#subcursor = ozcobbydb.cursor()
#subcursor.execute("SELECT DISTINCT Suburb FROM median_rent")
#sub_names = []
#for sub in subcursor:
#    sub_names.append(list(sub)[0])

@app.route('/')
def home():
    return render_template('index.html')
@app.route('/recommendation', methods=["POST", "GET"])
def get_recommendation():
    return render_template('recommendation.html')

suburbs = ['Albert Park-Middle Park-West St Kilda','Armadale','Carlton North','Carlton-Parkville','CBD-St Kilda Rd',
'Collingwood-Abbotsford','Docklands','East Melbourne','East St Kilda','Elwood','Fitzroy',
'Fitzroy North-Clifton Hill','Flemington-Kensington','North Melbourne-West Melbourne',
'Port Melbourne','Prahran-Windsor','Richmond-Burnley','South Melbourne','South Yarra','Southbank','St Kilda','Toorak',
'Balwyn','Blackburn','Box Hill','Bulleen-Templestowe-Doncaster','Burwood-Ashburton','Camberwell-Glen Iris',
'Canterbury-Surrey Hills-Mont Albert','Chadstone-Oakleigh','Clayton','Doncaster East-Donvale','East Hawthorn',
'Glen Waverley-Mulgrave','Hawthorn','Kew','Mount Waverley','Nunawading-Mitcham','Vermont-Forest Hill-Burwood East',
'Aspendale-Chelsea-Carrum','Bentleigh','Brighton','Brighton East','Carnegie','Caulfield','Cheltenham','Elsternwick',
'Hampton-Beaumaris','Malvern','Malvern East','Mentone-Parkdale-Mordialloc','Murrumbeena-Hughesdale',
'Altona','Footscray','Keilor East-Avondale Heights','Melton','Newport-Spotswood','St Albans-Deer Park','Sunshine',
'Sydenham','Werribee-Hoppers Crossing','West Footscray','Williamstown','Yarraville-Seddon',
'Broadmeadows-Roxburgh Park','Brunswick','Coburg-Pascoe Vale South','Craigieburn','East Brunswick','Essendon',
'Gladstone Park-Tullamarine','Keilor','Moonee Ponds-Ascot Vale','Oak Park-Glenroy-Fawkner','Pascoe Vale-Coburg North',
'Sunbury','West Brunswick','Berwick','Cranbourne','Dandenong','Dandenong North-Endeavour Hills',
'Narre Warren-Hampton Park','Noble Park','Pakenham','Springvale']

median_rent = pd.read_excel("Final_file.xlsx")
#suburb_req=10
@app.route('/accommodation', methods=["POST", "GET"])
def get_accommodation():
    while True:
        if request.method == "GET":
            #search = request.args.get('autocomplete')
            #app.logger.debug(search)
            return render_template('accommodation.html', suburbs=suburbs)
        if request.method == "POST":
            suburb_req = request.form['suburb']
            median_value = median_rent[median_rent['Suburb'] == suburb_req]
            median_value = median_value[median_value['Quarter'] == "Sep"]
            median_value = median_value[median_value['Property type'] == "Suburbs - All properties"]
            median_value = median_value[median_value['Year'] == 2021]
            a = ""
            if len(median_value) == 1:
                suburb_req = median_value.iloc[0]['Median']
                if suburb_req <= 250:
                    a = " less "
                else:
                    a = " more "
                answer_sub = "The weekly median rent price of " + request.form['suburb'] + " is " + str(suburb_req) + \
                             ". This value is" + a + "than the median weekly price of all suburbs which is $250."
            if len(median_value) != 1:
                answer_sub = "Suburb not found"
            return render_template('accommodation.html', answer_sub=answer_sub, suburbs=suburbs)
    #return render_template('accommodation.html')
if __name__ == '__main__':
    app.run(debug=True)