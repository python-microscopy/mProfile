# mProfile

Matlab style line-based profiling for python

Similar in principle to rkern's line_profiler (https://github.com/pyutils/line_profiler), this offers line-by-line profiling of python code.
It has a reasonably high profiling overhead, making it most suited for profiling code such as numpy array operations which spend a large
fraction of their time in compiled c code. When used for strait python functions, you will inevitably see some distortions due to the profiling overhead

### Installation

```bash
git clone https://github.com/python-microscopy/mProfile
cd mProfile
python setup.py install
```

pip & conda packages coming soon.

### Usage

```python
import mProfile

# turn profiling on and specify which files should be profiled. 
# matching occurs purely on the filename with directories ignored (essentially `os.path.split(fn)[-1] in filenames`)
mProfile.profileOn(['file1.py', 'file2.py'])

# expensive computations
# ....

mProfile.profileOff()
mProfile.report()
```

When called as above, `mProfile.report()` will open a new webbrowser window pointing at the profile output. It is possible to redirect
the profile output to file instead.

```python
mProfile.report(display=False, profiledir='/path/to/a/directory')
```

which will save one .html profile file for each of the files specified in the `profileOn()` call

An example snippet of profile output is given below:

![image](https://user-images.githubusercontent.com/19475296/117095084-721d2600-adb9-11eb-9895-848cfd1e4512.png)

### Key differences to `line_profiler`

- requires less modification of the code (no decorators etc)
- code to be profiled is selected on a per-file basis not per-function
- output is provided as pretty, syntax-highlighted HTML with expensive lines coloured
- performance is likely inferior / profiling overhead higher as it is implemented entirely in python (no cython optimisations etc...) 
