from flask import Flask,render_template,url_for,request,jsonify
import json
app = Flask(__name__)


@app.route('/')
def home():
    return render_template('Home.html')

@app.route('/recommendation', methods=["POST", "GET"])
def get_recommendation():
    return render_template('recommendation.html')


suburbs = ['Albert Park-Middle Park-West St Kilda','Armadale','Carlton North','Carlton-Parkville','CBD-St Kilda Rd'
    ,'Collingwood-Abbotsford','Docklands','East Melbourne','East St Kilda','Elwood','Fitzroy',
     'Fitzroy North-Clifton Hill','Flemington-Kensington','North Melbourne-West Melbourne',
'Port Melbourne','Prahran-Windsor','Richmond-Burnley','South Melbourne','South Yarra','Southbank','St Kilda','Toorak',]
@app.route('/accommodation', methods=["POST", "GET"])
def get_accommodation():
    if request.method == "GET":
        #search = request.args.get('autocomplete')
        #app.logger.debug(search)
        return render_template('accommodation.html', suburbs=suburbs)

if __name__ == '__main__':
    app.run(debug=True)


