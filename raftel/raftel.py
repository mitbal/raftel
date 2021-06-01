# package raftel contains the function to plot list of s2id easily

import math
import s2sphere
from staticmap import StaticMap, Polygon

def _rad_to_degree(x):
    """
    Convert radian to degree (duh)
    """
    return x * 180 / math.pi


def plot_s2id(s2ids, color='#00ff0088', auto_render=True):
    """
    Given list of s2id, plot the area in the map
    """

    m = StaticMap(800, 600, 5, 5, url_template='http://a.tile.stamen.com/toner/{z}/{x}/{y}.png')

    for s2 in s2ids:

        s2cell = s2sphere.CellId(int(s2))
        s = s2sphere.Cell(s2cell)

        lon0, lat0 = _rad_to_degree(s.get_latitude(0, 0)), _rad_to_degree(s.get_longitude(0, 0))
        lon1, lat1 = _rad_to_degree(s.get_latitude(1, 1)), _rad_to_degree(s.get_longitude(1, 1))
        points = [[lat0, lon0], [lat0, lon1], [lat1, lon1], [lat1, lon0]]

        region = Polygon(points, color, 'black', 20)
        m.add_polygon(region)

    if auto_render:
        return m.render()
    return m
