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


@app.route("/all-school")
def all_school():
    title = "All school"
    query = """
    SELECT mentors.first_name, mentors.last_name, schools.name, schools.country
    FROM mentors
    FULL OUTER JOIN schools ON mentors.city = schools.city
    ORDER BY mentors.id;
    """
    result = data_manager.run_query(query)
    header = ["first name", "last name", "school's name", "country"]
    return render_template("results.html", title=title, header=header, result=result)


@app.route("/mentors-by-country")
def mentors_by_country():
    title = "Mentors by country"
    query = """
    SELECT schools.country AS country, COUNT(mentors.id)
    FROM mentors
    FULL OUTER JOIN schools ON mentors.city = schools.city
    GROUP BY country
    ORDER BY country;
    """
    result = data_manager.run_query(query)
    header = ["country", "count"]
    return render_template("results.html", title=title, header=header, result=result)


@app.route("/contacts")
def contacts():
    title = "Contacts"
    query = """
    SELECT  schools.name, mentors.first_name, mentors.last_name
    FROM schools
    LEFT JOIN mentors ON schools.contact_person = mentors.id
    ORDER BY schools.name;
    """
    result = data_manager.run_query(query)
    header = ["school", "first name", "last name"]
    return render_template("results.html", title=title, header=header, result=result)


@app.route("/applicants")
def applicants():
    title = "Applicants"
    query = """
    SELECT applicants.first_name, applicants.application_code, applicants_mentors.creation_date
    FROM applicants
    JOIN applicants_mentors ON applicants.id = applicants_mentors.applicant_id
    WHERE applicants_mentors.creation_date > '2016-01-01'
    ORDER BY applicants_mentors.creation_date DESC;
    """
    result = data_manager.run_query(query)
    header = ["first name", "application code", "creation date"]
    return render_template("results.html", title=title, header=header, result=result)


@app.route("/applicants-and-mentors")
def aapplicants_and_mentors():
    title = "Applicants & mentors"
    query = """
    SELECT applicants.first_name, applicants.application_code, mentors.first_name, mentors.last_name
    FROM applicants
    LEFT JOIN applicants_mentors ON applicants.id = applicants_mentors.applicant_id
    LEFT JOIN mentors ON mentors.id = applicants_mentors.mentor_id
    ORDER BY applicants.id;
    """
    result = data_manager.run_query(query)
    header = ["applicant's first name", "application code", "mentor's first name", "mentor's last name"]
    return render_template("results.html", title=title, header=header, result=result)

if __name__ == '__main__':
    app.run(debug=True)
