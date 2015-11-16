from ..catalog import Catalog


def test_catalog():
    catalog_2fhl = Catalog('data/gll_psch_v08.fit.gz')
    assert len(catalog_2fhl.table) == 360
