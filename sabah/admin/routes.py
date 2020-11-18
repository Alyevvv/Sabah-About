import os
from random import randrange
from flask import Blueprint, render_template, url_for, request, flash, redirect
from sabah.models import Slider
from sabah.admin.forms import *
from werkzeug.utils import secure_filename
from sabah import db





admin = Blueprint('admin', __name__)

# Slide routes

@admin.route('/admin', methods=['GET', 'POST'])
def admin_home():
    slider = Slider.query.all()
    return render_template('admin/admin-home.html', slider=slider)



@admin.route('/admin/slider/create', methods=['GET', 'POST'])
def slider_create():
    form = SliderForm()
    if form.validate_on_submit():
        f = form.picture.data
        filename = str(randrange(1*10*100, 9*10**100)) + "." + secure_filename(f.filename).rsplit('.', 1)[1].lower() # generate random filename
        f.save(os.path.join(
            app.instance_path, 'pics', filename 
        ))
        form.picture = filename
        flash("Şəkliniz uğurlu yükləndi")
        return redirect(url_for('admin.admin_home'))
    # db ye add olunmalidir problem #1
    return render_template('admin/slider-create.html', form=form)



@admin.route('/admin-calendar')
def admin_calendar():
    return render_template('admin/calendar.html')



@admin.route('/admin-event')
def admin_event():
    return render_template('admin/admin-event.html')



@admin.route('/admin-news')
def admin_news():
    return render_template('admin/admin-news.html')



@admin.route('/admin-announcement')
def admin_announcement():
    return render_template('admin/admin-announcement.html')