# fhee

Fermi High Energy Explorer - A tutorial for PyGamma15

## Introduction

This is the repository for a Python tutorial for gamma-ray astronomers given by
Axel Donath and Christoph Deil in November 2015 at the
[PyGamma15](http://gammapy.github.io/PyGamma15/) workshop.

The 

## Data files

* `gll_psch_v08.fit.gz` -- The Fermi-LAT 2FHL catalog
  (downloaded from FSSC)
* `2fhl_events.fits.gz` -- The event list corresponding to 2FHL
  (obtained from Marco Ajello with permission to share publicly on November 12, 2015)


## Tutorial playbook

### Intro

- Everyone get the repo, have XY installed
- Idea for the tutorial -- incremental improvement of analysis script
- Data example = 2FHL catalog and event list
- Analysis: find highest-enery events near a given 2FHL source
- There are different versions of the code (v01 to v05),
  going from buggy spaghetti code to a production-quality Python package
  with re-usable classes and functions, tests, docs that can be shared
  with colleagues.

### v01 -- Spaghetti code

- The `analyse_data.py` script (~50 lines) implements the analysis.
  But it's buggy and not structured in a re-usable way.

### v02 -- Good code

Vastly improved code:

- Fix indexing bug in highest-energy event energy print-out.
- No import `*`, imports at the top
- Use `astropy.table.Table` instead of `astropy.io.fits.BinTableHDU`
- Re-factor code into functions and classes (make it more readable and re-usable)
- Compute results as `Table`
- Debug something

### v03 -- pytest tests

- Add file `test_....py`
- Run tests with pytests
- Run coverage.py

### v04 -- Sphinx docs

- Add folder `docs`
- Use sphinx-quickstart to add sphinx docs

### v05 -- Packaging, setup.py

- Use virtualenv to explain how Python install works.
- Add setup.py
- shareable package tarball (maybe put on PyPI, maybe not)
- leave as one module or make it a package?

## Will be done extra

- python-modernize and six - Python 2 / 3 compatible code
- pep8 and autopep8, static code analysis
