import numpy as np
import astropy.units as u
from astropy.coordinates import SkyCoord
from astropy.table import Table

class EventList(object):
    """Class to handle event lists conveniently"""
    def __init__(self, filename):
        self.table = Table.read(filename)

    def select_events_in_circle(self, position, radius):
        """Select all events in circular region around a given position in the sky"""
        position_radec = position.transform_to('icrs')
        events_radec = SkyCoord(self.table['RA'], self.table['DEC'], frame='icrs')
        separation = events_radec.separation(position_radec)
        return self.table[separation < radius]

class Catalog(object):
    """Class to handle catalogs conveniently"""
    def __init__(self, filename):
        self.table = Table.read(filename)

    def get_source_by_name(self, source_name):
        index = np.where(self.table['Source_Name'] == source_name)
        return self.table[index[0]]


def find_2fhl_highest_energy_events(source_name, radius):
    """Find highest energy events in a circle around a given 2fhl source"""
    catalog_2fhl = Catalog('gll_psch_v08.fit.gz')
    source = catalog_2fhl.get_source_by_name(source_name)
    
    source_radec = SkyCoord(source['RAJ2000'], source['DEJ2000'], frame='icrs')
    
    event_list_2fhl = EventList('2fhl_events.fits.gz')
    assert len(event_list_2fhl.table) == 60978

    source_events = event_list_2fhl.select_events_in_circle(source_radec, radius)
    source_events.sort('ENERGY')
    return source_events 
    
    
    
if __name__ == '__main__':
    source_name = '2FHL J0534.5+2201' # Crab
    radius = 3 * u.deg
    high_energy_events = find_2fhl_highest_energy_events(source_name, radius)
    
    print("The most energetic 2FHL events within a radius of {radius} from"
          " {source_name} are: {events}".format(radius=radius, source_name=source_name,
                                                events=high_energy_events[-3:]))
