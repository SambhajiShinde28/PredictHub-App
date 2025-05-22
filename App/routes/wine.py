from flask import Blueprint,render_template,jsonify,request
import joblib
import os

wine_bp=Blueprint("wine",__name__,template_folder="../templates",static_folder="../static")

wine_model=""

@wine_bp.route("/")
def wine_ui():
    return render_template("wine_page.html")


@wine_bp.route("/winepredict",methods=["POST"])
def wine_prediction():

    data = request.get_json()
    user_data=[]
    for i in data:
        user_data.append(data[i])

    pred = round(wine_model.predict([user_data])[0],2)

    print("This is user data : ",user_data)
    print("This is original data : ",data)
    
    return jsonify(pred)


def model_loading():

    global wine_model

    BASE_DIR = os.path.dirname(os.path.abspath(__file__)) 
    MODEL_PATH = os.path.join(BASE_DIR, '..', 'model_file', 'wine_quality_prediction_model.joblib')
    MODEL_PATH = os.path.abspath(MODEL_PATH)

    wine_model = joblib.load(MODEL_PATH)

model_loading()