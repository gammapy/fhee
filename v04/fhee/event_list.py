# Licensed under a 3-clause BSD style license - see LICENSE.rst
from __future__ import absolute_import, division, print_function, unicode_literals
from astropy.coordinates import SkyCoord
from astropy.table import Table


class EventList(object):
    """
    Class to handle event lists conveniently.

    Parameters
    ----------
    filename : str
        Filename of a FITS event list.
    """
    def __init__(self, filename):
        self.table = Table.read(filename)

    def select_events_in_circle(self, position, radius):
        """
        Select all events in circular region around a given position in the sky.

        Parameters
        ----------
        position : `astropy.coordinates.SkyCoord`
            Position of the center of the circle.
        radius : `astropy.units.Quantity`
            Radius of the circle.

        Returns
        -------
        event_table : `astropy.table.Table`
            Subset of the event list table.
        """
        position_radec = position.transform_to('icrs')
        events_radec = SkyCoord(self.table['RA'], self.table['DEC'], frame='icrs')
        separation = events_radec.separation(position_radec)
        return self.table[separation < radius]
