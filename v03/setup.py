from setuptools import setup

setup(
    name='fhee',
    version=0.1,
    py_modules=['fhee'],
    data_files=[('fhee_data',
                 ['data/2fhl_events.fits.gz',
                  'data/gll_psch_v08.fit.gz',
                  ])],
)
