from flask import Blueprint, render_template, url_for
from sabah.models import Slider



admin = Blueprint('admin', __name__)


@admin.route('/admin')
def admin_home():
    slider = Slider.query.all()
    return render_template('admin/admin-home.html', slider=slider)



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