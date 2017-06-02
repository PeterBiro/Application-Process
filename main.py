import data_manager
from flask import Flask, request, render_template, redirect

app = Flask(__name__)


@app.route("/")
def menu():
    menu_items = [
        {"name": "Mentors and schools page", "link": "/mentors"},
        {"name": "All school page", "link": "/all-school"},
        {"name": "Mentors by country page", "link": "/mentors-by-country"},
        {"name": "Contacts page", "link": "/contacts"},
        {"name": "Applicants page", "link": "/applicants"},
        {"name": "Applicants and mentors page", "link": "/applicants-and-mentors"}
    ]
    return render_template("index.html", menu_items=menu_items)

if __name__ == '__main__':
    app.run(debug=True)
