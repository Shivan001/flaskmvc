from App.models import Admin
from App.database import db

def create_admin(name):
    new_admin = Admin(name=name)
    db.session.add(new_admin)
    db.session.commit()
    return new_admin

def get_all_admins():
    return Admin.query.all()
