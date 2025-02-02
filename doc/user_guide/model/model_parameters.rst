.. _model-intro:

Getting and setting parameter values and attributes
---------------------------------------------------

Getting parameter values
^^^^^^^^^^^^^^^^^^^^^^^^

:py:meth:`~.model.BaseModel.print_current_values()` prints the properties of the
parameters of the components in the current coordinates. In the Jupyter Notebook,
the default view is HTML-formatted, which allows for formatted copying
into other software, such as Excel. One can also filter for only active
components and only showing component with free parameters with the arguments
``only_active`` and ``only_free``, respectively.

.. _Component.print_current_values:

The current values of a particular component can be printed using the
:py:attr:`~.component.Component.print_current_values()` method.

.. code-block:: python

    >>> m = s.create_model()
    >>> m.fit()
    >>> G = m[1]
    >>> G.print_current_values()
    Gaussian: Al_Ka
    Active: True
    Parameter Name |  Free |      Value |        Std |        Min
    ============== | ===== | ========== | ========== | ==========
                 A |  True | 62894.6824 | 1039.40944 |        0.0
             sigma | False | 0.03253440 |       None |       None
            centre | False |     1.4865 |       None |       None

The current coordinates can be either set by navigating the
:py:meth:`~.model.BaseModel.plot`, or specified by pixel indices in
``m.axes_manager.indices`` or as calibrated coordinates in
``m.axes_manager.coordinates``.

:py:attr:`~.component.Component.parameters` contains a list of the parameters
of a component and :py:attr:`~.component.Component.free_parameters` lists only
the free parameters.

The value of a particular parameter in the current coordinates can be
accessed by :py:attr:`component.Parameter.value` (e.g. ``Gaussian.A.value``).
To access an array of the value of the parameter across all navigation
pixels, :py:attr:`component.Parameter.map['values']` (e.g.
``Gaussian.A.map["values"]``) can be used. On its own,
:py:attr:`component.Parameter.map` returns a NumPy array with three elements:
``'values'``, ``'std'`` and ``'is_set'``. The first two give the value and
standard error for each index. The last element shows whether the value has
been set in a given index, either by a fitting procedure or manually.

If a model contains several components with the same parameters, it is possible
to change them all by using :py:meth:`~.model.BaseModel.set_parameters_value`.
Example:

.. code-block:: python

    >>> s = hs.signals.Signal1D(np.arange(100).reshape(10,10))
    >>> m = s.create_model()
    >>> g1 = hs.model.components1D.Gaussian()
    >>> g2 = hs.model.components1D.Gaussian()
    >>> m.extend([g1,g2])
    >>> m.set_parameters_value('A', 20)
    >>> g1.A.map['values']
    array([ 20.,  20.,  20.,  20.,  20.,  20.,  20.,  20.,  20.,  20.])
    >>> g2.A.map['values']
    array([ 20.,  20.,  20.,  20.,  20.,  20.,  20.,  20.,  20.,  20.])
    >>> m.set_parameters_value('A', 40, only_current=True)
    >>> g1.A.map['values']
    array([ 40.,  20.,  20.,  20.,  20.,  20.,  20.,  20.,  20.,  20.])
    >>> m.set_parameters_value('A',30, component_list=[g2])
    >>> g2.A.map['values']
    array([ 30.,  30.,  30.,  30.,  30.,  30.,  30.,  30.,  30.,  30.])
    >>> g1.A.map['values']
    array([ 40.,  20.,  20.,  20.,  20.,  20.,  20.,  20.,  20.,  20.])

Setting Parameters free / not free
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

To set the ``free`` state of a parameter change the
:py:attr:`~.component.Parameter.free` attribute. To change the ``free`` state
of all parameters in a component to `True` use
:py:meth:`~.component.Component.set_parameters_free`, and
:py:meth:`~.component.Component.set_parameters_not_free` for setting them to
``False``. Specific parameter-names can also be specified by using
``parameter_name_list``, shown in the example:

.. code-block:: python

    >>> g = hs.model.components1D.Gaussian()
    >>> g.free_parameters
    [<Parameter A of Gaussian component>,
    <Parameter sigma of Gaussian component>,
    <Parameter centre of Gaussian component>]
    >>> g.set_parameters_not_free()
    >>> g.set_parameters_free(parameter_name_list=['A','centre'])
    >>> g.free_parameters
    [<Parameter A of Gaussian component>,
    <Parameter centre of Gaussian component>]

Similar functions exist for :py:class:`~.model.BaseModel`:
:py:meth:`~.model.BaseModel.set_parameters_free` and
:py:meth:`~.model.BaseModel.set_parameters_not_free`. Which sets the
``free`` states for the parameters in components in a model. Specific
components and parameter-names can also be specified. For example:

.. code-block:: python

    >>> g1 = hs.model.components1D.Gaussian()
    >>> g2 = hs.model.components1D.Gaussian()
    >>> m.extend([g1,g2])
    >>> m.set_parameters_not_free()
    >>> g1.free_parameters
    []
    >>> g2.free_parameters
    []
    >>> m.set_parameters_free(parameter_name_list=['A'])
    >>> g1.free_parameters
    [<Parameter A of Gaussian component>]
    >>> g2.free_parameters
    [<Parameter A of Gaussian component>]
    >>> m.set_parameters_free([g1], parameter_name_list=['sigma'])
    >>> g1.free_parameters
    [<Parameter A of Gaussian component>,
         <Parameter sigma of Gaussian component>]
    >>> g2.free_parameters
    [<Parameter A of Gaussian component>]

