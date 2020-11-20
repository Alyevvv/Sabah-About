from flask import Blueprint, render_template, url_for
from sabah.models import Blog



blog = Blueprint('blog', __name__)


@blog.route('/xeber/<int:news_id>')
def xeber(news_id):
    news = Blog.query.all()
    for oneNews in news:
        if oneNews.id == news_id:
          return render_template('inner.html', oneNews=oneNews)


@blog.route('/tedbir')
def tedbir():
    return render_template('inner.html')


@blog.route('/elan')
def elan():
    return render_template('inner.html')