
from flask import Flask, request, url_for, redirect, render_template
import pickle
import json
import config
from Project_app import utils
import numpy as np


app = Flask(__name__, template_folder='./templates', static_folder='./static')

with open(config.MODEL_FILE_PATH,"rb") as f:
            model=pickle.load(f)
@app.route('/')

def hello_world():
    return render_template('login.html')



@app.route('/predict', methods=['POST','GET'])
def predict():
    print([x for x in request.form.values()])
    features = [x for x in request.form.values()]
    age=features[0]
    sex=features[1]
    bmi=features[2]
    children=features[3]
    smoker=features[4]
    region=features[5]
    print(features)
    md=utils.MedicalInsurance(age,sex,bmi,children,smoker,region)
    # final = np.array(features).reshape((1,6))
    # print(final)
    # pred = model.predict(final)[0]
    # print(pred)
    pred=md.get_predicted_charges()
    
    return render_template('op.html', pred='Expected amount is {}'.format(pred))

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=False)  
       


app.run()