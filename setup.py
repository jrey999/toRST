from setuptools import setup, find_packages


readme = """
==========================================================================================
<br>toRST
=====

Convert various data formats to reStructuredText tables.

**Currently supports**:
----------------------

- CSV
- JSON

**Planned formats**:


- Excel<br><br>

**installation**
```bash
pip install toRST
```
<br>

**CLI Usage**
-------------
example<br>
  Convert file1.csv and file2.json into RST
```bash
torst file1.csv file2.json -o ./outputfolder
```

**Positional Arguments**:
------------------------

inputs
  One or more input files to convert to RST. Currently only CSV and JSON files are 
  supported, but additional formats will be added.

**Optional Arguments**:
---------------------- 

-o, --output_dir
  Output directory for generated RST files. Defaults to the current 
  working directory if not provided.

**Python Usage**
-------------
example<br>
  
Import Table class
```python
from toRST.toRST import Table
```
Convert file1.csv into RST string
```python
rst_table = Table('file1').build_table()
```
""".strip()

with open('LICENSE') as f:
    license = f.read()
setup(
    name='toRST',
    version='0.0.9',
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