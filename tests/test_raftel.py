import math

from raftel import __version__
from raftel.raftel import _rad_to_degree


def test_version():
    assert __version__ == '0.2.0'


def test_rad_conversion():
    assert _rad_to_degree(0) == 0
    assert _rad_to_degree(math.pi) == 180
    assert _rad_to_degree(2*math.pi) == 360
