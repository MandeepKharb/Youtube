import os
import json
import numpy as np
import pandas as pd

from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image

# Flask utils
from flask import Flask, redirect, url_for, request, render_template
from werkzeug.utils import secure_filename
from gevent.pywsgi import WSGIServer



from splinter import Browser
from bs4 import BeautifulSoup
import pandas as pd
import requests
import os


# Define a flask app
app = Flask(__name__)

# Model saved with Keras model.save()
#MODEL_PATH = os.path.join("models","keras_models", "model-mobilenet-RMSprop0.0002-001-0.930507-0.647776.h5")
MODEL_PATH = os.path.join("models","keras_models", "model-mobilenet-RMSprop0.0002-008-0.995584-0.711503.h5")
                                              
# Load your trained model
model = load_model(MODEL_PATH)
print("Model loaded successfully !! Check http://127.0.0.1:5000/")

with open(os.path.join("static","food_list", "food_list.json"), "r", encoding="utf8") as f:
    food_labels = json.load(f)
class_names = sorted(food_labels.keys())
label_dict = dict(zip(range(len(class_names)), class_names))

food_calories = pd.read_csv(os.path.join("static","food_list", "Food_calories.csv"))

def prepare_image(img_path):
    img = image.load_img(img_path, target_size=(224, 224))
    # Preprocessing the image
    x = image.img_to_array(img) / 255
    x = np.expand_dims(x, axis=0)
    return x


@app.route("/", methods=["GET"])
def Home():
    # Main page
    #Food = mongo.db.collection.find_one()
    return render_template('Know_Before_You_Eat.html')

    


@app.route("/predict", methods=["GET", "POST"])
def upload():
    data = {}
    if request.method == "POST":
        # Get the file from post request
        f = request.files["image"]

        # Save the file to ./upload_image
        basepath = os.path.dirname(__file__)
        file_path = os.path.join(basepath, "upload_image", secure_filename(f.filename))
        f.save(file_path)

        # Make prediction
        image = prepare_image(file_path)
        preds = model.predict(image)
        predictions = preds.argmax(axis=-1)[0]
        pred_label = label_dict[predictions]

        food_retrieve = food_calories[food_calories["name"]==pred_label]

        food_nutrional_min = food_retrieve["nutritional value min,kcal"]
        food_nutrional_min=np.array(food_nutrional_min)
        food_nutrional_min = str(food_nutrional_min)


        food_nutrional_max = food_retrieve["nutritional value max,kcal"]
        food_nutrional_max=np.array(food_nutrional_max)
        food_nutrional_max = str(food_nutrional_max)

        Unit = food_retrieve["unit"]
        Unit=np.array(Unit)
        Unit = str(Unit)

        Calories = food_retrieve["average cal"]
        Calories=np.array(Calories)
        Calories = str(Calories)

        data = pred_label

        if data=="beef carpaccio":
           data="carpaccio"
        elif data=="cheese plate":
            data="cheese"
        elif data=="chicken quesadilla":
            data="quesadilla"
        elif data=="chicken wings":
            data="Buffalo wing"
        elif data=="grilled salmon":
            data="Salmon#As_food"    
        elif data=="lobster roll sandwich":
            data="lobster roll" 
        elif data=="strawberry shortcake":
            data="Shortcake#Strawberry_shortcake"

        path={'executable_path':'/usr/local/bin/chromedriver'}
        browser=Browser('chrome',**path,headless=False)
        # browser=Browser('chrome',path,headless=True)

        if data=="tuna tartare":
            url="http://ahealthylifeforme.com/tuna-tartare-recipe/"
            browser.visit(url)
            html=browser.html
            soup=BeautifulSoup(html,"html.parser")
            var=soup.select_one('div.entry-content')
            description=var.select('p')
        else:
            url="https://en.wikipedia.org/wiki/"
            browser.visit(url+data)
            html=browser.html
            soup=BeautifulSoup(html,"html.parser")
            var=soup.select_one('div.mw-parser-output')
            description=var.select('p')
            nutri=soup.select_one('table.infobox')

        if (data=="greek salad" or data=="oysters" or data=="smoked scallop" or data=="paella"):    
            output=description[1].text
        elif data=="mussels" :
            output=description[2].text
        elif data=="Salmon#As_food":
            output=description[3].text        
        else:
            if description[0].text!='\n':
                output=description[0].text    
            elif description[0].text=='\n' and description[1].text!='\n':
                output=description[1].text
            elif description[1].text=='\n' and description[2].text!='\n':
                output=description[2].text
        output
        description = output
        browser.quit()

        
        return "<center><i><h4>" + pred_label.title()+" </h4></i> "+"<b><h3>Probability</h3></b><h4>"+str(preds.max(axis=-1)[0]) + '\n' + "</h4><br><br><b><h4 class=\"desc\">" +\
        description + "</h4><br><br>" +\
        "<div class=\"heading-section\"><h2 class=\"mb-4\"><span>Nutrional Facts</span></h2></div><hr></hr>" + \
        "<h5><b>Nutrional Value - Min (kcal) &nbsp;: &nbsp;</b>" + food_nutrional_min + '\n' + "<br><br>" + \
        "<b>Nutrional Value - Max (kcal) &nbsp;: &nbsp;</b>" + food_nutrional_max + '\n' + "<br><br>" + \
        "<b> Avg Calories &nbsp;: &nbsp;</b>" + Calories + "<br><br>" + \
        "<b> Unit &nbsp;: &nbsp;</b>" + Unit + '\n' + "</h5></center> <br><br>" + \
        "<div id=\"Recipe\" class=\"heading-section\"><h2 class=\"mb-4\"><span>Recipe - Cookbook </span></h2></div><hr></hr>" + \
        str(nutri) 
        


    return None


if __name__ == "__main__":
    # Serve the app with gevent
    http_server = WSGIServer(("0.0.0.0", 5000), app)
    http_server.serve_forever()