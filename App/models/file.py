from App.database import db

class File(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    file_name = db.Column(db.String, nullable=False)
    file_size = db.Column(db.Float, nullable=False)

    def import_data(self):
        #importing results from file
        pass

    def to_dict(self):
        return {
            "id": self.id,
            "file_name": self.file_name,
            "file_size": self.file_size
        }
