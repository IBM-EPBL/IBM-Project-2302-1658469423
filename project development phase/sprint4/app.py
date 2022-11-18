import flask
from flask import request,render_template
from flask_cors import CORS 
import joblib

app=flask.Flask(__name__,static_url_path="")
CORS(app)
@app.route('/',methods=['GET'])
def sendHomePage():
    return render_template('index.html')
@app.route('/predict',methods=['POST'])
def predictdisease():
    rbc=float(request.form['rbc'])
    pc =float(request.form['pc'])
    bgr=float(request.form['bgr'])
    bu=float(request.form['bu'])
    pe=float(request.form['pe'])
    ane=float(request.form['ane'])
    dm=float(request.form['dm'])
    cad=float(request.form['cad'])
    x=[[rbc,pc,bgr,bu,pe,ane,dm,cad]]
    model=joblib.load('kidney.pkl')
    disease=model.predict(x)[0]
    return render_template('predict.html',predict=disease)

if __name__=='__main__':
    app.run()