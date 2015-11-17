Usage
=====

`fhee` implements the `fhee.Catalog` and `fhee.EventList` classes
that represent the 2FHL catalog and event list (data files in FITS format are bundled).

As an example application, there's the `fhee.find_2fhl_highest_energy_event` function
and the `fhee.run_example` function.


.. code-block:: python

    import fhee
    catalog = fhee.Catalog()
    print(len(catalog))
