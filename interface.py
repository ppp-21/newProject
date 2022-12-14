from flask import Flask,render_template,request,jsonify
from utils import Houseprd

hp=Houseprd()

app = Flask(__name__)

@app.route('/')
def index():
   return render_template('home.html')


@app.route('/get_location_names')
def get_location_names():
    locations =  hp.get_location_names()  
    return jsonify({"locations":locations})


@app.route('/predict_home_price', methods = ['POST','GET'])
def predict_home_price():
    if request.method == 'POST':
        user_data = request.form
        
        total_sqft = eval(user_data['sqft'])

        bhk = eval(user_data['bhk'])
        bath = eval(user_data['bath'])
        location = "location_"+user_data['loc']
        print('location, sqft, bath, bhk',location, total_sqft, bath, bhk)
        price = hp.get_house_price(location, total_sqft, bath, bhk)
        
        #return jsonify({"Message": f"Predicted House price is {price} Lakh"})
        return render_template('home.html', prediction_text = price)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080, debug=False)   
