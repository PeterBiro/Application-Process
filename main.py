import UI
import data_manager


def main():
    menu_options = [
                    "Mentors' first and last name",
                    "Nickname of mentors at Miskolc",
                    "Carol's full name and phone",
                    "The Hat Girl's full name and phone",
                    "Insert new applicant and show his attributes",
                    "Update Jemima's number and show it",
                    "Delete those folks",
                    "Free querry"
                    ]
    choice = ""
    while choice != "0":
        choice = UI.handle_menu(menu_options)
        if choice == "1":
            querry = "SELECT first_name, last_name FROM mentors;"
            headers = ["First name", "Last name"]
        elif choice == "2":
            querry = "SELECT nick_name FROM mentors WHERE city='Miskolc';"
            headers = ["Nick name"]
        elif choice == "3":
            querry = "SELECT first_name || ' ' || last_name AS full_name, phone_number FROM applicants WHERE first_name LIKE 'Carol%';"
            headers = ["Full Name", "Phone number"]
        elif choice == "4":
            querry = "SELECT first_name || ' ' || last_name AS full_name, phone_number FROM applicants WHERE email LIKE '%@adipiscingenimmi.edu';"
            headers = ["Full Name", "Phone number"]
        elif choice == "5":
            querry = "INSERT INTO applicants (first_name, last_name, phone_number, email, application_code) VALUES ('Markus', 'Schaffarzyk', '003620/725-2666', 'djnovus@groovecoverage.com', 54823);"
            data_manager.run_querry(querry)
            querry = "SELECT * FROM applicants WHERE application_code=54823;"
            headers = ["Id", "First name", "Last name", "Phone number", "E-mail", "Application code"]
        elif choice == "6":
            querry = "UPDATE applicants SET phone_number = '003670/223-7459' WHERE first_name = 'Jemima' AND last_name = 'Foreman';"
            data_manager.run_querry(querry)
            querry = "SELECT first_name, last_name, phone_number FROM applicants WHERE first_name = 'Jemima' AND last_name = 'Foreman';"
            headers = ["First name", "Last name", "Phone number"]
        elif choice == "7":
            querry = "DELETE FROM applicants WHERE email LIKE '%@mauriseu.net';"
            data_manager.run_querry(querry)
        elif choice == "8":
            querry = UI.ask_input("What is your SQL querry to run? ")
            table = data_manager.run_querry(querry)
            headers = ["*" for _ in range(len(table[0]))]

        if choice in {"1", "2", "3", "4", "5", "6", "8"}:
            table = data_manager.run_querry(querry)
            UI.show_table(table, headers)


if __name__ == '__main__':
    main()
"""

6.) Jemima Foreman, an applicant called us, that her phone number changed to: 003670/223-7459
Write an UPDATE query, that changes this data in the database for this applicant.
Also, write a SELECT query, that checks the phone_number column of this applicant.
Use both of her name parts in the conditions!

7.) Arsenio, an applicant called us, that he and his friend applied to Codecool.
They both want to cancel the process, because they got an investor for the site they run: mauriseu.net

Write DELETE query to remove all the applicants, who applied with emails for this domain (e-mail address has this domain after the @ sign).
"""