from app.helpers import pretty_date, less_than_day
from datetime import datetime, timedelta
def test_now():
    assert (pretty_date(datetime.utcnow())) == "just now"


def test_Yesterday():
    assert pretty_date(datetime.utcnow() - timedelta(days=1)) == "Yesterday"
def test_days_ago():
    assert pretty_date(datetime.utcnow() - timedelta(days=6)) == "6 days ago"
def test_weeks_ago():
    assert pretty_date(datetime.utcnow() - timedelta(weeks=2)) == "2 weeks ago"
