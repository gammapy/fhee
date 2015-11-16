# Licensed under a 3-clause BSD style license - see LICENSE.rst
from __future__ import absolute_import, division, print_function, unicode_literals
import astropy.units as u
from ..catalog import Catalog
from ..event_list import EventList
from ..app import find_2fhl_highest_energy_event


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
