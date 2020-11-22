from flask import Blueprint, render_template, url_for
from sabah.models import Blog



blog = Blueprint('blog', __name__)


@blog.route('/xeber/<int:news_id>')
def xeber(news_id):
    news = Blog.query.all()
    for oneNews in news:
        if oneNews.id == news_id:
          return render_template('inner.html', oneNews=oneNews)


@blog.route('/tedbir/<int:event_id>')
def tedbir(event_id):
    events = Blog.query.filter_by(type=2)
    for oneNews in events:
        if oneNews.id == event_id:
          return render_template('inner.html', oneNews=oneNews)


@blog.route('/elan/<int:ann_id>')
def elan(ann_id):
    announcement = Blog.query.filter_by(type=3)
    for oneAnnouncmenet in announcement:
        if oneAnnouncmenet.id == ann_id:
            return render_template('one-announce.html', oneAnnouncmenet=oneAnnouncmenet)