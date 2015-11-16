# Licensed under a 3-clause BSD style license - see LICENSE.rst
from __future__ import absolute_import, division, print_function, unicode_literals
import os


def get_data_filename(filename):
    """Helper function to find the data files."""
    here = os.path.abspath(os.path.dirname(__file__))
    return os.path.join(here, 'data', filename)
