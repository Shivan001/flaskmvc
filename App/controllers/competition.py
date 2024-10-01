from App.models import Competition
from App.database import db

def create_competition(name, date, location):
    competition = Competition(name=name, date=date, location=location)
    db.session.add(competition)
    db.session.commit()
    return competition

# def get_all_competitions():
#     competitions = Competition.query.all()
#     seen_ids = set()
#     unique_competitions = []

#     for competition in competitions:
#         if competition.id not in seen_ids:
#             seen_ids.add(competition.id)
#             unique_competitions.append({
#                 'id': competition.id,
#                 'name': competition.name,
#                 'date': competition.date
#             })

#     return unique_competitions

def get_all_competitions():
    competitions = Competition.query.distinct().all()
    return [{"id": comp.id, "name": comp.name, "date": comp.date} for comp in competitions]



def get_competition_by_id(competition_id):
    return Competition.query.get(competition_id)
