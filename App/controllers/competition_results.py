import csv
from App.models import CompetitionResult
from App.database import db

import csv
from App.models import CompetitionResult
from App.database import db

def import_results_from_file(file_path):
    try:
        with open(file_path, newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                result = CompetitionResult(
                    student_id=row['student_id'],  
                    competition_id=row['competition_id'],
                    rank=row['rank'],
                    score=row['score']
                )
                db.session.add(result)
            db.session.commit()
            print(f"Results imported successfully from {file_path}")
    except Exception as e:
        db.session.rollback()
        print(f"Failed to import results: {e}")


def create_competition_result(student_id, competition_id, rank, score):
    new_result = CompetitionResult(
        student_id=student_id, 
        competition_id=competition_id,
        rank=rank,
        score=score
    )
    db.session.add(new_result)
    db.session.commit()
    return new_result

def get_results_by_competition(competition_id):
    return CompetitionResult.query.filter_by(competition_id=competition_id).all()
