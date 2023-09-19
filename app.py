# save this as app.py
from flask import Flask, escape, request, render_template
import pickle
import numpy as np

app = Flask(__name__)
model = pickle.load(open('medical.pkl', 'rb'))


@app.route('/')
def home():
    return render_template("index.html")


@app.route('/about')
def about():
    return render_template("about.html")


@app.route('/predict', methods=['GET', 'POST'])
def predict():
    if request.method == 'POST':
        age = (int)(request.form['age'])
        sex = request.form['sex']
        bmi = int(float(request.form['bmi']))
        children = (int)(request.form['children'])
        smoker = request.form['smoker']
        region = request.form['region']
        
        # sex
        if (sex == "Male"):
            sex = 0
        else:
            sex = 1

        # smoker
        if (smoker == "Yes"):
            smoker = 0
        else:
            smoker = 1

        # regions
        if (region == "southeast"):
            region = 0
        elif (region == "southwest"):
            region = 1
        elif (region == "northeast"):
            region = 2
        else:
            region = 3

        prediction = model.predict([[age, sex, bmi, children, smoker, region]])

        return render_template("prediction.html", prediction_text="Cost is ${}".format(prediction))

    else:
        return render_template("prediction.html")


if __name__ == "__main__":
    app.run(debug=True)
