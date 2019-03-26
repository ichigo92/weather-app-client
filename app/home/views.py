from flask import render_template, redirect, url_for, request
from flask_login import login_required

from . import home

import requests
from .forms import AddCityForm

base_url = 'http://localhost:8080'

@home.route('/')
def homepage():
	return render_template('home/index.html', title = 'Welcome')

@home.route('/dashboard', methods=['GET', 'POST'])
# @login_required
def dashboard():
	url = base_url+'/weather'
	weather = requests.get(url).json()
	
	form = AddCityForm()

	if form.validate_on_submit():
		print('Submitted!!')
		print(url)
		requests.post(url, data = {'city': form.city.data})
		return redirect(url_for('home.dashboard'))

	return render_template('home/dashboard.html', title = 'Dashboard', base_url = base_url, form = form, weather_data = weather)