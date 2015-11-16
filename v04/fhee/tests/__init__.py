def test_event_list():
    event_list_2fhl = EventList('data/2fhl_events.fits.gz')
    assert len(event_list_2fhl.table) == 60978

def test_catalog():
    catalog_2fhl = Catalog('data/gll_psch_v08.fit.gz')
    assert len(catalog_2fhl.table) == 360
