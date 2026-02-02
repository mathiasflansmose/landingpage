from flask import Flask, render_template
from datetime import datetime

app = Flask(__name__)

"""
    {
        "title": "Software Engineering and Architecture", 
        "icon": "code", 
        "items": [
            "text...",
        ],
    },
    {
        "title": "Human-Computer Interaction", 
        "icon": "javascript", 
        "items": [
            "text...",
        ],
    },
    {
        "title": "Introduction to Probability Theory and Statistics", 
        "icon": "paid", 
        "items": [
            "text...",
        ],
    },
    {
        "title": "Computer Architecture, Networks and Operating Systems", 
        "icon": "lan", 
        "items": [
            "text...",
        ],
    },
    {
        "title": "Computability and Logic", 
        "icon": "desktop_windows", 
        "items": [
            "",
        ],
    },
"""

COURSE_CARDS = [

    {
        "title": "Programming Languages", 
        "icon": "data_array", 
        "items": [
            "Explain characteristic features of programming language paradigms (imperative, functional, and OOP)",
            "Formalize fundamental programming language features (scoping rules, type systems, state management, higher-order functions, closures, etc.)"
            "Implement simple language processors (interpreters and compilers)",
            "Use mathematical and structural induction to reason on recursion and program correctness",
            "Implement a simple type checker in a mini language (miniscala)",
        ],
    },
    {
        "title": "Algorithms and Data Structures", 
        "icon": "polyline", 
        "items": [
            "Implement and analyze algorithms using standard algorithm paradigms",
            "Identify, use and compare data structures and graph algorithms",
            "Evaluate performance of algorithms",
            "Analyze and compare the time and space usage of algorithms and data structures",
            "Identify valid invariants and prove the correctness of simple algorithms",
        ],
    },
    {
        "title": "Introduction to Mathematics and Optimisation", 
        "icon": "functions", 
        "items": [
            "Perform Gaussian elimination",
            "Calculat gradient descent with the Hessian matrix",
            "Work with multidimensional matrices and multivariable calculus",
            "Apply general and convex optimization on data from examples",
            "Apply techniques to establish global or local minima for convex functions",
        ],
    },
    {
        "title": "Introduction to Programming", 
        "icon": "notes", 
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
