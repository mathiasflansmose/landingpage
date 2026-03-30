from flask import Flask, render_template
from datetime import datetime
from course_cards import COURSE_CARDS

app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template("index.html", course_cards=COURSE_CARDS, current_year=datetime.now().year)


if __name__ == '__main__':
    # Flaks listen on all network: host='0.0.0.0'
    app.run(host='0.0.0.0', port=5000)
