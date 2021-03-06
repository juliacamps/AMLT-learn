from distutils.core import setup

setup(
    name='AMLT-learn',
    version='0.2.9',
    packages=['amltlearn', 'amltlearn.cluster', 'amltlearn.metrics', 'amltlearn.datasets', 'amltlearn.preprocessing',
              'amltlearn.feature_selection', 'amltlearn.feature_selection.unsupervised',
              'amltlearn.time_series',
              'amltlearn.time_series.discretization'],
    url='http://www.cs.upc.edu/~bejar/amlt/amlt.html',
    license='GPL 3.0',
    author='bejar',
    author_email='bejar@lsi.upc.edu',
    description='Python classes for the AMLT course of the Master in Artificial Intelligence (UPC)'
)
