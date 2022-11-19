import numpy as np
import pandas as pd
import flask

from flask import Flask, request, redirect, render_template
import pickle

loaded_reg = pickle. load(open('randomreg_chronic.pkl', 'rb'))

app = Flask(__name__,static_url_path="")
@app.route('/',methods=['GET'])
def index():
    return render_template('index.html')
@app.route('/val',methods=['POST'])


def val():
    test=[]
    if request.method == 'POST':
        test.append(float(request.form["age"]))
        test.append(float(request.form["bp"]))
        test.append(float(request.form["sg"]))
        test.append(float(request.form["al"]))
        test.append(float(request.form["su"]))
        rb=request.form["rbc"]
        if rb==0:
            test.append(1)
        else:
            test.append(0)
        pc=request.form["pc"]
        if pc==0:
            test.append(1)
        else:
            test.append(0)
        pcc=request.form["pcc"]
        if pcc==1:
            test.append(1)
        else:
            test.append(0)
        ba=request.form["ba"]
        if ba==1:
            test.append(1)
        else:
            test.append(0)
        test.append(float(request.form["bgr"]))
        test.append(float(request.form["bu"]))
        test.append(float(request.form["sc"]))
        test.append(float(request.form["sod"]))
        test.append(float(request.form["pot"]))
        test.append(float(request.form["hemo"]))
        test.append(float(request.form["pcv"]))
        test.append(float(request.form["wc"]))
        test.append(float(request.form["rc"]))
        ht=request.form["htn"]
        if ht==1:
            test.append(1)
        else:
            test.append(0)
        d=request.form["dm"]
        if d==1:
            test.append(1)
        else:
            test.append(0)
        ca=request.form["cad"]
        if ca==1:
            test.append(1)
        else:
            test.append(0)
        ap=request.form["appet"]
        if ap==1:
            test.append(1)
        else:
            test.append(0)
        
        p=request.form["pe"]
        if p==1:
            test.append(1)
        else:
            test.append(0)
        an=request.form["ane"]
        if an==1:
            test.append(1)
        else:
            test.append(0)
    print(test)
    test_df=pd.DataFrame(test)
    test_df=np.array(test_df).reshape(1, -1)
    
    ans2=loaded_reg.predict(test_df)
    if int(ans2)==1:
        answer1="You have CHRONIC DISEASE!!!"
        return render_template('rename.html',answer1=answer1)
    else:
        answer1="You don't have CHRONIC DISEASE"

        return render_template('rename2.html',answer1=answer1)
    
if __name__ == "__main__":
    app.debug=True
    app.run(debug=False)
