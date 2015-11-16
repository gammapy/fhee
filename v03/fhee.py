import numpy as np
import astropy.units as u
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


class Catalog(object):
    """
    Class to handle catalogs conveniently.

    Parameters
    ----------
    filename : str
        Filename of a FITS source catalog.
    """
    def __init__(self, filename):
        self.table = Table.read(filename)

    def get_source_by_name(self, source_name):
        """
        Get catalog row given a source name.

        Parameters
        ----------
        source_name : str
            Name of the source.
        """
        index = np.where(self.table['Source_Name'] == source_name)
        return self.table[index[0]]


def find_2fhl_highest_energy_event(source_name, radius,
                                   catalog_2fhl, event_list_2fhl):
    """
    Find highest energy events in a circle around a given 2fhl source.

    Parameters
    ----------
    source_name : str
        Name of the 2fhl source.
    radius : `astropy.units.Quantity`
        Search radius around the source.
    catalog_2fhl : `Catalog`
        2fhl catalog
    event_list_2fhl : `EventList`
        2fhl event list

    Returns
    -------
    source_events : `astropy.table.Row`
        Event list table row with the highest energy event.
    """
    source = catalog_2fhl.get_source_by_name(source_name)
    source_radec = SkyCoord(source['RAJ2000'], source['DEJ2000'], frame='icrs')
    source_events = event_list_2fhl.select_events_in_circle(source_radec, radius)
    return source_events[np.argmax(source_events['ENERGY'])]

def test_event_list():
    event_list_2fhl = EventList('data/2fhl_events.fits.gz')
    assert len(event_list_2fhl.table) == 60978

def test_catalog():
    catalog_2fhl = Catalog('data/gll_psch_v08.fit.gz')
    assert len(catalog_2fhl.table) == 360


if __name__ == '__main__':
    catalog_2fhl = Catalog('data/gll_psch_v08.fit.gz')
    event_list_2fhl = EventList('data/2fhl_events.fits.gz')

    source_name = '2FHL J0534.5+2201' # Crab
    radius = 3 * u.deg

    highest_energy_event = find_2fhl_highest_energy_event(source_name, radius,
                                                          catalog_2fhl, event_list_2fhl)

    print("The most energetic 2FHL event within a radius of {radius} from"
          " {source_name} is: {event}".format(radius=radius, source_name=source_name,
                                              event=highest_energy_event))
