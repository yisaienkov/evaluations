# Evaluations
[![PyPI version](https://badge.fury.io/py/evaluations.svg)](https://badge.fury.io/py/evaluations)
[![Documentation Status](https://readthedocs.org/projects/evaluations/badge/?version=latest)](https://evaluations.readthedocs.io/en/latest/?badge=latest)

* The library implements various metrics for evaluating machine learning algorithms
* Includes some of the [Kaggle Competitions](https://www.kaggle.com/competitions) metrics.


## Table of contents
- [How to use](#how-to-use)
- [Installation](#installation)
  - [PyPI](#pypi)
- [Documentation](#documentation)
- [Authors](#authors)


## How to use

```
>>> from evaluations.classification import confusion_matrix_binary
>>> confusion_matrix_binary([1, 1, 0, 0], [1, 0, 0, 1])
{'tp': 1, 'tn': 1, 'fp': 1, 'fn': 1}
```

## Installation

### PyPI
You can use pip to install evaluations:
```
pip install evaluations
```
You can clone and install the latest version of the library from GitHub:
```
pip install -U git+https://github.com/yisaienkov/evaluations
```

## Documentation
The full documentation is available at [https://evaluations.readthedocs.io/](https://evaluations.readthedocs.io/).

## Authors
[Yaroslav Isaienkov](https://www.linkedin.com/in/yisaienkov/)
