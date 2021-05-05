import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="mProfile", # Replace with your own username
    version="0.8.0",
    author="David Baddeley",
    author_email="d.baddeley@auckland.ac.nz",
    description="Line-by line profiling with html reports",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/python-microscopy/mProfile",
    classifiers=[
        'Programming Language :: Python :: 2.7',
        "Programming Language :: Python :: 3",
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        "Operating System :: OS Independent",
    ],
    package_dir={"": "."},
    packages=setuptools.find_packages(),
    python_requires=">=2.7",
)