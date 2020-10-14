import datetime
from datetime import datetime

def days_since_date(n):
    date_object = datetime.strptime(n, '%Y-%m-%d').date()
    diff = datetime.now().date() - date_object
    return diff.days