# -*- coding: utf-8 -*-
# Copyright 2007-2023 The HyperSpy developers
#
# This file is part of HyperSpy.
#
# HyperSpy is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# HyperSpy is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with HyperSpy. If not, see <https://www.gnu.org/licenses/#GPL>.

from __future__ import print_function

import hyperspy.Release as Release
import itertools
import subprocess
from setuptools import setup
import sys

v = sys.version_info
if v[0] != 3:
    error = "ERROR: From version 0.8.4 HyperSpy requires Python 3. " \
            "For Python 2.7 install Hyperspy 0.8.3 e.g. " \
            "$ pip install --upgrade hyperspy==0.8.3"
    print(error, file=sys.stderr)
    sys.exit(1)


install_req = [
    'dask[array]>=2021.3.1',
    'dill',
    # included in stdlib since v3.8, but this required version requires Python 3.10
    # We can remove this requirement when the minimum supported version becomes Python 3.10
    'importlib-metadata>=3.6',
    'jinja2',
    'matplotlib>=3.1.3',
    'natsort',
    # non-uniform axis requirement
    'numba>=0.52',
    'numexpr',
    'numpy>=1.20.0',
    'packaging',
    'pint>=0.10',
    'pooch',
    'prettytable>=2.3',
    'python-dateutil>=2.5.0',
    'pyyaml',
    'requests',
    'scikit-image>=0.18',
    'scipy>=1.5.0',
    'sympy>=1.6',
    'rosettasciio',
    'tqdm>=4.9.0',
    'traits>=4.5.0',
    ]


extras_require = {
	"ipython": ["IPython>7.0, !=8.0", "ipyparallel"],
    "learning": ["scikit-learn>=1.0.1"],
    "gui-jupyter": ["hyperspy_gui_ipywidgets>=1.1.0", "ipympl"],
    # UPDATE BEFORE RELEASE
    "gui-traitsui": ["hyperspy_gui_traitsui @ git+https://github.com/hyperspy/hyperspy_gui_traitsui#egg=hyperspy_gui_traitsui"],
    #"gui-traitsui": ["hyperspy_gui_traitsui>=1.1.0"],
    "tests": [
        "pytest>=3.6",
        "pytest-mpl",
        "pytest-xdist",
        "pytest-rerunfailures",
        "pytest-instafail",
        ],
    "coverage":["pytest-cov"],
    # required to build the docs
    "build-doc": [
        "pydata_sphinx_theme",
        "sphinx>=1.7",
        "sphinx-gallery",
        "sphinx-copybutton",
        "sphinxcontrib-mermaid",
        "sphinxcontrib-towncrier>=0.3.0a0",
        "sphinx-design",
        "towncrier",
        ],
}


# Don't include "tests" and "docs" requirements since "all" is designed to be
# used for user installation.
runtime_extras_require = {x: extras_require[x] for x in extras_require.keys()
                          if x not in ["tests", "coverage", "build-doc"]}
extras_require["all"] = list(itertools.chain(*list(
    runtime_extras_require.values())))

extras_require["dev"] = list(itertools.chain(*list(extras_require.values())))


def update_version(version):
    release_path = "hyperspy/Release.py"
    lines = []
    with open(release_path, "r") as f:
        for line in f:
            if line.startswith("version = "):
                line = "version = \"%s\"\n" % version
            lines.append(line)
    with open(release_path, "w") as f:
        f.writelines(lines)


class update_version_when_dev:

    def __enter__(self):
        self.release_version = Release.version

        # Get the hash from the git repository if available
        self.restore_version = False
        if self.release_version.endswith(".dev"):
            p = subprocess.Popen(["git", "describe",
                                  "--tags", "--dirty", "--always"],
                                 stdout=subprocess.PIPE,
                                 shell=True)
            stdout = p.communicate()[0]
            if p.returncode != 0:
                # Git is not available, we keep the version as is
                self.restore_version = False
                self.version = self.release_version
            else:
                gd = stdout[1:].strip().decode()
                # Remove the tag
                gd = gd[gd.index("-") + 1:]
                self.version = self.release_version + "+git."
                self.version += gd.replace("-", ".")
                update_version(self.version)
                self.restore_version = True
        else:
            self.version = self.release_version
        return self.version

    def __exit__(self, type, value, traceback):
        if self.restore_version is True:
            update_version(self.release_version)


