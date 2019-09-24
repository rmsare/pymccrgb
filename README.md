# pymccrgb

[![Build Status](https://travis-ci.com/rmsare/pymccrgb.svg?branch=master)](https://travis-ci.com/rmsare/pymccrgb)
[![Documentation Status](https://readthedocs.org/projects/pymccrgb/badge/?version=latest)](https://pymccrgb.readthedocs.io/en/latest/?badge=latest)

**pymccrgb** is a Python package for multiscale curvature classification of
point clouds with color features. 

It extends a popular classification method
([MCC lidar](https://sourceforge.net/p/mcclidar/wiki/Home/)) [[0]](#references) to point cloud datasets with multiple color channels, such as those
commonly produced in surveys using drone photography or other platforms. It can be used to extract points from the
ground surface and higher vegetation in data for which multiple laser
returns are not available.

The intended users are scientists in geomorphology, ecology, or planetary science
who want to classify points in datasets produced by structure from motion photogrammetry,
stereo photogrammetry, or multi-spectral lidar scanning.

### Installation

If LibLAS is installed, you can [use a virtual environment](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html) to install the package and the rest of the dependencies:

```bash
git clone https://github.com/rmsare/pymccrgb
cd pymccrgb
conda env create -f environment.yml
conda activate pymcc
py.test pymccrgb/tests
```

### Requirements

This package is developed for Linux/OS X and Python 3.6+.

The LibLAS C library is required for MCC and `pymccrgb`. On Ubuntu, you can install it via `apt`:

```bash
sudo apt-get install liblas-c-dev
```

Or directly from source

```bash
mkdir ~/liblas
cd ~/liblas
apt-get download liblas-c-dev  # Downloads the LibLAS .deb file
dpkg -x <deb-file> ~/liblas
export LD_LIBRARY_PATH=~/liblas/usr/include/:$LD_LIBRARY_PATH
```

On OS X, it is [available through Homebrew](https://liblas.org/start.html#installation):

```bash
brew install liblas
```

It also requires Boost and the C++11 standard library, which are likely installed as system libraries.

### Examples

#### Topography under tree cover

```python
from pymccrgb import mcc, mcc_rgb
from pymccrgb.datasets import load_mammoth_lidar
from pymccrgb.plotting import plot_results

# Load sample data (Mammoth Mountain, CA)
data = load_mammoth_lidar(npoints=1e6)

# MCC algorithm
ground_mcc, labels_mcc = mcc(data)

# MCC-RGB algorithm
ground_mccrgb, labels_mccrgb = mcc_rgb(data)

plot_results_wd(data, labels_mcc, labels_mccrgb)
```

[![MCC results](docs/img/mccrgb.png)]()

Results of MCC and MCC-RGB on forested area near Mammoth Mountain, CA. 

### Documentation

Read the documentation for example use cases, an API reference, and more. They
are hosted at [pymccrgb.readthedocs.io](https://pymccrgb.readthedocs.io).

### Contributing

#### Bug reports

Bug reports are much appreciated. Please [open an issue](https://github.com/rmsare/pymccrgb/issues/new) with the `bug` label,
and provide a minimal example illustrating the problem.

#### Suggestions

Feel free to [suggest new features](https://github.com/rmsare/pymccrgb/issues/new) in an issue with the `new-feature` label.

#### Pull requests

If you would like to add a feature or fix a bug, please fork the repository, create a feature branch, and [submit a PR](https://github.com/rmsare/pymccrgb/compare) and reference any relevant issues. There are nice guides to contributing with GitHub [here](https://akrabat.com/the-beginners-guide-to-contributing-to-a-github-project/) and [here](https://yourfirstpr.github.io/). Please include tests where appropriate and check that the test suite passes (a Travis build or `pytest pymccrgb/tests`) before submitting.

### Support and questions

Please [open an issue](https://github.com/rmsare/pymccrgb/issues/new) with your question.

### References

[0] Evans, J. S., & Hudak, A. T. 2007. A multiscale curvature algorithm for classifying discrete return LiDAR in forested environments. IEEE Transactions on Geoscience and Remote Sensing, 45(4), 1029-1038 [doi](https://doi.org/10.1109/TGRS.2006.890412) 

[1] 

[2] 

### License

This work is licensed under the MIT License (see [LICENSE](LICENSE)). It also
incorporates a wrapper for the [`mcc-lidar` implementation](https://sourceforge.net/p/mcclidar),
which is distributed under the Apache license (see [pymcc/LICENSE.txt](pymcc/LICENSE.txt)).
