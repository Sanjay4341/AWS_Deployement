from flask import Flask,render_template,request
import numpy as np
import pickle
# create a flask object
app=Flask(__name__)
'''
@app.route('/')
def hello():
    """test function"""
    return "Welcome to the Flask"

@app.route('/sanjay',methods=['GET'])
def check():
    """new function"""
    return "Codegnan is in KITS College"
'''
#First let's read the pickle file
with open('House_Price.pkl','rb') as f:
    model=pickle.load(f)

    
@app.route('/',methods=['GET'])
def home():
    return render_template('index.html')


@app.route('/predict',methods=['POST'])
def predict():
    Rooms=int(request.form['bedrooms'])# python left html right
    Bathrooms=int(request.form['bathrooms'])
    Place=int(request.form['location'])
    Area=int(request.form['area'])
    Status=int(request.form['status'])
    Facing=int(request.form['facing'])
    P_Type=int(request.form['type'])
    #Now take the above form data and convert to array
    input_data=np.array([[Place,Area,Status,Rooms,Bathrooms,Facing,P_Type]])
    #by taking above data we will predict the House_price
    prediction=model.predict(input_data)[0]
    #now we will pass above predicted data to template
    return render_template('index.html',prediction=prediction)
app.run()


