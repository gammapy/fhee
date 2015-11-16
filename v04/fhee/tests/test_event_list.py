from ..event_list import EventList


def test_event_list():
    event_list_2fhl = EventList('data/2fhl_events.fits.gz')
    assert len(event_list_2fhl.table) == 60978
