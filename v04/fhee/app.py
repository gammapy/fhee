import astropy.units as u
import numpy as np
from astropy.coordinates import SkyCoord
from .catalog import Catalog
from .event_list import EventList


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
    event_list_2fhl : `v04.fhee.event_list.EventList`
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


def run_example():
    catalog_2fhl = Catalog('data/gll_psch_v08.fit.gz')
    event_list_2fhl = EventList('data/2fhl_events.fits.gz')

    source_name = '2FHL J0534.5+2201'  # Crab
    radius = 3 * u.deg

    highest_energy_event = find_2fhl_highest_energy_event(source_name, radius,
                                                          catalog_2fhl, event_list_2fhl)

    print("The most energetic 2FHL event within a radius of {radius} from"
          " {source_name} is: {event}".format(radius=radius, source_name=source_name,
                                              event=highest_energy_event))

if __name__ == '__main__':
    run_example()
