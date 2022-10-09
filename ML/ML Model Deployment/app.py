from flask import Flask, request, jsonify, render_template
import pickle
import numpy as np


app = Flask(__name__)
model = pickle.load(open('nbclassifier.pkl', 'rb'))
scaler = pickle.load(open('scaler.pickle', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
    '''
    For rendering results on HTML GUI
    '''
    int_features = [int(x) for x in request.form.values()]
    print("intial values -->", int_features)
    pre_final_features = [np.array(int_features)]
    final_features = scaler.transform(pre_final_features)
    print("scaled values -->", final_features)
    prediction = model.predict(final_features)   
    print('predictio value is ', prediction[0])
    if (prediction[0] == 1):
        output = "True"
    elif(prediction[0] == 0):
        output = "False"
    else:
        output = "Not sure"
        

    return render_template('index.html', prediction_text='This user will buy from social network ad  {}'.format(output))


if __name__ == "__main__":
    app.run(debug=True)