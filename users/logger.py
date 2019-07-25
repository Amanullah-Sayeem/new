from datetime import datetime

from users.models import Action
from users.models import Statistics

def log(type, description, user):
    action = Action(
        type=type,
        timePerformed=datetime.now(),
        description=description,
        user=user,
    )
    action.save()


def statlog(stats):
    stat = Statistics(
        stats = stats)
    stat.save()
