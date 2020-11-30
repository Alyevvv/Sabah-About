import os
from sabah import app
from random import randrange
from flask import Blueprint, render_template, url_for, request, flash, redirect
from flask_login import login_required
from sabah.models import Slider, Blog
from sabah.admin.forms import *
from werkzeug.utils import secure_filename
from sabah import db


admin = Blueprint('admin', __name__)


@app.route("/admin-login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'sabahAlyev@gmail.com' and form.password.data == 'fabregas056':
            flash('Siz admin panelə uğurla daxil oldunuz.', 'success')
            return redirect(url_for('admin.admin_home'))
        else:
            flash('Daxil olarkən xəta baş verdi. Zəhmət olmasa email ilə şifrənizi yenidən yoxlayın.', 'danger')
    return render_template('admin/admin-login.html', form=form)


# Slide routes
@admin.route('/admin', methods=['GET', 'POST'])
def admin_home():
    slider = Slider.query.all()
    return render_template('admin/admin-home.html', slider=slider)




@admin.route('/admin/slider/create', methods=['GET', 'POST'])
def slider_create():
    form = SliderForm()
    if form.validate_on_submit():
        f = form.image.data
        filename = str(randrange(1*10*100, 9*10**100)) + "." + secure_filename(
            f.filename).rsplit('.', 1)[1].lower()  # generate random filename
        f.save(os.path.join(
            app.root_path, 'static', 'pics', filename
        ))
        temp = Slider(url=form.url.data)
        temp.image = filename
        flash("Slider uğurla yükləndi", 'success')
        db.session.add(temp)
        db.session.commit()
        return redirect(url_for('admin.admin_home'))
    return render_template('admin/slider-create.html', form=form, label='Slider əlavə et', description='Buradan yeni slider üçün link və şəkil əlavə edə bilərsiniz.')


@admin.route('/admin/slider/<int:slider_id>/update', methods=['GET', 'POST'])
def slider_update(slider_id):
    slider = Slider.query.get_or_404(slider_id)
    form = SliderForm()
    if form.validate_on_submit():
        f = form.image.data
        filename = str(randrange(1*10*100, 9*10**100)) + "." + secure_filename(
            f.filename).rsplit('.', 1)[1].lower()  # generate random filename
        f.save(os.path.join(
            app.root_path, 'static', 'pics', filename
        ))
        slider.image = filename
        slider.url = form.url.data
        db.session.commit()
        flash('Şəkil uğurla yeniləndi', 'success')
        return redirect(url_for('admin.admin_home'))
    elif request.method == 'GET':
        form.url.data = slider.url
    return render_template('admin/slider-create.html', form=form, label='Slider yenilə', slider=slider)


@admin.route('/admin/slider/<int:slider_id>/delete', methods=['GET', 'POST'])
def slider_delete(slider_id):
    slider = Slider.query.get_or_404(slider_id)
    os.remove(os.path.join(app.root_path, 'static', 'pics', slider.image))
    db.session.delete(slider)
    db.session.commit()
    flash('Slider uğurla silindi', 'success')
    return redirect(url_for('admin.admin_home'))








# News Routes

@admin.route('/admin/news', methods=['GET', 'POST'])
def admin_news():
    news = Blog.query.filter_by(type=1).order_by(Blog.add_date.desc())
    return render_template('admin/admin-news.html', news=news)


@admin.route('/admin/news/create', methods=['GET', 'POST'])
def news_create():
    form = NewsForm()
    if form.validate_on_submit():
        f = form.image.data
        filename = str(randrange(1*10*100, 9*10**100)) + "." + secure_filename(
            f.filename).rsplit('.', 1)[1].lower()  # generate random filename
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
        if form.image.data:
            f = form.image.data
            filename = str(randrange(1*10*100, 9*10**100)) + "." + secure_filename(
                f.filename).rsplit('.', 1)[1].lower()  # generate random filename
            f.save(os.path.join(
                app.root_path, 'static', 'pics', filename
            ))
            news.image = filename
        news.title = form.title.data
        news.text = form.text.data
        db.session.commit()
        flash('Xəbər uğurla yeniləndi', 'success')
        return redirect(url_for('admin.admin_news', news_id=news.id))
    elif request.method == 'GET':
        form.title.data = news.title
        form.text.data = news.text
        form.image.data = news.image
    return render_template('admin/news-create.html', legend='Xəbər yenilə', button='Yenilə', form=form, news=news)


@admin.route('/admin/news/<int:news_id>/delete', methods=['GET', 'POST'])
def news_delete(news_id):
    news = Blog.query.get_or_404(news_id)
    os.remove(os.path.join(app.root_path, 'static', 'pics', news.image))
    db.session.delete(news)
    db.session.commit()
    flash('Xəbər uğurla silindi', 'success')
    return redirect(url_for('admin.admin_news'))










# Event Routes
@admin.route('/admin-event', methods=['GET', 'POST'])
def admin_event():
    events = Blog.query.filter_by(type=2).order_by(Blog.add_date.desc())
    return render_template('admin/admin-event.html', events=events)


@admin.route('/admin/event/create', methods=['GET', 'POST'])
def event_create():
    form = EventForm()
    if form.validate_on_submit():
        f = form.image.data
        filename = str(randrange(1*10*100, 9*10**100)) + "." + secure_filename(
            f.filename).rsplit('.', 1)[1].lower()  # generate random filename
        f.save(os.path.join(
            app.root_path, 'static', 'pics', filename
        ))
        events = Blog(title=form.title.data, text=form.text.data, type=2)
        events.image = filename
        flash("Tədbir uğurla yükləndi", 'success')
        db.session.add(events)
        db.session.commit()
        return redirect(url_for('admin.admin_event'))
    return render_template('admin/event-create.html', legend='Tədbir əlavə et', button='Yüklə', form=form)


@admin.route('/admin/events/<int:event_id>/update', methods=['GET', 'POST'])
def event_update(event_id):
    events = Blog.query.get_or_404(event_id)
    form = EventForm()
    if form.validate_on_submit():
        if form.image.data:
            f = form.image.data
            filename = str(randrange(1*10*100, 9*10**100)) + "." + secure_filename(
                f.filename).rsplit('.', 1)[1].lower()  # generate random filename
            f.save(os.path.join(
                app.root_path, 'static', 'pics', filename
            ))
            news.image = filename
        events.title = form.title.data
        events.text = form.text.data
        db.session.commit()
        flash('Tədbir uğurla yeniləndi', 'success')
        return redirect(url_for('admin.admin_event', event_id=event.id))
    elif request.method == 'GET':
        form.title.data = events.title
        form.text.data = events.text
        form.image.data = events.image
    return render_template('admin/event-create.html', legend='Tədbir yenilə', button='Yenilə', form=form, events=events)


@admin.route('/admin/events/<int:event_id>/delete', methods=['GET', 'POST'])
def event_delete(event_id):
    events = Blog.query.get_or_404(event_id)
    os.remove(os.path.join(app.root_path, 'static', 'pics', events.image))
    db.session.delete(events)
    db.session.commit()
    flash('Tədbir uğurla silindi', 'success')
    return redirect(url_for('admin.admin_event'))









# Announcement

@admin.route('/admin-announcement', methods=['GET', 'POST'])
def admin_announcement():
    announcement = Blog.query.filter_by(type=3).order_by(Blog.id.desc())
    return render_template('admin/admin-announcement.html', announcement=announcement)


@admin.route('/admin/announcement/create', methods=['GET', 'POST'])
def announcement_create():
    form = AnnouncementForm()
    if form.validate_on_submit():
        f = form.image.data
        filename = str(randrange(1*10*100, 9*10**100)) + "." + secure_filename(
            f.filename).rsplit('.', 1)[1].lower()  # generate random filename
        f.save(os.path.join(
            app.root_path, 'static', 'pics', filename
        ))
        announcement = Blog(title=form.title.data,
                            text=form.text.data, add_date=form.date.data, type=3)
        announcement.image = filename
        flash("Elan uğurla yükləndi", 'success')
        db.session.add(announcement)
        db.session.commit()
        return redirect(url_for('admin.admin_announcement'))
    return render_template('admin/announcement-create.html', legend='Elan əlavə et', button='Yüklə', form=form)


@admin.route('/admin/announcement/<int:ann_id>/update', methods=['GET', 'POST'])
def announcement_update(ann_id):
    announcement = Blog.query.get_or_404(ann_id)
    form = AnnouncementForm()
    if form.validate_on_submit():
        if form.image.data:
            f = form.image.data
            filename = str(randrange(1*10*100, 9*10**100)) + "." + secure_filename(
                f.filename).rsplit('.', 1)[1].lower()  # generate random filename
            f.save(os.path.join(
                app.root_path, 'static', 'pics', filename
            ))
            announcement.image = filename
        announcement.title = form.title.data
        announcement.text = form.text.data
        announcement.add_date = form.date.data
        db.session.commit()
        flash('Elan uğurla yeniləndi', 'success')
        return redirect(url_for('admin.admin_announcement', ann_id=ann_id))
    elif request.method == 'GET':
        form.title.data = announcement.title
        form.text.data = announcement.text
        form.date.data = announcement.add_date
        form.image.data = announcement.image
    return render_template('admin/announcement-create.html', legend='Elan yenilə', button='Yenilə', form=form, announcement=announcement)


@admin.route('/admin/announcement/<int:ann_id>/delete', methods=['GET', 'POST'])
def announcement_delete(ann_id):
    announcement = Blog.query.get_or_404(ann_id)
    os.remove(os.path.join(app.root_path, 'static', 'pics', announcement.image))
    db.session.delete(announcement)
    db.session.commit()
    flash('Elan uğurla silindi', 'success')
    return redirect(url_for('admin.admin_announcement'))
