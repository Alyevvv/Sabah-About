from flask import Blueprint, render_template, url_for



blog = Blueprint('blog', __name__)


@blog.route('/xeber')
def xeber():
    return render_template('inner.html')


@blog.route('/tedbir')
def tedbir():
    return render_template('inner.html')


@blog.route('/elan')
def elan():
    return render_template('inner.html')