from setuptools import setup, find_packages


readme = """
Command line tool for converting CSV and JSON files into reStructuredText Tables.
""".strip()

with open('LICENSE') as f:
    license = f.read()
setup(
    name='toRST',
    version='0.0.2',
    description='Command line tool for converting CSV and JSON files into reStructuredText Tables.',
    long_description=readme,
    author='John Reynolds',
    author_email='reynoldsjohngreg@gmail.com',
    url='https://github.com/jrey999/toRST',
    license=license,
    packages=find_packages(exclude=('tests',)),
    entry_points={
        'console_scripts': [
            'torst = toRST.write:torst'
        ]
    }
)