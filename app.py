from flask import Flask, render_template, jsonify, redirect
import yaml
import os
import optparse

developer = os.getenv("DEVELOPER", "User")
environment = os.getenv("ENVIRONMENT", "development")

app = Flask(__name__)

info = yaml.load(open('info.yml', 'r'))                 #Informacion personal
infoAc = yaml.load(open('infoA.yml', 'r'))              #Informacion Academica
infoExp = yaml.load(open('infoEXP.yml', 'r'))           #Informacion de experiencia de trabajo

@app.route('/info')
def hello_world():                                      #Despliega la informacion (test)
    return jsonify(info)


@app.route('/')                                         #Es la ruta "home"
def index():
    #return render_template('index.html')
    return render_template("index.html", info=info['info'], developer=developer, infoAc=infoAc['infoA'], infoExp=infoExp['infoExp'])


@app.route('/about', methods=['GET'])           #En esta ruta, se podra ver mi informacion personal
def about():
    
    return redirect("http://localhost:5000/#about")
    #return render_template("about.html", info=info['info'])


@app.route('/academic', methods=['GET'])            #En esta ruta, se podra ver mi formacion academica 
def aca():

    return redirect("http://localhost:5000/#academic")


@app.route('/work', methods=['GET'])                #En esta ruta, se podra ver mi experiencia laboral 
def work():

    return redirect("http://localhost:5000/#Work")          #La verdad, no he trabajado jajaja Solo dejare uno de prueba


if __name__ == '__main__':
  app.run(host="0.0.0.0", debug=True)
