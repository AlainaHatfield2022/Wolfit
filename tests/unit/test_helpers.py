from app.helpers import pretty_date
from datetime import datetime, timedelta
def test_now():
    assert (pretty_date(datetime.utcnow())) == "just now"
def seconds_ago():
    assert (pretty_date(datetime.utcnow() - timedelta(seconds=60))) == "seconds ago"
def test_yesterday():
    assert (pretty_date(datetime.utcnow() - timedelta(days=1))) == "Yesterday"
