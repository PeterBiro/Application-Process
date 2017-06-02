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


@app.route("/mentors")
def mentors():
    title = "Mentors and schools page"
    query = """
    SELECT mentors.first_name, mentors.last_name, schools.name, schools.country
    FROM mentors
    LEFT JOIN schools ON mentors.city = schools.city
    ORDER BY mentors.id;
    """
    result = data_manager.run_query(query)
    header = ["first name", "last name", "school's name", "country"]
    return render_template("results.html", title=title, header=header, result=result)

if __name__ == '__main__':
    app.run(debug=True)
