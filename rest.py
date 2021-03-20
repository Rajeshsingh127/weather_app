from flask import Flask,jsonify,render_template,url_for,request
import requests
from flask_restful import Resource,Api
app=Flask(__name__)
api=Api(app)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/result',methods=['POST'])
def result():
    city_name = request.form['city_name']
    try:
            data = get_weather(city_name)
            temp= str(data['main']['temp'])
            temp_min = str(data['main']['temp_min'])
            temp_max = str(data['main']['temp_max'])
            weather = data['weather'][0]['main']
            location=data['name']
            return render_template('result.html',temp=temp,temp_min=temp_min,temp_max=temp_max,weather=weather,location=location)
    except:
            return "<h1>Oops city not found. Try larger city name nearby</h1>"




def get_weather(city_name):
        appurl = "http://api.openweathermap.org/data/2.5/weather?q={},IN&units=metric&appid=Enter your api key".format(
            city_name)
        r = requests.get(appurl)
        return r.json()


if __name__ == '__main__':
    app.run()
