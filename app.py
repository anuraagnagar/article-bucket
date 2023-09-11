from dotenv import load_dotenv
from flask import Flask
from flask import abort, redirect, render_template, request, url_for
from newsapi import NewsApiClient
from datetime import datetime
import os

load_dotenv()

app = Flask(__name__, template_folder='templates')

API_KEY = os.getenv("API_KEY", None)

client = NewsApiClient(api_key=API_KEY)

CATEGORIES = ['business', 'entertainment', 'general', 'healths', 'sports', 'technology', 'science']


@app.template_filter('date_time')
def date(timestamp):
    """
    Returns the date formatted string for the given timestamp.
    """
    format_datetime = datetime.strptime(timestamp, '%Y-%m-%dT%H:%M:%SZ')
    return format_datetime.strftime('%B %d, %Y %I:%M %p')


@app.route("/")
@app.route("/page=<int:page>")
def index(page=1, page_size=20):
    try:
        data = client.get_top_headlines(page=page, page_size=page_size)
        news_article = data["articles"]
        return render_template('index.html', article=news_article, page=page)
    except Exception as e:
        return abort(500)


@app.route("/category/<string:category>")
@app.route("/category/<string:category>/page=<int:page>")
def news_category(category=None, page=1, page_size=16):
    if category in CATEGORIES: 
        try:
            data = client.get_everything(q=category, page=page, page_size=16)
            news_article = data["articles"]
            return render_template(
                    "category.html", article=news_article, category=category, page=page
                )
        except Exception as e:
            return abort(500)
            
    return abort(404)

@app.route("/news/search")
def search_news(page_size=20):
    query = request.args.get('q')

    if not query:
        return abort(404)

    try:
        data = client.get_everything(q=query, page_size=page_size)
        news_article = data["articles"]
    except Exception as e:
            return abort(500)

    return render_template("search.html", article=data)


@app.errorhandler(404)
def not_found(e):
    return render_template(
            "error.html",
            error_message="404 Page Not Found"
            ,status=404
        ), 404

@app.errorhandler(500)
def server_error(e):
    return render_template(
            "error.html",
            error_message="500 Internal Server Error"
            ,status=500
        ), 500


if __name__ == '__main__':
    app.run()


