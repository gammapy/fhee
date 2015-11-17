
Fermi High Energy Explorer (fhee)
=================================

This is a Python package to explore the Fermi-LAT high-energy data.

It's not a real project, just an example for a tutorial, see:
https://github.com/gammapy/fhee

Installation
------------

.. code-block:: bash

    cd v04
    python setup.py install

Testing
-------

`fhee` is well-tested. See for youself:

.. code-block:: bash

    cd v04
    py.test fhee


Usage
-----

`fhee` implements the `fhee.Catalog` and `fhee.EventList` classes
that represent the 2FHL catalog and event list (data files in FITS format are bundled).

As an example application, there's the ``fhee.find_2fhl_highest_energy_event` function
and the `fhee.run_example` function.


.. code-block:: python

    import fhee
    catalog = fhee.Catalog()
    print(len(catalog))


Contents:

.. toctree::
   :maxdepth: 2


