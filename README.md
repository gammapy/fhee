# Fermi High Energy Explorer (FHEE)

This is the repository for a Python tutorial for gamma-ray astronomers given by
Axel Donath and Christoph Deil in November 2015 at the
[PyGamma15](http://gammapy.github.io/PyGamma15/) workshop.

It's for advanced beginners, i.e. gamma-ray astronomers
that have used FITS files and written a script that uses
Python and Astropy before, but don't know much about
Python functions, classes, modules, packages, tests, docs yet.

**If you want to follow along in the tutorial by running the
code examples and doing the exercise at the end, please
follow the instructions in the [Preparation / Requirements](https://github.com/gammapy/fhee#preparation--requirements) section below and install the required software
before the tutorial starts**!

## How does the tutorial work?

The basic idea of the tutorial is to start with some bad Python code and
incrementally turn it into better Python code. We will go from buggy spaghetti
code to a well-structured Python package with tests and docs and functionality
that can be re-used (installed and imported from other packages and shared with
colleagues as a tarball).

This will be mostly a demo, where we do live coding and explain what's going on.
In the second half we'll introduce a bunch of Python development tools (e.g.
`pytest` to run tests or `sphinx` to generate HTML documentation), there it's
easier if you want to follow along and run the commands for yourself.

We've structured the tutorial into a series of TODO steps and put the starting
point for each step of this project into folders called `vXX`. You can also use
these during or after the tutorial to try stuff out.

At the end we'll leave 30 minutes for an exercise where you get to apply the
newly learned skills and extend the package by writing a function with docs and
tests.

## What's the `fhee` package?

In this tutorial we'll create the Fermi-LAT High Energy Explorer (`fhee`)
package together. The goal is to write some code to find the highest-energy
photons near 2FHL catalog sources.

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

- Take your Python skills to the next level, from writing a script for yourself to
writing re-usable, maintainable code that would be appropriate for a
contribution to the open-source packages we'll be sprinting on at this workshop.
- Introduce you to some Python developer tools that will help you if you decide to
do more Python coding from now on.

Do all of this using a very small toy problem / package, which you can use as a
playground during and after the tutorial.

Hopefully you'll have some fun and find the example we've chosen interesting!

## Preparation / Requirements

If you want to follow along during the tutorial by coding and running commands
yourself and doing the exercise, you should git clone the
https://github.com/gammapy/fhee repo (or download it as a zip file and extract
it).

And you should install the following software listed here.

