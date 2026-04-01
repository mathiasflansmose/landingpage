from flask import Flask, render_template, send_from_directory
from datetime import datetime
from course_cards import COURSE_CARDS


app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template("index.html", course_cards=COURSE_CARDS, current_year=datetime.now().year)


@app.route('/robots.txt')
def static_from_root():
    return send_from_directory(app.static_folder, 'robots.txt')


if __name__ == '__main__':
    # Flaks listen on all network: host='0.0.0.0'
    app.run(host='0.0.0.0', port=5000)

