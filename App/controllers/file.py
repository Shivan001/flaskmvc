from App.models import File
from App.database import db

def import_file_data(file_name, file_size):
    new_file = File(file_name=file_name, file_size=file_size)
    db.session.add(new_file)
    db.session.commit()
    return new_file

def get_all_files():
    return File.query.all()
