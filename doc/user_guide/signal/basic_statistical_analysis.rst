.. _signal.statistics:

Basic statistical analysis
--------------------------

:py:meth:`~.api.signals.BaseSignal.get_histogram` computes the histogram and
conveniently returns it as signal instance. It provides methods to
calculate the bins. :py:meth:`~.api.signals.BaseSignal.print_summary_statistics`
prints the five-number summary statistics of the data.

These two methods can be combined with
:py:meth:`~.api.signals.BaseSignal.get_current_signal` to compute the histogram or
print the summary statistics of the signal at the current coordinates, e.g:

.. code-block:: python

    >>> s = hs.signals.EELSSpectrum(np.random.normal(size=(10,100)))
    >>> s.print_summary_statistics()
    Summary statistics
    ------------------
    mean:	0.021
    std:	0.957
    min:	-3.991
    Q1:	-0.608
    median:	0.013
    Q3:	0.652
    max:	2.751

    >>> s.get_current_signal().print_summary_statistics()
    Summary statistics
    ------------------
    mean:   -0.019
    std:    0.855
    min:    -2.803
    Q1: -0.451
    median: -0.038
    Q3: 0.484
    max:    1.992

Histogram of different objects can be compared with the functions
:py:func:`~.api.plot.plot_histograms` (see
:ref:`visualisation <plot_spectra>` for the plotting options). For example,
with histograms of several random chi-square distributions:


.. code-block:: python

    >>> img = hs.signals.Signal2D([np.random.chisquare(i+1,[100,100]) for
    ...                            i in range(5)])
    >>> hs.plot.plot_histograms(img,legend='auto')

.. figure::  ../images/plot_histograms_chisquare.png
   :align:   center
   :width:   500

   Comparing histograms.
