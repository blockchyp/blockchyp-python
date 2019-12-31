"""Get the version as seen by PyPI."""

from pkg_resources import get_distribution, DistributionNotFound

try:
    VERSION = get_distribution(__name__).version
except DistributionNotFound:
    VERSION = "unknown"