Setting twin parameters
^^^^^^^^^^^^^^^^^^^^^^^

The value of a parameter can be coupled to the value of another by setting the
:py:attr:`~.component.Parameter.twin` attribute:

.. code-block:: python

    >>> gaussian.parameters # Print the parameters of the Gaussian components
    (<Parameter A of Carbon component>,
    <Parameter sigma of Carbon component>,
    <Parameter centre of Carbon component>)
    >>> gaussian.centre.free = False # Fix the centre
    >>> gaussian.free_parameters  # Print the free parameters
    [<Parameter A of Carbon component>, <Parameter sigma of Carbon component>]
    >>> m.print_current_values(only_free=True) # Print the values of all free parameters.
    Model1D:
    Gaussian: Carbon
    Active: True
    Parameter Name |  Free |      Value |        Std |        Min |        Max
    ============== | ===== | ========== | ========== | ========== | ==========
                 A |  True |        1.0 |       None |        0.0 |       None
             sigma |  True |        1.0 |       None |       None |       None

    Gaussian: Long Hydrogen name
    Active: True
    Parameter Name |  Free |      Value |        Std |        Min |        Max
    ============== | ===== | ========== | ========== | ========== | ==========
                 A |  True |        1.0 |       None |        0.0 |       None
             sigma |  True |        1.0 |       None |       None |       None
            centre |  True |        0.0 |       None |       None |       None

    Gaussian: Nitrogen
    Active: True
    Parameter Name |  Free |      Value |        Std |        Min |        Max
    ============== | ===== | ========== | ========== | ========== | ==========
                 A |  True |        1.0 |       None |        0.0 |       None
             sigma |  True |        1.0 |       None |       None |       None
            centre |  True |        0.0 |       None |       None |       None

    >>> # Couple the A parameter of gaussian2 to the A parameter of gaussian 3:
    >>> gaussian2.A.twin = gaussian3.A
    >>> gaussian2.A.value = 10 # Set the gaussian2 A value to 10
    >>> gaussian3.print_current_values()
    Gaussian: Nitrogen
    Active: True
    Parameter Name |  Free |      Value |        Std |        Min |        Max
    ============== | ===== | ========== | ========== | ========== | ==========
                 A |  True |       10.0 |       None |        0.0 |       None
             sigma |  True |        1.0 |       None |       None |       None
            centre |  True |        0.0 |       None |       None |       None

    >>> gaussian3.A.value = 5 # Set the gaussian1 centre value to 5
    >>> gaussian2.print_current_values()
    Gaussian: Long Hydrogen name
    Active: True
    Parameter Name |  Free |      Value |        Std |        Min |        Max
    ============== | ===== | ========== | ========== | ========== | ==========
                 A | False |        5.0 |       None |        0.0 |       None
             sigma |  True |        1.0 |       None |       None |       None
            centre |  True |        0.0 |       None |       None |       None

.. deprecated:: 1.2.0
    Setting the :py:attr:`~.component.Parameter.twin_function` and
    :py:attr:`~.component.Parameter.twin_inverse_function` attributes. Set the
    :py:attr:`~.component.Parameter.twin_function_expr` and
    :py:attr:`~.component.Parameter.twin_inverse_function_expr` attributes
    instead.

.. versionadded:: 1.2.0
    :py:attr:`~.component.Parameter.twin_function_expr` and
    :py:attr:`~.component.Parameter.twin_inverse_function_expr`.

By default the coupling function is the identity function. However it is
possible to set a different coupling function by setting the
:py:attr:`~.component.Parameter.twin_function_expr` and
:py:attr:`~.component.Parameter.twin_inverse_function_expr` attributes.  For
example:

.. code-block:: python

    >>> gaussian2.A.twin_function_expr = "x**2"
    >>> gaussian2.A.twin_inverse_function_expr = "sqrt(abs(x))"
    >>> gaussian2.A.value = 4
    >>> gaussian3.print_current_values()
    Gaussian: Nitrogen
    Active: True
    Parameter Name |  Free |      Value |        Std |        Min |        Max
    ============== | ===== | ========== | ========== | ========== | ==========
                 A |  True |        2.0 |       None |        0.0 |       None
             sigma |  True |        1.0 |       None |       None |       None
            centre |  True |        0.0 |       None |       None |       None

.. code-block:: python

    >>> gaussian3.A.value = 4
    >>> gaussian2.print_current_values()
    Gaussian: Long Hydrogen name
    Active: True
    Parameter Name |  Free |      Value |        Std |        Min |        Max
    ============== | ===== | ========== | ========== | ========== | ==========
                 A | False |       16.0 |       None |        0.0 |       None
             sigma |  True |        1.0 |       None |       None |       None
            centre |  True |        0.0 |       None |       None |       None

Batch setting of parameter attributes
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The following model methods can be used to ease the task of setting some important
parameter attributes. These can also be used on a per-component basis, by calling them
on individual components.

* :py:meth:`~.model.BaseModel.set_parameters_not_free`
* :py:meth:`~.model.BaseModel.set_parameters_free`
* :py:meth:`~.model.BaseModel.set_parameters_value`
