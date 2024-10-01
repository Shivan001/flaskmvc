from App.database import db

class CompetitionResult(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    student_id = db.Column(db.Integer, db.ForeignKey('student.id'), nullable=False)
    competition_id = db.Column(db.Integer, db.ForeignKey('competition.id'), nullable=False)
    rank = db.Column(db.Integer, nullable=False)
    score = db.Column(db.Float, nullable=False)

    def to_dict(self):
        return {
            "id": self.id,
            "student_id": self.student_id,
            "competition_id": self.competition_id,
            "rank": self.rank,
            "score": self.score
        }
