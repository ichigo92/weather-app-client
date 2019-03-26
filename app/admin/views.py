from flask import abort, flash, redirect, render_template, url_for
from flask_login import current_user, login_required

from . import admin
from .forms import CityForm

import requests

base_url = 'http://localhost:8080'

@admin.route('/cities', methods=['GET', 'POST'])
# @login_required
def list_cities():
    """
    List all cities
    """
    # TODO: Get all cities from db
    url = base_url+'/weather'
    weather = requests.get(url).json()
    print(weather)

    return render_template('admin/cities.html',
                           cities=weather, title="Weather")


@admin.route('/cities/add', methods=['GET', 'POST'])
# @login_required
def add_city():
    """
    Add a city to the database
    """

    add_city = True

    form = CityForm()
    if form.validate_on_submit():
        city = form.city.data
        url = base_url+'/weather'
        try:
            # add department to the database
            # TODO: Add City to the database
            print('data')
            requests.post(url, data = {'city': city})
            flash('You have successfully added a new city.')
        except:
            # in case department name already exists
            flash('Error: city name already exists.')

        # redirect to departments page
        return redirect(url_for('admin.list_cities'))

    # load city template
    return render_template('admin/city.html', action="Add",
                           add_city=add_city, form=form,
                           title="Add City")


@admin.route('/cities/edit/<int:id>', methods=['GET', 'POST'])
# @login_required
def edit_city(id):
    """
    Edit a city
    """

    add_city = False

    url = base_url+'/weather/{id}'
    url = url.format(id = id)

    # department = Department.query.get_or_404(id)
    # TODO: Get current City to edit
    city = requests.get(url).json()

    form = CityForm(obj=city)
    if form.validate_on_submit():
        city['city'] = form.city.data
        print('before updating')
        # Update the details in database
        requests.put(url, data = {'city': city})
        flash('You have successfully edited the city.')

        # redirect to the departments page
        return redirect(url_for('admin.list_cities'))


    form.city.data = city['city']
    return render_template('admin/city.html', action="Edit",
                           add_city=add_city, form=form,
                           city=city, title="Edit City")


@admin.route('/cities/delete/<int:id>', methods=['GET', 'POST'])
# @login_required
def delete_city(id):
    """
    Delete a city from the database
    """

    #  Get City from database
    
    url = base_url+'/weather/{id}'
    url = url.format(id = id)

    city = requests.delete(url).json()

    flash('You have successfully deleted the city.')

    # redirect to the departments page
    return redirect(url_for('admin.list_cities'))

    return render_template(title="Delete City")