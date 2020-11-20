import os
from sabah import app
from random import randrange
from flask import Blueprint, render_template, url_for, request, flash, redirect
from sabah.models import Slider, Blog
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
            app.root_path, 'static', 'pics', filename 
        ))
        temp = Slider()
        temp.image = filename
        flash("Slider uğurla yükləndi", 'success')
        db.session.add(temp)
        db.session.commit()
        return redirect(url_for('admin.admin_home'))
    return render_template('admin/slider-create.html', form=form)




@admin.route('/admin/slider/<int:slider_id>/update', methods=['GET', 'POST'])
def slider_update(slider_id):
    slider = Slider.query.get_or_404(slider_id)
    form = SliderForm()
    if form.validate_on_submit():
        
        slider.image = form.picture.data
        db.session.commit()
        flash('Şəkil uğurla yeniləndi', 'success')
        return redirect(url_for('admin.admin_home'))
    elif request.method == 'GET':
        form.picture.data = slider.image

    return render_template('admin/slider-create.html', form=form)





@admin.route('/admin/slider/<int:slider_id>/delete', methods=['GET', 'POST'])
def slider_delete(slider_id):
    slider = Slider.query.get_or_404(slider_id)
    db.session.delete(slider)
    db.session.commit()
    flash('Slider uğurla silindi', 'success')
    return redirect(url_for('admin.admin_home'))




@admin.route('/admin-calendar')
def admin_calendar():
    return render_template('admin/calendar.html')


#News Routes

@admin.route('/admin/news', methods=['GET', 'POST'])
def admin_news():
    news = Blog.query.all()
    return render_template('admin/admin-news.html', news=news)


@admin.route('/admin/news/create', methods=['GET', 'POST'])
def news_create():
    form = NewsForm()
    if form.validate_on_submit():
        f = form.image.data
        filename = str(randrange(1*10*100, 9*10**100)) + "." + secure_filename(f.filename).rsplit('.', 1)[1].lower() # generate random filename
        f.save(os.path.join(
            app.root_path, 'static', 'pics', filename 
        ))
        news = Blog(title=form.title.data, text=form.text.data, type=1)
        news.image = filename
        flash("Xəbər uğurla yükləndi", 'success')
        db.session.add(news)
        db.session.commit()
        return redirect(url_for('admin.admin_news'))
    return render_template('admin/news-create.html', legend='Xəbər əlavə et', button='Yüklə', form=form)



@admin.route('/admin/news/<int:news_id>/update', methods=['GET', 'POST'])
def news_update(news_id):
    news = Blog.query.get_or_404(news_id)
    form = NewsForm()
    if form.validate_on_submit():
        f = form.image.data
        filename = str(randrange(1*10*100, 9*10**100)) + "." + secure_filename(f.filename).rsplit('.', 1)[1].lower() # generate random filename
        f.save(os.path.join(
            app.root_path, 'static', 'pics', filename 
        ))
        news.image = filename
        news.title=form.title.data
        news.text=form.text.data
        db.session.commit()
        flash('Xəbər uğurla yeniləndi', 'success')
        return redirect(url_for('admin.admin_news', news_id=news.id))
    elif request.method == 'GET':
        form.title.data = news.title
        form.image.data = news.image
        form.text.data = news.text
    return render_template('admin/news-create.html', legend='Xəbər yenilə', button='Yenilə', form=form)

        


@admin.route('/admin/news/<int:news_id>/delete', methods=['GET', 'POST'])
def news_delete(news_id):
    news = Blog.query.get_or_404(news_id)
    db.session.delete(news)
    db.session.commit()
    flash('Xəbər uğurla silindi', 'success')
    return redirect(url_for('admin.admin_news'))









@admin.route('/admin-event')
def admin_event():
    return render_template('admin/admin-event.html')


@admin.route('/admin-announcement')
def admin_announcement():
    return render_template('admin/admin-announcement.html')