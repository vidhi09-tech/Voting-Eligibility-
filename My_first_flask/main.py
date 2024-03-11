from flask import Flask, redirect, url_for, request, render_template
import numpy as np
import pandas as pd
app = Flask(__name__)
df=pd.read_csv('Book1.csv')
df.set_index('Country',inplace=True)

@app.route('/')
@app.route('/home')
def index_page():
    dropdown_options = list(df.index)  # Define your dropdown options
    return render_template('index.html',dropdown_options=dropdown_options)

@app.route('/success/<country>')
def success(country):
   age = df.loc[country, 'Voting Age']
   links = df.loc[country, 'Links']
   return render_template('success.html',country=country,age =age, links = links)


@app.route('/fail/<country>')
def fail(country):
   age = df.loc[country, 'Voting Age']
   links = df.loc[country, 'Links']
   return render_template('fail.html',country=country,age =age, links = links)

@app.route('/login',methods = ['POST', 'GET'])
def login():
   if request.method == 'POST':
      country = request.form.get('dropdown')
      age= int(request.form['Age'])


   if df.loc[country, 'Voting Age'] <= age:
      stat="success"
   else:
      stat="fail"

   return redirect(url_for(stat, country=country))


if __name__ == '__main__':
   app.run(debug = True)