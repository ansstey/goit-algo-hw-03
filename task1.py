from datetime import datetime

def get_days_from_today(date):
    date_datetime = datetime.strptime(date, '%Y-%m-%d').date()
    current_date = datetime.today().date()
    difference = current_date - date_datetime
    return difference.days
