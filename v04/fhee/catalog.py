import numpy as np
from astropy.table import Table


class Catalog(object):
    """
    Class to handle catalogs conveniently.

    Parameters
    ----------
    filename : str
        Filename of a FITS source catalog.
    """
    def __init__(self, filename):
        self.table = Table.read(filename)

    def get_source_by_name(self, source_name):
        """
        Get catalog row given a source name.

        Parameters
        ----------
        source_name : str
            Name of the source.
        """
        index = np.where(self.table['Source_Name'] == source_name)
        return self.table[index[0]]