with update_version_when_dev() as version:
    setup(
        name="hyperspy",
        package_dir={'hyperspy': 'hyperspy'},
        version=version,
        packages=['hyperspy',
                  'hyperspy.datasets',
                  'hyperspy._components',
                  'hyperspy.datasets',
                  'hyperspy.docstrings',
                  'hyperspy.drawing',
                  'hyperspy.drawing._markers',
                  'hyperspy.drawing._widgets',
                  'hyperspy.learn',
                  'hyperspy._signals',
                  'hyperspy.utils',
                  'hyperspy.tests',
                  'hyperspy.tests.axes',
                  'hyperspy.tests.component',
                  'hyperspy.tests.datasets',
                  'hyperspy.tests.drawing',
                  'hyperspy.tests.learn',
                  'hyperspy.tests.model',
                  'hyperspy.tests.samfire',
                  'hyperspy.tests.signals',
                  'hyperspy.tests.utils',
                  'hyperspy.tests.misc',
                  'hyperspy.models',
                  'hyperspy.misc',
                  'hyperspy.misc.eels',
                  'hyperspy.misc.eds',
                  'hyperspy.misc.holography',
                  'hyperspy.misc.machine_learning',
                  'hyperspy.external',
                  'hyperspy.external.astropy',
                  'hyperspy.external.matplotlib',
                  'hyperspy.external.mpfit',
                  'hyperspy.samfire_utils',
                  'hyperspy.samfire_utils.segmenters',
                  'hyperspy.samfire_utils.weights',
                  'hyperspy.samfire_utils.goodness_of_fit_tests',
                  ],
        python_requires='~=3.8',
        install_requires=install_req,
        tests_require=["pytest>=3.0.2"],
        extras_require=extras_require,
        package_data={
            'hyperspy':
            [
                'tests/drawing/*.png',
                'tests/drawing/data/*.hspy',
                'tests/drawing/plot_signal/*.png',
                'tests/drawing/plot_signal1d/*.png',
                'tests/drawing/plot_signal2d/*.png',
                'tests/drawing/plot_markers/*.png',
                'tests/drawing/plot_model1d/*.png',
                'tests/drawing/plot_model/*.png',
                'tests/drawing/plot_roi/*.png',
                'misc/dask_widgets/*.html.j2',
                'misc/eds/example_signals/*.hspy',
                'misc/holography/example_signals/*.hdf5',
                'tests/drawing/plot_mva/*.png',
                'tests/drawing/plot_widgets/*.png',
                'tests/drawing/plot_signal_tools/*.png',
                'tests/signals/data/test_find_peaks1D_ohaver.hdf5',
                'tests/signals/data/*.hspy',
                'hyperspy_extension.yaml',
            ],
        },
        author=Release.authors['all'][0],
        description=Release.description,
        long_description=open('README.rst').read(),
        license=Release.license,
        platforms=Release.platforms,
        url=Release.url,
        project_urls=Release.PROJECT_URLS,
        keywords=Release.keywords,
        classifiers=[
            "Programming Language :: Python :: 3",
            "Programming Language :: Python :: 3.8",
            "Programming Language :: Python :: 3.9",
            "Programming Language :: Python :: 3.10",
            "Programming Language :: Python :: 3.11",
            "Development Status :: 4 - Beta",
            "Environment :: Console",
            "Intended Audience :: Science/Research",
            "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
            "Natural Language :: English",
            "Operating System :: OS Independent",
            "Topic :: Scientific/Engineering",
            "Topic :: Scientific/Engineering :: Physics",
        ],
    )
