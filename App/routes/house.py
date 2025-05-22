from flask import Blueprint,render_template,jsonify,request
import os 
import joblib

house_bp=Blueprint("house",__name__,template_folder="../templates",static_folder="../static")

house_model=""

@house_bp.route("/")
def house_ui():
    return render_template("house_page.html")

@house_bp.route("/housepredict",methods=["POST"])
def wine_prediction():

    data = request.get_json()
    user_data=[]
    for i in data:
        user_data.append(data[i])

    pred = round(house_model.predict([user_data])[0],2)
    
    return jsonify(pred)


def model_loading():

    global house_model

    BASE_DIR = os.path.dirname(os.path.abspath(__file__)) 
    MODEL_PATH = os.path.join(BASE_DIR, '..', 'model_file', 'house_price_prediction_model.joblib')
    MODEL_PATH = os.path.abspath(MODEL_PATH)

    house_model = joblib.load(MODEL_PATH)

model_loading()