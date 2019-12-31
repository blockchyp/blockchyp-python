"""Utility functions."""


from datetime import datetime


def iso_timestamp():
    # type: () -> str
    """Return the current time in UTC RFC3339 encoding."""
    return f"{datetime.utcnow().isoformat('T', 'seconds')}Z"


def from_iso_timestamp(timestamp):
    # type: (str) -> datetime
    """Return a datetime from an RFC3339 encoded timestamp. Assumes UTC."""
    return datetime.strptime(timestamp, "%Y-%m-%dT%H:%M:%SZ")
