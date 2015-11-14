# fhee

Fermi High Energy Explorer - A tutorial for PyGamma15

## How does the tutorial work?

This is the repository for a Python tutorial for gamma-ray astronomers given by
Axel Donath and Christoph Deil in November 2015 at the
[PyGamma15](http://gammapy.github.io/PyGamma15/) workshop.

The basic idea of the tutorial is to start with some bad Python code and incrementally turn it into better Python code. We will go from buggy spaghetti code to a well-structured Python package with tests and docs and functionality that can re-used (installed and imported from other packages and shared with colleagues as a tarball).

This will be mostly a demo, where we do live coding and explain what's going on. In the second half we'll introduce a bunch of Python development tools (e.g. `pytest` to run tests or `sphinx` to generate HTML documentation), there it's easier if you want to follow along and run the commands for yourself.

We've structured the tutorial into a series of TODO steps and put the starting point for each step of this project into folders called `vXX`. You can also use these during or after the tutorial to try stuff out.

At the end we'll leave 30 minutes for an exercise where you get to apply the newly learned skills and extend the package by writing a function with docs and tests.

## What's the `fhee` package?

In this tutorial we'll create the Fermi-LAT High Energy Explorer (`fhee`) package together.

The goal is to write some code to find the highest-energy photons near 2FHL catalog sources.

The input data files are:

* `data/gll_psch_v08.fit.gz` -- The Fermi-LAT 2FHL catalog
  (downloaded from FSSC)
* `data/2fhl_events.fits.gz` -- The event list corresponding to 2FHL
  (obtained from Marco Ajello with permission to share publicly on November 12, 2015)

We've added soft links to some of the versions of this package
to avoid duplicating the data files (a few MB) in the git repo.
E.g. `v01/gll_psch_v08.fit.gz` is a soft link to `data/gll_psch_v08.fit.gz`.


## Goals

The goals of this tutorial are:

- 

The goal is to make you aware of some of the existing tools and get you
started. Using the links provided here you can then follow up later at 
your own pace and really get to know the tools you think might be useful
to you.

We plan to cover the following tools (deviations from this plan are possible
though):

* [pytest](http://pytest.org/latest/) – Testing Python packages
* [Sphinx](http://sphinx-doc.org/) – Documenting Python packages
* [coverage.py](http://coverage.readthedocs.org/en/latest/) - Measure code coverage
* [PyCharm](https://www.jetbrains.com/pycharm/) - The most intelligent Python IDE
* [python-modernize](https://github.com/mitsuhiko/python-modernize) and [six](http://pythonhosted.org/six/) - Python 2 / 3 compatible code
* [pep8](http://pep8.readthedocs.org/en/latest/) - Python [PEP8](https://www.python.org/dev/peps/pep-0008/) style guide checker
* [autopep8](https://github.com/hhatto/autopep8#autopep8) - Python PEP8 auto code formatter
* [prospector](http://prospector.readthedocs.org/en/master/) - Python static analysis
* [pip](https://pip.pypa.io/en/latest/),
  [virtualenv](https://virtualenv.pypa.io/en/latest/),
  [setuptools](http://pythonhosted.org/setuptools/) - [Python packaging](https://packaging.python.org/en/latest/current.html)
* [conda](http://conda.pydata.org/docs/) - Multi-platform package and environment management system
* (Probably no time, maybe very briefly: [debugging](http://scipy-lectures.github.io/advanced/debugging/))

## How to prepare

If you want to follow along during the tutorial and do the exercises,
you should install the tools listed above before and check that they work.

As an example, to install pytest, use `pip install pytest`
or `conda install pytest` and then run `py.test --help` to make sure
it's working (if you see some help message, you're all set).


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
- Add a license

## Will be done on extra files

- python-modernize and six - Python 2 / 3 compatible code
- pep8 and autopep8, static code analysis

### Exercise

![Mission: Possible!](images/exercise.png)

Your mission, should you decide to accept it, is to use the rest of the tutorial (30 min?) to apply your newly learned skills to extend the `fhee` package with a new function that finds the 2FHL sources with the highest-energy event nearby.

Here's a suggestion how to do this step-by-step:

- Add a function `find_most_energetic_2fhl_sources` in the file `TODO` that takes arguments ``

- If you've never make a contribution on Github before,
  you can make a pull request with your code if you like.

  (Just to practice git / Github a bit, we won't merge it
  anyways, no worries if the code is unfinished or you didn't
  get around to writing tests or docs.)


### Wrap-up

Some questions:

- Who learned something new?
- Did you accept / complete the mission?
- Do you think the `fhee` package is good code now?
- Do you think it is worth the extra effort to make the
  code modular, add tests, docs, package it up?
- What factor in time do you think it takes to go from
  working Python script to production-quality code?
  2, 5, 10, 20 times as long?

Some comments:

- As you saw, it is possible to create and share a Python
  package via Github and PyPI within a few hours.
- We think that it's great if you do that for code you've
  written that's useful for your colleagues!
- But there's also a concern. There's 1000s of small
  open-source Python packages written by one person that
  are somewhat useful, but aren't used much and are
  unmaintained, because the author moved on to another
  project or job.
- So start your own project if you like, but please also consider contributing to an existing package!
