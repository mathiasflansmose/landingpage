from flask import Flask, render_template
from datetime import datetime

app = Flask(__name__)

COURSE_CARDS = [
    {
        "title": "Databases", 
        "icon": "school", 
        "items": [
            "text...",
            "text2...",
        ],
    },
    {
        "title": "Distributed Systems and Security", 
        "icon": "school", 
        "items": [
            "text...",
            "text2...",
        ],
    },
    {
        "title": "Numerical Linear Algebra", 
        "icon": "school", 
        "items": [
            "text...",
            "text2...",
        ],
    },
    {
        "title": "Software Engineering and Architecture", 
        "icon": "school", 
        "items": [
            "text...",
            "text2...",
        ],
    },
    {
        "title": "Human-Computer Interaction", 
        "icon": "school", 
        "items": [
            "text...",
            "text2...",
        ],
    },
    {
        "title": "Introduction to Probability Theory and Statistics", 
        "icon": "school", 
        "items": [
            "text...",
            "text2...",
        ],
    },
    {
        "title": "Computer Architecture, Networks and Operating Systems", 
        "icon": "school", 
        "items": [
            "text...",
            "text2...",
        ],
    },
    {
        "title": "Computability and Logic", 
        "icon": "school", 
        "items": [
            "text...",
            "text2...",
        ],
    },
    {
        "title": "Programming Languages", 
        "icon": "school", 
        "items": [
            "text...",
            "text2...",
        ],
    },
    {
        "title": "Algorithms and Data Structures", 
        "icon": "school", 
        "items": [
            "text...",
            "text2...",
        ],
    },
    {
        "title": "Introduction to Mathematics and Optimisation", 
        "icon": "school", 
        "items": [
            "text...",
            "text2...",
        ],
    },
    {
        "title": "Introduction to Programming", 
        "icon": "school", 
        "items": [
            "Programming concepts and techniques in Java",
            "Program architecture concepts (inheritance, abstract classes, interfaces)",
            "Apply simple specification models",
            "Perform testing and debugging of programs",
        ],
    },
]


@app.route('/')
def hello_world():
    return render_template("index.html", course_cards=COURSE_CARDS, current_year=datetime.now().year)


if __name__ == '__main__':
    # Flaks listen on all network: host='0.0.0.0'
    app.run(host='0.0.0.0', port=5000)
