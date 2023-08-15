from flask import Flask, request, render_template
from flask_cors import cross_origin
import sklearn
import pickle
import pandas as pd
from sklearn.preprocessing import LabelEncoder
from urllib.request import Request, urlopen
import re
app = Flask(__name__)
model = pickle.load(open("mainBookpickle.pkl", "rb"))


@app.route("/")
@cross_origin()
def home():
	return render_template("index.html")



@app.route("/predict", methods = ["GET", "POST"])
@cross_origin()
def predict():
    if request.method == "POST":
        age = request.form["f1"]
        bp = request.form["f2"]
        rbc = request.form["f3"]
        wbc = request.form["f4"]
        appet = request.form["f5"]
        pc = request.form["f6"]
        htn = request.form["f7"]
        hemo = request.form["f8"]
        bgr = request.form["f9"]
        dm = request.form["f10"]
        ane = request.form["f11"]
        if pc=="Normal":
            pc = 1
        else:
            pc = 0
        if(appet=="Good"):

            appet = 1
        else:
            appet = 0


        


        if htn == "Yes":
            htn =1
        else:
            htn = 0

        if dm == "Yes":
            dm =1
        else:
            dm =0

        if ane ==  "Yes":
            ane = 1
        else:
            ane =0

        prediction = model.predict([[
                age,bp,rbc,wbc,appet,pc,htn,hemo,bgr,dm,ane
            ]])
        prediction = int(prediction)
        yes = ["Sorry! You have predicted positive for the Chronic Kidney Disease. Please consult the Doctor and take the proper measures."]
        yes.extend(find_doctors())
        no = ["You have predicted negative for the Chronic Kidney Disease. Please take care of your health."]
        return render_template('output.html',output= yes if prediction==1 else no)

    return render_template("index.html")

def find_doctors():
    req = Request("https://www.lyfboat.com/doctors/best-nephrology-doctors-in-india/", headers={'User-Agent': 'Mozilla/5.0'})
    webpage = urlopen(req).read().decode('utf-8')
    pattern1 ='India includes the following:'
    arr=[]
    for pos in re.finditer(pattern1,webpage):
        print("yes")
        pos2= webpage.find('\n"}},',pos.end())
        html = webpage[pos.end():pos2]
        #print(html)
        pattern2 ="<tr><td><p>"
        for pos21 in re.finditer(pattern2,html):
            pos22 = html.find("</p></td></tr>",pos21.end())
            #print(html[pos21.end():pos22])
            arr.append(html[pos21.end():pos22])

    for i in range(len(arr)):
        if i<9:
            arr[i] = arr[i][14:]
        elif i>=9:
            arr[i] = arr[i][15:]
        arr[i] = arr[i].replace("</td><td><p>",",")
        print(arr[i])
    return arr




if __name__ == "__main__":
	app.run(debug=True)