We recommend you follow the instructions [here](https://github.com/gammapy/PyGamma15/tree/gh-pages/tutorials#anaconda)
(if there's no conda package, use pip) to simultaneously install a scientific **Python version 2.7 and 3.4**,
(because one of the things we'll explain is the differences between Python 2 and 3):

* Python itself
* [IPython](http://ipython.org/), including the [Jupyter notebook](http://jupyter.org/) for Python 2 and 3
* [Numpy](http://www.numpy.org/)
* [Astropy](http://www.astropy.org/)
* [pytest](http://pytest.org/latest/) – Testing Python packages
* [Sphinx](http://sphinx-doc.org/) – Documenting Python packages
* [coverage.py](http://coverage.readthedocs.org/en/latest/) - Measure code coverage
* [pip](https://pip.pypa.io/en/latest/),
  [virtualenv](https://virtualenv.pypa.io/en/latest/),
  [setuptools](http://pythonhosted.org/setuptools/) - [Python packaging](https://packaging.python.org/en/latest/current.html)
* [six](http://pythonhosted.org/six/) - Python 2 / 3 compatible code

The following packages / tools we only use as command line tools, not Python
packages, and they work the same whether you install it using Python 2 or 3. So
it's enough to install those in one version of Python (using the Python 3.4
version is fine, here):

* [python-modernize](https://github.com/mitsuhiko/python-modernize) and
* [pep8](http://pep8.readthedocs.org/en/latest/) - Python [PEP8](https://www.python.org/dev/peps/pep-0008/) style guide checker
* [autopep8](https://github.com/hhatto/autopep8#autopep8) - Python PEP8 auto code formatter
* [prospector](http://prospector.readthedocs.org/en/master/) - Python static analysis

We'll also demo PyCharm ... install it if you'd like to try it out, but if you
have another editor you like for Python programming, that's OK, too:

* [PyCharm](https://www.jetbrains.com/pycharm/) - The most intelligent Python IDE

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

### v01 to v02 -- Improve code

- Start with `v01`
- The `analyse_data.py` script (~50 lines) implements the analysis.
  But it's buggy and not structured in a re-usable way.
- Fix indexing bug in highest-energy event energy print-out.
- No import `*`, imports at the top
- Use `astropy.table.Table` instead of `astropy.io.fits.BinTableHDU`
- Re-factor code into functions and classes (make it more readable and re-usable)
- Compute results as `Table`
- Debug something
- Now code should be roughly like `v02`

### v02 to v03 -- Add a `setup.py`

- Start with `v02`
- Put data files in `data` folder (adapt source code) and rename module to `fhee.py`:
```
$ tree .
.
├── data
│   ├── 2fhl_events.fits.gz -> ../../data/2fhl_events.fits.gz
│   └── gll_psch_v08.fit.gz -> ../../data/gll_psch_v08.fit.gz
├── fhee.py
└── setup.py
```
- Write a `setup.py` so that the code can be installed.
 See [here](https://github.com/pypa/sampleproject/blob/master/setup.py) and [here](https://packaging.python.org/en/latest/distributing/)
for an example how to write it:

```python
from setuptools import setup

setup(
    name='fhee',
    version=0.1,
    py_modules=['fhee'],
)
```
- Show how `python setup.py install` installs Python packages using a virtualenv:
```
$ pyvenv-3.4 --system-site-packages venv
$ source venv/bin/activate
```
- Adding this to the `setup()` call didn't work for me:
```python
data_files=[('fhee_data',
             ['data/2fhl_events.fits.gz',
              'data/gll_psch_v08.fit.gz',
              ])],
```
- Now code should be roughly like `v03`

### v03 to v04 -- Restructure module to package

- Start with `v03`
- Restructure into a package:
```
.
├── Makefile
├── fhee
│   ├── __init__.py
│   ├── app.py
│   ├── catalog.py
│   ├── data
│   │   ├── 2fhl_events.fits.gz -> ../../../data/2fhl_events.fits.gz
│   │   └── gll_psch_v08.fit.gz -> ../../../data/gll_psch_v08.fit.gz
│   ├── event_list.py
│   └── tests
│       ├── __init__.py
│       ├── test_app.py
│       ├── test_catalog.py
│       └── test_event_list.py
└── setup.py
```
- The `Makefile` is just to clean generated files,
it's not related to `setup.py` or needed for Python.
```
$ cat Makefile 
clean:
	rm -rf dist *.egg-info build
	find . -name "*.pyc" -exec rm {} \;
	find . -name __pycache__ | xargs rm -fr
```
- The `setup.py` file has changed a bit and now also supports installing the data files and to declare some metadata about our package:
```python
from setuptools import setup

setup(
    name='fhee',
    version=1.0,
    description='Fermi high-energy explorer',
    url='https://github.com/gammapy/fhee',
    packages=['fhee', 'fhee.tests'],
    install_requires=['numpy', 'astropy'],
    package_data={
        'fhee': ['data/*'],
    },
    license='MIT',
)
```
- Explain imports
  - implicit relative (only works on Python 2, don't use this!)
  - explicit relative (OK)
  - absolute (OK)
- Add 2 lines of boilerplate to every source file:
```python
# Licensed under a 3-clause BSD style license - see LICENSE.rst
from __future__ import absolute_import, division, print_function, unicode_literals
```
The future import makes Python 2 behave more like Python 3.
(All of our code was already Python 2 / 3 compatible,
so it doesn't make a difference in this case, but it usually does.)
- Now code should be roughly like `v04`

- To run `pytest`:
```
py.test fhee
```
- To make a coverage report pip install [pytest-cov](https://pypi.python.org/pypi/pytest-cov) and run
```
py.test fhee --cov=fhee --cov-report html
open htmlcov/index.html 
```
- Finally, let's add some documentation for `fhee`.
Like all Python projects, we'll use the [Sphinx](http://sphinx-doc.org/) tool
and the [restructured text (RST)](http://sphinx-doc.org/rest.html#rst-primer)
markup language.
- We'll use [sphinx-quickstart](http://sphinx-doc.org/invocation.html)
and answer some questions to generate an `index.rst`, `conf.py` and `Makefile`:
```
mkdir docs
cd docs
sphinx-quickstart # answer questions interactively
make html
open _build/html/index.html
```
- Next we write some high-level docs in RST (titles, code blocks, references),
re-running `make html` and re-freshing the browser to see if the markup is OK.
- To auto-generate API documentation we'll use the 
```rst
.. automodule:: fhee
   :members:
```

## Code analysis and transformation tools

- This is an optional part, will be skipped if we're short on time...
- `cd bad_code` and see the `bad.py` file
- python-modernize and six - Python 2 / 3 compatible code
- pep8 and autopep8, static code analysis

### Exercise

![Mission: Possible!](images/exercise.png)

Your mission, should you decide to accept it, is to use the rest of the tutorial
(30 min?) to apply your newly learned skills to extend the `fhee` package with a
new function that finds the 2FHL sources with the highest-energy event nearby.

- Find a partner and do [pair programming](https://en.wikipedia.org/wiki/Pair_programming)!

- Decide who will be the "driver" and who will be the "observer".

- Start with a clean version of the repo and the `V04` folder and a new feature branch:
```
git status # should show no changes
git checkout -b most-energetic
cd V04
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

- Add a function `find_most_energetic_2fhl_sources` in the file `fhee/app.py` that
takes arguments `n_sources` and `radius` and returns an `astropy.table.Table`
with `n_sources` rows (sorted by highest-energy event near that source) and
columns `Source_Name`, `Event_Energy` (TeV), `Event_Offset` (deg).

- Add a test function `test_find_most_energetic_2fhl_sources`
in the file `fhee/tests/test_app.py` that executes
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
All of these assert statements will fail because the reference value is
incorrect. For float number assertions you should use
`numpy.testing.assert_allclose`. It is instructive to see what failing test
reports from `pytest` look like though, so please take some time to play with
this. We'd even encourage you to add code that raises errors (e.g. `1/0` will
raise a `ZeroDivisionError`) in various places to practice reading `pytest`
error reports (e.g. in `test_find_most_energetic_2fhl_sources`, in
`find_most_energetic_2fhl_sources` as well as in the modules containing these
functions at the top level, so that the error happens during test collection,
not test running).

- Check the code coverage for the new code you added.

- Add a docstring to your new function and add it to the `__all__` list at the top
of the file. Then re-run the Sphinx build and see if the API docs for your
function show up and are correctly formatted.

 Sphinx errors can sometimes be hard to pin-point and resolve, so please
 intentionally insert some [restructured text](http://sphinx-doc.org/rest.html)
 and [Numpy
 docstring](https://github.com/numpy/numpy/blob/master/doc/HOWTO_DOCUMENT.rst.txt)
 formatting errors and try to understand the Sphinx warnings and errors.

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
-   So start your own project if you like, but please also consider contributing to
an existing package! We think that fewer, higher-quality packages with a small
community of users and developers / maintainers is better and starting such
collaborations is an explicit goal of the
[PyGamma15](http://gammapy.github.io/PyGamma15/) workshop.
