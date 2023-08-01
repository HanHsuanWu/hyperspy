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

from hyperspy.docstrings.markers import OFFSET_DOCSTRING
from hyperspy.drawing.markers import Markers
from hyperspy.drawing._markers.relative_markers import RelativeMarkers
from hyperspy.external.matplotlib.collections import TextCollection


class Texts(Markers):
    """
    A set of text markers
    """

    def __init__(self, offsets, **kwargs):
        """
        Initialize the set of Circle Markers.

        Parameters
        ----------
        %s
        sizes : array-like
            The size of the text in points.
        facecolors : matplotlib color or list of colors
            Set the facecolor(s) of the markers. It can be a color
            (all patches have same color), or a sequence of colors;
            if it is a sequence the patches will cycle through the sequence.
            If c is 'none', the patch will not be filled.
        kwargs : dict
            Keyword arguments are passed to :py:class:`matplotlib.collections.CircleCollection`.
        """
        super().__init__(
            collection_class=TextCollection,
            offsets=offsets,
            **kwargs
        )
        self.name = self.__class__.__name__

    __init__.__doc__ %= OFFSET_DOCSTRING


class RelativeTextCollection(RelativeMarkers, Texts):
    """A set of text markers which are plotted relative to the current data value or index.
    """
    pass
