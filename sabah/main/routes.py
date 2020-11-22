from flask import Blueprint, render_template, url_for, request
from sabah import db
from sabah.models import *
import datetime




main = Blueprint('main', __name__)


@main.route('/')
@main.route('/home')
def home():
    slider = Slider.query.all()
    news = Blog.query.filter_by(type=1).order_by(Blog.add_date.desc()).limit(3)
    return render_template('home.html', slider=slider, news=news)



@main.route('/about')
def about():
    return render_template('about.html')



@main.route('/specialities')
def specialities():
    return render_template('specialties.html')



@main.route('/groups-and-subject')
def groups():
    return render_template('groups.html')


    
@main.route('/teachers-table')
def teachers_table():
    return render_template('teachers-table.html')


@main.route('/teachers-recommend')
def teachers_recommend():
    return render_template('teachers-recommend.html')


@main.route('/sabah-achivements')
def sabah_achivements():
    return render_template('Sabah-achivements.html')


@main.route('/sabah-volunteer')
def sabah_volunteer():
    return render_template('Sabah-volunteer.html')


@main.route('/xeberler')
def news():
    page = request.args.get('page', 1, type=int) #slug
    news = Blog.query.filter_by(type=1).order_by(Blog.add_date.desc()).paginate(page=page, per_page=6)
    return render_template('news.html', news=news)




@main.route('/sabah-event')
def sabah_event():
    page = request.args.get('page', 1, type=int) #slug
    events = Blog.query.filter_by(type=2).order_by(Blog.add_date.desc()).paginate(page=page, per_page=6)
    return render_template('sabah-event.html', events=events)



@main.route('/announcement')
def announcement():
    page= request.args.get('page', 1, type=int)
    announcement=Blog.query.filter_by(type=3).order_by(Blog.id.desc()).paginate(page=page, per_page=5)
    news = Blog.query.filter_by(type=1).order_by(Blog.add_date.desc()).limit(3)
    return render_template('announcement.html', announcement=announcement, news=news)


@main.route('/contact')
def contact():
    return render_template('contact.html')
