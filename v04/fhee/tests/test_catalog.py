# Licensed under a 3-clause BSD style license - see LICENSE.rst
from __future__ import absolute_import, division, print_function, unicode_literals
from .. import Catalog, get_data_filename


def test_catalog():
    catalog_2fhl = Catalog(get_data_filename('gll_psch_v08.fit.gz'))
    assert len(catalog_2fhl.table) == 360
