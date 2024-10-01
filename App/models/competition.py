from App.database import db

class Competition(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    date = db.Column(db.Date, nullable=False)
    location = db.Column(db.String, nullable=False)
    
    results = db.relationship('CompetitionResult', backref='competition', lazy=True)

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "date": str(self.date),
            "location": self.location,
            "results": [result.to_dict() for result in self.results]
        }
