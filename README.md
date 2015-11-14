# Fermi High Energy Explorer (FHEE)

This is the repository for a Python tutorial for gamma-ray astronomers given by
Axel Donath and Christoph Deil in November 2015 at the
[PyGamma15](http://gammapy.github.io/PyGamma15/) workshop.

It's for advanced beginners, i.e. gamma-ray astronomers
that have used FITS files and written a script that uses
Python and Astropy before, but don't know much about
Python functions, classes, modules, packages, tests, docs yet.

## How does the tutorial work?

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

- Find a partner and do [pair programming](https://en.wikipedia.org/wiki/Pair_programming)!

- Decide who will be the "driver" and who will be the "observer".

- Start with a clean version of the repo and the `VTODO` folder and a new feature branch:
```
git status # should show no changes
git checkout -b most-energetic
cd VTODO
```

There are three main steps:

1. Add code
2. Add tests
3. Add docs

Actually these steps can be done in any order,
there is a lot to be said for test-driven development
(write the test first) or documentation-driven development
(write the docs first).

In practice it's often a creative an iterative procedure ...
write one first test, write some code to make it pass,
write another test, write some more code,
interactively debug and fix issues with IPython,
add a docstring, do some more coding, add one more test,
then the high-level docs and make a pull request.

Everyone has to find their own workflow that's effective for
them, and different workflows work better or worse for different cases.

Here's detailed instructions what to do:

- Add a function `find_most_energetic_2fhl_sources` in the file `TODO` that
takes arguments `n_sources` and `radius` and returns an `astropy.table.Table`
with `n_sources` rows (sorted by highest-energy event near that source) and
columns `Source_Name`, `Event_Energy` (TeV), `Event_Offset` (deg).

- Add a test function `test_find_most_energetic_2fhl_sources`
in the file `TODO` that executes
```python
table = find_most_energetic_2fhl_sources(n_sources=3, radius=0.5)
```
and then does a few assert statements on the result table:
```python
assert len(table) == 4
source = table[2] # get the third row
assert source['Source_Name'] == 'spam'
assert source['Energy'] == 42.4
```
All of these assert statements will fail because the reference
value is incorrect. For float number assertions you should use `numpy.testing.assert_allclose`. It is instructive to see what failing test reports from `pytest` look like though, so please take some time to play with this. We'd even encourage you to add code that raises errors (e.g. `1/0` will raise a `ZeroDivisionError`) in various places to practice reading `pytest` error reports (e.g. in `test_find_most_energetic_2fhl_sources`, in `find_most_energetic_2fhl_sources` as well as in the modules containing these functions at the top level, so that the error happens during test collection, not test running).

- Check the code coverage for the new code you added.

- Add a docstring to your new function and add it to the `__all__` list at the top of the file. Then re-run the Sphinx build and see if the API docs for your function show up and are correctly formatted.

 Sphinx errors can sometimes be hard to pin-point and resolve, so please intentionally insert some [restructured text](http://sphinx-doc.org/rest.html) and [Numpy docstring](https://github.com/numpy/numpy/blob/master/doc/HOWTO_DOCUMENT.rst.txt) formatting errors and try to understand the Sphinx warnings and errors.

  Add a one-sentence description and a code example to the
  high-level narrative docs in `docs/index.rst` and include
  a link to the new function.

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
- So start your own project if you like, but please also consider contributing to an existing package! We think that fewer, higher-quality packages with a small community of users and developers / maintainers is better and starting such collaborations is an explicit goal of the [PyGamma15](http://gammapy.github.io/PyGamma15/) workshop.
