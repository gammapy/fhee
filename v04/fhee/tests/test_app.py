# Licensed under a 3-clause BSD style license - see LICENSE.rst
from __future__ import absolute_import, division, print_function, unicode_literals
from numpy.testing import assert_allclose
import astropy.units as u
from .. import get_data_filename, Catalog, EventList, find_2fhl_highest_energy_event


def test_find_2fhl_highest_energy_event():
    catalog_2fhl = Catalog(get_data_filename('gll_psch_v08.fit.gz'))
    event_list_2fhl = EventList(get_data_filename('2fhl_events.fits.gz'))

    source_name = '2FHL J0534.5+2201'  # Crab
    radius = 3 * u.deg

    event = find_2fhl_highest_energy_event(
        source_name, radius, catalog_2fhl, event_list_2fhl)

    assert_allclose(event['ENERGY'], 1682116.25)
