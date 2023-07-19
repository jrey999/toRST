=====
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
[PyPI](https://pypi.org/project/toRST/0.0.1/)<br>
```bash
pip install toRST
```
<br>

**Usage Cli**
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

**What toRST was built for**
----------------------------

While building [mlb-positive-ev](https://github.com/jrey999/mlb-positive-ev), I wanted a quick and readable output of a SQLite query and couldn't find anything suitable.