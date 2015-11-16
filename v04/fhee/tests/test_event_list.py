# Licensed under a 3-clause BSD style license - see LICENSE.rst
from __future__ import absolute_import, division, print_function, unicode_literals
from .. import get_data_filename, EventList


def test_event_list():
    event_list_2fhl = EventList(get_data_filename('2fhl_events.fits.gz'))
    assert len(event_list_2fhl.table) == 60978
