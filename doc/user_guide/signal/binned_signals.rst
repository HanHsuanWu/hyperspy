.. _signal.binned:

Binned and unbinned signals
---------------------------

Signals that are a histogram of a probability density function (pdf) should
have the ``is_binned`` attribute of the signal axis set to ``True``. The reason
is that some methods operate differently on signals that are *binned*. An
example of *binned* signals are EDS spectra, where the multichannel analyzer
integrates the signal counts in every channel (=bin).
Note that for 2D signals each signal axis has an ``is_binned``
attribute that can be set independently. For example, for the first signal
axis: ``signal.axes_manager.signal_axes[0].is_binned``.

The default value of the ``is_binned`` attribute is shown in the
following table:

.. table:: Binned default values for the different subclasses.


    +-------------------------------------------------+--------+
    |           BaseSignal subclass                   | binned |
    +=================================================+========+
    |    :py:class:`~.api.signals.BaseSignal`         | False  |
    +-------------------------------------------------+--------+
    |    :py:class:`~.api.signals.Signal1D`           | False  |
    +-------------------------------------------------+--------+
    |    :py:class:`~.api.signals.EELSSpectrum`       | True   |
    +-------------------------------------------------+--------+
    |    :py:class:`~.api.signals.EDSSEMSpectrum`     | True   |
    +-------------------------------------------------+--------+
    |    :py:class:`~.api.signals.EDSTEMSpectrum`     | True   |
    +-------------------------------------------------+--------+
    |    :py:class:`~.api.signals.Signal2D`           | False  |
    +-------------------------------------------------+--------+
    |    :py:class:`~.api.signals.ComplexSignal`      | False  |
    +-------------------------------------------------+--------+
    |    :py:class:`~.api.signals.ComplexSignal1D`    | False  |
    +-------------------------------------------------+--------+
    |    :py:class:`~.api.signals.ComplexSignal2D`    | False  |
    +-------------------------------------------------+--------+



To change the default value:

.. code-block:: python

    >>> s.axes_manager[-1].is_binned = True

.. versionchanged:: 1.7 The ``binned`` attribute from the metadata has been
    replaced by the axis attributes ``is_binned``.

Integration of binned signals
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

For binned axes, the detector already provides the per-channel integration of
the signal. Therefore, in this case, :py:meth:`~.api.signals.BaseSignal.integrate1D`
performs a simple summation along the given axis. In contrast, for unbinned
axes, :py:meth:`~.api.signals.BaseSignal.integrate1D` calls the
:py:meth:`~.api.signals.BaseSignal.integrate_simpson` method.

