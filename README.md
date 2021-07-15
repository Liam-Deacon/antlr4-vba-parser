# antlr4-vba-parser

Navigate antlr VBA Parse Trees in python.

<!--lint disable no-inline-padding-->

[![ ](https://github.com/Liam-Deacon/antlr4-vba-parser/workflows/Python%20CI/badge.svg)](https://github.com/Liam-Deacon/antlr4-vba-parser/actions?query=workflow%3A"Python+CI")
[![ ](https://img.shields.io/pypi/pyversions/antlr4-vba-parser.svg?logo=python)](https://pypi.org/pypi/antlr4-vba-parser/)
[![ ](https://img.shields.io/pypi/l/antlr4-vba-parser.svg)](https://pypi.org/pypi/antlr4-vba-parser/)
[![ ](https://img.shields.io/pypi/implementation/antlr4-vba-parser?color=seagreen)](https://pypi.org/pypi/antlr4-vba-parser/)
[![ ](https://img.shields.io/pypi/dm/antlr4-vba-parser.svg?color=yellow)](https://pypi.org/pypi/antlr4-vba-parser/)
[![ ](https://coveralls.io/repos/github/Liam-Deacon/antlr4-vba-parser/badge.svg?branch=master)](https://coveralls.io/github/Liam-Deacon/antlr4-vba-parser?branch=master)
[![ ](https://codecov.io/gh/Liam-Deacon/antlr4-vba-parser/branch/master/graph/badge.svg)](https://codecov.io/gh/Liam-Deacon/antlr4-vba-parser)
[![ ](https://api.codacy.com/project/badge/Grade/de571d98b5ed4203b6eda5f927c8835d)](https://www.codacy.com/gh/Liam-Deacon/antlr4-vba-parser?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=Liam-Deacon/antlr4-vba-parser&amp;utm_campaign=Badge_Grade)
[![ ](https://img.shields.io/codefactor/grade/github/LightSlayer/antlr4-vba-parser?logo=codefactor)](https://www.codefactor.io/repository/github/Liam-Deacon/antlr4-vba-parser)
![ ](https://img.shields.io/pypi/v/antlr4-vba-parser)
[![ ](https://img.shields.io/badge/Donate-buy%20me%20a%20coffee-green?logo=Buy%20me%20a%20coffee&logoColor=white)](https://ko-fi.com/lightbytes)
![ ](https://img.shields.io/badge/dev-Open%20in%20Gitpod-blue?logo=gitpod&link=https://gitpod.io/#https://github.com/Liam-Deacon/antlr4-vba-parser)
[![ ](https://camo.githubusercontent.com/52feade06f2fecbf006889a904d221e6a730c194/68747470733a2f2f636f6c61622e72657365617263682e676f6f676c652e636f6d2f6173736574732f636f6c61622d62616467652e737667)](https://colab.research.google.com/github/Liam-Deacon/antlr4-vba-parser)
[![ ](https://img.shields.io/badge/Binder%20Launch:-Jupyter%20Lab-blue.svg?colorA=&logo=data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABwAAAAcCAYAAAByDd+UAAAABGdBTUEAALGPC/xhBQAAACBjSFJNAAB6JgAAgIQAAPoAAACA6AAAdTAAAOpgAAA6mAAAF3CculE8AAAABmJLR0QA/wD/AP+gvaeTAAAACXBIWXMAAC4jAAAuIwF4pT92AAAAB3RJTUUH4gsEADkvyr8GjAAABQZJREFUSMeVlnlsVFUUh7/7ZukwpQxdoK2yGGgqYFKMQkyDUVBZJECQEERZVLQEa4iKiggiFjfqbkADhVSgEVkETVSiJBATsEIRja1RoCwuU5gC7Qww03Zm3rzrH/dOfJSZUm4y6Xt9957vnnN/55wruI7RVjMNQAA3AiX6bxw4BTQAQQDvnF1pbYjrAAEUAmXADGAQ0AOQwCWgHqgGdgCRdNBrAm2wW4A1wN2ACZwG/gbcQBFwg/Z2I/AS0JoKanQzmoXAamA0cBx4EhgDTAYmAvcArwNhYD6wHHDbNts9D20LlgMrgWPAXKAO/j8rPc8A5uiNAUwH9tjnddfDAn1mFkJWyoRR58hsv8KIfraAz/QvC3golf2UwEBZBYGyCoJfj/LFz/ceDxRJ09Hccbz/6dDu0ozg7lICZRVXrNFQEyWaDmAkkNslMAnSE59x9IrsMVt8awBP4rI3P9acs83hC3+BkFMAd2eoHn8BrdpG77RA2+IiYDPwHnAbEAOkMGQMcAKTdNheBXqmgDoBhw6xda2Q9tGHPhE4hRTlrrxQGRB29IqE3IUtTyDFu9rQC8AiwAiUVdgFNhTIA85oT68G2nb5ODABJf25niL/emfexX1AA0IWeIr8xWbY+yKwBJVzC4FSm71MlFIdwH505UnnYT5KWRawCvgp0eYBCKEqSBwpFuVMqp2a5Q1WO6TcakiZ55DWwyVVKxDC8gLPA1OAJh32q8qcHTgEKEbl2ncAua99lPy2FdgskH2FlFXNI8IVewcO8P+WUyjr8vqPfmvt+plhmVltIJeilLoK+CWVopy250LAgyrELcl/9nB/ixkbF3GKyOJ/rJs8hxNDZx1KDFvsz+9jJvINAQz1EKvxR7OddzrroyXGiRV5zvp1WPlSzN7bJVCmEtKDF38khguQeR5iBRYGFoaZaUUv9YsEc+KGYfq9vssN1qDsP2MDHRZiYBRXpoEMwa1XAe3Gm4A2YDDQ1z7JTbyvG3O1hXEvcNI0xFPzTh5ZueB4HeXH6hoGR1onC2SlhQgD5RnEl7kwXTOqfu4SeBT4Q5/jVIBtL29KfnsUGAecsISY++W+mpohwQujXJYlPAnzh2HBc7Uxw1iGSpU2VAu7C6Az1A68gEr4ZI6NXT78Pkxh9JEwU4JlGsYbO3a+c7g50/esFGIqcBb4fEzgNBlWwgI2AVsAH13V0oL1K5LvNcBOYACwsfb7qiX3n2mcmGXGirPjHf8uPHqw/Xy/IeuAV/TG3gaOAGyfPwJUbm4HosAdpKilzk7vIVT1iAPTTWG8Of5MY/vIFn8Pt2UVZkfbqi0hvFrFlcBaQNo2DKoxt6CqjQ84nzKktkV+YIE+hz1OaUVyou0iKx41BAR02KYB7wMdnWBJm4aOgOz8MWUDTpa6/NazGdUlo8c2ZuVukdBWfOnCtHlffXAwdPsEK2o47Ju0i2MysAt1xxkLtOpwpwzpFd4+sOHXKHDAIa16YNTJrJzS3x9ZVdvoy+WbecNTLfUCs7Xd/aQr3umGy0rgshIhQ8pNhpSmIeVzTZm9pnjNuLDLXT97gKdRKXUWXUvt3qUNqX1oYz2Bj1H3mXPABh22JlRnuBl4DHWPAVgKfAjIzkDntYB6hIHFKPXO0gbLUQp0oO49Xv1eCXySCtYtDzt56kU159moQulDqfEccAD4FDgEJFLBrgtog4I6r36oG0IC1d0DqNZEOhjAfzgw6LulUF3CAAAAJXRFWHRkYXRlOmNyZWF0ZQAyMDE4LTExLTA0VDAwOjU3OjQ3LTA0OjAwLtN9UwAAACV0RVh0ZGF0ZTptb2RpZnkAMjAxOC0xMS0wNFQwMDo1Nzo0Ny0wNDowMF+Oxe8AAAAASUVORK5CYII=)](https://mybinder.org/v2/gh/Liam-Deacon/antlr4-vba-parser/master?urlpath=lab)

<!--lint enable no-inline-padding-->

This python package provides an interface to the the antlr4 tooling and allows parsing
and lexing of VBA grammar.

```python
>>> from antlr4_vba_parser.vba_parser import Antlr4VbaParser

>>> parsed = Antlr4VbaParser("""
... SUB square(x)
...   DIM y: REM Some comment
...   y = x * x  ' same as x**2
... END SUB
... """)  # also accepts a filepath

>>> from pprint import pprint
>>> pprint(parsed)
('(startRule (module (endOfLine \\n) (moduleBody (moduleBodyElement (subStmt '
 'SUB   (ambiguousIdentifier square) (argList ( (arg (ambiguousIdentifier x)) '
 ')) (endOfStatement (endOfLine \\n   )) (block (blockStmt (variableStmt DIM   '
 '(variableListStmt (variableSubStmt (ambiguousIdentifier y))))) '
 '(endOfStatement :   (endOfLine (remComment REM Some comment)) (endOfLine '
 '\\n   )) (blockStmt (letStmt (implicitCallStmt_InStmt '
 '(iCS_S_VariableOrProcedureCall (ambiguousIdentifier y)))   =   (valueStmt '
 '(valueStmt (implicitCallStmt_InStmt (iCS_S_VariableOrProcedureCall '
 '(ambiguousIdentifier x))))   *   (valueStmt (implicitCallStmt_InStmt '
 '(iCS_S_VariableOrProcedureCall (ambiguousIdentifier x))))))) (endOfStatement '
 "(endOfLine    (comment ' same as x**2)) (endOfLine \\n))) END SUB)) "
 '(endOfLine \\n))) <EOF>)')
```

## Installation

`antlr4_vba_parser` itself is a pure python package, but depends on a `java` runtime in order to run.
The ANTLR4 jar needed to perform the parsing/lexing is included in the package distribution and
is bundled from third-party sources at the time of packaging with `setup.py build`.

To install, simply try:

```bash
pip install antlr4_vba_parser
```

## Development

To set up a development environment, first create either a new virtual or
conda environment before activating it and then run the following:

```bash
git clone https://github.com/Liam-Deacon/antlr4-vba-parser
cd antlr4-vba-parser
pip install -r requirements-dev.txt requirements-test.txt -r requirements.txt
pip install -e .
```

This will install the package in development mode. Note that is you have forked
the repo then change the URL as appropriate.

## Documentation

Documentation can be found within the `docs/` directory. This project
uses sphinx to autogenerate API documentation by scraping python docstrings.

To generate the HTML documentation, simply do the following:

```bash
cd docs
make html
```

## Contribution Guidelines

<!--lint disable list-item-bullet-indent -->

Contributions are extremely welcome and highly encouraged. To help with consistency
please can the following areas be considered before submitting a PR for review:

  - Use `autopep8 -a -a -i -r .` to run over any modified files to ensure basic pep8 conformance,
    allowing the code to be read in a style expected for most python projects.
  - New or changed functionality should be tested, running `pytest` should
  - Try to document any new or changed functionality. Note: this project uses
    [numpydoc](https://numpydoc.readthedocs.io/en/latest/format.html) for it's
    docstring documentation style.

<!--lint enable list-item-bullet-indent -->

## License

Released under the BSD license.

## TODO

This package is mostly a proof of concept and as such there are a number of
areas to add to, fix and improve.

- Create listener(s) capable of capturing contextual information and creating a JSON-friendly dictionary output.
- Produce simple script turns the above into a command line tool.
- Contribute to [`oletools.vba`](https://github.com/decalage2/oletools/blob/master/oletools/olevba.py) 
  to hopefully extend capabilities using this package.


## Acknowledgements
- Andrew Lockhart for the initial idea of combining ANTLR4 and python to handle VBA grammar
