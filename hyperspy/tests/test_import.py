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


def test_import_version():
    from hyperspy import __version__


def test_import():
    import hyperspy
    for obj_name in hyperspy.__all__:
        getattr(hyperspy, obj_name)


def test_import_api():
    import hyperspy.api
    for obj_name in hyperspy.api.__all__:
        getattr(hyperspy.api, obj_name)


def test_import_api_nogui():
    import hyperspy.api_nogui
    for obj_name in hyperspy.api_nogui.__all__:
        getattr(hyperspy.api_nogui, obj_name)


def test_import_datasets():
    import hyperspy.datasets
    for obj_name in hyperspy.datasets.__all__:
        getattr(hyperspy.datasets, obj_name)


def test_import_utils():
    import hyperspy.utils
    for obj_name in hyperspy.utils.__all__:
        getattr(hyperspy.utils, obj_name)


def test_import_components1D():
    import hyperspy.api as hs
    for obj_name in hs.model.components1D.__all__:
        getattr(hs.model.components1D, obj_name)


def test_import_components2D():
    import hyperspy.api as hs
    for obj_name in hs.model.components2D.__all__:
        getattr(hs.model.components2D, obj_name)


def test_import_signals():
    import hyperspy.api as hs
    for obj_name in hs.signals.__all__:
        getattr(hs.signals, obj_name)


def test_import_attribute_error():
    import hyperspy
    try:
        hyperspy.inexisting_module
    except AttributeError:
        pass


def test_import_api_attribute_error():
    import hyperspy.api
    try:
        hyperspy.api.inexisting_module
    except AttributeError:
        pass


def test_dir():
    import hyperspy
    d = dir(hyperspy)
    assert d == ['__version__', 'api']


def test_dir_api():
    import hyperspy.api
    d = dir(hyperspy.api)
    assert d == [
        '__version__',
        'datasets',
        'eds',
        'get_configuration_directory_path',
        'interactive',
        'load',
        'material',
        'model',
        'plot',
        'preferences',
        'print_known_signal_types',
        'roi',
        'samfire',
        'set_log_level',
        'signals',
        'stack',
        'transpose',
        ]


def test_dir_api_nogui():
    import hyperspy.api_nogui
    d = dir(hyperspy.api_nogui)
    assert d == [
        '__version__',
        'datasets',
        'eds',
        'get_configuration_directory_path',
        'interactive',
        'load',
        'material',
        'model',
        'plot',
        'preferences',
        'print_known_signal_types',
        'roi',
        'samfire',
        'set_log_level',
        'signals',
        'stack',
        'transpose',
        ]


def test_dir_datasets():
    import hyperspy.datasets
    d = dir(hyperspy.datasets)
    assert d == ['artificial_data', 'eelsdb', 'example_signals']


def test_dir_datasets2():
    import hyperspy.datasets.artificial_data
    d = dir(hyperspy.datasets.artificial_data)
    assert d == [
        'get_atomic_resolution_tem_signal2d',
        'get_core_loss_eels_line_scan_signal',
        'get_core_loss_eels_model',
        'get_core_loss_eels_signal',
        'get_low_loss_eels_line_scan_signal',
        'get_low_loss_eels_signal',
        'get_luminescence_signal',
        'get_wave_image',
        ]


def test_dir_datasets3():
    import hyperspy.datasets.example_signals
    d = dir(hyperspy.datasets.example_signals)
    assert d == [
    'EDS_SEM_Spectrum',
    'EDS_TEM_Spectrum',
    ]


def test_dir_utils():
    import hyperspy.utils
    d = dir(hyperspy.utils)
    assert d == [
        'eds',
        'interactive',
        'markers',
        'material',
        'model',
        'plot',
        'print_known_signal_types',
        'roi',
        'samfire',
        'stack',
        'transpose',
        ]


def test_dir_utils_eds():
    import hyperspy.utils.eds
    d = dir(hyperspy.utils.eds)
    assert d == [
        'edx_cross_section_to_zeta',
        'electron_range',
        'get_xray_lines_near_energy',
        'take_off_angle',
        'xray_range',
        'zeta_to_edx_cross_section',
        ]


def test_dir_utils_markers():
    import hyperspy.utils.markers
    d = dir(hyperspy.utils.markers)
    assert d == [
        'Arrow',
        'Ellipse',
        'HorizontalLine',
        'HorizontalLineSegment',
        'LineSegment',
        'Point',
        'Rectangle',
        'Text',
        'VerticalLine',
        'VerticalLineSegment',
        ]


def test_dir_utils_materials():
    import hyperspy.utils.material
    d = dir(hyperspy.utils.material)
    assert d == [
        'atomic_to_weight',
        'density_of_mixture',
        'elements',
        'mass_absorption_coefficient',
        'mass_absorption_mixture',
        'weight_to_atomic',
        ]


def test_dir_utils_model():
    import hyperspy.utils.model
    d = dir(hyperspy.utils.model)
    assert d == [
        'components1D',
        'components2D',
        ]


def test_dir_utils_plot():
    import hyperspy.utils.plot
    d = dir(hyperspy.utils.plot)
    assert d == [
        'markers',
        'plot_histograms',
        'plot_images',
        'plot_signals',
        'plot_spectra',
        ]


def test_dir_utils_roi():
    import hyperspy.utils.roi
    d = dir(hyperspy.utils.roi)
    assert d == [
        'CircleROI',
        'Line2DROI',
        'Point1DROI',
        'Point2DROI',
        'RectangularROI',
        'SpanROI',
        ]


def test_dir_utils_samfire():
    import hyperspy.utils.samfire
    d = dir(hyperspy.utils.samfire)
    assert d == [
        'SamfirePool',
        'fit_tests',
        'global_strategies',
        'local_strategies',
        ]


def test_dir_utils_samfire2():
    import hyperspy.utils.samfire
    d = dir(hyperspy.utils.samfire.fit_tests)
    assert d == [
        'AIC_test',
        'AICc_test',
        'BIC_test',
        'red_chisq_test',
        ]


def test_dir_utils_samfire3():
    import hyperspy.utils.samfire
    d = dir(hyperspy.utils.samfire.global_strategies)
    assert d == [
        'GlobalStrategy',
        'HistogramStrategy',
        ]


def test_dir_utils_samfire4():
    import hyperspy.utils.samfire
    d = dir(hyperspy.utils.samfire.local_strategies)
    assert d == [
        'LocalStrategy',
        'ReducedChiSquaredStrategy',
        ]
