# DeepMind Lab Python Module

The DeepMind Lab Python module is the recommended way to use DeepMind Lab
outside of a Bazel project. You can create and run environments using the same
Python API that you would use with a Bazel project.

## Build and Install

The build and install process has the following steps:

- Install project dependencies.
- Build project assets and binaries with Bazel.
- Bundle project assets and binaries into a Python package.
- Install the package.

Here's the short version if you have already set up the dependencies.

```sh
git clone git clone https://github.com/deepmind/lab.git && cd lab
bazel build python/pip_package:build_pip_package
./bazel-bin/python/pip_package/build_pip_package /tmp/dmlab_pkg
pip install /tmp/dmlab_pkg/DeepMind_Lab-1.0-py2-none-any.whl --force-reinstall
```

#### Dependencies

First, see
[External dependencies, prerequisites and porting notes](https://github.com/deepmind/lab/blob/master/README.md)
and install any requirements you might be missing. In addition to the
requirements listed there, you may also need:

- [pip](https://pip.pypa.io/en/stable/installing/)
- [NumPy](https://docs.scipy.org/doc/numpy/user/install.html)
- [virtualenv](https://virtualenv.pypa.io/en/stable/installation/) (optional)

If you prefer, NumPy can be installed as part of the **install** step below so
it is added to the virtualenv for your project. Instructions are provided below
for doing so.

#### Build assets/binaries

Following this are more detailed instructions on how to build and install if you
haven't followed the short version of the instructions above. To begin, if you
haven't already, clone DeepMind Lab.

```sh
$ git clone https://github.com/deepmind/lab.git
```


To build the prerequisite assets and binaries for the Python package, change to
the `lab` directory and run the Bazel command to build the pip package script:

```sh
$ cd lab
$ bazel build python/pip_package:build_pip_package
```

If the build command fails, make sure you've grabbed the latest version and
double check that you've installed all of the dependencies for DeepMind Lab,
then [file a bug](https://github.com/deepmind/lab/issues/new).

Keep in mind that for most changes you make to DeepMind Lab, including adding
new game scripts, models, textures, and code, that you will need to rebuild the
package script and perform the following installation instructions again.

#### Package assets/binaries

To create a Python package for DeepMind Lab run the following:

```sh
$ ./bazel-bin/python/pip_package/build_pip_package /tmp/dmlab_pkg
```
This script copies all of the relevant files for the package to a temporary
directory and bundles them up into the distribution file saved in the directory
specified. (It needs to be run from the root of the DeepMind Lab source
directory since it expects to find `bazel-bin` in the directory from which it is
called.)

#### Install

The recommended way to use the DeepMind Lab Python Module is with Virtualenv, a
tool that allows you to keep the dependencies for projects separate from one
another. Instructions provided are for building and installing with Virtualenv,
but you can skip these steps to install the package with your system-wide
packages.

First, create a virtual environment in your project directory:

```sh
$ cd ~/my_agent
$ virtualenv agentenv
```

Once you've created your virtualenv, you can activate it using:

```sh
$ source agentenv/bin/activate
```

Once your virtualenv is activated, install any remaining dependencies:

```sh
(agentenv)$ pip install numpy
```

The package generation step will have created a `.whl` file in `/tmp/dmlab_pkg`.
This is the binary distribution file for DeepMind Lab. Install it using:

```sh
(agentenv)$ pip install /tmp/dmlab_pkg/DeepMind_Lab-1.0-py2-none-any.whl
```

After a successful install you're now ready to start using DeepMind Lab as a
standalone module.

Finally, when you're done using your virtualenv you can deactivate it by
running:

```sh
(agentenv)$ deactivate
```

#### Testing the Installation

Create a new file `agent.py` and add the following:

```python
import deepmind_lab
import numpy as np

# Create a new environment object.
lab = deepmind_lab.Lab("tests/empty_room_test", ['RGB_INTERLACED'],
                       {'fps': '30', 'width': '80', 'height': '60'})
lab.reset(seed=1)

# Execute 100 walk-forward steps and sum the returned rewards from each step.
print sum(
    [lab.step(np.array([0,0,0,1,0,0,0], dtype=np.intc)) for i in range(0, 100)])
```

Run `agent.py`:

```sh
(agentenv)$ python agent.py
```

DeepMind Lab prints debugging/diagnostic info to the console, but at the end it
should print out a number showing the reward. For the seed provided, the reward
should be 11.0.

#### Uninstall

If you make changes to any files that get bundled in the package then you can
either uninstall the old version of DeepMind Lab before installing the new
version, or invoke the above `pip install` command with the flag
`--force-reinstall`.

If you really want to say goodbye, just run:

```sh
$ pip uninstall deepmind_lab
```

If you've installed this to your virtualenv and to your system-wide packages you
will need to run this command once for each.

## DeepMind Lab Python API

You can use the same API for the standalone Python module as you do when
building with the Bazel project. See:
[DeepMind Lab environment documentation: Python](https://github.com/deepmind/lab/blob/master/docs/python_api.md).
