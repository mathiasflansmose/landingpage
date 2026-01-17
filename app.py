from flask import Flask, render_template

app = Flask(__name__)

# Static card data so you can render repeating blocks without JavaScript.
COURSE_CARDS = [
    {"title": "Databases", "icon": "school", "items": []},
    {"title": "Distributed Systems and Security", "icon": "school", "items": []},
    {"title": "Numerical Linear Algebra", "icon": "school", "items": []},
    {"title": "Software Engineering and Architecture", "icon": "school", "items": []},
    {"title": "Human-Computer Interaction", "icon": "school", "items": []},
    {"title": "Introduction to Probability Theory and Statistics", "icon": "school", "items": []},
    {"title": "Computer Architecture, Networks and Operating Systems", "icon": "school", "items": []},
    {"title": "Computability and Logic", "icon": "school", "items": []},
    {"title": "Programming Languages", "icon": "school", "items": []},
    {"title": "Algorithms and Data Structures", "icon": "school", "items": []},
    {"title": "Introduction to Mathematics and Optimisation", "icon": "school", "items": []},
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
    return render_template("index.html", course_cards=COURSE_CARDS)


if __name__ == '__main__':
    # Flaks listen on all network: host='0.0.0.0'
    app.run(host='0.0.0.0', port=5000)
