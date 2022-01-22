from app.helpers import pretty_date, less_than_day
from datetime import datetime, timedelta
def test_now():
    assert (pretty_date(datetime.utcnow())) == "just now"


def test_Yesterday():
    assert pretty_date(datetime.utcnow() - timedelta(days=1)) == "Yesterday"
