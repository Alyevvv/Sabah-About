from flask import Blueprint, render_template, url_for



main = Blueprint('main', __name__)


@main.route('/')
@main.route('/home')
def home():
    return render_template('home.html')



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


@main.route('/sabah-event')
def sabah_event():
    return render_template('sabah-event.html')


@main.route('/sabah-achivements')
def sabah_achivements():
    return render_template('Sabah-achivements.html')


@main.route('/sabah-volunteer')
def sabah_volunteer():
    return render_template('Sabah-volunteer.html')


@main.route('/news')
def news():
    return render_template('news.html')


@main.route('/announcement')
def announcement():
    return render_template('announcement.html')


@main.route('/contact')
def contact():
    return render_template('contact.html')
