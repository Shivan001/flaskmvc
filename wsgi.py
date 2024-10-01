import click
from datetime import datetime
from flask import Flask
from App.main import create_app
from App.database import db, get_migrate
from App.controllers.student import create_student, get_all_students
from App.controllers.admin import create_admin, get_all_admins
from App.controllers.competition import create_competition, get_all_competitions
from App.controllers.competition_result import create_competition_result
from App.controllers.competition_result import import_results_from_file
from App.controllers.competition_result import get_results_by_competition
from App.controllers.file import import_file_data

app = create_app()
migrate = get_migrate(app)

@app.cli.command("init", help="Creates and initializes the database")
def init():
    db.create_all()
    print("database initialized!")

#commands student
@app.cli.command("create-student", help="Creates a student")
@click.argument("name")
def create_student_command(name):
    create_student(name)
    print(f'Student {name} created!')

@app.cli.command("list-students", help="Lists all students")
def list_students_command():
    students = get_all_students()
    for student in students:
        print(student.to_dict())

#commands admin
@app.cli.command("create-admin", help="Creates an admin")
@click.argument("name")
def create_admin_command(name):
    create_admin(name)
    print(f'Admin {name} created!')

@app.cli.command("list-admins", help="Lists all admins")
def list_admins_command():
    admins = get_all_admins()
    for admin in admins:
        print(admin.to_dict())

#commands competition
@app.cli.command("create-competition", help="Creates a competition")
@click.argument("name")
@click.argument("date")
@click.argument("location")
def create_competition_command(name, date, location):
    try:
        date_obj = datetime.strptime(date, '%Y-%m-%d').date()
        create_competition(name, date_obj, location)
        print(f'Competition {name} created!')
    except ValueError as e:
        print(f"Error: {e}. Date format should be YYYY-MM-DD.")

@app.cli.command("import-results", help="Imports competition results from a CSV file")
@click.argument("file_path")
def import_results_command(file_path):
    import_results_from_file(file_path)

@app.cli.command("list-competitions", help="Lists all competitions")
def list_competitions_command():
    competitions = get_all_competitions()
    
    if not competitions:
        print("There are no competitions.")
    else:
        for competition in competitions:
            print(f"ID: {competition['id']}, Name: {competition['name']}, Date: {competition['date']}")


@app.cli.command("view-results", help="View results for a specific competition")
@click.argument("competition_id", type=int)
def view_results_command(competition_id):
    results = get_results_by_competition(competition_id)
    
    if not results:
        print(f"No results found for competition ID {competition_id}.")
    else:
        for result in results:
            print(f"Student ID: {result.student_id}, Rank: {result.rank}, Score: {result.score}")


