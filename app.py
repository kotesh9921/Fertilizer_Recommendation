from flask import *
from numpy import *
import joblib
app=Flask(__name__)
p={
  "17": "Urea",
  "10": "DAP",
  "13": "MOP",
  "5": "19:19:19 NPK",
  "15": "SSP",
  "14": "Magnesium Sulphate",
  "1": "10:26:26 NPK",
  "7": "50:26:26 NPK",
  "9": "Chilated Micronutrient",
  "2": "12:32:16 NPK",
  "11": "Ferrous Sulphate",
  "3": "13:32:26 NPK",
  "8": "Ammonium Sulphate",
  "0": "10:10:10 NPK",
  "12": "Hydrated Lime",
  "18": "White Potash",
  "6": "20:20:20 NPK",
  "4": "18:46:00 NPK",
  "16": "Sulphur"
}


model=joblib.load("model.pkl")
@app.route('/',methods=['GET',"POST"])
def index():
    if request.method == 'GET':
        return render_template('index.html')
    else:
        x=[int(i) for i in request.form.values()]
        x=array(x).reshape(1,-1)
        x=model.predict(x)
        return render_template('index.html',pred=p[str(x[0])])
app.run()