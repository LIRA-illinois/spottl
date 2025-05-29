# spottl
pip-installable version of spot TL library

## Installation
To install the latest version of spottl, use pip:

```bash
pip install spottl
```
### Prerequisites for spottl < v2.12
- Python 3.10 or 3.11
- spot < 2.12
For spot installation instructions, see https://spot.lrde.epita.fr/install.html

### Prerequisites for spottl >= v2.12
- Python 3.10 or higher

## Usage
```python
import spot
```
This will import the `spot` module from the `spottl` package.
The usage of the `spot` module is the same as in the original `spot` library from https://spot.lrde.epita.fr/.

## Contributing
### Procedure
1. Copy binaries and Python files from the original spot library to the `spot` directory.
    - Don't forget `buddy` binaries
2. Build the package using `poetry build`.
3. Repair the dynamic library paths in the `spot` Python files using `auditwheel`.
    - Run `export LD_LIBRARY_PATH=$(pwd)/spottl/spot` to set the library path.
    - Use `auditwheel repair dist/spot-<version>-py3-none-any.whl` to create a new wheel with fixed paths.
4. Publish the repaired package to PyPI using `poetry publish`.
