from App.database import db

class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    
    results = db.relationship('CompetitionResult', backref='student', lazy=True)

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "results": [result.to_dict() for result in self.results]
        }
